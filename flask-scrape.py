from flask import Flask, render_template,request, jsonify
from src.scrape import anime,save_img,image_link
import json


app = Flask(__name__)
@app.route('/')
def index():
    if config['save_img']=='True':
        img_link = anime(config['website'])
        save_img(img_link)
        return "<h2>scrapping<h2>"
    if config['show_web']=='True':
        img_link = anime(config['website'])
        return render_template('index.html', **locals())
    else:
        img_link=image_link(config["image_path"])
        return render_template('index.html', **locals())


if __name__ == '__main__':
    with open('./config/web.json') as json_file:
        config = json.load(json_file)
    app.run(debug=True)