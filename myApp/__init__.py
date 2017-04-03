from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('../config/appSettings.py')
app.config.from_object('config.appProperties')


from myApp.views import views

app.register_blueprint(views.mod)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
