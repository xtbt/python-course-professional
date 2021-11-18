def make_division_by(x):
    assert str(x).isnumeric(), 'You must enter only numbers'
    def division_by(y):
        assert str(y).isnumeric(), 'You must enter only numbers'
        return y / x
    return division_by


def main():
    try:
        division_by_3 = make_division_by(3)
        print(division_by_3(18))

        division_by_5 = make_division_by(5)
        print(division_by_5(100))

        division_by_18 = make_division_by(18)
        print(division_by_18(54))
    except ZeroDivisionError as z:
        print('Cannot divide by 0')


if __name__ == '__main__':
    main()