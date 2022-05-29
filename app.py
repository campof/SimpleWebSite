from flask import Flask
from flask import render_template
import yaml
import SimpleWebSite.settings as config

app = Flask(__name__)
site_config=config.load_config("config/settings.yaml")
for x,y in site_config['flask'].items():
    app.config[x] = y

@app.route("/")
def home_page():
    return render_template('v1/template.html', title=site_config["site"]["title"])

@app.route("/about")
def about_page():
    return render_template('v1/template.html', title=site_config["site"]["title"])

if __name__ == '__main__':
    app.run(extra_files=["config/settings.yaml"])
