import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from obsws_python import ReqClient
from obsws_python.error import OBSSDKError

DATA_SCHEMA = vol.Schema({
    vol.Required("host"): str,
    vol.Required("port", default=4455): int,
    vol.Required("password"): str,
})

class OBSConfigFlow(config_entries.ConfigFlow, domain="obs_recording"):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            try:
                # Test connection using new client
                client = ReqClient(
                    host=user_input["host"],
                    port=user_input["port"],
                    password=user_input["password"],
                    timeout=3
                )
                # Make a simple request to verify connection
                await self.hass.async_add_executor_job(client.get_version)
                return self.async_create_entry(title="OBS Recording", data=user_input)
            except OBSSDKError as e:
                errors["base"] = "cannot_connect"
                _LOGGER.error("Connection error: %s", str(e))
            except Exception as e:
                errors["base"] = "unknown"
                _LOGGER.exception("Unexpected error: %s", str(e))
        
        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return OBSOptionsFlow(config_entry)

class OBSOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host", default=self.config_entry.data["host"]): str,
                vol.Required("port", default=self.config_entry.data["port"]): int,
                vol.Required("password", default=self.config_entry.data["password"]): str,
            }),
            errors=errors,
        )