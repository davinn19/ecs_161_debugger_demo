
class fibonacci_counter():
    start_1 = 0
    start_2 = 1

    def __init__(self) -> None:
        self.num_1 = fibonacci_counter.start_1
        self.num_2 = fibonacci_counter.start_2
        pass

    def next(self) -> int:
        temp = self.num_1
        self.num_1 = self.num_2
        self.num_2 = temp + self.num_2
        return temp


def add_nums(a : int, b : int) -> int:
    return a + b

if __name__ == "__main__":
    num_1 = 1
    num_2 = 2
    sum = add_nums(num_1, num_2)
    print("sum: " + str(sum))

    counter = fibonacci_counter()
    for i in range(10):
        print("fib " + str(i + 1) + ": " + str(counter.next()))
    pass
