def largest_pair_sum(numbers): 
    length = len(numbers)
    largest = None
    for i in range(length):
        for j in range(i+1, length):
            if (largest == None) or (numbers[i] + numbers[j]) > largest:
                largest = numbers[i] + numbers[j]
            
    return largest

print(largest_pair_sum([-10, -8, -16, -18, -19]))