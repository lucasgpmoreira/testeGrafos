import json
import string

def converter_json_para_formato_desejado(json_data):
    grafo_formatado = {}
    vertices_numeros = {str(i): c for i, c in enumerate(string.ascii_uppercase, start=1)}

    for vertice, vizinhos in json_data.items():
        try:
            vertice_formatado = vertices_numeros[vertice]
        except KeyError:
            # Se não conseguir encontrar a correspondência, use a própria chave
            vertice_formatado = vertice

        vizinhos_formatados = {vertices_numeros.get(v, v) for v in map(str, vizinhos)}
        grafo_formatado[vertice_formatado] = vizinhos_formatados

    return grafo_formatado

# Lê o JSON do arquivo
caminho_arquivo = '/home/lucas/PycharmProjects/testeGrafos/grafo_10_vertices.json'  # Substitua pelo caminho real do seu arquivo
with open(caminho_arquivo, 'r') as file:
    json_data = json.load(file)

# Converte para o formato desejado
grafo_exemplo = converter_json_para_formato_desejado(json_data)

# Exibe o resultado
print("grafo_exemplo =", grafo_exemplo)
