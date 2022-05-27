# remove even numbers from list
def remove_even(lst):
    # with hand
    res = []
    for i in lst:
        if i % 2 != 0:
            res.append(i)
    return res


def remove_even(lst):
    # list comprehension
    return [i for i in lst if i % 2 != 0]
