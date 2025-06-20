#!/usr/bin/env python
# coding: utf-8

# In[3]:


def say_hi(name=""):
    print("Hello", name)

while True:
    name = input("Your name: ")
    if name in ("Stop", "stop", "Exit", "exit"):
        break
    say_hi(name)







