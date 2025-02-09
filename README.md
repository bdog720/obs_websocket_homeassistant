# OBS Recording Status - Home Assistant Custom Component
This custom integration for Home Assistant allows you to monitor the recording status of OBS Studio (Open Broadcaster Software) using its WebSocket API. It provides a binary sensor that updates in real-time when OBS starts or stops recording.

---

## Features
- **Real-Time Monitoring**: Tracks the recording status of OBS Studio.
- **Easy Setup**: Configure via the Home Assistant UI.
- **Lightweight**: Uses the `obsws-python` library for efficient communication.
- **Customizable**: Adjust the polling interval to suit your needs.

---

## Prerequisites

1. **OBS Studio** installed and running.
2. **OBS WebSocket Server** enabled:
   - Open OBS → Tools → WebSocket Server Settings.
   - Enable "Enable WebSocket server".
   - Set a port (default: `4455`) and password.
   - Click "Apply".
3. **Home Assistant** installed and running.
4. **HACS (Home Assistant Community Store)** installed. [Install HACS](https://hacs.xyz/docs/setup/download).

---

## Installation

### Method 1: Install via HACS (Recommended)

1. Click the button below to automatically add this repository to HACS:
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=bdog720&repository=obs_websocket_homeassistant&category=integration)
2. In HACS, go to **Integrations** and search for "OBS Recording Status".
3. Click **Install**.
4. Restart Home Assistant.

### Method 2: Manual Installation
1. Download this repository.
2. Copy the `obs_recording` folder to your Home Assistant `custom_components` directory:
```
config/custom_components/obs_recording/
```
3. Restart Home Assistant.

---

## Configuration

1. Go to **Settings > Devices & Services > Integrations**.
2. Click **Add Integration** and search for "OBS Recording Status".
3. Enter the following details:
- **Host**: IP address of the machine running OBS (e.g., `192.168.1.100`).
- **Port**: WebSocket server port (default: `4455`).
- **Password**: WebSocket server password.
4. Click **Submit**.

---

## Usage

Once configured, a new binary sensor will be created:
- **Entity ID**: `binary_sensor.obs_recording_status`
- **State**:
- `on`: OBS is recording.
- `off`: OBS is not recording.

You can use this sensor in automations, scripts, or dashboards. For example:

```yaml
automation:
- alias: Notify when OBS starts recording
 trigger:
   platform: state
   entity_id: binary_sensor.obs_recording_status
   to: "on"
 action:
   service: notify.notify
   data:
     message: "OBS has started recording!"
Troubleshooting
Common Issues
Sensor shows as unavailable:
```

---

## Troubleshooting

### Common Issues

1. **Sensor shows as unavailable:**
  - Ensure OBS is running and the WebSocket server is enabled.
  - Verify the host, port, and password are correct.
  - Check your firewall settings to allow communication between Home Assistant and OBS.
2. **Errors in the logs:**
  - Enable debug logging by adding the following to your `configuration.yaml`:
    ```yaml
    logger:
      default: info
      logs:
        custom_components.obs_recording: debug
        obsws_python: debug
    ```
  - Restart Home Assistant and check the logs for detailed error messages.
3. **Connection issues**:
  - Ensure the OBS WebSocket server is accessible from the Home Assistant machine.
  - Test connectivity using a tool like `telnet` or `curl`.

---

## Development

### Requirements
- Python 3.9+
- `obsws-python` library
- Home Assistant Dev Container (optional)

### Testing
1. Clone this repository.
2. Copy the `obs_recording` folder to your Home Assistant `custom_components` directory.
3. Restart Home Assistant.
4. Add the integration via the UI and test.

### Debugging
1. Add breakpoints in VS Code.
2. Use the Home Assistant debugger to step through the code.
3. Check the logs for detailed output.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## Acknowledgments
- [OBS Studio](https://obsproject.com/) for the amazing software.
- [obsws-python](https://github.com/aatikturk/obsws-python) for the WebSocket client library.
- Home Assistant Community for inspiration and support.

---

## Support
If you find this integration useful, consider supporting the project:

- ⭐ Star this repository on GitHub.
- 🐛 Report issues or suggest features in the [Issues](https://github.com/bdog720/obs_websocket_homeassistant/issues) section.
- ☕ Buy me a coffee: [Donate](https://buymeacoffee.com/bdog720).

---

Enjoy monitoring your OBS recordings in Home Assistant! 🎥

---
