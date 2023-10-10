from src.connections.client import Client

if __name__ == '__main__':
    client = Client('0.0.0.0', 8085, '/Users/blu/Desktop/client').main()