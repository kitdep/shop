#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install dnspython')
get_ipython().system('pip install pymongo[srv]')
get_ipython().system(' pip install update')


# In[2]:


get_ipython().system('pip --version')


# In[7]:


import pymongo


client = pymongo.MongoClient("mongodb://kittu:Kittu1995@ac-nsrwuca-shard-00-00.dldhqvh.mongodb.net:27017,ac-nsrwuca-shard-00-01.dldhqvh.mongodb.net:27017,ac-nsrwuca-shard-00-02.dldhqvh.mongodb.net:27017/?ssl=true&replicaSet=atlas-793vv6-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.fruit_shop
rec = db.items_list


# In[8]:


items={'apple':100,'graps':50,'papaya':70,'banana':40,'mango':80,'oranges':60,'kiwi':120,'strawberries':150,'pineapple':40,'watermelon':80,'dragon fruit':150,'apricots':80,'raspberries':100}
rec.insert_one(items)


# In[13]:


rec1=db.user_data
rec2 = db.bills


# In[16]:


import datetime

print('for billing person press 1 \n for store manager press 2\n')
user_input=int(input())

if user_input==1:
    print('enter your mobile number:')
    mobile_number=int(input())
    
    product=[]
    x=1
    bill_no = 0
    qunt_list = []
    price_list =[]
    efg = []
    store_name = "Billal fruit shop"
    time = datetime.datetime.now()
    
    while x==1:
        print('enter item',items)
        selected_item = input()
        y=items.get(selected_item)
        print('select quantity :')
        quantity=int(input())
        print('do you want to add further items press 1 for yes,2 for no')
        
        price_list.append(y)
        
        qunt_list.append(quantity)
        
        x= int(input())
        
        
        efg.append(selected_item)
        
        
        print(efg)
        print(qunt_list)
        
        

for i,j in zip(price_list,qunt_list):
    product.append(i*j)
print(product)
print(sum(product))
z = sum(product)
bill_no = bill_no+1
cust = {'_id':mobile_number,'items':efg,'quantity':qunt_list,'price':product,'total_price':z}
bills = {'_id':mobile_number,'bill_no':bill_no,'total_value':z,'storeName':store_name,'DateTime':time}
rec1.insert_one(cust) 
rec2.insert_one(bills)


# In[ ]:




