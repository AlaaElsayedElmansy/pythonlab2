s='abdulrahman'
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print("longest string in alph", longest)
