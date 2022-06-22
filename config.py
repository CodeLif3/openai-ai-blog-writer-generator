##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

    
config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
