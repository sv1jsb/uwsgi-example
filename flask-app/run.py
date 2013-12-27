from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    ret = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Feature B branch</title>
            </head>
            <body>
            <h1>Hello world!</h1>
            <h3>from feature-b branch</h3>
            <img src="/static/feature-b.png"/>
            </body>
            </html>
    """
    return ret


if __name__ == "__main__":
    app.run()