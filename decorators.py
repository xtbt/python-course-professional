from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_enlapsed = final_time - initial_time
        print('Executing time: ' + str(time_enlapsed.total_seconds()))
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def addition(a: int, b: int) -> int:
    return a + b


def main():
    random_func()
    addition(1234, 9876)


if __name__ == '__main__':
    main()