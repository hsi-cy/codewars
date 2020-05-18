# Happy Holidays fellow Code Warriors!
# Now, Dasher! Now, Dancer! Now, Prancer, and Vixen! On, Comet! On, Cupid! 
# On, Donder and Blitzen! That's the order Santa wanted his reindeer...right? 
# What do you mean he wants them in order by their last names!? Looks like we need your help Code Warrior!

# Sort Santa's Reindeer
# Write a function that accepts a sequence of Reindeer names, and returns a sequence with 
# the Reindeer names sorted by their last names.

# Notes:
# It's guaranteed that each string is composed of two words
# In case of two identical last names, keep the original order

def sort_reindeer(reindeer_names):
    import pandas as pd
    df = pd.DataFrame(columns = ['first name','last name'])
    for ppl in reindeer_names:
        name = ppl.split(' ')
        fstn = name[0]
        lstn = name[1]
        dff = pd.DataFrame(columns = ['first name','last name'],
                        data = [{'first name':fstn, 'last name':lstn}])
        df = df.append(dff, ignore_index=True)
    df = df.reset_index().sort_values(by= ['last name', 'index'])
    df = df.reset_index(drop=True).drop(columns=['index'],axis=1)
    rows = df.shape[0]
    ans = []
    for row in range(rows):
        name = df.iloc[row][0] + ' ' + df.iloc[row][1]
        ans.append(name)
    return ans

# others' solution
def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda s:s.split()[1])