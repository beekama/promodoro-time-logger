from dotenv import load_dotenv
from server.main import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
        app.run(host="::", port=5005, debug=True)
