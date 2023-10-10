import os

from src.app.server_app import ServerApp

if __name__ == '__main__':
    server = ServerApp('127.0.0.1', 6967, f'/Users/blu/Desktop').main()