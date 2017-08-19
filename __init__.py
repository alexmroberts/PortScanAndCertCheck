import socket
import threading
import ssl
from queue import Queue

q = Queue()
max_threads = 100
starting_port = 1
max_port = 445
secure_ports = [22, 443, 465, 993, 995]
print_errors = False
ports_failed = []


host = input("Enter host to check (example: www.google.com): ")
print("Checking ports \n")




def port_scan(port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = socket.create_connection((host, port))
        with threading.Lock():
            print('Port', port, 'is open on', host)
            if port in secure_ports:
                cert_result = check_certificate(connection, port)
                print("Certificate expires:", cert_result['notAfter'])
        connection.close()
    except Exception as e:
        with threading.Lock():
            ports_failed.append("Port {} responded: {}".format(str(port), e))

def check_certificate(connection, port):
    cert_context = ssl.create_default_context()
    with cert_context.wrap_socket(connection, server_hostname=host) as cert:
        return cert.getpeercert()

def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()


for idx in range(max_threads):
    threads = threading.Thread(target=threader)
    threads.daemon = True
    threads.start()

for worker in range(starting_port, max_port):
    q.put(worker)

q.join()

if print_errors:
    for error in ports_failed:
        print(error)
