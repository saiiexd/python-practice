s = {1, 2, 3, 4, 5, 4, 4, 4}

e = set() #dont use s = {} as it will create an empty dictionary
 
print(s, type(s))
#set does not repeat value

s.add(45)
print(s)

# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.