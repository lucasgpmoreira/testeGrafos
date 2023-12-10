def forca_bruta_cobertura_vertices(grafo):
    vertices = list(grafo.keys())
    menor_cobertura = None

    for i in range(2 ** len(vertices)):
        cobertura_atual = [vertices[j] for j in range(len(vertices)) if (i >> j) % 2 == 1]

        grafo_temp = {v: grafo[v].copy() for v in grafo}
        for v in cobertura_atual:
            for u in grafo[v]:
                if u in grafo_temp:
                    grafo_temp[u].remove(v)
            del grafo_temp[v]

        arestas_cobertas = all([not grafo_temp[v] for v in grafo_temp])

        if arestas_cobertas and (menor_cobertura is None or len(cobertura_atual) < len(menor_cobertura)):
            menor_cobertura = cobertura_atual

    return menor_cobertura


# ------------------------------------------------------------

# Define uma função que verifica se um subconjunto é um vertex cover de um grafo
def is_vertex_cover(graph, subset):
    # Para cada aresta do grafo
    for u in graph:
        for v in graph[u]:
            # Se nenhum dos vértices da aresta está no subconjunto
            if u not in subset and v not in subset:
                # Retorna falso
                return False
    # Se todas as arestas foram cobertas, retorna verdadeiro
    return True


# Define uma função que gera todos os subconjuntos de um conjunto com um dado tamanho
def generate_subsets(set, size, subset=[], subsets=[]):
    # Se o tamanho do subconjunto é igual ao tamanho desejado
    if len(subset) == size:
        # Adiciona o subconjunto à lista de subconjuntos
        subsets.append(subset.copy())
    # Se não
    else:
        # Para cada elemento do conjunto
        for i in range(len(set)):
            # Adiciona o elemento ao subconjunto
            subset.append(set[i])
            # Chama a função recursivamente com o resto do conjunto
            generate_subsets(set[i + 1:], size, subset, subsets)
            # Remove o elemento do subconjunto
            subset.pop()
    # Retorna a lista de subconjuntos
    return subsets


# Define uma função que encontra o menor vertex cover de um grafo
def brute_force_vertex_cover(graph):
    # Inicializa o menor vertex cover como vazio
    min_vertex_cover = []
    # Para cada tamanho possível de subconjunto, de 1 até o número de vértices do grafo
    for size in range(1, len(graph) + 1):
        print(size)
        # Gera todos os subconjuntos de vértices com esse tamanho
        subsets = generate_subsets(list(graph.keys()), size)
        # Para cada subconjunto gerado
        for subset in subsets:
            # Verifica se o subconjunto é um vertex cover do grafo
            if is_vertex_cover(graph, subset):
                # Se for, atribui o subconjunto ao menor vertex cover e encerra o laço
                min_vertex_cover = subset
                break
        # Se o menor vertex cover não está vazio, encerra o laço
        if min_vertex_cover:
            break
    # Retorna o menor vertex cover
    return min_vertex_cover


# Exemplo de uso
grafo = {
    "A": {"B", "C", "D"},
    "B": {"A", "D", "E"},
    "C": {"A", "D"},
    "D": {"A", "B", "C", "E"},
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




# cobertura = forca_bruta_cobertura_vertices(grafo)
cobertura = brute_force_vertex_cover(grafoAl)
print("Cobertura mínima de vértices:", cobertura)
print("Tamanho da cobertura:", len(cobertura))
