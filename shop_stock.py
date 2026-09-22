print("----shop stock--------")
inventory={"apple": 10, "banana": 5, "orange": 8}
#order_items=tuple(input("enter items").split())
#order_quantity=[]
#n=len(order_items)
#for i in range(n):
    #order_quantity.append(input("enter element"))

#print(order_items)
#for i  in order_items:
   # print(i)
#for i in order_quantity:
    #print(i)

#order_items=list(order_items)

#d={(k,v) for k,v in zip(order_items,order_quantity)}
#print(d)

print(inventory)
test=(tuple(input("enter req items").split()))
print(test)

for i in test:

    if i not in inventory:
        print(i, "not sold here")

    elif inventory[i]>=0:
        inventory[i]=inventory[i]-1
        print(i,"purchsed")

    elif inventory[i]==0:
        print("already sold")
        
   
print("-----updated inventory--------------")
print(inventory)
    
