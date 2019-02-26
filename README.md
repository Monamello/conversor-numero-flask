# Conversor de números inteiros para a versão por extenso

Esse é um projeto em flask que retorna a versão por extenso de um número informado. Entre o Range [-99999, 99999].

Ex: 1 -
```json
{"extenso" : "um"}
```

Ou retorna um erro, caso não esteja no range [-99999, 99999] ou não seja um numero.

Ex: 
```json
{"erro":"Esse parâmetro não suportado."}`
```

## Como baixar o projeto
Estando na pasta onde queira baixar o projeto, digite no terminal o seguinte comando:

```bash
$ git clone https://github.com/Monamello/conversor-numero-flask.git
```

Entre na pasta do projeto
```bash
$ cd conversor-numero-flask
```

## Como instalar as dependencias

Digite no terminal o seguinte comando:  
 ```bash
 $ pip install -r requirements.txt
 ```

## Como rodar o projeto

Digite no terminal o seguinte comando:
```bash
$ FLASK_APP=api.py flask run
```

#### Para rodar o projeto com Host e Porta especificos:
```bash
$ FLASK_APP=api.py flask run --host=<host> --port=<porta>
```

## Para fazer a chamada
Abra o navegador e digite a url:

```http://<host-escolhido>:<porta-escolhida>/extensao/<valor-para-converter>```

#### Com os valores default de host e porta, a URL ficaria:

```http://127.0.0.1:5000/extensao/<valor-para-converter>```
