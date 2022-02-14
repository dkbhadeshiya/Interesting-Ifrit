import os

from dotenv import load_dotenv


class DefaultConfig:
    """ Bot Configuration """
    load_dotenv()

    HOST = os.environ.get("HOST", "localhost")
    PORT = os.environ.get("PORT", 3978)
    APP_ID = os.environ.get("MICROSOFT_APP_ID", "")
    APP_PASSWORD = os.environ.get("MICROSOFT_APP_PASSWORD", "")
    ENTITY_DETECTION_API_URL = os.environ.get("ENTITY_DETECTION_API_URL", "")
    DICTIONARY_API_KEY = os.environ.get("DICTIONARY_API_KEY", "")
    ENABLE_LOGGER = os.environ.get("ENABLE_LOGGER", False)
    LUIS_APP_ID = os.environ.get("LUIS_APP_ID", "")
    LUIS_PREDICTION_ENDPOINT = os.environ.get("LUIS_PREDICTION_ENDPOINT", "")
    LUIS_PREDICTION_KEY = os.environ.get("LUIS_PREDICTION_KEY", "")


CONFIG = DefaultConfig()
