import cs50

def main():
    creditCardNo = getCreditNo()
    print(check(creditCardNo))
    
def getCreditNo():
    while True:
        cardNum = cs50.get_int();
        if(cardNum > 0):
            break
    return cardNum
    
def check(num):
    tmp = num
    len = 0
    while tmp > 0:
        len += 1
        tmp //= 10
        
    if (len == 15 and num % 10000000000000 == 34 or 
    num % 10000000000000 == 37):
        if(Luhn(num)):
            return "AMEX"
        else:
            return "INVALID"
            
    elif(len == 16 and num % 10000000000000 == 34 or 
    num % 10000000000000 == 37)