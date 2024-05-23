def print_adj(kg):
    node_list1 = kg[0]
    edge_list1 = kg[1]
    result1 = [[[0] for i in range(len(node_list1))] for j in range(len(node_list1))]
    for i, edge in enumerate(edge_list1):
        n1, n2 = edge.node_set
        i1 = node_list1.index(n1)
        i2 = node_list1.index(n2)
        result1[i1][i2][0] += 1
        result1[i1][i2].append(edge.tag)
    count_edge1 = None
    return result1, count_edge1
