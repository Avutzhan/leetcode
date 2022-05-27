def find_first_unique(lst):
    for index1 in range(len(lst)):
        index2 = 0
        # iterate the second list using index2
        while(index2 < len(lst)):
            if (index1 != index2 and lst[index1] == lst[index2]):
                break
            index2 += 1
        if (index2 == len(lst)):
            return lst[index1]
    return None


