import json

file = input("")

try:
    with open(file, encoding='utf-8') as json_data:
        text = json.load(json_data)
        print(text)
except:
    print("Ocorreu um erro!")
finally:
    print("Processo concluído!")