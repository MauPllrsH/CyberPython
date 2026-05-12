from dataclasses import dataclass
import socket, time, argparse, sys, logging

logger = logging.getLogger(__name__)

@dataclass
class ScanResult:
    port: int
    state: str
    response_time: float

def parse_port_range(port: str) -> list[int]:
    logger.debug("Preparing list of ports to scan.")
    separator_index = port.index('-')
    initial_port = int(port[0:separator_index])
    final_port = int(port[separator_index+1:])
    ports = []
    for i in range(initial_port, final_port + 1):
        ports.append(i)

    return ports

def scan_port(target: str, port: int, timeout: float) -> ScanResult:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        start = time.perf_counter()
        result = sock.connect_ex((target, port))
        elapsed = time.perf_counter() - start
        is_open = "open" if (result == 0) else "closed"
        return ScanResult(port=port, state=is_open, response_time=elapsed)
    finally:
        sock.close()
    
def scan_target(target: str, ports: list[int], timeout: float) -> list[ScanResult]:
    logger.info(f"Scanning port range {ports[0]}-{ports[-1]} on target with IP {target}.")
    results = []
    for port in ports:
        result = scan_port(target, port, timeout)
        results.append(result)
    return results

def print_results(results: list[ScanResult]) -> None:
    for result in results:
        if result.state == "open":
            print(f"[+] Port {result.port} is {result.state}! ---- Response {result.response_time:.5f}s")
    

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port(s) to scan | -p 80 for singular port | -p 1-1024 for port range", required=True, type=str)
    parser.add_argument("-t", "--target", help="IP of target", required=True, type=str)
    parser.add_argument("--timeout", help="Timeout", type=float, default=10.0)
    
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument("-v", "--verbose", help="Show debugging messages", action="store_true")
    verbosity.add_argument("-q", "--quiet", help="Show only warnings and errors", action="store_true")

    args = parser.parse_args()
    
    if args.verbose:
        level = logging.DEBUG
    elif args.quiet:
        level = logging.WARNING
    else:
        level = logging.INFO
        
    logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")
    
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        logger.error(f"Could not resolve target: {args.target}")
        sys.exit(1)
    
    if target_ip != args.target:
        logger.info(f"Resolved {args.target} to {target_ip}")
    
    if '-' in args.port:
        port_list = parse_port_range(args.port)
    else:
        port_list = [int(args.port)]
    
    start_time = time.perf_counter()
    try:
        results = scan_target(target_ip, port_list, args.timeout)
        print_results(results)
    except KeyboardInterrupt:
        logger.warning("Scan interrupted by user.")
    finally:
        elapsed = time.perf_counter() - start_time
        logger.info(f"Total time: {elapsed:.4f} seconds")
    
    
if __name__ == "__main__":
    main()
