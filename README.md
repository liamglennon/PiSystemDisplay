# Raspberry Pi System Display for Remote Windows Monitoring

This project uses a Raspberry Pi to visually monitor system metrics from a Windows PC. It runs a Python-based Flask server on the Windows machine and displays real-time system stats in a full-screen terminal on the Raspberry Pi.

## Project Features

- Displays CPU, memory, disk usage, temperature, fan speed, and power status
- Lightweight Flask server on Windows
- Terminal-based dashboard on the Raspberry Pi
- Launches automatically in fullscreen
- Designed for use with a Raspberry Pi running Raspberry Pi OS with a GUI

## Requirements

### On Windows PC

- Python 3
- `psutil`
- `flask`

Install required packages:

```bash
pip install flask psutil 
```

### On Raspberry Pi
Python 3
- `requests`
- `wmctrl`
- A display and GUI environment

```bash
sudo apt install wmctrl -y
pip3 install requests
```

### Setup
## Windows Flask Server
system_metrics.py

```bash
python system_metrics.py
```
Ensure port 5000 is allowed through your Windows firewall.


## Raspberry Pi Display Script
```bash
python system_metrics.py
```

## Future Improvements
- Add Raspberry Pi self-monitoring

- Include network usage and GPU stats

- Add error logs and retry logic

- Better GUI 
