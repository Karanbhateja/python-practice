# In Python, iterable and iterator are two related but distinct concepts used for working with collections of data. Understanding the difference between them is crucial.

# Iterable:
# An iterable is an object that can be looped over or iterated. It is any collection of items that can be accessed sequentially one at a time. Common iterable types include lists, tuples, strings, dictionaries, and sets.

# Example of an iterable:
my_list = [1, 2, 3, 4, 5]

# You can loop over the elements of a list using a for loop:
for item in my_list:
    print(item)

# Iterator:
# An iterator is an object that represents a stream of data and can be iterated (looped) over. It maintains state and remembers the current position during iteration. To create an iterator from an iterable, you use the iter() function.

# Example of creating an iterator from an iterable:
my_iterable = [1, 2, 3]
my_iterator = iter(my_iterable)

# You can loop over the elements of an iterator using a for loop or the next() function:
for item in my_iterator:
    print(item)

# Or using next():
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Difference between Iterable and Iterator:
# - An iterable is an object with an associated iterator.
# - An iterator is an object that tracks the current position in the iterable and returns the next item in the sequence.
# - An iterable can be looped over directly (e.g., using a for loop).
# - An iterator requires explicit iteration using the next() function.

# In summary, an iterable is a container with data that can be iterated, while an iterator is an object that keeps track of the iteration state. You can create an iterator from an iterable, and iterators allow you to access elements one at a time.

# Python's built-in functions like iter() and next() make it easy to work with iterable and iterator objects.

# Note: Some objects, like lists, are both iterable and iterator by nature, so you can directly use them in for loops.
