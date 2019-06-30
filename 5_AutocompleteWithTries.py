#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[62]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def is_empty(self):
        return(not self.children)
           
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        
    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True
        
    
    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return(None)
            else:
                current = current.children[char]
        return(current)


# In[64]:


#Some testing:
trie = Trie()
print(trie.root.is_empty())
trie.insert("Aloha")
print(trie.root.is_empty())
node = trie.root
while not node.is_empty():
    print(node.children.keys())
    node = node.children[list(node.children.keys())[0]]

no = trie.find("Aloha")

print(no.children.keys())


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[81]:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
            
    def suffixes(self):
        suflist = []
        node = self
        self._find_suffixes(node, suflist)
        return(suflist)
    
    def _find_suffixes(self, node, suflist, current_suffix = "", previous_key = ""):
        current_node = node
        current_suffix = "".join([current_suffix,previous_key])
        #update suffix list if a complete word is found
        if current_node.is_word:
            suflist.append(current_suffix)
        
        for key in current_node.children.keys():
            next_node = current_node.children[key]
            self._find_suffixes(next_node, suflist, current_suffix, key)
        
        


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[82]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[83]:


#some testing
print(MyTrie.root.suffixes())


# In[85]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




