import os

from src.app.client_app import ClientApp

if __name__ == '__main__':
    client = ClientApp('127.0.0.1', 6968, f'/Users/blu/Desktop').main()