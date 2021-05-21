import socket

hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

print("YOU ARE WORKING ON" +hostname)
print("YOUR IP IS" + myip)
