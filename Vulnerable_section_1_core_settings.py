 import dj_database_url
 from dotenv import load_dotenv
 
 ENV_STATE = os.getenv("ENV_STATE")
 
 BASE_DIR = Path(__file__).resolve().parent.parent