"""
Basic Port Scanner Script
------------------------

This script performs a simple TCP port scan against a specified host. It attempts to
connect to a range of ports and reports which ones are open. This kind of tool
demonstrates a fundamental red team skill: enumerating services on a target system
to identify potential entry points.

Usage:

```
python3 port_scanner.py <host> [start_port] [end_port]
```

* ``host``: IP address or hostname to scan (e.g. 127.0.0.1 or example.com)
* ``start_port``: First port number in the range (default: 1)
* ``end_port``: Last port number in the range (default: 1024)

Example:

```
python3 port_scanner.py scanme.nmap.org 20 25
```

Note: Scanning systems without permission is unethical and illegal. Only use this
tool against systems you own or have explicit authorization to test.
"""

import socket
import sys
from datetime import datetime


def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    """Attempt to connect to a TCP port on the given host.

    Args:
        host (str): The target hostname or IP address.
        port (int): The port number to scan.
        timeout (float): Timeout in seconds for the socket connection.

    Returns:
        bool: True if connection succeeds (port open), False otherwise.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        return result == 0


def port_scan(host: str, start_port: int = 1, end_port: int = 1024) -> list[int]:
    """Perform a port scan on the specified host.

    Args:
        host (str): Target hostname or IP address.
        start_port (int): Starting port number in the range to scan.
        end_port (int): Ending port number in the range to scan.

    Returns:
        list[int]: A list of open ports discovered.
    """
    open_ports = []
    print(f"Starting scan of {host} from port {start_port} to {end_port}...")
    start_time = datetime.now()
    try:
        for port in range(start_port, end_port + 1):
            if scan_port(host, port):
                open_ports.append(port)
                print(f"Port {port} is open")
    except KeyboardInterrupt:
        print("Scan interrupted by user.")
        sys.exit(0)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit(1)
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit(1)

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Scan completed in {duration.seconds} seconds. {len(open_ports)} open ports found.")
    return open_ports


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 port_scanner.py <host> [start_port] [end_port]")
        sys.exit(1)
    host = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    port_scan(host, start_port, end_port)


if __name__ == "__main__":
    main()
