import time

class FiboIter():

    def __init__(self, max = None):
        self.max = max

    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if type(self.max) == int and self.aux >= self.max:
                raise StopIteration
            else:
                self.n1 = self.n2
                self.n2 = self.aux
                self.counter += 1
                return self.aux
                

def main():
    fibonacci = FiboIter(100)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


if __name__ == '__main__':
    main()