def process_x(lst):
    new_lst = lst.copy()

    while len(new_lst) > 1:
        temp_lst = []
        for i in range(len(new_lst) - 1):
            if new_lst[i] != new_lst[i + 1]:
                temp_lst.append(new_lst[i + 1] - new_lst[i])
        
        if len(temp_lst) == 0:
            return False
        
        new_lst = temp_lst.copy()
    
    return True if len(new_lst) > 1 else False


def reduce_to_repeated_element(data):
    values = list(data.values())

    while not process_x(values):
        values = process_x(values)
    
    return len(values) > 1
