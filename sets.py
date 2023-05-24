# Create an empty set 

s = set()

# Add elements to a set 

s.add(1)
s.add(2)
s.add(3)
s.add(4)

# sets can only have unique values, so this won't change the set

s.add(3)

print (s)
print(f"The set has {len(s)} elements")
#this removes a value in a set 
s.remove(2)

print(s)

# give the number of elements in the set

print(f"The set has {len(s)} elements")