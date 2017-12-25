#SoundEffects/items
#Softwares/items
#BooksandVideos/items
#Brands/brandslist/items
#VirtualInstrument/table/items
#SampleLoopLibrary/table/items
#EffectPlugin/table/items
from  collections import OrderedDict
import re,csv
import time
from pyquery import PyQuery as pquery
import requests

#基础方法---------------------------------------------------

def write_file(filepath,items):
    with open(filepath,"w",encoding="utf-8") as bshtml:
        for x, i in enumerate(items):
            items[x]="  ".join(i)+"\n"
        bshtml.writelines(items)

def get_items(url):
    items = []
    req=requests.get(url)
    req_content=req.content
    pqcontent=pquery(req_content)(".supplier_box .list_prd_box")
    for item in pqcontent.items():
        cppr=item(".list_prd_box1 a")
        iteminfo = OrderedDict()
        pdetails=[]
        productdt=[]
        for p in pquery(cppr).items():
            productdt.append(p.text())
        iteminfo["company"]=productdt[0]
        iteminfo["product"]=productdt[1]
        prprice=item(".list_prd_box2 .list_prd_box2a .list_prd_price2")
        iteminfo["price"]=prprice.text().replace(u'\xa0',u'')
        #pdetails.append(prprice.text().replace(u'\xa0',u''))
        prbrief = item(".list_prd_box3 .list_prd_txshort")
        #pdetails.append(prbrief.text())
        iteminfo["brief"]=prbrief.text()
        prdetails=item(".list_prd_box3 .list_prd_detail a").attr("href")
        pdetails.append(iteminfo)
        pdetails.append(completeurl(prdetails))
        items.append(pdetails)
    return items



def get_tables(url):
    tables = []
    req = requests.get(url)
    req_content = req.content
    pqcontent = pquery(req_content)(".pg_box_top .l1_kachel_on")
    for table in pqcontent.items():
        tdetails=[]
        tinfo={}
        tablename=table(".l1_kachel_txt a")
        tinfo["Kinds"]=tablename.text()
        tdetails.append(tinfo)
        tdetails.append(completeurl(tablename.attr("href")))
        tables.append(tdetails)
    return tables

def get_brandlist(url):
    brandlist = []
    req = requests.get(url)
    req_content = req.content.decode("utf-8")
    pqcontent = pquery(req_content)(".supplier_box .sup_list_box")
    for brand in pqcontent.items():
        blist=[]
        brandinfo = {}
        brandinfo["brands"]=brand(".sup_list_title a").text()
        blist.append(brandinfo)
        blist.append(completeurl(brand(".sup_list_title a").attr("href")))
        brandlist.append(blist)
    return brandlist

def completeurl(parturl):
    return "".join(["https://www.bestservice.com/",parturl])

def get_page(url):
    page_info=OrderedDict()
    req = requests.get(url)
    req_content = req.content
    pqcontent = pquery(req_content)(".pg_h_nav")
    for pg in pqcontent.items():
        if "reviews"in  pg("h2").text().replace(u'\xa0',u'').lower():
            pre=pquery(pg.next_all(".detail_box_prd")[0])
            reviewstime=[]
            for hs in pre("h3").items():
                t=re.search(r".*(\d\d\d\d)",hs.text())
                if t:
                    vt=t.group(1)
                    if t and vt not in reviewstime :
                        reviewstime.append(vt)
            if reviewstime:
                reviewstime.sort()
                page_info["newest time"]=reviewstime[-1]
                page_info["oldest time"]=reviewstime[0]
            else:
                page_info["newest time"] = "no reviews"
                page_info["oldest time"] = "no reviews"



        elif "requirements" in  pg("h2").text().replace(u'\xa0',u'').lower():
            prd=pg.next_all(".detail_box_prd")
            content="".join([ i.text().lower() for i in prd("p strong").items()])
            m = re.search(r"kontakt",content)
            if m:
                print("Kontatk product")
                page_info["if Kontakt"]="1"
            else:
                page_info["if Kontakt"]="0"
    if "newest time" not in page_info:
        page_info["newest time"] = "no reviews"
        page_info["oldest time"] = "no reviews"
    if "if Kontakt" not in page_info:
        page_info["if Kontakt"]="no requirement"
    print(page_info)
    return page_info

#抓取方法---------------------------------------------------
#brands-----------------------------------------------
def get_brands_items(url,sleeptime):
    with open("BSItems/brands.csv",'w',encoding="utf-8") as brandfile:
        fieldnames = ["brands", "company","product","price","brief","newest time","oldest time","if Kontakt"]
        writer = csv.DictWriter(brandfile, fieldnames=fieldnames, dialect="unix")
        writer.writeheader()
        bl=get_brandlist(url)
        n=0
        for brand in bl:
            time.sleep(sleeptime/2)
            branditems=get_items(brand[1])
            for item in branditems:
                n=n+1
                print(n)
                contentdict = {}
                contentdict.update(brand[0])
                contentdict.update(item[0])
                time.sleep(sleeptime)
                contentdict.update(get_page(item[1]))
                writer.writerow(contentdict)

# def write_brand_csv(infodict):
#     with open("BSItems/brands.csv",'a',encoding="utf-8") as brandfile:
#         fieldnames = ["brands", "company","product","price","brief","newest time","oldest time","if Kontakt"]
#         writer = csv.DictWriter(brandfile, fieldnames=fieldnames, dialect="unix")
#         writer.writeheader()
#         writer.writerow(infodict)

#table items---------------------------------------------------------------------

def get_table_items(url,sleeptime,ktname):
    with open("BSItems/"+ktname+".csv",'w',encoding="utf-8") as ktfile:
        fieldnames = ["Kinds", "company","product","price","brief","newest time","oldest time","if Kontakt"]
        writer = csv.DictWriter(ktfile, fieldnames=fieldnames, dialect="unix")
        writer.writeheader()
        tl=get_tables(url)
        n=0
        for kt in tl:
            time.sleep(sleeptime / 2)
            ktitems=get_items(kt[1])
            for item in ktitems:
                n = n + 1
                print(n)
                contentdict = {}
                contentdict.update(kt[0])
                contentdict.update(item[0])
                time.sleep(sleeptime)
                contentdict.update(get_page(item[1]))
                writer.writerow(contentdict)

# def write_kt_csv(ktname,infodict):
#     with open("BSItems/"+ktname+".csv",'a',encoding="utf-8") as ktfile:
#         fieldnames = ["Kinds", "company","product","price","brief","newest time","oldest time","if Kontakt"]
#         writer = csv.DictWriter(ktfile, fieldnames=fieldnames, dialect="unix")
#         writer.writeheader()
#         writer.writerow(infodict)
#strit items--------------------------------------------------------------

def items_write(surl,itname):
    with open("BSItems/" + itname + ".csv", 'w', encoding="utf-8") as itfile:
        fieldnames = ["company", "product", "price", "brief", "newest time", "oldest time", "if Kontakt"]
        writer = csv.DictWriter(itfile, fieldnames=fieldnames, dialect="unix")
        writer.writeheader()
        it=get_items(surl)
        for item in it:
            contentdict = {}
            contentdict.update(item[0])
            time.sleep(2)
            contentdict.update(get_page(item[1]))
            writer.writerow(contentdict)


if __name__=="__main__":
    # Brands/brandslist/items
    # Brandurl = "https://www.bestservice.com/brands.html"
    # get_brands_items(Brandurl, 2)

    #SoundEffect/Items
    # SEurl="https://www.bestservice.com/sound_effects.html"
    # items_write(SEurl,"SoundEffect")
    
    # Softwares/items
    # STurl="https://www.bestservice.com/software.html"
    # items_write(STurl, "Softwares")
    # BooksandVideos/items
    # BVurl="https://www.bestservice.com/books_videos.html"
    # items_write(BVurl, "BookVideos")

    # VirtualInstrument/table/items
    VTurl="https://www.bestservice.com/virtual_instruments.html"
    get_table_items(VTurl,2,"VirtualInstrument")
    # SampleLoopLibrary/table/items
    SLurl = "https://www.bestservice.com/sample__loop_libraries.html"
    get_table_items(SLurl, 2, "SampleLoopLibrary")
    # EffectPlugin/table/items
    EPurl = "https://www.bestservice.com/effect_plugins.html"
    get_table_items(EPurl, 2, "EffectPlugin")

    '''   
    brandlist=get_brandlist(Brandurl)
    BrandItems=[]
    print("list ok")
    n=0
    for brand in brandlist:
        n=n+1
        btlist=[]
        btlist.append(brand[0])
        print(n)
        print(brand[0])
        time.sleep(2)
        btlist.append(get_items(completeurl(brand[1])))
        BrandItems.append(btlist)
    with open("BSItems/Brands.txt","w",encoding="utf-8") as brand:
        for bitem in BrandItems:
            brand.write(bitem[0]+"-------------------------------------------\n")
            for x,i in enumerate(bitem[1]):
                bitem[1][x]="   ".join(i)+"\n"
            brand.writelines(bitem[1])
    
    '''







