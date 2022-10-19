#learning how to make .join() with for loop
def hypAndWord():
    word = "banaani"
    hyp = "-"
    return word,hyp

def joinFunction(word,hyp):
    count = 0
    for i in word:
        count +=1
        print(f"{i}",end="")
        if count != len(word):
            print(f"{hyp}",end="")
    return None

def main():
    word,hyp = hypAndWord()
    joinFunction(word,hyp)
main()
