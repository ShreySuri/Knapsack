def list_format(list_1, x):
    length = len(list_1)
    if length < x:
        repeat = x - length
        list_1.reverse()
        for i in range (0, repeat):
            list_1.append(0)
        list_1.reverse()
        return(list_1)
    else:
        return(list_1)

def combinations(x):
    y = 2 ** x
    for i in range (0, y):
        combo_list = list(bin(i))
        combo_list.pop(0)
        combo_list.pop(0)
        combo_list = list_format(combo_list, x)
        for j in range (0, x):
            combo_list[j] = int(combo_list[j])
        
    
