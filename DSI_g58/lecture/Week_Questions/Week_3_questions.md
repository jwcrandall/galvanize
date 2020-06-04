## Week 3 Review Questions

1. Linear Algebra: Instantiate matrices A and B, and vector x like:
  ``` python
  A = np.random.randint(0, 50, size=(4, 4))
  B = np.random.randint(0, 50, size=(4, 3))
  x = np.random.randint(0, 50, size=(20, ))
  ```
  Note that the answers will all be different because you have used random numbers to create the matrices. The important piece here is the code to perform the operation. These should all be one line of code

  * Return only the elements of x that are even.
  A[A % 2 == 0]

  * Multiply matrices A and B.
  A.dot(B)
  * Compute the inverse of A. Can B be inverted? Why or why not?

  np.linalg.norm(A)
  * Compute the euclidean distance between rows 1 and 3 of matrix A.

  np.linalg.norm(col1 - col2)

  * Compute the cosine similarity between columns 1 and 2 of matrix A.

  theta = math.acos( A[1].dot(A[2])/ np.linalg.norm(A) x np.linalg.norm(B) )

  * Find the matrix C such that B * C = A (write C in terms of A and B)
  C = np.linalg.listsq(B,A)[0]
  np.solve(B,A)

  * Find the eigenvalues and eigenvectors of matrix A. Describe what eigenvalues and eigenvectors tell you.

Scalar number that serve the same function as scalar matrix.
w,v = np.linalg.eig(A)

2. What are the assumptions behind OLS linear regression?
'''
A1. The linear regression model is “linear in parameters.”

A2. There is a random sampling of observations.

A3. The conditional mean should be zero.

A4. There is no multi-collinearity (or perfect collinearity).

A5. There is homoscedasticity and no autocorrelation

A6: Error terms should be normally distributed.
'''
3. What are some metrics for linear regression goodness of fit, and what do they mean?

F-stat
MSE
Adjusted R

4. In the context of machine learning, what are bias and variance?  And what is the bias-variance trade-off?
Bias how far your results are from target
Var is the distance the results from the mean of the results

Variance and Bias^2 are inverse related.
What is the complexity relative to the true signal.

5. Explain what kFold cross-validation is and why it's used.

Process of splitting data into val and training. Building the modeling on the training and comparing it to val for k number of times while trying to lower the RMSE.

6. What is the curse of dimensionality?  How is it addressed?

The sparseness in the feature space increases EXP-ly with each additional demninion. Regularization (Ridge or LASSO or ElasticNet). Demnsionality can overfit the model.

7. We talked about L1 and L2 regularization.  What are they and in what situations might one be used instead of the other?

L2: Ridge; The cost function is square of a coeff.
L1: LASSO; the cost function is the absolute value, magnitude, of the coeff.



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
SELECT
  AVG( neighborhood AS avg_beds2,
      AVG(sqft) AS avg_sqft)
FROM houses
WHERE (nieghborhood = 'longfellow')
GROUPBY neighborhood, type
ORDER BY avg_sqft DESC,

  * Return the average sale price for each  neighborhood and home type.
