import os
import json

def validate(path):
    try:
        data = json.loads(open(path, 'r').read())
        assert isinstance(data, dict), 'O arquivo JSON deve ser um dicionario com uma lista de comandos dentro.'
        assert 'commands' in data, 'Nao foi encontrado o campo "commands" no arquivo JSON.'
        assert isinstance(data['commands'], list), 'O campo "commands" deve ser uma lista.'
        
    except json.decoder.JSONDecodeError:
        print('Arquivo JSON inválido.')
        exit(1)

if __name__ == '__main__':
    validate(os.path.join(os.path.dirname(__file__), '..', 'commands.json'))
