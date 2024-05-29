sizes = [1]*n
centers = [i for i in range(n)]
def find(node):
    while centers[node] != node:
        node = centers[centers[node]]
    return node
    
def union(n1,n2):
    p1,p2 = find(n1),find(n2)
    if sizes[p1] >= sizes[p2]:
        sizes[p1] += sizes[p2]
        centers[p2] = centers[p1]
    else:
        sizes[p2] += sizes[p1]
        centers[p1] = centers[p2]
for [u,v] in edges:
    union(u,v)