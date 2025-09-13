# Red Team Port Scanner

This project contains a simple **Python port scanner** that demonstrates one of the basic skills used in red‑team engagements: **service enumeration**. During a red‑team assessment, ethical hackers often scan a range of ports on authorized systems to identify open services and potential attack surfaces. Understanding how to enumerate services is fundamental to effective offensive security work.

## Overview

The included `port_scanner.py` script uses Python’s built‑in `socket` module to attempt TCP connections to a specified host. It reports which ports respond and calculates the total scan duration. By default, it scans ports 1 through 1024, but you can specify a custom range on the command line.

### Features

- **Configurable port range:** Specify start and end ports from the command line.
- **Timeout control:** Uses a reasonable connection timeout to avoid hanging on unreachable hosts.
- **User‑friendly output:** Prints each open port as it’s found and summarises the results at the end.

## Usage

> **Warning:** Scanning systems without explicit authorization is unethical and may be illegal. Always obtain permission before testing any network or host.

```
python3 port_scanner.py <host> [start_port] [end_port]
```

**Examples**

Scan the first 1024 ports on `scanme.nmap.org`:

```
python3 port_scanner.py scanme.nmap.org
```

Scan ports 20–25 on a host:

```
python3 port_scanner.py 192.168.1.10 20 25
```

## License

This project is provided for educational purposes. You may modify and use the code under the terms of the MIT License. See the [LICENSE](LICENSE) file (if provided) for details.

## Disclaimer

The author is not responsible for misuse of this tool. Use it **only** on systems you own or have been authorized to test. Ethical hacking involves obeying laws, respecting privacy, and ensuring that your actions improve security rather than cause harm.
