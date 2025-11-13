from dotenv import load_dotenv
import os

def load_environment():
    """
    Carga las variables desde .env si existe,
    de lo contrario las toma del sistema.
    """
    if os.path.exists(".mini"):
        load_dotenv()
    else:
        print("⚠️  No se encontró .mini, usando solo variables del sistema...")

class Settings:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    USER = os.getenv("USER", "unknown")
    HOSTNAME = os.getenv("HOSTNAME", "localhost")
    TZ = os.getenv("TZ", "UTC")
    LANG = os.getenv("LANG", "en_US.UTF-8")
    API_KEY = os.getenv("API_KEY", "dev-1234")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    def summary(self):
        return {
            "environment": self.ENVIRONMENT,
            "user": self.USER,
            "hostname": self.HOSTNAME,
            "timezone": self.TZ,
            "language": self.LANG,
            "api_key": self.API_KEY,
            "debug": self.DEBUG,
        }

settings = Settings()
