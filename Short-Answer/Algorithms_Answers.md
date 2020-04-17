#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
a)  a = 0                 # time:O(1) 
    while (a < n * n * n):  # time:O(n)
      a = a + n * n       # time:O(1) 
----
Answer a: The time complexity for this code snippet is O(n)


b)  sum = 0         # time:O(1) 
    for i in range(n): # time:O(n)
      j = 1          # time:O(1)
      while j < n:   # time:O(log(n))
        sum += 1    # time:O(1)
----
Answer b: The time complexity for this code snippet is O(nlog(n))


c)  def bunnyEars(bunnies):
      if bunnies == 0:      # time:O(n)
        return 0

      return 2 + bunnyEars(bunnies-1)   # time:O(1) 
----
Answer: The time complexity for this code snippet is O(n)

Answer c: The time complexity for this code snippet is O(n)

## Exercise II
A solution for this exercise would be to use a binary search which has a time complexity of O(log(n)):

1. Start with the middle floor.
2. Do the egg-drop-test
3. If "Egg broke":
     Eliminate all of the higher floors.
     Make the highest floor the floor below the current floor.
     Make the lowest floor the first floor.
     Repeat the egg-drop-test until "Egg did not break" is returned.
     Return the current floor.
4. If "Egg did not break":
     Eliminate all of the lower floors.
     Make the lowest floor the floor above the current floor.
     Make the highest floor the top floor.
     Repeat the egg-drop-test until "Egg broke" is returned.
     Return the floor below the current floor.

Egg-drop-test:
    Drop the egg from the floor you are on
    If the egg drops return: "Egg broke"
    If the egg didn't break return: "Egg did not break"

