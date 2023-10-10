import os

from src.app.server_app import ServerApp
from src.connections.server import Server

if __name__ == '__main__':
    server = ServerApp('127.0.0.1', 6968, f'/Users/blu/Desktop').main()