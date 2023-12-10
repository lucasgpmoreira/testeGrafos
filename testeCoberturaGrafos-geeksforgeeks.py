def isCover(V, k, E, gr, vertex_cover):
    Set = (1 << k) - 1
    limit = (1 << V)
    vis = [[0] * maxn for _ in range(maxn)]

    while Set < limit:
        vis = [[0] * maxn for _ in range(maxn)]
        cnt = 0
        j = 1
        v = 1

        while j < limit:
            if Set & j:
                for i in range(1, V + 1):
                    if gr[v][i] and not vis[v][i]:
                        vis[v][i] = 1
                        vis[i][v] = 1
                        cnt += 1
            j = j << 1
            v += 1

        if cnt == E:
            vertex_cover.clear()
            j = 1
            v = 1
            while j < limit:
                if Set & j:
                    vertex_cover.append(v)
                j = j << 1
                v += 1
            return True

        c = Set & -Set
        r = Set + c
        Set = (((r ^ Set) >> 2) // c) | r
    return False


def findMinCover(n, m, gr):
    left = 1
    right = n
    vertex_cover = []

    while right > left:
        mid = (left + right) >> 1
        if not isCover(n, mid, m, gr, vertex_cover):
            left = mid + 1
        else:
            right = mid

    return vertex_cover


def insertEdge(u, v, gr):
    gr[u][v] = 1
    gr[v][u] = 1  # Undirected graph


maxn = 25
gr = [[0] * maxn for _ in range(maxn)]


V = 6
E = 7
insertEdge(1, 2, gr)
insertEdge(1, 3, gr)
insertEdge(2, 3, gr)
insertEdge(2, 4, gr)
insertEdge(3, 5, gr)
insertEdge(4, 5, gr)
insertEdge(4, 6, gr)

min_cover = findMinCover(V, E, gr)
print("Conjunto mínimo de vértices:", min_cover)
