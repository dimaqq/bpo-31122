import ssl
import socket

context = ssl.SSLContext()
context.load_verify_locations(cafile="ca.pem")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 2123))

sock = context.wrap_socket(s, server_hostname="localhost")
