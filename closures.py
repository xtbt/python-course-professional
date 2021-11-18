def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'You can only input a string'
        return string * n
    return repeater


def main():
    repeat5 = make_repeater_of(5)
    print(repeat5('Hello'))

    repeat10 = make_repeater_of(10)
    print(repeat10('Jonny'))


if __name__ == '__main__':
    main()