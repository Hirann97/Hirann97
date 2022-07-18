#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


a=np.array([[[1,2,3],[1,5,6]],[[10,20,3],[4,5,6]]])
a


# In[7]:


# creating an empty array 2 diamensional array with 3 rows
#row 1 =employee id
#row 2 dept id
#row3 - salary
emp2=np.ones((3,2000),dtype='int32')
emp2.dtype
emp2


# In[9]:


#generating employee id
for i in range(2001):
    emp2[0,i-1]=i
print(emp2)


# # task1

# In[10]:


# code 1 = hr
# 2=finance
#3=it
#4=sales
for i in range(2001):
    if i<501:
        emp2[1,i-1]=1
    elif i<1001:
        emp2[1,i-1]=2
    elif i<1501:
        emp2[1,i-1]=3
    else:
        emp2[1,i-1]=4
print(emp2)


# In[11]:


# code to generate random salary between 25000 & 50000 for hr dept 
import random 
for i in range(501):
    #index of hr department is 0-499 records
    #using random package to genarate salary below 250000 to 50000
    emp2[2,i-1]=random.randint(25000,50000)
    if emp2[2,i-1]<0:
        emp2[2,i-1]=-1*emp2[2,i-1]
print(emp2[2,0:10])


# In[12]:


# genarating for finance
#genarating the salary of finance coresponds to hr ie 1.25% more salary of hr perso
#hremploy * 1.25% = finance personal salary
for i in range(501,1001):
    sal1=emp2[2,i-500]
    sal1=1.25*sal1
    emp2[2,i-1]=sal1
print(emp2[2,501:510])
print(emp2[2,999])


# In[13]:


#generating for sales
#employee id of sales is ranging from 1501-2000
# and for finance it was 501-1000
#sales employee alary is =0.5*of finance ie half
for i in range(1500,2001):
    sal2=emp2[2,i-1001]
    sal2=0.5*sal2
    emp2[2,i-1]=sal2
print(emp2[2,1501:1510])
print(emp2[2,499])
print(emp2[2,1499])


# In[14]:


# generating for it dept
#salary of it dept is 5000$ more than that of hr dept.
for i in range(1000,1501):
    sal3=emp2[2,i-1000]
    sal3=sal3+5000
    emp2[2,i-1]=sal3

print(emp2[2,1001:1010])
print(emp2[2,0])
print(emp2[2,999])


# In[15]:


print(emp2)


# In[16]:


#total expence of hr
print(np.sum(emp2[2,0:500]))


# In[18]:


# total expence of finance
print(np.sum(emp2[2,501:1000]))


# In[19]:


# total expence of it dept
print(np.sum(emp2[2,1001:1500]))


# In[20]:


# total expence of sales
print(np.sum(emp2[2,1501:2000]))


# # task2

# In[21]:


#importing the numpy-indexed for createing an array of sum of the salary with respect to emp id ,it will be 1D array.
import numpy_indexed as npi
npi.group_by(emp2[1,:]).sum(emp2[2,:])


# In[22]:


# for agregating the top 10 salary of the whole compnay
sal_array=emp2[2,:]
 #print(sal_array)
sort_index=np.argsort(sal_array)
#print(sort_index)
sorted_sal_array=sal_array[sort_index]
#print(sorted_sal_array)

for i in range(1,10):
    print(sorted_sal_array[-i])


# # task 3

# In[23]:


#spliting it by using split meathod of numpy indexes based on the department
split_sal=npi.group_by(emp2[1,:]).split(emp2[2,:])
print(split_sal)


# In[25]:


x=npi.group_by(emp2[1,:]).split(emp2[2,:])
def top10salary(x):
    sort_index=np.argsort(x)
    sort_sal_array=x[sort_index]
    for i in range (1,10):
        print(sorted_sal_array[-i])


# In[ ]:





# # task 4

# In[31]:



salary=npi.group_by(emp2[1,:]).split(emp2[2,:])
#defineing the function to print the top10 salaryies of respective department
def top10(x):
    sort_index=np.argsort(x)
    sort_x=x[sort_index]
    for i in range(1,10):
        print(sort_x[-i])
    
print(top10(salary[0]))


# # task5

# In[32]:


#here we are taking the count of employees who are having more than 45000 in the salary

# also we are printing the whole array of employee salary which are having salary of 45k
print(sal_array)
print(sal_array>45000)
count_sal=(sal_array>45000).sum()
print(count_sal)


# # task6

# In[33]:


#updating the salary of sales employees who are having 20k salary by 20%
print(emp2[2,1002])
count=0
for i in range(1000,1501):
    if emp2[2][i]<20000:
        count+=1
        emp2[2][i]=(emp2[2][i]*0.2)+emp2[2][i]
print("count of sales employes who are having the salary less than 20000 is : ",count)
print(emp2[2,1002])
print(emp2[2,1000:1500])


# # task 7

# In[34]:


#deleting a set of rows 
# for that we uses the indexing the rows that are need to be deleted.
index=[1995,1996,1997,1998,1999]
#then these index will be siigned into theprogram
emp2=np.delete(emp2,index,axis=1)
#here the axis terms the coulums and rows axis 0 is rows and 1 is for columns ,these are in the case of a 2 diamensional arrys.
print(emp2)

#then we need to add some


# In[35]:


#adding to the existing array
index2=[2001,2002,2003,2004,2005]
emp2=np.append(emp2,index2)
print(emp2)


# In[ ]:




