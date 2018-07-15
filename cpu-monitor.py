import time
import psutil
import socket
import requests


# Function to make HTTP GET request
def http_get(endpoint, db, query):
        host = 'http://localhost:8086/'
        r = requests.get(url = host + endpoint, params = {'db': db, 'q': query})
        return r


# Function to make HTTP POST request
def http_post(endpoint, db, data):
        print('METHOD   : POST')

        host = 'http://localhost:8086/'
        print('URL      : ' + host + endpoint + 'db=' + db + '&precision=ms')
        print('DATA     : ' + data)

        r = requests.post(url = host + endpoint + 'db=' + db, data = data)
        print('RESPONSE : ' + str(r) + '\n')

        return r


# Function to get no of open ports
def get_no_of_open_ports():
        ports = set()
        connections =  psutil.net_connections(kind='all')
        for connection in connections:
                ports.add(connection.laddr.port)

        return len(ports)


# Function to get current time in millis
current_milli_time = lambda: int(round(time.time() * 1000))



########################################################################
# Code starts here
########################################################################

# Create DB in InfluxDB
print(http_post('query?', '', 'CREATE DATABASE cpu_monitor'))

# Name of host machine
name = socket.gethostname()
print('Name: ' + name)

# Continuously sending cpu stats through HTTP POST method to InfluxDB (every 1 second)
while True:
        cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
        no_of_process = len(psutil.pids())
        no_of_open_ports = get_no_of_open_ports()

        query = 'logs,' + \
                'machine_name=' + name + \
                ' usage=' + str(cpu_usage) + ',no_of_process=' + str(no_of_process) + ',no_of_open_ports=' + str(no_of_open_ports) + \
                ' ' + str(current_milli_time())
        http_post('write?', 'cpu_monitor', query)

        time.sleep(1)
