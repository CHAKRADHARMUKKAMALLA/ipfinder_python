import socket

hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

url = "www.chakradharreddy.me"
print("THE IP FOR " + url +"IS" ,socket.gethostbyname(url))