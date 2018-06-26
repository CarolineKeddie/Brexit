<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

#  Python Review Iterations - for and while loops

---

### Core
- Formulate for and while loops
- Iterate using for loops

```python
    for iterator_name in iterating_sequence:
        …statements…
```

- Typical iterating sequences
 - `my_list`, an existing list
 - `range(10)`, creating a list over which to iterate
 - `range(len(my_list))`, iterating over the indices of an existing list
 - `some_string`, iterating over the letters in a string

- Iterate using while loops

```python
    while condition:
        …statements…
```

- Typical conditions
 - `count < 5`
 - `reply!='stop'`
 
### Target
- Know about the dangers of using while loops
 - Don't forget to modify the condition in the loop body
