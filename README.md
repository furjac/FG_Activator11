# Activator 11

A modern GUI application for Windows and Office activation utilities.

## Features

- Clean, modern interface using CustomTkinter
- Real-time command output display
- Dark/Light/System theme switching
- Process control with stop button functionality
- Easy access to all activation utilities in one place

## Available Utilities

### Main Utilities
- **Check Activation Status**: Verify the current activation status of Windows and Office
- **Change Windows Edition**: Modify your Windows edition
- **Change Office Edition**: Modify your Office edition
- **Extract OEM Folder**: Extract OEM information
- **Troubleshoot**: Run diagnostics and fix common activation issues

### Activation Tools
- **HWID Activation**: Permanent Windows activation using Hardware ID
- **KMS38 Activation**: Windows activation valid until 2038
- **Online KMS Activation**: Windows and Office activation using online KMS
- **Ohook Activation**: Office activation solution
- **TSforge Activation**: Advanced activation tool

## Requirements

- Python 3.7 or higher
- CustomTkinter
- Pillow (PIL)

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the application with Python:

```
python main.py
```

Then use the sidebar to select which utility or activation tool you want to run:
- Main utilities are displayed at the top
- Activation tools are highlighted in red
- The output will be displayed in the main window
- Long-running processes can be stopped with the Stop button

## Notes

- Some commands may require administrator privileges to run properly
- For best results, run the application as administrator
- Each utility executes the corresponding CMD file in the `activation` directory

## License

This software is provided as-is without any warranty. Use at your own risk. 