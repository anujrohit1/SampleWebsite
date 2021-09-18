from socket import gethostbyname, gethostname

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    hostname = gethostname()
    ipaddress = gethostbyname(hostname)
    return render_template('index.html', hostname=hostname, ipaddress=ipaddress)


if __name__ == '__main__':
    app.run(port=8080)
