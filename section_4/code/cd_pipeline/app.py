from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://ko.wikipedia.org/wiki/GIF#/media/%ED%8C%8C%EC%9D%BC:Rotating_earth_(large).gif",
    "https://media1.tenor.com/images/d278f33e1e8305c98f8f6cc8fb40d5ae/tenor.gif?itemid=10744149",
    "https://media1.tenor.com/images/e65cdc9ce37ae6c0223c4033a4d0a3cb/tenor.gif?itemid=4980602",
    "https://media1.tenor.com/images/2017f28c4a349252731718c556c91e16/tenor.gif?itemid=14266999",
    "https://media1.tenor.com/images/eaf41323dccd993b8cbda1d9e24088ae/tenor.gif?itemid=16016616"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
