#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?
The two values are True and False.
True means 1 and False means 0

# 2. What are the three different types of Boolean operators?
AND, OR and Not are three different types of boolean operators
# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).
AND:
    A B AandB
    0 0  0
    0 1  0
    1 0  0
    1 1  1 
OR:
    A B AorB
    0 0  0
    0 1  1
    1 0  1
    1 1  1
NOT:
    A  NOTA
    0   1
    1   0
# 4. What are the values of the following expressions?

# In[1]:


(5 > 4) and (3 == 5)


# In[2]:


not (5 > 4)


# In[3]:


(5 > 4) or (3 == 5)


# In[4]:


not ((5 > 4) or (3 == 5))


# In[5]:


(True and True) and (True == False)


# In[6]:


(not False) or (not True)


# 5. What are the six comparison operators?

# In[ ]:


>,<,>=,<=,==,!=


# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.
Equal operator compares the 2 or more values are equal or not.
Example:
a=10
b=10
if a==b:
    print("True" )
else:
    print("False" )
    
Assignment operator assign the value to the variable.
In the above example a=10. The value 10 is assigned to A. Assignment operator is used.
# In[3]:


a=10
b=10
if a==b:
    print("True" )
else:
    print("False" )


# 7. Identify the three blocks in this code:

# In[8]:



spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

# In[5]:


spam=int(input(("Enter the value")))
if spam == 1:
    print("Hello")
elif spam ==2:
    print("Howdy")
else:
    print("Greetings!")


# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# 

# In[ ]:


ctrl+C 


# 10. How can you tell the difference between break and continue?

# In[ ]:


Break:
    This keyword is used to stop the loop or current itretation or exit from the iteration
    
Continue:
    This keyword is used to continue the loop or forces to continue the next itretaion
    


# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
range(10):
    The range keyword is used to return the sequence of numbers from 0 to 9
Example:
for i in range(10):
    print(i)
    
range(0,10):
In this the start index and stop index are mentioned . It will start from th number in the start index and end at Stop index -1

range(0,10,1):
In the the start index, stop index and step is added. This indicates the start index to be started and how many steps to be taken to next number and stop index -1
# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.
# 

# In[4]:


#for loop
for i in range(1,11):
    print(i)


# In[8]:


#While loop
i=1
while i<=10:
    print(i)
    i+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?

# In[ ]:


spam.bacon()

