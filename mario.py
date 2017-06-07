import cs50

def main():
    h = get_height()
    for r in range(h):
        print(" " * (h - r), end = "")
        print("#" * (r + 1), end = "")
        print("  ", end = "")
        print("#" * (r + 1), end = "")
        print()
        
def get_height():
    while True:
        print("Height: ", end = "")
        h = cs50.get_int()
        if h >= 0 and h <= 23:
            break
    return h

if __name__ == "__main__":
    main()