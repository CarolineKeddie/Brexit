<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Intro to Python: Lists & Dictionaries

---

### Core
- Create lists and operate on them
- Create dictionaries and operate on them
- Extract values from a list or dictionary

### Target

- Make use of built-in functions for lists and dictionaries
- Know the difference between tuples and lists

### Stretch

- Know the difference between functions which return a new expression and those which act in place


### Some built-in functions

#### Lists
- use **`.append(item)`** to add item to a list
- use **`.extend([item1, item2])`** to join another list to the end of the list
- use **`.insert(index, item)`** to add an item to a list at an index
- use **`.remove(item)`** to remove an item from a list
- use **`.sort()`** to sort a list
- use **`.count(item)`** to count the number of times an item appears in a list
- use **`.index(item)`** to find the index of an element in a list
- use **`.pop()`** to extract (and remove) the last element of a list
- use **`.reverse()`** to reverse a list
- use **`del my_list[index]`** to remove an item at the index position from a list

#### Dictionaries
- use **`.pop(key)`** to remove a `key:value` pair from the dictionary and return the value
- use **`.get(key)`** to get the value for a `key`
- use **`my_key in my_dictionary`** to check if a key `my_key` is in the dictionary `my_dictionary`
- use **`.keys()`** to get a list of the keys in the dictionary
- use **`.items()`** to get a list of the `key:value` pairs in the dictionary
- use **`.update(other_dictionary)`** to merge a second dictionary into the current dictionary
- use **`.clear()`** to remove all `key:value` pairs from the dictionary
- use **`del my_dict[key]`** to remove a key-value pair from the dictionary