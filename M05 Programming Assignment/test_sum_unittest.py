#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Max Mattern
# SDEV220 Fall 2022
# M05 Programming Assignment-Testing
# 11/28/22

# Unittest Tutorial 1
import unittest

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.asserEqual(sum([1,2,3]),6,"Should be 6")
        
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)),6,"Should be 6")

if __name__ == '__main__':
    unittest.main()


# In[ ]:




