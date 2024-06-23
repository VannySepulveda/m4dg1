from te import Te

te1= Te(1,300)
te2= Te(1,500)

type_te1= type(te1)
type_te2= type(te2)

print(type_te1)
print(type_te2)

if type(te1)==type(te2):
    print("Son del mismo tipo")
else:
    print("No son del mismo tipo")
    