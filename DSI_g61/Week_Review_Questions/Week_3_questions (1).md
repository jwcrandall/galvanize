## Week 3 Review Questions

1. Linear Algebra: Instantiate matrices A and B, and vector x like:
  ``` python
  A = np.random.randint(0, 50, size=(4, 4))
  B = np.random.randint(0, 50, size=(4, 3))
  x = np.random.randint(0, 50, size=(20, ))
  ```
  Note that the answers will all be different because you have used random numbers to create the matrices. The important piece here is the code to perform the operation. These should all be one line of code

  * Return only the elements of x that are even.
  '''
  [num for num in x  if num % 2 == 0]
  x[x%2 == 0]
  '''

  * Multiply matrices A and B.
  A.dot(B)
  

  * Compute the inverse of A. Can B be inverted? Why or why not?
  np.linalg.inv(A)
  B can not invertible because it is not an n x n matrix.


  * Compute the euclidean distance between rows 1 and 3 of matrix A.
  '''
	import numpy as np
	def distance(v1, v2):
    	return np.sqrt(np.sum((v1 - v2) ** 2))
    	
    np.linalg.norm(A[:,1:], A[:,3:]
     
    	''' 
  * Compute the cosine similarity between columns 1 and 2 of matrix A.
  	'''
  	mag_col1 = math.sqrt(sum(i**2 for i in A[:,1]))
  	mag_col2 = math.sqrt(sum(i**2 for i in A[:,2]))
  	result = A[:,1].dot(A[:,2])/(mag_col1*mag_col2)
  	
  	np.dot(A[:,0],A[:,1])/np.linalg.norm(A[:,0]).dot(np.linalg.norm(A[:,0])
		'''
  * Find the eigenvalues and eigenvectors of matrix A. Describe what eigenvalues and eigenvectors tell you.
    eig_val, eig_vee = np.linalg.eig(A), np.linalg.eigvals(A)

  * Bonus: Find the matrix C such that B * C ≈ A (write C in terms of A and B)
  C = A*B'
  or 
  np.linalg.pinv(B).dot(A)
  or 
  C = np.linalg.lstq(B,A) = np.linalg.

2. What are the assumptions behind OLS linear regression?
- Linear
- strict exogeneity 
- linear independence in X
- spherical error: Homoscedasticity, and no autocorrelation
- normality of errors


3. What are some metrics for linear regression goodness of fit, and what do they mean?
TSS = 
RSS = 
MSE
RMSE
Standard Deviation
R^2
Adj R^2
F-test - probability that the null hypothosis is false 
BIC
AIC
Mallow Cp

4. In the context of machine learning, what are bias and variance?  And what is the bias-variance trade-off?

Bias: The difference between our model's average prediction of y_0 and the true target, y_hat,
over all possible training sets. Also, "the expected value of the differenece of your model's predictions from the true value."

Variance: The expected value of the squared deviation of your model's predictions from the mean of those predictions.

A trade-off often exists between bias and variance because some amount of
model complexity (“flexibility”) is often required to match the underlying
population signal, but this same complexity also makes the fit more sensitive
to noise in the data on which the model is fit.
So as bias decreases, variance often increases — and vice-versa.


5. Explain what kFold cross-validation is and why it's used.



6. What is the curse of dimensionality?  How is it addressed?

increase the number of samples or reduce your feature set (lASSO or backward reduction) or cosine similarities

7. We talked about L1 and L2 regularization.  What are they and in what situations might one be used instead of the other?

8. Draw a confusion matrix for binary predictions.

9. Give an example for each case:
  * Precision is more important than recall.  

  * Recall is more important than precision.  

  * You consider both to be important (and what metric would you use for that?)

10. How is a ROC curve generated?  What does it show?

11. What are the similarities and differences between linear and logistic regression regression and how do you interpret the coefficients in each case?

12. SQL: Given table `houses` below, write a query to...

| id | sqft | beds | neighborhood | type | sale_price |
|:----------:|:------------:|:----------:|:----------:|:-----------:|:-----------:|
| 1 | 1150 | 2 | prospect-park | townhome | 244052 |
| 2 | 2600 | 3 | calhoun-isles | single_family | 609536 |
| 3 | 860 | 1 | uptown | condo | 472993 |
| 4 | 1320 | 3 | north-loop | townhome | 309485 |
| 5 | 1030 | 2 | downtown | townhome | 456141 |
| 6 | 3000 | 3 | uptown | single_family | 544431 |
| 7 | 1400 | 2 | longfellow | condo | 305314 |
| 8 | 3000 | 4 | longfellow | single_family | 485802 |
| 9 | 1700 | 3 | stephens-square | single_family | 337029 |

  * Return the average number of bedrooms and square footage for each type of home in the longfellow neighborhood.

  * Return the average sale price for each  neighborhood and home type.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
