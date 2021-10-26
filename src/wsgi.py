from app.main import create_application

server = create_application()

if __name__ == "__main__":
    server.run(host='0.0.0.1', port=8080)