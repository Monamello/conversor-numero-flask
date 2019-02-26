from flask import Flask, jsonify
import conversor
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/extensao/<string:num>")
def hello(num):
    # num = int(num)
    return jsonify({'extenso': conversor.get_extenso(str(num))})