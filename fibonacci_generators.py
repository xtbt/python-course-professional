from time import sleep


def fibo_gen(max = None):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            yield n1
        elif counter == 1:
            yield n2
        else:
            aux = n1 + n2
            if not aux or aux <= max:
                n1, n2 = n2, aux
                yield aux
            else:
                break
        counter += 1


def main():
    fibonacci = fibo_gen(100)
    for element in fibonacci:
        print(element)
        sleep(0.5)


if __name__ == '__main__':
    main()