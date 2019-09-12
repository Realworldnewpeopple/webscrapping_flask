from flask import Flask, render_template,request, url_for,redirect
from src.scrape import anime,save_img,image_link
from src import save_json
import json

app = Flask(__name__)

@app.route('/picture')
def index():
    with open('./config/weblink.json') as json_file:
        webpage = json.load(json_file)
    if config['save_img']=='True':
        if config['user_input']=='True':
            img_link=anime([webpage['website']])
            save_img(img_link)
        else:
            img_link = anime(config['website'])
            save_img(img_link)
        return "<h2>scrapping<h2>"
    if config['show_web']=='True':
        if config['user_input'] == 'True':
            img_link = anime([webpage['website']])
        else:
            img_link = anime(config['website'])
        return render_template('index.html', **locals())
    else:
        img_link=image_link(config["image_path"])
        return render_template('index.html', **locals())

@app.route('/',methods=['POST','GET'])
def formweb():
    if request.method == 'POST':
        webpage = request.form.get('webpages')
        if len(list(webpage))>0:
            save_json.json_update(webpage)
            return redirect(url_for('index'))
        else:
            webpage=config['website'][0]
            save_json.json_update(webpage)
            return redirect(url_for('index'))
    return render_template('form.html', **locals())

if __name__ == '__main__':
    with open('./config/web.json') as json_file:
        config = json.load(json_file)
    app.run(debug=True)