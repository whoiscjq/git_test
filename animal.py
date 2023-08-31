import sys

def default():
    print("hello!")
def main():
    if sys.argv[1]=="dog":
        dog()
    else:
        default()
def dog():
    print("woof")
if __name__=="__main__":
    main()
