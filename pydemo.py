from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>DevOps Flask Application Hosted on pydemo.waqasazam.info on Digital Ocean 
and pushed via Jenkins from Github.com Alhamdullillah!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
