from flask import Flask, jsonify
import conversor
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/extensao/<string:num>")
def hello(num):
    try:
        int(num)
        return jsonify({'extenso': conversor.get_extenso(str(num))}), 200
    except:
        return jsonify({'erro': 'Esse parâmetro não é um número.'}), 400