from src.connections.server import Server

if __name__ == '__main__':
    server = Server('0.0.0.0', 6980, '/Users/blu/Desktop/server').main()