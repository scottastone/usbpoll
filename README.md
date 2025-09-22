# usbpoll

A simple USB device poller that works on Windows and Linux.

## How to Run

0. **Setup (yes there is a step 0):**

    If you are using `uv`, simply use `uv sync` and it will pull dependencies based on your OS.

    If you are old school, on Windows you will need:
    ```bash
    pip install wmi tabulate
    ```

    and on Linux:
    ```bash
    pip install pyudev tabulate
    ```

1.  **Clone the repository (or download `usbpoll.py`):**

    ```bash
    git clone https://github.com/your-username/usbpoll.git
    cd usbpoll
    ```

2.  **Execute the script:**

    ```bash
    python usbpoll.py
    ```

    or if you use `uv`

    ```bash
    uv run usbpoll.py
    ```

    Sample output: 
    ```
    Polling for available USB devices...

    --- Connected USB Devices ---
    +---------------+----------------------------------+------------------+-----------+--------------+
    | Device Name   | Description                      | Manufacturer     | Status    | Device ID    |
    +===============+==================================+==================+===========+==============+
    | 2.0 root hub  | EHCI_Host_Controller             | Linux Foundation | Connected | ID 1d6b:0002 |
    +---------------+----------------------------------+------------------+-----------+--------------+
    | 1.1 root hub  | Generic_Platform_OHCI_controller | Linux Foundation | Connected | ID 1d6b:0001 |
    +---------------+----------------------------------+------------------+-----------+--------------+
    | 2.0 root hub  | EHCI_Host_Controller             | Linux Foundation | Connected | ID 1d6b:0002 |
    +---------------+----------------------------------+------------------+-----------+--------------+
    | 1.1 root hub  | Generic_Platform_OHCI_controller | Linux Foundation | Connected | ID 1d6b:0001 |
    +---------------+----------------------------------+------------------+-----------+--------------+
    | 2.0 root hub  | EHCI_Host_Controller             | Linux Foundation | Connected | ID 1d6b:0002 |
    +---------------+----------------------------------+------------------+-----------+--------------+
    | 1.1 root hub  | Generic_Platform_OHCI_controller | Linux Foundation | Connected | ID 1d6b:0001 |
    +---------------+----------------------------------+------------------+-----------+--------------+
    ```

## Building an Executable with PyInstaller

You can package `usbpoll` into a standalone executable using PyInstaller, so it can be run without a Python interpreter installed.

1.  **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

    Note: if you used `uv` earlier, pyinstaller comes installed in the `.venv/` environment.

2.  **Build the executable:**

    Navigate to the directory containing `usbpoll.py` in your terminal and run:

    ```bash
    pyinstaller --onefile usbpoll.py
    ```

    This command will create a `dist` directory containing the `usbpoll.exe` (or `usbpoll`) executable.