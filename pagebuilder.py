from flask import Flask, render_template
from flask_restful import Resource, Api

api_key = '76c8c5d6e44c3ba74340ca749a10cb24'

#open connection 
owm = pyowm.OWM(api_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

if __name__ == "__main__":
    app.run(debug = True)
