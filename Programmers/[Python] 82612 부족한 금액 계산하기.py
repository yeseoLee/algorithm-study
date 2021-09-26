def solution(price, money, count):
    result = count*(count+1)*price//2 - money
    return result if result>0 else 0
