import psutil

def get_connections():
    results = []
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "ESTABLISHED":
            local_ip, local_port = conn.laddr
            remote_ip, remote_port = conn.raddr
            if conn.type=="SOCK_STREAM":
                proto = "TCP"
            else:
                proto = "UDP"

            results.append((local_ip, local_port, remote_ip, remote_port, proto))
    return results


