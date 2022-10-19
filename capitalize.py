# Capitalizing 1st letter with ascii
def word():
    word = "banaani"
    return word

def capitalize(word):
    ascVal = ord(word[0])
    if 65 <= ascVal <= 90:
        print("Word is already capitalized")
    elif 97 <= ascVal <= 127:
        print(f"Word capitalized {chr(ascVal - 32)}{word[1:]}")
def main():
    capitalize(word())
    
main()
