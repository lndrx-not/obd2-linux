import socket

sock = socket.socket(
    socket.AF_BLUETOOTH,
    socket.SOCK_STREAM,
    socket.BTPROTO_RFCOMM,
)

sock.connect(("XX:XX:XX:XX:XX:XX", 1))

sock.send(b"ATZ\r")

response = sock.recv(1024)

print(response.decode(errors="ignore"))

sock.close()