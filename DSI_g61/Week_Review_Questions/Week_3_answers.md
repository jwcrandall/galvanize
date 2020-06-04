## Week 3 Review Question Answers

<br>1. **Linear Algebra: Instantiate matrices A and B, and vector x like:**
  ``` python
  A = np.random.randint(0, 50, size=(4, 4))
  B = np.random.randint(0, 50, size=(4, 3))
  x = np.random.randint(0, 50, size=(20, ))
  ```
  **Note that the answers will all be different because you have used random numbers to create the matrices. The important piece here is the code to perform the operation. These should all be one line of code**

  * **Return only the elements of x that are even.**
  ```python
  x[x % 2 == 0]
  ```  
  * **Multiply matrices A and B.**
  ```python
  # possible answer 1
  A.dot(B)
  # possible answer 2
  np.dot(A, B)
  ```
  * **Compute the inverse of A. Can B be inverted? Why or why not?**
  ```python
  np.linalg.inv(A)
  ```
  B cannot be inverted because it is not a square matrix.

  * **Compute the euclidean distance between rows 1 and 3 of matrix A.**
  ```python
  # possible answer 1 (easy way)
  np.linalg.norm((A[0, :] - A[2, :]))
  # possible answer 2 (long way)
  ((A[0, :] - A[2, :])**2).sum()**0.5
  ```
  * **Compute the cosine similarity between columns 1 and 2 of matrix A.**
  ```python
  # possible answer 1 (indexing columns)
  col1, col2 = A[:, 0], A[:, 1]
  np.dot(col1, col2) / (np.linalg.norm(col1) * np.linalg.norm(col2))
  # possible answer 2 (using matrix transpose)
  col1, col2 = A.T[0], A.T[1]
  np.dot(col1, col2) / (np.linalg.norm(col1) * np.linalg.norm(col2))
  ```
  * **Find the eigenvalues and eigenvectors of matrix A. Describe what eigenvalues and eigenvectors tell you.**  
  ```python
  vals, vecs = np.linalg.eig(A)
  for i in range(A.shape[0]):
    print('eigenvalue {} is associated with eigenvector {}'.format(vals[i], vecs[:, i]))
  ```
  * **Bonus: Find the matrix C such that B * C ≈ A (write C in terms of A and B)**
  ```python
  C = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(A)
  ```

<br>2. **What are the assumptions behind OLS linear regression?**
  * Linear relationship between predictors and response.
  * Linear independence of regressors (X)
  * Errors are normally distributed
  * Errors have mean of 0 (“strict exogeneity”).  E[e | X] = 0
  * (Spherical errors)
    * Homoscedasticity: constant variance of errors
    * No autocorrelation of errors

<br>3. **What are some metrics for linear regression goodness of fit, and what do they mean?**
  * RSS = Residual sum of squares. What the model tries to minimize. Scales with the number of data points, hard to compare across different training set sizes.  
  * MSE = mean squared error. RSS divided by the number of points in the sample.
  * RMSE = Root mean squared error. Square root of MSE so very easy to interpret as it is in same scale as Y.
  * R^2 = “proportion of variance explained” by the model = 1 - RSS/TSS.  Between 0 and 1, 1 is best.
  * Adjusted R^2 = penalizes R^2 with addition of features
  * F-statistic: Tests whether there is a relationship between predictors and response.  Used to test null hypothesis that all beta coefficients are 0. If F is large then p-value of F is small, and your model is not meaningless.

<br>4. **In the context of machine learning, what are bias and variance?  And what is the bias-variance trade-off?**  
    Bias is the offset of the expected value of a prediction from the true value.  Variance is the scatter of the predictions around the expected value.  The bias-variance tradeoff is the general inverse relationship between the two:  as model complexity (or flexibility) changes either bias will increase and variance will decrease, or vice versa.  This occurs because the underlying signal is unknown and the data that the model trains on has some irreducible error that is also unknown.  Therefore, changes in model complexity will change the ability of the model to fit the training data, and its performance on test data will be affected by the inherent assumption associated with the functional form of the "signal" in the model and its relation to the true underlying signal.

<br>5. **Explain what kFold cross-validation is and why it's used.**  
    Cross-validation is a model validation technique for assessing how the results of a statistical analysis will generalize to an independent data set. It is mainly used in settings where the goal is prediction, and one wants to estimate how accurately a predictive model will perform in practice. **kFold** cross-validation takes a training set and divides it into a number (k) of similarly sized training-validation set groups (folds) where the model is fit on the training set in that fold and then evaluated in the validation set in this fold.  The metric of interest for each fold is averaged with the other folds and then presented as representative of that model's performance on unseen data.  In the end, the selected (through cross-validation as the best performing model on the training data) model's performance can be checked at the end on the completely unseen holdout set.

<br>6. **What is the curse of dimensionality?  How is it addressed?**  
  As the number of dimensions increase, the volume that the existing data occupy grows exponentially. You can relate the sample density in two differently dimensioned spaces through the relation N1^(1/D1) ~ N2^(1/D2) where N1 and N2 are the number of samples in dimensions D1 and D2.  In high dimensional spaces all distance based metrics are far apart.    Common ways that dimensionality are addressed are by 1) gathering more data, 2) regularization, 3) collapsing multiple dimensions into fewer dimensions that contain the most variance (PCA, SVD), and 4) if a distance metric is required, using something like cosine similarity instead.

<br>7. **We talked about L1 and L2 regularization.  What are they and in what situations might one be used instead of the other?**
  * Regularization is a technique to control overfitting by introducing a penalty
  term over the error function to discourage coefficients from reaching large values.
  L1 regularization (Lasso) regularizes using the absolute values of the coefficients,
  while L2 regularization (Ridge) regularizes using the square of the coefficients.

  * In the case of two features that are collinear, an L1 will eventually pick one and
  zero the other one out, while L2 will shrink both coefficients.  And so depending
  on use case L1 or L2 might be preferable here.

  * If you have a sparse signal (most of your features aren't predictive), then L1
  will do a better job finding the few predictive features.

  * L2 will generally make more predictive models than L1.

  * Remember you can have both: it's called an Elastic Net.

<br>8. **Draw a confusion matrix for binary predictions.**  

  || Predict N | Predict P |
  |-|:-:|:-:|
  | Actual N |TN|FP|
  | Actual P |FN|TP|  

<br>9. **Give an example for each case: **
  * **Precision is more important than recall.**  
    Precision is the fraction of the predicted positives that were actually positive. This would be more important in prison sentences and courts. `TP/(TP+FP)`
  * **Recall is more important than precision.**    
    Recall is the fraction of the actually positive cases that were predicted positive.  This would be more important in community health related domains, such as catching possible sources of contaminated food, or early screening for disease. `TP/(TP+FN)`
  * **You consider both to be important (and what metric would you use for that?)**
    The F1 score is the harmonic average of precision and recall and often used as a metric that takes both into account.  You'd like a process that screens for an expensive medical procedure to have a large F1 score.

<br>10. **How is a ROC curve generated?  What does it show?**   
    A ROC curve is made by taking predicted classification probabilities and thresholding them to a positive or negative class to compare to actual classifications to get true and false positive rates for that model evaluated at that threshold.  The ROC curve then displays the effect of the threshold on the true positive and false positive rates for all thresholds.  ROC curves are useful for comparing models and the effect of the classification threshold in a given model.

<br>11. **What are the similarities and differences between linear and logistic regression and how do you interpret the coefficients in each case?**  
Both are linear models where the response is a linear function of the inputs.  However, in linear regression the target or response *is* the sum of the coefficients and the inputs, yielding a continuously values response, while in logistic regression the sum of the coefficients and inputs is related to the logit - the log odds of (usually) the positive class occurring.  A classification threshold is used with the probabilities calculated from the odds to classify samples into discrete classes.

<br>12. **SQL: Given table `houses` below, write a query to...**

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

  * **Return the average number of bedrooms and square footage for each type of home in the longfellow neighborhood.**
  ```SQL
  SELECT type, AVG(beds) AS avg_beds, AVG(sqft) AS avg_sqft
  FROM houses
  WHERE neighborhood = 'longfellow'
  GROUP BY type
  ```
  * **Return the average sale price for each neighborhood and home type.**
  ```SQL
  SELECT neighborhood, type, AVG(sale_price) AS avg_price
  FROM houses
  GROUP BY neighborhood, type
  ```
