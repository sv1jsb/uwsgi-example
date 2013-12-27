from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    ret = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Feature A branch</title>
            </head>
            <body>
            <h1>Hello world!</h1>
            <h3>from feature-a branch</h3>
            <img src="/static/feature-a.png"/>
            </body>
            </html>
    """
    return ret


if __name__ == "__main__":
    app.run()