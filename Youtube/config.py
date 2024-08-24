import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("7476545767:AAGDc1h1y6PY93X5WEAEMznHT-80GHDxgdw", "")
    API_ID = int(os.environ.get("27284252", ))
    API_HASH = os.environ.get("12b5cf802b8f859d9506c91fee7a6c3b", "")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
