OBS Recording Status - Home Assistant Custom Component
This custom integration for Home Assistant allows you to monitor the recording status of OBS Studio (Open Broadcaster Software) using its WebSocket API. It provides a binary sensor that updates in real-time when OBS starts or stops recording.

Features
Real-Time Monitoring: Tracks the recording status of OBS Studio.

Easy Setup: Configure via the Home Assistant UI.

Lightweight: Uses the obsws-python library for efficient communication.

Customizable: Adjust the polling interval to suit your needs.

Prerequisites
OBS Studio installed and running.

OBS WebSocket Server enabled:

Open OBS → Tools → WebSocket Server Settings.

Enable "Enable WebSocket server".

Set a port (default: 4455) and password.

Click "Apply".

Home Assistant installed and running.

HACS (Home Assistant Community Store) installed. Install HACS.

Installation
Method 1: Install via HACS (Recommended)
Click the button below to automatically add this repository to HACS:

Open your Home Assistant instance and open the repository inside the Home Assistant Community Store.

In HACS, go to Integrations and search for "OBS Recording Status".

Click Install.

Restart Home Assistant.

Method 2: Manual Installation
Download this repository.

Copy the obs_recording folder to your Home Assistant custom_components directory:

Copy
config/custom_components/obs_recording/
Restart Home Assistant.

Configuration
Go to Settings > Devices & Services > Integrations.

Click Add Integration and search for "OBS Recording Status".

Enter the following details:

Host: IP address of the machine running OBS (e.g., 192.168.1.100).

Port: WebSocket server port (default: 4455).

Password: WebSocket server password.

Click Submit.

Usage
Once configured, a new binary sensor will be created:

Entity ID: binary_sensor.obs_recording_status

State:

on: OBS is recording.

off: OBS is not recording.

You can use this sensor in automations, scripts, or dashboards. For example:

yaml
Copy
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

Ensure OBS is running and the WebSocket server is enabled.

Verify the host, port, and password are correct.

Check your firewall settings to allow communication between Home Assistant and OBS.

Errors in the logs:

Enable debug logging by adding the following to your configuration.yaml:

yaml
Copy
logger:
  default: info
  logs:
    custom_components.obs_recording: debug
    obsws_python: debug
Restart Home Assistant and check the logs for detailed error messages.

Connection issues:

Ensure the OBS WebSocket server is accessible from the Home Assistant machine.

Test connectivity using a tool like telnet or curl.

Development
Requirements
Python 3.9+

obsws-python library

Home Assistant Dev Container (optional)

Testing
Clone this repository.

Copy the obs_recording folder to your Home Assistant custom_components directory.

Restart Home Assistant.

Add the integration via the UI and test.

Debugging
Add breakpoints in VS Code.

Use the Home Assistant debugger to step through the code.

Check the logs for detailed output.

Contributing
Contributions are welcome! Please follow these steps:

Fork this repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OBS Studio for the amazing software.

obsws-python for the WebSocket client library.

Home Assistant Community for inspiration and support.

Support
If you find this integration useful, consider supporting the project:

⭐ Star this repository on GitHub.

🐛 Report issues or suggest features in the Issues section.

☕ Buy me a coffee: Donate.

Enjoy monitoring your OBS recordings in Home Assistant! 🎥

How to Use This README
Replace your_github_username and your_username with your GitHub username.

Replace obs_recording with the name of your repository if it’s different.

Add a LICENSE file to your repository if needed.

Customize the "Support" section with your donation links (optional).

Push the README.md file to your GitHub repository.

How the HACS Button Works
The button uses the my.home-assistant.io service to redirect users to their Home Assistant instance and automatically add the repository to HACS. It requires:

The repository to be public on GitHub.

HACS to be installed in the user’s Home Assistant instance.