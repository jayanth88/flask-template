from flask import Blueprint, render_template, jsonify
from myApp.controller import Controller
from myApp.controller import ConfigController
from myApp.controller import global_func as globalF

mod = Blueprint('view',__name__,url_prefix='/view')

controller = Controller()
confController = ConfigController()

@mod.route('/')
def hello():
    result = globalF() + controller.local_func("test") + confController.getConf();
    return result
