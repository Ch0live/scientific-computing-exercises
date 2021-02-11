def matrix_translator(f_obj):
    import numpy as np
    mat = []
    for line in f_obj:
        line = line.strip()
        mat.append(line)
    return np.asarray(mat)


def matrix_brain(mat_list, oper_list):
    print(mat_list)
    print('\n')
    print(oper_list)


def matrix_calculator(args):
    files = []
    operations = []
    for argument in args[1:]:
        if str(argument[-4:]) == ".csv":
            files.append(argument)
        else:
            # only handles 1 operation right now
            operations.append(argument)

    matrices = []
    for file in files:
        with open(file) as f:
            matrices.append(matrix_translator(f))
    print(matrices)

    #result = matrix_brain(matrices, operations)

    # if len(matrices) < 3:
    # print('The {oper} of {0} and {1} is {res}.'.format(
    # matrices[0], matrices[1], oper=operations[0], res=result))

if __name__ == "__main__":
    import sys
    matrix_calculator((sys.argv))
