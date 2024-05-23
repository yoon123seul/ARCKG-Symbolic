#this function now also contains for the color set count 
def GridSize_pridictorr(task):
    solver_h, solver_w, solver_color = Solution_generaterrs(task)
    KG_test = Make_test_KG(task)
    adj, _ = print_adj(KG_test)
    candi_node = []
    candi_node_info = []
    candi_answer_h = []
    candi_answer_w = []
    candi_answer_color = []  #####
    
    for n in KG_test[0]:
        if n.type == "Onode" or n.type == "Gnode":
            candi_node.append(n)
            candi_node_info.append(extractor(KG_test, adj, n))
            
    for s in solver_h:
        for i, n in enumerate(candi_node):
            if speci_tester(s, candi_node_info[i]):
                candi_answer_h.append(s[1][0](n))
                
    for s in solver_w:
        for i, n in enumerate(candi_node):
            if speci_tester(s, candi_node_info[i]):
                candi_answer_w.append(s[1][0](n))
                
    for s in solver_color:
        for i, n in enumerate(candi_node):
            if speci_tester(s, candi_node_info[i]):
                candi_answer_color.append(s[1][0](n))
                
    return candi_answer_h, candi_answer_w, candi_answer_color  ####
