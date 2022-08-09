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
    total_combos = []
    for i in range (0, y):
        combo_list = list(bin(i))
        combo_list.pop(0)
        combo_list.pop(0)
        combo_list = list_format(combo_list, x)
        for j in range (0, x):
            combo_list[j] = int(combo_list[j])
        total_combos.append(combo_list)
    return(total_combos)


def knapsack(max_weight, weights, values):
    length = len(weights)
    for i in range (0, length):
        if weights[i] > max_weight:
            weights.pop(i)
            values.pop(i)
        else:
            toggle = True

    length = len(weights)
    total_combo_list = combinations(length)
    capable = []
    for i in range (0, 2 ** length):
        total_weight = 0
        total_value = 0
        combo = total_combo_list[i]
        for j in range (0, length):
            total_weight = total_weight + combo[j] * weights[j]
            total_value = total_value + combo[j] * values[j]
        if total_weight <= max_weight:
            capable.append(total_value)
        else:
            toggle = False

    capable.sort()
    capable.reverse()
    return(capable[0])
        


print(knapsack(10, [3, 7, 6], [40, 80, 50]))        
    
