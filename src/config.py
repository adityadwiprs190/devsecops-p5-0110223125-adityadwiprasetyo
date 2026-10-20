import os

class AppConfig:
    """Konfigurasi dasar aplikasi menggunakan environment variables agar aman."""
    APP_NAME = "SecureInventoryApp"
    VERSION = "1.0.0"
    DEBUG_MODE = os.getenv("APP_DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("APP_SECRET_KEY", "default-fallback-key-for-dev")
    MAX_LOGIN_ATTEMPTS = int(os.getenv("MAX_LOGIN_ATTEMPTS", "3"))

    @classmethod
    def get_summary(cls) -> dict:
        return {
            "app_name": cls.APP_NAME,
            "version": cls.VERSION,
            "debug": cls.DEBUG_MODE,
            "max_attempts": cls.MAX_LOGIN_ATTEMPTS,
        }