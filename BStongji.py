import csv

company=[]
product=[]

companydict={}

with open(r'C:\Users\TBT_E\PycharmProjects\py_lit\BSItems\brands.csv','r',encoding='utf-8') as bscsvfile:
    reader=csv.DictReader(bscsvfile)
    for row in reader:
        compname=row['company']
        if compname not in company:
            company.append(compname)
            companydict[compname]=[]
        companydict[row['company']].append([row['product'],row['price'],row["if Kontakt"]])
    #for key,value in companydict.items():
        #print(key,value)

def sortcompany(cdict):
    resultlist=[]

    for key,value in cdict.items():
        ifkt='n'
        tlist=[]
        money = []
        tlist.append(key)
        tlist.append(len(value))
        for i in value:
            money.append(get_num(i[1]))
            if ifkt=='n':
                ifkt=find_kontakt(i[2])
        totalm=sum(money)
        tlist.append(totalm)
        tlist.append(ifkt)
        resultlist.append(tlist)
    return resultlist


def get_num(mstr):
    return float(mstr.split('$')[1])

def find_kontakt(ifkt):
    if ifkt=='1':
        return 'y'
    else:
        return 'n'


if __name__=="__main__":
    result=sortcompany(companydict)
    sortresult=reversed(sorted(result, key=lambda i: i[1]))
    sortresult=list(sortresult)

    print(sortresult)
    with open("bscomparekt.csv","w") as cpcsvfile:
        cpwriter=csv.writer(cpcsvfile,dialect="unix")
        for i in sortresult:
            i[1]=str(i[1])
            i[2] = str(i[2])
        cpwriter.writerows(sortresult)






# ...     reader = csv.DictReader(csvfile)
# ...     for row in reader:
# ...         print(row['first_name'], row['last_name'])

