import cs50
import sys

def main():
    if len(sys.argv) != 2:
        print("Enter a single word key")
        exit(1)
        
    key = sys.argv[1]
    length = len(key)
    
    for c in key:
        if not c.isalpha():
            print("Keywords should only have alphabets")
            exit(1)
    
    print("plaintext: ", end = "")
    text = cs50.get_string()
    print("ciphertext: ", end = "")
    
    i = 0
    for c in text:
        theKey = key[i % length]
        if theKey.isupper():
            numKey = ord(theKey) - ord("A")
        elif theKey.islower():
            numKey = ord(theKey) - ord("a")
            
        
        if c.isupper():
            print(chr((ord(c) - ord("A") + numKey) % 26 + ord("A")), end = "")
            i += 1
        elif c.islower():
            print(chr((ord(c) - ord("a") + numKey) % 26 + ord("a")), end = "")
            i += 1
        else:
            print(c, end = "")
            
    print()        
    exit(0)
    
    
if __name__ == "__main__":
    main()