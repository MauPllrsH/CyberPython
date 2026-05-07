# CyberPython

A collection of Python projects for learning cybersecurity concepts hands-on.

## Scanner

### v1.0 — Port Scanner

A TCP connect port scanner built with Python's `socket` library.

**Features**
- Scan a single port or a port range
- Accepts IPv4 addresses or hostnames (auto-resolves via DNS)
- Configurable connection timeout
- Graceful handling of Ctrl+C interrupts
- Reports total scan time

**Usage**
```bash
python scanner.py -t <target> -p <port|range> [--timeout <seconds>]
```

**Examples**
```bash
# Single port
python scanner.py -t scanme.nmap.org -p 80

# Port range
python scanner.py -t 192.168.1.1 -p 1-1024

# Custom timeout
python scanner.py -t example.com -p 1-100 --timeout 2.0
```

**Sample output**
```
[*] Resolved scanme.nmap.org to 45.33.32.156
[*] Preparing list of ports to scan.

[*] Scanning port range 20-100 on target with IP 45.33.32.156.

[+] Port 22 is open.
[+] Port 80 is open.

[*] Total time: 8.2341 seconds
```
