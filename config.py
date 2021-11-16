#import os
class Config:
    '''
    General configuration parent class
    '''
    #NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=a0811784c6544548b7bef41c29abb906'
    #NEWS_API_KEY = os.environ.get('a0811784c6544548b7bef41c29abb906')
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

