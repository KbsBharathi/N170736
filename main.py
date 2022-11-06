product_num=int(input("Enter number of products :"))
products=[]
for i in range(product_num):
    d = {}
    print("Product :",i+1)
    d['price']=int(input("Enter price :"))
    d['name'] = str(input("Enter name :"))
    d['period'] = int(input("Enter period :"))
    products.append(d)
print(products)

print("What you want to do?")
print("1.Search by name","2.Seach by price or period","3.Seach by price and period",
      "4.Delete product","5.Update product")
a=str(input("Enter number:"))
if a=='1':
   sub=str(input("Search by Name :"))
   for i in products:
       item=i.get('name')
       if(item.find(sub)==-1):
           continue
       else:
          print(i)

elif a=='2':
    x = int(input("Enter low cost :"))
    y = int(input("Enter high cost :"))
    u = int(input("Enter less warrenty days :"))
    v = int(input("Enter more warrenty days :"))
    print("Search by price or period")
    for i in products:
        cost=i.get('price')
        days=i.get('period')
        if(x<=cost<=y) or (u<=days<=v):
           print(i)

elif a=='3':
    x = int(input("Enter low cost :"))
    y = int(input("Enter high cost :"))
    u = int(input("Enter less warrenty days :"))
    v = int(input("Enter more warrenty days :"))
    print("Search by price and period")
    for i in products:
        cost=i.get('price')
        days=i.get('period')
        if(x<=cost<=y) and (u<=days<=v):
           print(i)

elif a=='4':
   sub=str(input("Enter product name to delete :"))
   for i in products:
       pro=i.get('name')
       print(pro)
       if pro==sub:
          products.remove(i)
   print(products)

elif a=='5':
   sub=str(input("Enter product name to update :"))
   for i in products:
       val=i.get('name')
       if(val==sub):
           i['price']=int(input("Enter new price"))
           i['period']=int(input("Enter new period"))
   print(products)
else:
    print('Oops! Sorry')