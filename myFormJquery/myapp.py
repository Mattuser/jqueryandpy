import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def renderForm():
    return render_template("form.html")

@app.route("/api/result", methods=['POST'])
def getResult():
    json = request.get_json()
    first_name = json['first']
    last_name = json['last']
    favorite_team = json['combo']
    return jsonify(first_name=first_name, last_name=last_name, favorite_team=favorite_team)

    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)