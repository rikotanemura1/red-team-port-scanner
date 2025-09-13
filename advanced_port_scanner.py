#!/usr/bin/env python3

"""
Advanced Port Scanner Script
----------------------------

This script performs a multi-threaded TCP port scan against a specified host. It scans a range of ports concurrently and optionally grabs banner information from each open port. This advanced tool can help you learn key red team skills: service enumeration, concurrency, and banner grabbing.

Usage:
    python3 advanced_port_scanner.py <host> [start_port] [end_port] --threads <num_threads> [--banner]

Arguments:
    host        IP address or hostname to scan (e.g. 127.0.0.1 or example.com)
    start_port  First port number in the range (default: 1)
    end_port    Last port number in the range (default: 1024)
Options:
    -t, --threads       Number of concurrent threads to use (default: 100)
    -b, --banner        Attempt to grab banner information from open ports.

Example:
    python3 advanced_port_scanner.py scanme.nmap.org 20 25 --threads 50 --banner

Note: Scanning systems without permission is unethical and illegal. Only use this tool against systems you own or have explicit authorization to test.
"""

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host, port, banner=False, timeout=1.0):
    """Scan a single port on the host and optionally grab banner information."""
    result = {"port": port, "open": False, "banner": None}
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((host, port)) == 0:
                result["open"] = True
                if banner:
                    try:
                        sock.sendall(b"\r\n")
                        data = sock.recv(1024)
                        result["banner"] = data.decode(errors="ignore").strip()
                    except Exception:
                        result["banner"] = None
    except Exception:
        pass
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Multi-threaded port scanner with optional banner grabbing"
    )
    parser.add_argument("host", help="target host to scan")
    parser.add_argument("start_port", nargs="?", type=int, default=1,
                        help="start port number (default: 1)")
    parser.add_argument("end_port", nargs="?", type=int, default=1024,
                        help="end port number (default: 1024)")
    parser.add_argument("-t", "--threads", type=int, default=100,
                        help="number of threads to use (default: 100)")
    parser.add_argument("-b", "--banner", action="store_true",
                        help="grab banner information from open ports")
    args = parser.parse_args()

    host = args.host
    start = args.start_port
    end = args.end_port
    threads = args.threads
    banner = args.banner

    print(f"Scanning {host} from port {start} to {end} with {threads} threads "
          f"(banner grabbing: {'enabled' if banner else 'disabled'})...")

    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(scan_port, host, port, banner): port
            for port in range(start, end + 1)
        }
        for future in as_completed(futures):
            result = future.result()
            if result["open"]:
                open_ports.append(result)

    open_ports.sort(key=lambda x: x["port"])
    for entry in open_ports:
        port = entry["port"]
        banner_text = entry["banner"]
        if banner and banner_text:
            print(f"Port {port} is open - Banner: {banner_text}")
        else:
            print(f"Port {port} is open")

    print(f"Scan complete. {len(open_ports)} open ports found.")


if __name__ == "__main__":
    main()
