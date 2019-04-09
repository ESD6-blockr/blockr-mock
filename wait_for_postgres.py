import os
import socket
import time

port = 5432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect((os.environ["DB_HOST"], port))
        s.close()
        break
    except socket.error:
        time.sleep(0.1)
