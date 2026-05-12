# CyberPython
A collection of Python projects for learning cybersecurity concepts hands-on.

## Scanner

### v2.0 — Port Scanner
A TCP connect port scanner with structured results, verbosity control, and response time reporting.

**Features**
- Scan a single port or a port range
- Accepts IPv4 addresses or hostnames (auto-resolves via DNS)
- Configurable connection timeout
- Per-port response time reporting
- Verbosity flags: `-v` for debug output, `-q` for warnings/errors only
- Graceful handling of Ctrl+C interrupts
- Reports total scan time

**Usage**
```bash
python scanner.py -t  -p  [--timeout ] [-v | -q]
```

**Examples**
```bash
# Single port
python scanner.py -t scanme.nmap.org -p 80

# Port range
python scanner.py -t 192.168.1.1 -p 1-1024

# Custom timeout with verbose output
python scanner.py -t example.com -p 1-100 --timeout 2.0 -v

# Quiet mode (warnings and errors only)
python scanner.py -t 10.0.0.1 -p 1-65535 -q
```

**Sample output**
[INFO] Resolved scanme.nmap.org to 45.33.32.156
[INFO] Scanning port range 20-100 on target with IP 45.33.32.156.
[+] Port 22 is open! ---- Response 0.00412s
[+] Port 80 is open! ---- Response 0.00387s
[INFO] Total time: 8.2341 seconds

---

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
[] Resolved scanme.nmap.org to 45.33.32.156
[] Preparing list of ports to scan.
[] Scanning port range 20-100 on target with IP 45.33.32.156.
[+] Port 22 is open.
[+] Port 80 is open.
[] Total time: 8.2341 seconds
