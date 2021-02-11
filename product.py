def product(args):
    numbers = [int(x) for x in args[1:]]
    result = 1
    for x in numbers:
         result = result * x
    print(result)
    return result


if __name__ == "__main__":
    import sys
    product((sys.argv))
