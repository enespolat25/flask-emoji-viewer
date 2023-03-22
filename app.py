from flask import Flask, render_template, url_for
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    image_files = []
    for filename in os.listdir('static'):
        if filename.endswith('.png'):
            image_files.append(filename)
    random_image = random.choice(image_files)
    return render_template('index.html', random_image=random_image)

if __name__ == "__main__":
    app.run()
