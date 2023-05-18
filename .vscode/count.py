# Write a function to count the occurrences of each character in a given string.
# Wrie
x = 'sssssssuuuuuupp'
d = {}
for item in x:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
print(d)
