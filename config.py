import os

BROKER_URL = os.environ.get("BROKER_URL") or "redis://127.0.0.1:6379/0"
RESULT_BACKEND = os.environ.get("RESULT_BACKEND") or "db+mysql+pymysql://root:123456@127.0.0.1:3306/celery?charset=utf8mb4"

class Config(object):
    enable_utc = False
    timezone = "Asia/Shanghai"
    result_extended = True
    
class TestingConfig(Config):
    pass

class DevelopmentConfig(Config):
    broker_url = BROKER_URL
    result_backend = RESULT_BACKEND

class ProductionConfig(Config):
    broker_url = BROKER_URL
    result_backend = RESULT_BACKEND
    
celery_config_map = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

