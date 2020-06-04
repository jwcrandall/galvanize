'''
1. An objective function is any function for which we wish to find the minimum
or maximum.

"A cost functin is a type of objective function"

example of max: Maximize the log-likelihood of data
example of min: Minimize the "loss function" or "error function"
'''
'''
2. Gradient Descent
'''

X = np.array([[-9, -7, -1],
             [ 6, -5, -2],
             [-7, -1,  8],
             [ 3, -1,  6]])

y = np.array([[-26],
             [-10],
             [ 15],
             [ 19]])

N = X.shape[0]
y_p = np.dot(X, coeffs)
cost_func = 1/N * np.sum((y - y_p)**2)
cost_dot = -2/N * np.dot(X.T, (y - y_p))
alpha = 0.0001
beta_array = alpha * cost_dot # = [0.99775, 1.0041, 1.0106]

'''
3.
Describe the three types of gradient descent and discuss advantages and
disadvantages of each. What are the main hyperparameters to tune in gradient
descent?

Stocastic Gradient descent : performs gradient descent for each training
example in x along with its corresponding y.
Adv:
Dis-adv: saddle points and reviens
hyperparameters: stopping condition, change in gradient, change in cost func.

Bach gradient descent: Computes the gradient of the cost funciont wrt
theta for the entire data set
Adv:
Dis-adv:


mini-bach: peformes an update for every mini-bach of training examples
Adv:
Dis-adv:
Learning rate, stopping condition, bach size

4. Name some other optimization algorithms/ variants on gradient descent
and give a brief overview of how they work.

Gradient decent with momentum (Nestrov), Adagrab: how gradient has changed between interation
to change learning rate, Newton's Method.

5. Curse of demensionality...
regularization, change distance formula, get more data, drop features.

6.
Step-by-step:
 1- Maximize IG: for through each feature
 Classification: Gini, Shannon
 Regression: RSS

 OVERFITTING! Limit the number of splits, number the value of the splits
 use k-fold validation

 7. Boostraping and selection of features
 8. It's not deterministic
 9. feature importance, IG, measure how many points go throw a single split.
 10.
 RF: trees are build on the same data, B sequential trees
 RF: randomly picks the features at a given split, you're only looking at a few features;  B: alpha, learning rate, and reweighting
 [skipped]
 RF is a low bias ,high variance B: low bias, low variance

11.
convert weak learning into strong learniner
Adaboost - modifies weights
Gredient Boosting - weak learning train on remaining errors

12. lambda and the ratio between a/(a+b)

'''
