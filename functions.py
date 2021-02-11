def return_squared_list(ls):
    for i in range(len(ls)):
        ls[i] = ls[i]**2
    return ls


def return_pos_list(ls):
    lsnew = []
    for i in ls:
        if i > 0:
            lsnew.append(i)
    return lsnew


def cjo_factorial(x):
    ls = []
    result = 1
    while x > 0:
        ls.append(x)
        x -= 1
    for x in ls:
        result = result * x
    return result


def e_series_value():
    e = 1
    a = 1
    #while len(str(e)) < 11:
    while a < 34:
        e = e + 1/cjo_factorial(a)
        a += 1
    return e


def mean_of_list(ls):
    total = sum(ls)
    return total/len(ls)


def return_dict_from_lists(keys,values):
    return dict(zip(keys, values))


def return_list_of_dicts(dictionary):
    import numpy as np
    arr = np.array([dictionary["a"], dictionary["b"]], dtype=[('a', int), ('b', int)])


def matrix_multiply(matA, matB):
    import numpy as np
    matA = np.asarray(matA)
    matB = np.asarray(matB)
    return np.matmul(matA, matB)

n = 100000
large_set = set(range(n))
for i in large_set:
    print(matrix_multiply([[2,i],[2,3]], [[1,i],[4,2]]))
    print(mean_of_list([32,5,124,6,3,i]))
    print("\n no tv and no beer make homer go something something \n")
