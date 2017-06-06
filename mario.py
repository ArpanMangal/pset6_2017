import cs50

def main():
    h = get_height()
    for r in range(h):
        for c in range (h - r):
            print(" ", end = "")
        for c in range (r):
            print("#", end = "")
        print("#")
        
def get_height():
    while True:
        print("Height: ", end = "")
        h = cs50.get_int()
        if h >= 0 and h <= 23:
            break
    return h

if __name__ == "__main__":
    main()