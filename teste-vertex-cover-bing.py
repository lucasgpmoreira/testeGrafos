# Função que retorna o grau de um vértice em um grafo
def grau(grafo, vertice):
    return len(grafo[vertice])


# Função que retorna o vértice de maior grau em um grafo
def maior_grau(grafo):
    max_grau = 0
    max_vertice = None
    for v in grafo:
        grau_atual = len(grafo[v])
        if grau_atual > max_grau:
            max_grau = grau_atual
            max_vertice = v
    return max_vertice


# Função que aplica a heurística gulosa para a cobertura de vértices mínima
def cobertura_gulosa(grafo):
    cobertura = set()  # conjunto que armazena a cobertura

    copia = grafo.copy()  # cópia do grafo original

    while copia:  # enquanto o grafo não estiver vazio
        v = maior_grau(copia)  # escolhe o vértice de maior grau

        if v is not None:
            cobertura.add(v)  # adiciona o vértice à cobertura
            for u in copia[v]:  # para cada vizinho do vértice
                copia[u].remove(v)  # remove a aresta que liga os vértices
            copia.pop(v)  # remove o vértice do grafo
        else:
            break  # evita um loop infinito se algo der errado

    return cobertura  # retorna a cobertura encontrada


# Exemplo de uso
grafo = {
    "A": {"B", "C", "D"},
    "B": {"A", "D", "E"},
    "C": {"A", "D"},
    "D": {"A", "B", "C", "E"},
    "E": {"B", "D"}
}

grafo1 = {
    "A": {"B", "D"},
    "B": {"A", "C"},
    "C": {"B"},
    "D": {"A", "E", "G"},
    "E": {"F", "D", "I"},
    "F": {"E", "G"},
    "G": {"F", "H"},
    "H": {"G"},
    "I": {"E"}
}

grafoRepo = {
    "A": {"B", "C"},
    "B": {"A", "C", "D", "E"},
    "C": {"A", "B", "D"},
    "D": {"B", "C", "E"},
    "E": {"B", "D"}
}

grafoAl={
'0': {'23', '3', '22', '24', '18', '9'},
'1': {'12', '23', '7', '22', '6', '24', '18', '9'},
'2': {'5', '23', '22', '6', '16', '21', '18', '15', '14', '8'},
'3': {'5', '23', '0', '17', '20', '24', '18', '15', '14', '8'},
'4': {'11', '23', '22', '6', '21', '15', '14', '9'},
'5': {'11', '12', '3', '17', '20', '13', '2', '8', '16', '21', '15', '9'},
'6': {'10', '12', '23', '20', '1', '7', '22', '2', '19', '4', '15', '8'},
'7': {'11', '17', '1', '22', '6', '13', '8', '21', '15', '14', '9'},
'8': {'5', '10', '3', '7', '6', '2', '13', '18', '9'},
'9': {'5', '10', '0', '1', '7', '4', '15', '8'},
'10': {'23', '17', '6', '13', '8', '24', '18', '15', '9'},
'11': {'5', '12', '7', '22', '16', '21', '4', '15'},
'12': {'11', '5', '1', '22', '6', '13', '19', '14'},
'13': {'5', '10', '12', '23', '20', '7', '16', '18', '8'},
'14': {'12', '3', '7', '22', '2', '24', '4'},
'15': {'11', '5', '10', '3', '17', '7', '22', '6', '2', '4', '9'},
'16': {'11', '5', '13', '2', '24', '18'},
'17': {'5', '10', '23', '3', '7', '15'},
'18': {'10', '23', '0', '3', '20', '1', '13', '2', '16', '21', '8'},
'19': {'6', '20', '12'},
'20': {'5', '3', '6', '13', '19', '21', '18'},
'21': {'11', '5', '23', '20', '7', '2', '4', '18'},
'22': {'11', '12', '23', '0', '1', '7', '6', '2', '4', '15', '14'},
'23': {'10', '0', '3', '17', '1', '22', '6', '2', '13', '21', '4', '18'},
'24': {'10', '0', '3', '1', '16', '14'},
}

cobertura = cobertura_gulosa(grafoAl)
print("A cobertura encontrada é:", cobertura)
print("O tamanho da cobertura é:", len(cobertura))
