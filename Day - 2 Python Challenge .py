#!/usr/bin/env python
# coding: utf-8

# # Day-2 Python Challenge

# # Variables and Operators

# In[2]:


x=10
print(x)


# In[3]:


y=2
x=4.5
print(x,y)


# In[4]:


x=" Mango "
print(x)


# In[5]:


student = 25
print(student)

Do not use different symbols on variables (1@$) -- (A-Z and A1, 2B)
# # Many values to multiples variable

# In[8]:


m,b,a = "Mango", "banana", "Apple"
print(m,b,a)


# In[9]:


m,b,a = "Mango", "banana", "Apple"
print(m)


# In[11]:


m=b=a= "Mango"
print(m)
print(b)
print(a)


# # Python Output Variable

# In[14]:


b="Python"
c="Is"
a="Easy"
print(b,c,a)

print() #Two Outputs are Here

print(b)
print(c)
print(a)


# # Data type

# In[15]:


b="Apple"
print(b)
print(type(b))


# In[16]:


a=1
print(a)
print(type(a))


# In[17]:


c=1.3
print(c)
print(type(c))


# In[19]:


d = 2+5j
print(d)
print(type(d))


# In[20]:


a = [1,2,3,4,5,6]
print(a)
print(type(a))


# In[21]:


b = {1,2,3,4,5}
print(b)
print(type(b))


# In[23]:


d = (1,2,3,4,5)
print(d)
print(type(d))


# In[24]:


get_ipython().run_line_magic('whos', '#Show all the elements')


# # Operators in Python

# In[25]:


a = 10
b = 20
print(a+b)


# In[26]:


a = 10
b = 10.5
print(a+b)


# In[29]:


a = "Python"
b = "Easy"
print(a+ " " +b)


# # Subtraction

# In[30]:


a = 10
b = 5
print(a-b)


# In[31]:


a = 20.5
b = 14.7
print(a-b)


# # Multiplication

# In[32]:


a = 5
b = 2
print(a*b)


# In[33]:


a = 45.5
b = 1.7
print(a*b)


# # Division

# In[37]:


a = 10
b = 70
print(b/a)


# In[38]:


a = 70.6
b = 45.67
print(a/b)


# # Modulous

# In[43]:


a = 19
b = 3
print(a%b)


# In[41]:


a = 10.55
b = 35.6
print(a%b)


# # Exponent 

# In[46]:


a = 10
print(a**2)


# # Logical Operators

# In[48]:


a = True
b = False
print(not(b))


# In[49]:


a = True
b = False
print(not(a))

