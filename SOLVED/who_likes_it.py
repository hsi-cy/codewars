#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

def likes(names):
    #names is a list of names of whom pressed like
    if len(names) == 0:
        return("no one likes this")
    elif len(names) == 1:
        p1 = names[0]
        return(f"{p1} likes this")
    elif len(names) == 2:
        p1 = names[0]
        p2 = names[1]
        return(f"{p1} and {p2} like this")
    elif len(names) == 3:
        p1 = names[0]
        p2 = names[1]
        p3 = names[2]
        return(f"{p1}, {p2} and {p3} like this")
    else:
        n = str(len(names) - 2)
        p1 = names[0]
        p2 = names[1]
        return(f"{p1}, {p2} and {n} others like this")
