 import base64
 import json
 import socket
from pathlib import Path
 from time import sleep
 
 from clan_cli.errors import ClanError
 #   - no need to initialize by asking for capabilities
 #   - results need to be base64 decoded
 class QgaSession:
    def __init__(self, socket_file: Path | str) -> None:
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # try to reconnect a couple of times if connection refused
        for _ in range(100):
            try:
                self.sock.connect(str(socket_file))
            except ConnectionRefusedError:
                sleep(0.1)
            else:
                return
        self.sock.connect(str(socket_file))
 
     def get_response(self) -> dict:
         result = self.sock.recv(9999999)