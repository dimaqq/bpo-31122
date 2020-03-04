### Reproduce BPO-31122

`client.py` → `interposer.py` → `httpbin.org`
(local port) `localhost:31122` `httpbin.org:443`

Run the interposer, that acts as man-in-the-middle and closes client's connection after specific number of bytes delivered from upstream to the client.

```sh
> python interposer.py
# ignore errors
```

Now run the client:

```py
> python client.py
Traceback (most recent call last):
  File "client.py", line 7, in <module>
    sock = ssl.create_default_context().wrap_socket(s, server_hostname="httpbin.org")
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/ssl.py", line 1040, in _create
    self.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
OSError: [Errno 0] Error
```
