datal=[]
filename="takeinfo"
with open(filename,'r') as file:

    for data in file.readlines():
        datal.append(data.split(":")[0].strip())
#print(datal)

for i in datal:
    print("".join([i,"=",repr(i)]))