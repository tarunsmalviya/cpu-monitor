import time
import psutil
import socket

def get_no_of_open_ports():
        ports = set()
        connections =  psutil.net_connections(kind='all')
        for connection in connections:
                ports.add(connection.laddr.port)

        return len(ports)


count = psutil.cpu_count(logical=True)


while True:
        name = socket.gethostname()
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        no_of_process = len(psutil.pids())
        no_of_open_ports = get_no_of_open_ports()

        print(name)
        print(cpu_usage)
        print(no_of_process)
        print(no_of_open_ports)

        time.sleep(1)
