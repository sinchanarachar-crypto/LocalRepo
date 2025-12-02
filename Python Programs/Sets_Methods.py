ex=set()
ex.add(2)
ex.add(5)
ex.add(7)   #we can add strings an tuples but not lists
ex.add((12,17,29))
ex.add("SHINCHAN")
ex.add(9)   #adds the following elements to the set 'ex' 

print(ex)   #position of elements added will vary as set doesn't have index

ex.remove(5)   #removes 5 from the set 'ex'. If I command to remove something that didn't exist in set it shows error

print(ex.pop())  #removes a randomm element

ex.clear()  #erase all the elements in the set. lenght of set will be returned as 0

print(ex)  # prints set() as output inndicating set is empty