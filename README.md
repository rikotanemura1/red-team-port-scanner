# Red Team Port Scanner

This repository contains simple Python port scanner scripts that demonstrate basic red-team skills in service enumeration. During red-team assessments, ethical hackers often scan a range of ports on authorized systems to identify open services and potential attack surfaces. Understanding how to enumerate services is fundamental to offensive security work.

## Overview

The repository includes two Python scripts:

- **port_scanner.py** – A basic TCP port scanner that scans a target host over a configurable port range using synchronous connections. It allows you to specify start and end ports and uses a timeout to determine open ports.
- **advanced_port_scanner.py** – An enhanced scanner that performs multi-threaded scanning and can optionally grab banner information from services. It accepts optional start and end ports and a thread count to control concurrency. A `--banner` flag enables banner grabbing.

## Features

- Configurable port range (start and end ports)
- Multi-threaded scanning with configurable number of threads
- Optional banner grabbing using the `--banner` flag
- Timeout control to avoid hanging on unreachable hosts
- User-friendly output that prints open ports and banners
- Ethical use reminder to scan only authorized systems

## Usage

**Warning:** Scanning systems without explicit authorization is unethical and may be illegal. Use these scripts only on systems you own or have explicit permission to test.

### Basic scanner

```sh
python3 port_scanner.py <host> [start_port] [end_port]
```

Example: Scan the first 1024 ports on `scanme.nmap.org`:

```sh
python3 port_scanner.py scanme.nmap.org 1 1024
```

### Advanced scanner

```sh
python3 advanced_port_scanner.py <host> [start_port] [end_port] --threads <num_threads> [--banner]
```

Examples:

- Scan ports 1–1024 on a host using 100 threads:

```sh
python3 advanced_port_scanner.py example.com 1 1024 --threads 100
```

- Scan ports 20–25 and grab banners:

```sh
python3 advanced_port_scanner.py 192.168.1.10 20 25 --threads 50 --banner
```

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

## Disclaimer

This project is provided for educational purposes. Use it only on systems you own or have authorization to test. Ethical hacking involves obeying laws, respecting privacy and improving security rather than causing harm.
