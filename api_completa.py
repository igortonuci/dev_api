from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':0,'nome':'Rafael','habilidades':['Python', 'Flask']

    },
    {'id':1,'nome':'Igor','habilidades':['BluePrism', 'Regex']

    }
]

#Define a URI de cada API, neste caso estamos usando os metodos para diferenciar
#GET = Consulta por ID o desenvolvedor
#PUT =  Faz alteração, manda no body as informações
#DELETE =  Deleta o dado referente ai ID que informou

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        #se der erro na execução
        try:
            response = desenvolvedores[id]
        #se o erro for IndexError aparecerá essa mensagem
        except IndexError:
            mensagem = 'Desenvolvedor ID {} não existe'.format(id)
            response = {'Status':'erro', 'mensagem':mensagem}
        #caso der algum erro não mapeado
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'Erro','mensagem':mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status':'Sucesso', 'Mensagem':'Registro excluido'})

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run()
