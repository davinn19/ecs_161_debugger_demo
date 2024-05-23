def add_nums(a : int, b : int) -> int:
    return a + b

if __name__ == "__main__":
    num_1 = 1
    num_2 = 2
    sum = add_nums(num_1, num_2)
    print("sum: " + str(sum))

    for i in range(10):
        loop_sum = add_nums(i, i + 1)
        print(loop_sum)
    pass
