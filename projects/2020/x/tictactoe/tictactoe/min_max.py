elements = (-1,0,-2,3)
v = -100
for item in elements:
    print('antes',v,item)
    v = max(v,item)
    print('despues',v,item)