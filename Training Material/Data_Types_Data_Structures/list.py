listobj = [1,2,3,4,5]

print("First Index",listobj[0])
print("Second Index",listobj[1])
print("Third Index",listobj[2])
print("Fourth Index",listobj[3])
print("Last Index",listobj[4])
print("Last Index", listobj[-1])

print("Range",listobj[1:3])
print("range",listobj[2:])

listobj[3] = 6
print("Updated List", listobj)

listobj.append(7)
print("Updated List", listobj)

print("range",listobj[:-1])