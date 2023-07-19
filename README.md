### Stat-Connect

A light-weight Python based cmdline tool to get live updates of your PC's stats like temperature on a phone app.

## Installation and Running
- Install the latest version of Python 3
- Clone this repo
- Install the following packages through `pip`: `psutil`, `py3nvml`, `pythonnet`
- Open Powershell **as an administrator** (required; CPU temperatures might not be accessible without admin privileges)
- Run the command `python path/to/dir/main.py`

## Features Included
- CPU and GPU temperatures on commandline

## Planned Features
- GUI for Windows Client
- Sync data with Firebase
- Phone application to display the temperature and other stats in real-time

## Compatibility
- **OS**: Windows
- **CPU**: Intel (tested and verified), AMD (untested)
- **GPU**: nVidia (tested and verified), AMD (untested)
