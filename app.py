from dotenv import load_dotenv
import server.main as main
import os

load_dotenv()

def createApp(environment=None, start_response=None):
    main.app.secret_key = os.environ["FLASK_SECRET_KEY"]
    with main.app.app_context():
        main.create_app()
    return main.app

if __name__ == "__main__":
    main.app.run(debug=True)
