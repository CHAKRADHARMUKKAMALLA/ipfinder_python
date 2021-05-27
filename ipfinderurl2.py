import socket

hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

url = "paste the url here"
print("THE IP FOR " + url +"IS" ,socket.gethostbyname(url))
