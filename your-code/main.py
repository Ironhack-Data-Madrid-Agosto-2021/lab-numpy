#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.



#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

# random.random, returns random floats in the half-open interval [0.0, 1.0):
a = np.random.random((2,3,5))
#print(a)

#random.randint, return random integers from low (inclusive) to high (exclusive):

a1 = np.random.randint(1, 10, size= (2,3,5))
#print(a1)

#random.rand, random values in a given shape:
a2 = np.random.rand(2,3,5)

#print(a2)

#random.rand, return a sample (or samples) from the “standard normal” distribution.
a3 = np.random.rand(2,3,5)

#print(a3)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#print (b)


#7. Do a and b have the same size? How do you prove that in Python code?

#print(a.size == b.size)


#8. Are you able to add a and b? Why or why not?

#suma = a + b

#No, because a and b have different shapes (ranks)

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)

#print(c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c

#No the addition works because they have same rank

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#the difference is that the array d has the same values than a but with 1 added to all of them

#12. Multiply a and c. Assign the result to e.

e = a * c

#13. Does e equal to a? Why or why not?

e == a

#True, because e is the product of a and the identity matrix, wich is the neutral element for product of matices

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#print(d_max)
#print(d_min)
#print(d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty([2,3,5])

#print(f)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, 
assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for i in range(2):
        for j in range(3):
                for k in range(5):
                        if d[i][j][k] > d_min and d[i][j][k] < d_mean:
                                f[i][j][k] = 25
                        elif d[i][j][k] > d_min and d[i][j][k] < d_max:
                                f[i][j][k] = 75
                        elif d[i][j][k] == d_mean:
                                f[i][j][k] = 50
                        elif d[i][j][k] == d_min:
                                f[i][j][k] = 0
                        elif d[i][j][k] == d_max:
                                f[i][j][k] = 100


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
"""

#print(f)
#print(d)


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
f2 = np.empty([2,3,5], str)

for i in range(2):
        for j in range(3):
                for k in range(5):
                        if d[i][j][k] > d_min and d[i][j][k] < d_mean:
                                f2[i][j][k] = 'B'
                        elif d[i][j][k] > d_min and d[i][j][k] < d_max:
                                f2[i][j][k] = 'D'
                        elif d[i][j][k] == d_mean:
                                f2[i][j][k] = 'C'
                        elif d[i][j][k] == d_min:
                                f2[i][j][k] = 'A'
                        elif d[i][j][k] == d_max:
                                f2[i][j][k] = 'E'



