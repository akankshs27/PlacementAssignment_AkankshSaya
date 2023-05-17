#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Answer 1
def highest_frequency_word_length(string):
    words = string.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_frequency = max(word_counts.values())
    highest_frequency_words = [word for word, count in word_counts.items() if count == max_frequency]
    highest_frequency_word_length = len(highest_frequency_words[0])

    return highest_frequency_word_length


# In[16]:


#Testcase 1:
input_string = "write write write all the number from from from 1 to 100"
result = highest_frequency_word_length(input_string)
print(result)
                                       


# In[17]:


#Testcase 2:
input_string = "she sells sea shells on the sea shore"
result = highest_frequency_word_length(input_string)
print(result)


# In[19]:


#Testcase 3:
input_string = "hello to world hello to to hello to world"
result = highest_frequency_word_length(input_string)
print(result)


# In[ ]:




