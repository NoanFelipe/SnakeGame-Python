import json

def createFile(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    
    else:
        print(f"Arquivo \033[1;35m{nome}\033[m criado com sucesso")


def fileExists(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def WriteOnJsonFile(obj, arq):
    jsonobject = json.dumps(obj)
    file = open(arq, "w")
    file.write(jsonobject)
    file.close()


def ReadJsonFile(file): 
    f = open(file, "r")
    string = f.read()
    if string == '':
        f.close()
        return [{'gold': 0, 'blue': False, 'green': False, 'br': False, 'usa': False, 'equiped': 0, 'highscore': 0}]
    else:
        listaCarregada = json.loads(string)
        f.close()
        return listaCarregada
