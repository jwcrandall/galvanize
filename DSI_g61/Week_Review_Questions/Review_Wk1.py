## Week 1 Review Questions

1. Compare and contrast functional and object oriented programming paradigms.  Then discuss the the 3 pillars of OOP and how they relate to Python.

Functional programing evaluate an expression and use the result, while OOP passes messages between meaningful objects.
Python is an imperative programming language that has both functional and object-oriented aspects.
The three pillars of OOP are as follows:
- Inheritance: Organizing complex systems from general to specific by reuse of base classes to form derived classes
Example:
- Polymorphism: Methods/operations of the same name act differently on objects of different types.
Polymorphism just works if object supports the necessary attribute or method (ie duck-typing).
Example: ‘+’ operator works on both ints and Points and strings
- Encapsulation: Data and methods are bundled within class definitions
Example: Outside code can directly access and change an object's data

2. **What are some distinguishing characteristics of the Python programming
language?**
    * Python supports many different programming paradigms:
        * imperative: focuses on describing how a program operates; uses statements to change a program's state
        * object-oriented: focuses on objects that contain data and methods to work on that data
        * procedural: based on the idea of a procedural call, it's a type of imperative programming that relies heavily on blocks and scope
        * functional: computation is based on the evaluation of mathematical functions, and avoids changing state and mutable data. It's a declarative programming paradigm.
    * It's interpreted, instead of compiled.
    * Design philosophy emphasizes code readability
    * Has a large development community, and open source development.

3. **What are some differences between Python 2 and Python 3?  Why was Python 3
developed?**
    * print function is different
    * many of the functions that returned a list in python 2 return an iterator in Python

    One of the guiding principles of Python 3 was to "reduce feature duplication by removing the old ways of doing things."
4. **List major data structures in Python.  Which data structure(s) would you use to
in each of the following situations, and why:**

  * Unchanging sales records - tuple, because it's a lightweight data structure good for unchanging data

  * A customer database where changing information, such as address, email, and purchases are associated with a given customer name. - dictionary, with key as customer identifier(name), and a list as values, where the list elements can be changed

  * Driving waypoint locations between arbitrary points A and B. - an arbitrary length list of tuples associated with each waypoint

  * The unique words used in a text corpus. - set, unique values

  * A search engine that returns results quickly for a given search term. - dictionary with key as search term and value as the results

5. **Write a one line list comprehension to perform the following matrix
multiplication (A dot product B).  Describe how it works. How would you check
it with NumPy?**

    import numpy as np

    def matrix_multiplication(A, B):
        return [[sum(A[i][j]*B[j][k] for j in range(len(A[0])))
            for k in range(len(B[0]))] for i in range(len(A))]

    if __name__ == '__main__':
        A = [ [ 2, 4], [ 1, 7], [-1, 8] ]

        B = [ [3, 2, -5, 6],  [1, -3, 4, 8] ]

        print("Matrix multiplication results:")
        mat = matrix_multiplication(A, B)
        for line in mat:
            print(line)

        print("\nNumpy results:")
        Anp = np.array(A)
        Bnp = np.array(B)
        print(np.dot(Anp,Bnp))
        #[[ 10  -8   6  44]
        # [ 10 -19  23  62]
        # [  5 -26  37  58]]

6. Estimate the run-time complexity (O(N) notation) of the following code:
  ```python
  def find_duplicates(l1, l2):
    '''
    searches through lists 1 and 2 and eliminates duplicate entries from list 2
    '''
    for item1 in l1:
      for item2 in l2:
        if item2 == item1:
          # removes item from list
          l2.remove(item2)
    return l1, l2
  ```
  Write another function with the same functionality that works more efficiently. Use timeit to see how well you can do!

  (Hint: you could use something like
  ```np.random.randint(0, 100, 50)```
  to create random lists to practice with)

7. Use datatable 'customers' (example rows below), write a SQL query to....

| cust_id | cust_name | current_city | hometown |
|:----------:|:------------:|:----------:|:-----------:|
| 1 | Amanda | Atlanta | Raleigh |
| 2 | Brittany | Denver | New York |
| 3 | Charles | Paris | Raleigh |
| 4 | David | San Diego | Los Angeles |
| 5 | Elizabeth | Atlanta | London |
| 6 | Greg | Denver | Atlanta |
| 7 | Maria | Raleigh | New York |
| 8 | Sarah | New York | Raleigh |
| 9 | Thomas | Atlanta | Raleigh |

  **Assume that everyone has moved**

  A) Return the city with the highest population growth. (Highest net of people who currently live there minus people who used to live there)

  B) Return pairs of "friends" (can be two columns or a tuple) that have both the same hometown and current city. Remove duplicates!
