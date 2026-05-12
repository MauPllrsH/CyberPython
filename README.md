# CyberPython
A collection of Python projects for learning cybersecurity concepts hands-on.

## Scanner

### v3.0 — Port Scanner
A concurrent TCP connect port scanner with optional banner grabbing.

**Features**
- Scan a single port or a port range
- Accepts IPv4 addresses or hostnames (auto-resolves via DNS)
- Concurrent scanning via thread pool (`--threads`)
- Optional banner grabbing on open ports (`--service`)
- Configurable connection timeout
- Per-port response time reporting
- Verbosity flags: `-v` for debug output, `-q` for warnings/errors only
- Graceful handling of Ctrl+C interrupts
- Reports total scan time

**Usage**
```bash
python scanner.py -t  -p  [--timeout ] [--threads ] [--service] [-v | -q]
```

**Examples**
```bash
# Single port
python scanner.py -t scanme.nmap.org -p 80

# Port range
python scanner.py -t 192.168.1.1 -p 1-1024

# With banner grabbing
python scanner.py -t scanme.nmap.org -p 1-1024 --service

# Custom threads and timeout
python scanner.py -t 10.0.0.1 -p 1-65535 --threads 200 --timeout 2.0

# Quiet mode
python scanner.py -t 10.0.0.1 -p 1-1024 -q
```

**Sample output**
```bash
[INFO] Resolved scanme.nmap.org to 45.33.32.156
[INFO] Scanning port range 20-100 on target with IP 45.33.32.156.
[INFO] Number of threads: 100.
[INFO] Performing banner scan!
[+] Port 22 is open! ---- Response 0.00412s
Port 22 responded with following banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
```
[+] Port 80 is open! ---- Response 0.00387s
[INFO] Total time: 1.2341 seconds
