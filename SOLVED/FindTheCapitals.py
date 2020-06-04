# Write a method that takes a sequence of objects with two keys each: country or state, and capital. 
# Keys may be symbols or strings

# The method should return an array of sentences declaring the state or country and its capital.
# [{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
# [{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
# [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> 
# ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]

def capital(capitals): 
    rtn_ary = []
    for country in capitals:
        if 'state' in country.keys():
            place = country['state']
        else:
            place = country['country']
        capital = country['capital']
        rtn_ary.append(f"The capital of {place} is {capital}")

    return rtn_ary


# x = [{'state': 'Maine', 'capital': 'Augusta'}]
# state = x[0]['state']
# capital = x[0]['capital']
# print(f"The capital of {state} is {capital}")