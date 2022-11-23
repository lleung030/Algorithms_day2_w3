#!/usr/bin/env python
# coding: utf-8

# # Cl

# ## Tasks Today:
#  
# 1) <b>In-Place Algorithms</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Out of Place Algorithm <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) In-Class Exercise #1 <br>
# 2) <b>Two Pointers</b> <br>
# 3) <b>Linked Lists</b> <br>
# 4) <b>Merge Sort</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Video on Algorithms <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) How it Works <br>
# 5) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Reverse a List in Place Using an In-Place Algorithm <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Exercise #2 - Find Distinct Words <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Exercise #3 - Write a program to implement a Linear Search Algorithm. <br>

# ## In-Place Algorithms

# In[ ]:


an inplace algorithims modifies the parameter that is passed in 


# In[ ]:





# #### Syntax

# In[7]:


def double_num(a_lst):
    print(hex(id(a_lst)))
    for idx in range(len(a_lst)):
        a_lst[idx] *= 2


# In[8]:


nums = [1,2,3,4,5]
print(hex(id(nums)))
double_num(nums)


# In[13]:


def custom_append(a_lst, num):
    a_lst = a_lst[:]
    a_lst.append(num)


# In[14]:


nums = [1,2,3]
custom_append(nums, 4)
print(nums)


# #### Out of Place Algorithm

# In[16]:


num = [1,2,3]

num[0], num[1]=num[1], num[0]


# In[17]:


num


# In[18]:


temp = num[0]
num[0] = num[1]
num[1] = num[0]


# In[ ]:


def swap(a_list, idx1, idx2):
    a_list[idx1], a_list[idx2] = a_list[idx2], a_list[idx1]


# In[ ]:


def swap(a_list, idx1, idx2):
    a_list = a_list[:]
    a_list[idx1], a_list[idx2] = a_list[idx2], a_list[idx1]
    return a_list


# #### In-Class Exercise #1 <br>
# <p>Write a function that takes in four arguments (list, index1, index2, index3), and swaps those three positions in the list passed in.</p>

# In[34]:


l_1 = [10, 4, 3, 8, 4, 2, 6]

#swap out of place
def swap_op(a_list, idx1, idx2, idx3):
    a_list = a_list[:]
    a_list[idx1], a_list[idx2], a_list[idx3] = a_list[idx3], a_list[idx1], a_list[idx2]
    print(hex(id(a_list)))
    return a_list
    # 10, 8, 4, 3...
    
#swap in place
def swap_in(a_list, idx1, idx2, idx3):
    a_list[idx1], a_list[idx2], a_list[idx3] = a_list[idx3], a_list[idx1], a_list[idx2]
    print(hex(id(a_list)))
    


# In[38]:


print(swap_op(l_1, 1, 2, 3))
swap_in(l_1, 1, 3, 5)


# ## Two Pointers

# #### Syntax

# In[39]:


#write an algorithm in reverse order 
# i              j
#[1, 2, 3, 4, 5, 6]
#    i        j
#[6, 2, 3, 4, 5, 1]
#       i  j
#[6, 5, 3, 4, 2, 1]

#[6, 5, 4, 3, 2, 1]

#1. define pointer 1 as 0
#2. define pointer 2 as the length of the list minus 1
#3. swap the items at positions of pointer 1 and 2
#4. increment pointer 1
#5. decrement pointer 2
#6. repeat steps 3, 4, 5, until pointer 1 is greater than pointer 2

def reverse(a_list):
    #step 1
    i = 0 #pointer 1
    #step 2
    j = len(a_list)-1 #pointer 2
    
    #step 6
    while i<j:
        #step 3
        a_list[i], a_list[j] = a_list[j], a_list[i]
        #step 4
        i+=1
        #step 5
        j-=1
        


# In[40]:


nums = [1,2,3,4,5,6,7]
reverse(nums)

print(nums)


# In[ ]:


### Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


# In[42]:


#step 1 loop through the list for i in range(len(list))
#step 2 i = 0 pointer 1
#step 3 j = 1 pointer 2
#step 4 if sum i + j == target then return indices (i, j)
#step 5 if not then j += 1 and repeat step 4
#step 6 i +=1 
#step 7 if sum i + j == target then return indicies (i, j)
#step 8 if not repeat step 5
#step 9 


# In[ ]:


def reverse(a_list):
    #step 1
    i = 0 #pointer 1
    #step 2
    j = len(a_list)-1 #pointer 2
    
    #step 6
    while i<j:
        #step 3
        a_list[i], a_list[j] = a_list[j], a_list[i]
        #step 4
        i+=1
        #step 5
        j-=1


# In[66]:


def two_sum(a_list, target):
     # Step 1
    i = 0 # pointer 1
    
    # Step 8
    while i < len(a_list):
    
        # Step 2 / Step 7 
        j = len(a_list) - 1 # pointer 2

        # Step 5
        while i < j:

        #    Step 3
            if a_list[i] + a_list[j] == target:
                return a_list[i], a_list[j]

            # Step 4
            j -= 1

        # Step 6
        i += 1


# In[75]:


def two_sum(a_list, target):
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)):
            
            if a_list[i] + a_list[j] == target:
                return a_list[i], a_list[j]
            


# In[85]:


i = 0
while i < len(a_list):
    # step 2
    j = i + 1
    while j < len(a_list):
        
        # step 3
        if a_list[i] + a_list[j] == target:
            # step 4
            return [i, j]
        
        j += 1
        
    i += 1
        
two_sum([3,2,4,5,6], 6)


# In[79]:


print(two_sum([2,7,11,15], 9))


# In[77]:


print(two_sum([2,7,11,15], 13))


# #### Video of Algorithms <br>
# <p>Watch the video about algorithms.</p>
# 
# https://www.youtube.com/watch?v=Q9HjeFD62Uk
# 
# https://www.youtube.com/watch?v=kPRA0W1kECg
# 
# https://www.youtube.com/watch?v=ZZuD6iUe3Pc

# # Sorting Algorithms

# #### Bubble Sort
# 
# Worst Case: O(n^2) Time - O(1) Space

# In[86]:


#set a pointer at the beginning of the list
#set end_index to the length of the list minus 1
#set of flag of sorted to false

def bubble_sort(a_list):
    a_list = a_list[:]
    
    end_index = len(a_list)-1
    
    is_sorted = False
    #continue looping through pairs until sorted becomes true
    while not is_sorted:
        is_sorted = True
        
        for i in range(end_index):
            j = i + 1
        
            if a_list[i]>a_list[j]:
                a_list[i], a_list[j] = a_list[j], a_list[i]
                is_sorted = False
                
        end_index -= 1
    
    return a_list
        


# In[87]:


bubble_sort([99,4,5,2,596,4,1,0])


# ##### Insertion Sort
# 
# Worst Case: O(n^2) time - O(1)space

# In[ ]:





# ## Merge Sort

# #### How it Works

# In[ ]:





# # Binary Search
# 
# The Binary Search algorithm works by finding the number in the middle of a given array and comparing it to the target. Given that the array is sorted
# 
# * The worst case run time for this algorithm is `O(log(n))`

# In[ ]:





# # Exercises

# ### Exercise #1 <br>
# <p>Reverse the list below in-place using an in-place algorithm.<br>For extra credit: Reverse the strings at the same time.</p>

# In[241]:


words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_string(a_list):
    new_list = [letters[::-1] for letters in a_list]
    new_list.reverse()
    return new_list
    


# In[242]:


print(reverse_string(words))


# In[195]:


words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_(a_list):
    a_list.reverse()
    return a_list


# In[196]:


print(reverse_(words))


# ### Exercise #2 <br>
# <p>Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.<br>Should output:<br>{'a': 5,<br>
#  'abstract': 1,<br>
#  'an': 3,<br>
#  'array': 2, ... etc...</p>

# In[163]:


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

word_dict = {}

def word_count(string):
    words = string.split()
    for word in words:
        if word not in word_dict:
            word_dict.update({word:words.count(word)})
    return word_dict








# In[164]:


print(word_count(a_text))


# In[ ]:




