from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    new_list = []
    for i in range(row_start, row_end+1):
        n_new = []
        for k in range(column_start, column_end+1):
            n_new.append(i*k)
        new_list.append(n_new)

    return new_list


    pass


