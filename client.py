import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 2123))

sock = ssl.create_default_context().wrap_socket(s, server_hostname="httpbin.org")
