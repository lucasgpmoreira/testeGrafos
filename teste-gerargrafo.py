import os

import networkx as nx
import random
import json


def generate_random_graph(num_vertices):
    G = nx.Graph()

    # Adiciona vértices ao grafo com base em números
    vertices = list(range(1, num_vertices + 1))

    G.add_nodes_from(vertices)

    # Adiciona arestas ao grafo de forma aleatória
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.choice([True, False]):
                G.add_edge(vertices[i], vertices[j])

    # Adiciona vértices adicionais se o número for menor que 10
    while len(G.nodes()) < num_vertices:
        novo_vertice = random.randint(1, num_vertices)
        if novo_vertice not in G.nodes():
            G.add_node(novo_vertice)

    # Converte o grafo para o formato desejado
    grafo_formatado = {v: list(G.neighbors(v)) for v in G.nodes()}

    return grafo_formatado

# Gera um grafo aleatório com 10 vértices
grafo_10_vertices = generate_random_graph(20)

# Especifica o caminho completo para o arquivo
caminho_arquivo = os.path.join(os.getcwd(), 'grafo_10_vertices.json')

# Salva o grafo em um arquivo JSON
with open(caminho_arquivo, 'w') as file:
    json.dump(grafo_10_vertices, file)

print(f"Grafo salvo em '{caminho_arquivo}'")