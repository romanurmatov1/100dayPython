a = [
   {'John':14},
   {'Mary':15},
   {"Stae":16}
]
b = []
print(a)
print(b)
b.append(a[1])
a.pop(1)
print(a)
print(b)
for i in b:
   a.append(i)
b.clear()
print(a)
print(b)