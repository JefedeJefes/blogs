from flask import Flask, render_template
import requests




app = Flask(__name__)



@app.route('/')
def home():
    url = "https://api.npoint.io/6b128354d6f7b1cd27aa"
    response = requests.get(url)
    data = response.json()
    return render_template("index.html",data=data)

@app.route('/post/<int:get_id>')
def get_data(get_id):
    url1 = "https://api.npoint.io/6b128354d6f7b1cd27aa"
    response = requests.get(url1)
    data = response.json()
    show_data = []
    for id_data in data:
        if id_data["id"] == get_id:
            show_data.append(id_data)


    return render_template("post.html",show_data=show_data)

if __name__ == "__main__":
    app.run(debug=True)
