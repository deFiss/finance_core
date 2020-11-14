from main import Server
from dotenv import load_dotenv

load_dotenv()
app = Server().config_app()
