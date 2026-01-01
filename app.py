from dotenv import load_dotenv
import server.main as main

load_dotenv()

def createApp(environment=None, start_response=None):
    with main.app.app_context():
        main.create_app()
    return main.app
