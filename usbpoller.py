import sys
from tabulate import tabulate

def get_usb_devices_windows():
    """
    Queries WMI for connected USB devices and returns a list of them.
    Each device is represented as a dictionary of its properties.
    """
    import wmi

    try:
        c = wmi.WMI()
    except wmi.x_wmi as e:
        print(f"Error connecting to WMI: {e}")
        print("Please ensure you are running this script with sufficient privileges.")
        return []

    usb_devices = []
    # Query Win32_PnPEntity to find devices with a DeviceID containing 'USB\'
    # This is a reliable way to identify USB-connected hardware.
    for device in c.Win32_PnPEntity():
        if device.DeviceID and 'USB\\' in device.DeviceID:
            device_info = {
                "Name": device.Name or "N/A",
                "Device ID": device.DeviceID,
                "Description": device.Description or "N/A",
                "Manufacturer": device.Manufacturer or "N/A",
                "Status": device.Status or "N/A",
            }
            usb_devices.append(device_info)
    return usb_devices

def get_usb_devices_linux():
    """
    Uses pyudev to find connected USB devices and returns a list of them.
    Each device is represented as a dictionary of its properties.
    """
    import pyudev

    usb_devices = []
    try:
        context = pyudev.Context()
        for device in context.list_devices(subsystem='usb', DEVTYPE='usb_device'):
            device_info = {
                "Name": device.get('ID_MODEL_FROM_DATABASE') or device.get('ID_MODEL', 'N/A'),
                "Device ID": f"ID {device.get('ID_VENDOR_ID')}:{device.get('ID_MODEL_ID')}",
                "Description": device.get('ID_MODEL', 'N/A'),
                "Manufacturer": device.get('ID_VENDOR_FROM_DATABASE') or device.get('ID_VENDOR', 'N/A'),
                "Status": "Connected", # pyudev typically only shows connected devices
            }
            usb_devices.append(device_info)
    except ImportError:
        print("The 'pyudev' library is required on Linux. Please install it using 'pip install pyudev'.")
        return []
    except Exception as e:
        print(f"An error occurred on Linux: {e}")
        return []
    return usb_devices

def get_usb_devices():
    """
    Detects the OS and calls the appropriate function to get USB devices.
    """
    if sys.platform == 'win32':
        return get_usb_devices_windows()
    elif sys.platform.startswith('linux'):
        return get_usb_devices_linux()
    else:
        print(f"Unsupported operating system: {sys.platform}")
        return []

def display_devices_table(devices):
    """
    Displays the list of devices in a formatted table in the command line.
    """
    if not devices:
        print("No USB devices found.")
        return

    # Prepare data for tabulate
    headers = ["Device Name", "Description", "Manufacturer", "Status", "Device ID"]
    table_data = [
        [
            device.get("Name", "N/A"),
            device.get("Description", "N/A"),
            device.get("Manufacturer", "N/A"),
            device.get("Status", "N/A"),
            device.get("Device ID", "N/A"),
        ]
        for device in devices
    ]

    # Print the table
    print("\n--- Connected USB Devices ---")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"\nFound {len(devices)} USB device(s).")

if __name__ == "__main__":
    print("Polling for available USB devices...")
    all_devices = get_usb_devices()
    display_devices_table(all_devices)
