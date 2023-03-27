from flask import Flask

app = Flask(__name__)

@app.route("/hello-world")
def hello_world():
    return 'Привет, мир!'

@app.route("/goodbye-world")
def goodbye_world():
    return 'Прощай, мир!'

@app.errorhandler(404)
def site_map(e: 404):
    links = []
    html = "Страница, которую вы пытаетесь найти не найдены, пожалуйста выберите любую из возможных страниц: <br>"
    for rule in app.url_map.iter_rules():
        links.append(str(rule))
    for link in links[1:]:
        html += f"<a href='http://127.0.0.1:5000/{link}'>{link}</a><br>"
    return html

if __name__ == '__main__':
    app.run(debug=True)