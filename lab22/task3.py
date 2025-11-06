import socket

def scan_ports(target_host, port_range=(1, 1024)):
    """
    Simple network port scanner.
    Scans the ports on the given target_host within port_range (inclusive).
    Returns a list of open ports.
    """
    open_ports = []
    print(f"Scanning {target_host} for open ports {port_range[0]}-{port_range[1]}...")
    for port in range(port_range[0], port_range[1]+1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass  # Ignore errors for now (e.g., host unreachable)
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"Open ports: {open_ports}")
    return open_ports

if __name__ == "__main__":
    print("=== Simple Network Port Scanner ===")
    target = input("Enter target host (e.g., 127.0.0.1): ").strip()
    port_start = input("Enter start port [default 1]: ").strip() or "1"
    port_end = input("Enter end port [default 1024]: ").strip() or "1024"
    try:
        port_start = int(port_start)
        port_end = int(port_end)
        scan_ports(target, (port_start, port_end))
    except Exception as e:
        print("Invalid port range entered.")

    print("\n--- Discussion ---")
    print("""
This network port scanner demonstrates a classic 'dual-use' dilemma.
Ethical cybersecurity professionals use such tools to audit their own systems, check for vulnerabilities, and fix misconfigurations.
However, malicious actors can use the same code to find and exploit weaknesses in unauthorized systems.

Should AI refuse to generate code like this?
On one hand, refusal could prevent some harm. On the other, port scanning is widely documented, and refusal could limit legitimate security research and education.
AI could, instead of outright refusing, warn users about ethical/legal considerations and encourage responsible use.
Ultimately, the responsibility lies with both tool creators and users: AI and developers should promote ethical use, provide disclaimers, and avoid advanced exploit code, while users must obey the law and obtain proper authorization for any testing.

Where to draw the line? Basic tools with educational context may be acceptable.
Generating code for exploitation or illegal access should be refused.
""")
