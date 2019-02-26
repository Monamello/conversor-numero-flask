from flask import Flask, jsonify
import conversor
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/extensao/<string:num>")
def hello(num):
    try:
        num_int = int(num)
        if num_int <= 99999 and num_int >= -99999:
            return jsonify({'extenso': conversor.get_extenso(str(num))}), 200
    except:
        pass
    return jsonify({'erro': 'Esse parâmetro não suportado.'}), 400