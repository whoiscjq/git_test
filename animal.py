import sys

def default():
    print("hello!")

def cat():
    print("meow!!!!")

def dog():
    print("Wooooooooooof")
    
def main():
    if sys.argv[1] == "cat":
        cat()
    elif sys.argv[1]=="dog":
        dog()
    else:
        default()
#I like someone in the note
if __name__=="__main__":
    main()
