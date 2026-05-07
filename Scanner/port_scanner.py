import socket, time, argparse, sys

def parse_port_range(port: str):
    print("[*] Preparing list of ports to scan.\n")
    separator_index = port.index('-')
    initial_port = int(port[0:separator_index])
    final_port = int(port[separator_index+1:])
    ports = []
    for i in range(initial_port, final_port + 1):
        ports.append(i)

    return ports

def scan_port(target: str, port: int, timeout: float) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((target, port))
        is_open = (result == 0)
        if is_open:
            print(f"[+] Port {port} is open.")
        return is_open
    finally:
        sock.close()
    
def scan_target(target: str, ports: list[int], timeout: float):
    print(f"[*] Scanning port range {ports[0]}-{ports[-1]} on target with IP {target}.\n")
    
    for port in ports:
        scan_port(target, port, timeout)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port(s) to scan | -p 80 for singular port | -p 1-1024 for port range", required=True, type=str)
    parser.add_argument("-t", "--target", help="IP of target", required=True, type=str)
    parser.add_argument("--timeout", help="Timeout", type=float, default=10.0)
    args = parser.parse_args()
    
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"[-] Could not resolve target: {args.target}")
        sys.exit(1)
    
    if target_ip != args.target:
        print(f"[*] Resolved {args.target} to {target_ip}")
    
    if '-' in args.port:
        port_list = parse_port_range(args.port)
    else:
        port_list = [int(args.port)]
    
    start_time = time.perf_counter()
    try:
        scan_target(target_ip, port_list, args.timeout)
    except KeyboardInterrupt:
        print("\n[-] Scan interrupted by user.")
    finally:
        elapsed = time.perf_counter() - start_time
        print(f"\n[*] Total time: {elapsed:.4f} seconds")
    
    
if __name__ == "__main__":
    main()
