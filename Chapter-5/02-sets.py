# Making sets.
# Sets does not allow duplicate values.
s = {1, 5, 45, 5}
print(s)
print(type(s))

# Making empty set.
e = set()
print(e)
print(type(e))

# 'len' function is used determine length of the set.
print(len(s))

# 'add' method adds an element to a set.
s.add(7)
print(s)

# 'remove' method removes elements from a set and return error if the value is not found.
s.remove(7)  # shows error if the value is not found.
print(s)

# 'discard' element remove the specified element from the set but does not show error if the value is not found.
s.discard("7")
print(s)

# 'pop' method removes and return an arbitrary element from the set.
popped_item = s.pop()
print(s)
print(popped_item)

# 'update' method adds multiple elements to the set.
s.update([3, 6, 2])
print(s)

# 'copy' element returns a shallow copy of the set.
new_set = s.copy()
print(new_set)

# 'clear' element clears the entire set.
new_set.clear()
print(new_set)

# 'intersection' method returns a new set with elements common to the set and all other sets.
s1 = {1, 2, 3}
s2 = {2, 4, 6}
intersection_set = s1.intersection(s2)
print(intersection_set)

# 'difference' method returns a new set with elements that are in the original set but not in specified set.
difference_set = s1.difference(s2)
print(difference_set)

# 'symmetric_difference' method returns a new set with elements that are not common in both sets.
symmetric_set = s1.symmetric_difference(s2)
print(symmetric_set)

# 'issubset' method returns True if a set is subset of another set.
ss1 = {1, 2, 3, 4}
ss2 = {1, 2, 3, 4, 5}
print(ss1.issubset(ss2))

# 'issuperset' method returns True if a set is superset of another set.
ss1 = {1, 2, 9}
ss2 = {1, 2, "4"}
print(ss2.issuperset(ss1))

# 'isdisjoint' method returns True if the set has no elements in common with another set.
sss1 = {1, 2, 3}
sss2 = {"1", "2", "3"}
print(sss1.isdisjoint(sss2))

# 'union' method return a new set containing all the unique elements from the original set and any other provided set or iterable.
ns1 = {10, 8, 6, 45}
ns2 = [9, 4, 8, 7, 6, 2]
print(ns1.union(ns2))
