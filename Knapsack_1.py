def list_format(list_1, x):
    length = len(list_1)
    if length < x:
        repeat = x - length
        list_1.reverse()
        for i in range (0, repeat):
            list_1.append(0)
        list_1.reverse()
        ret = list_1
    else:
        ret = list_1
    return(ret)

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

def higher_than(x, y_list):
    length = len(y_list)
    index_list = []
    for i in range (0, length):
        if y_list[i] > x:
            index_list.append(i)
        else:
            toggle = True

    return(index_list)
    

def knapsack(max_weight, weights, values):

    infractions = higher_than(max_weight, weights)
    length = len(infractions)
    if length != 0:
        infractions = infractions.reverse()
        for i in range (0, length):
            value = infractions[i]
            weights.pop(value)
            values.pop(value)
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
        
def validate(x):
    list_x = list(x)
    length = len(list_x)
    counter = 0
    for i in range (0, length):
        for j in range (0, 10):
            j = str(j)
            if list_x[i] == j:
                counter = counter + 1
            else:
                toggle = True
    if counter == length:
        return(True)
    else:
        return(False)

def validate_float(x):
    list_x = list(x)
    length = len(list_x)
    accepted_val = []
    for i in range (0, 10):
        i = str(i)
        accepted_val.append(i)
    accepted_val.append(".")
    period_count = 0

    counter = 0
    for j in range (0, length):
        for k in range (0, 11):
            if list_x[j] == accepted_val[k]:
                counter = counter + 1
                if k == 10:
                    period_count = period_count + 1
                else:
                    toggle = True
            else:
                toggle = False
    if counter == length and period_count < 2:
        return(True)
    else:
        return(False)

    
weight_limit = " "
while validate_float(weight_limit) == False:
    print("")
    weight_limit = input("Enter a weight limit. ")
weight_limit = float(weight_limit)

items = " "
while validate(items) == False:
    print("")
    items = input("How many items are in question? Enter an integer. ")
items = int(items)

item_weights = []
item_values = []
for i in range (1, items + 1):
    weight = " "
    while validate_float(weight) == False:
        print("")
        weight = input("Enter a weight for item %s. " % i)
    item_weights.append(float(weight))

    value = " "
    while validate_float(value) == False:
        print("")
        value = input("Enter a value for item %s. " % i)
    item_values.append(float(value))

print("")
print(knapsack(weight_limit, item_weights, item_values))








    
