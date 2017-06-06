import cs50

def main():
    print("O hai! ", end = "")
    change = get_change()
    
    #confirm whether normal rounding needed or floor
    sum = round(change * 100)
    count = 0
    if sum >= 25:
        count += sum // 25
        sum %= 25
    if sum >= 10:
        count += sum // 10
        sum %= 10
    if sum >= 5:
        count += sum // 5
        sum %= 5
    count += sum
        
    print(count)
    
def get_change():
    while True:
        print("How much change is owed?")
        change = cs50.get_float()
        if (change >= 0):
            break
    return change
    
if __name__ == "__main__":
    main()