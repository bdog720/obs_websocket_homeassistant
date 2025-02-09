import logging
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from obsws_python import ReqClient
from obsws_python.error import OBSSDKError

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=10)

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = OBSDataCoordinator(hass, config_entry)
    await coordinator.async_config_entry_first_refresh()
    async_add_entities([OBSRecordingSensor(coordinator, config_entry)])

class OBSDataCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, config_entry):
        super().__init__(
            hass,
            _LOGGER,
            name="OBS Recording Status",
            update_interval=SCAN_INTERVAL,
        )
        self.config = config_entry.data
        self.client = None

    async def _async_update_data(self):
        try:
            if not self.client:
                self.client = ReqClient(
                    host=self.config["host"],
                    port=self.config["port"],
                    password=self.config["password"],
                    timeout=3
                )
            
            # Get recording status using new method
            status = await self.hass.async_add_executor_job(
                self.client.get_record_status
            )
            return {"recording": status.output_active}
            
        except OBSSDKError as e:
            self.client = None  # Force reconnect on next attempt
            raise UpdateFailed(f"OBS connection error: {str(e)}")
        except Exception as e:
            self.client = None
            raise UpdateFailed(f"Unexpected error: {str(e)}")

class OBSRecordingSensor(SensorEntity):
    def __init__(self, coordinator, config_entry):
        self.coordinator = coordinator
        self.config_entry = config_entry
        self._attr_name = "OBS Recording Status"
        self._attr_unique_id = f"obs_recording_{config_entry.entry_id}"

    @property
    def state(self):
        return "on" if self.coordinator.data.get("recording", False) else "off"

    async def async_update(self):
        await self.coordinator.async_request_refresh()

    @property
    def should_poll(self):
        return False

    async def async_added_to_hass(self):
        self.async_on_remove(
            self.coordinator.async_add_listener(
                self.async_write_ha_state
            )
        )