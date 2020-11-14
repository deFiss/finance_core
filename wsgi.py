from main import Server
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    app = Server().config_app()
