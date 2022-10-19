#Prints a square with user input
def menu():
    print("1) Size")
    print("2) Symbol")
    print("3) Result")
    print("0) exits")
    choice = int(input("Give your choice: "))
    return choice
def askSize():
    size = int(input("Give the size of the square: "))
    return size
def askSymbol():
    symbol = str(input("Give the symbol: "))
    return symbol
def calcSquare(size,symbol):
    count = 1
    while count < size:
        for i in range(size-count):
            if i <= size:
                print(" ",end="")
        for j in range(count):
                print(f"{symbol}",end="")
        for p in range(count-1):
                print(f"{symbol}",end="")
        print()
        count +=1
    while count >= 1:
        for i in range(size-count):
            if i <= size:
                print(" ",end="")
        for j in range(count):
                print(f"{symbol}",end="")
        for p in range(count-1):
                print(f"{symbol}",end="")
        print()
        count -=1
    return None
def main():
    print("This program makes a cool square with your inputs")
    choice = menu()
    while True:
        if choice != 0:
            if choice == 1:
                size = askSize()
            elif choice == 2:
                symbol = askSymbol()
            elif choice == 3:
                calcSquare(size,symbol)
            else:
                print("Unknown option")
            choice = menu()
        else:
            break
main()
