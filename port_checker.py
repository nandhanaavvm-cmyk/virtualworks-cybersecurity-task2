import socket

def check_port(host, port, timeout=2.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            return result == 0
    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{host}'.")
        return None
    except socket.error as err:
        print(f"Socket error: {err}")
        return None


def main():
    print("=== Port Status Checker ===")
    host = input("Enter target host or IP (press Enter for 127.0.0.1): ").strip()
    if not host:
        host = "127.0.0.1"

    port_input = input("Enter port number to scan (1-65535): ").strip()

    if not port_input.isdigit():
        print("Error: Please enter a valid numeric port.")
        return

    port = int(port_input)
    if not (1 <= port <= 65535):
        print("Error: Port number must be between 1 and 65535.")
        return

    print(f"\nScanning {host} on port {port}...")
    status = check_port(host, port)

    if status is True:
        print(f"Result: Port {port} is OPEN on {host}.")
    elif status is False:
        print(f"Result: Port {port} is CLOSED or filtered on {host}.")


if __name__ == "__main__":
    main()
