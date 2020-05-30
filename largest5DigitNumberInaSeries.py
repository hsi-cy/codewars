def solution(digits):
    largest = None
    digits = str(digits)
    num = len(digits) - 4
    for i in range(num):
        if largest is None or int(largest) < int(digits[i:i+5]):
            largest = digits[i:i+5]
    return int(largest)