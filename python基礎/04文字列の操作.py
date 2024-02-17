s = "helloworld"
for i in range(0, len(s)):
    print(i, s[i], end='\t\t')

print()

s1=s[0:5:2]
print(s1)
print(s[:5:1])
print(s[:5:])
print(s[::2])

print(s[::-1])


print(('e' in s))
print(('e' not in s))

print(max(s))
print(min(s))

print(s.index("o"))
# print(s.index('v'))
print(s.count('o'))