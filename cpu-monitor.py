import time
import psutil
import socket
import requests

def http_get(endpoint, db, query):
        host = 'http://localhost:8086/'
        r = requests.get(url = host + endpoint, params = {'db': db, 'q': query})
        return r.json()

def http_post(endpoint, db, query):
        host = 'http://localhost:8086/'
        r = requests.post(url = host + endpoint, params = {'db': db, 'q': query})
        return r.json()

# print(http_get('query', 'mydb', 'select * from cpu'))

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

        print('Name             : ' + name)
        print('CPU Usage        : ' + str(cpu_usage))
        print('No of Processes  : ' + str(no_of_process))
        print('No of Open Ports : ' + str(no_of_open_ports))
        print('\n')
        
        time.sleep(1)




