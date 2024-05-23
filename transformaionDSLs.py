## solvers

# def linear(input, target):
#     As = [0,1,2,3,4,5, 1/2]
#     Bs = [1, -4, -3, -2, -1, 0, 2, 3, 4, 1/2]
#     answer = []
#     for a in As:
#         for b in Bs:
#             if a * input + b == target:
#                 answer.append([a,b])
#     return answer


def linear(input, target):
    As = [1,2,3,4,5, 1/2, 0]
    Bs = [0, 1, -4, -3, -2, -1, 2, 3, 4, 1/2]
    answer = []
    for a in As:
        for b in Bs:
            if a * input + b == target:
                answer = [a,b]
                return answer
    return None

def xnode_h (Xnode):
    if isinstance(Xnode, Pnode) or isinstance(Xnode, Vnode):
        return None
    return get_height(Xnode)

def xnode_w (Xnode):
    if isinstance(Xnode, Pnode) or isinstance(Xnode, Vnode):
        return None
    return get_width(Xnode)

def number_of_colorsett(Xnode):
    if isinstance(Xnode, Pnode) or isinstance(Xnode, Vnode):
        return None
    return set(Xnode.color)  # Returning the set of colors instead of its length

def number_of_colorset(Xnode):
    if isinstance(Xnode, Gnode):
        return len(Xnode.color)
    return None


def node_size(Xnode):
    if isinstance(Xnode, Pnode) or isinstance(Xnode, Vnode):
        return None
    return get_number_of_nodes(Xnode)

def onode_count1(Xnode):
    if isinstance(Xnode, Gnode):
        count = 1
        for onode in Xnode.Onode_list:
            if onode.condition == ("single_color", "get_manhattan_dist") and onode.color != {0}:
                count += 1
        return count
    else :
        return None
    
def onode_count2(Xnode):
    if isinstance(Xnode, Gnode):
        count = 1
        for onode in Xnode.Onode_list:
            if onode.condition == ("multi_color", "get_polar_dist") and onode.color != {0}:
                count += 1
        return count
    else :
        return None
    
def onode_count3(Xnode):
    if isinstance(Xnode, Gnode):
        count = 1
        for onode in Xnode.Onode_list:
            if onode.condition == ("single_color", "get_polar_dist") and onode.color != {0}:
                count += 1
        return count
    else :
        return None
    
def onode_count4(Xnode):
    if isinstance(Xnode, Gnode):
        count = 1
        for onode in Xnode.Onode_list:
            if onode.condition == ("multi_color", "get_manhattan_dist") and onode.color != {0}:
                count += 1
        return count
    else :
        return None
