def addNumbers(numlist):
    sum = 0
    for num in numlist:
        sum += num
    return sum

def main():
    numlist = list()
    num = input("Enter an integer: ")
    while num != "done":
        numlist.append(int(num))
        num = input("Enter an integer: ")
    result = addNumbers(numlist)
    print("Result: " + str(result))

main()
