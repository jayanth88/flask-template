import os
from myApp import app


def global_func():
    return "prefix - "

class Controller:

    def local_func(self,query):
        print app.config['DEBUG']
        return "result"


class ConfigController:

    def getConf(self):
        return str(" "+app.config['ACCESS_KEY'])
