1. Gradient Descent: What is an objective function? Give an example of a cost function to minimize and a cost function to maximize.

2. Gradient Descent : instantiate the dataset

  ```python
  X = np.array([[-9, -7, -1],
                [ 6, -5, -2],
                [-7, -1,  8],
                [ 3, -1,  6]])

  y = np.array([[-26],
                [-10],
                [ 15],
                [ 19]])
  ```
  * Compute the gradient for the objective function with respect to the parameters.
  <p>(1/N) Σ (y - xβ)<sup>2</sup> = (1/N) Σ (y - (x<sub>1</sub>β<sub>1</sub> + x<sub>2</sub>β<sub>2</sub> + x<sub>3</sub>β<sub>3</sub>))<sup>2</sup>
  <p>(parameters are β<sub>1</sub>, β<sub>2</sub>, β<sub>3</sub>)
  * Evaluate the gradient at β<sub>1</sub> = β<sub>2</sub> = β<sub>3</sub> = 1
  * Compute a parameter update for a learning rate of α = .0001.

3. Describe the three types of gradient descent and discuss advantages and disadvantages of each. What are the main hyperparameters to tune in gradient descent?

4. Name some other optimization algorithms/ variants on gradient descent and give a brief overview of how they work.

5. You're trying to make model that will predict the female gold medal winner in the high jump in the next Olympics.  You have results and data for 1000 high-jumpers in the past.  You're using four features: `jumper_height`, `jumper_weight`, `best_jump_height`, and `fastest_100m_time` as features and your model performs ... just ok during cross-validation. Then it hits you: you also have `maximum_squat_weight` for all the jumpers, why don't you use that as a feature too?  Using this additional feature (5 total now) during cross-validation, however, you get widely varying estimates of model performance.  What do you think is going on?  
  As a bonus, how many data points would you need with 5 features to have the same sample density as your model had with 4 features?

6. Decision tree questions:  
  * Describe, step-by-step, how a decision tree is built.
  * Describe how a binary split is made at a node in the case of:
    * classification
    * regression
  * You decide to use a Decision Tree on the Olympic high jumper problem and you end up with a model that does very well on the training data but predicts poorly in cross-validation.  What can you do?
<p>

7. What are the two things that make a random forest "random"? 

8. What problem from bagging is solved by using a random forest? Hint: what type of algorithm is a decision tree split?

9. You are a data scientist at a subscription company, and you decide to use a random forest model for predicting churn. The model works well, but your boss wants some insight into what factors contribute to customer churn. What can you tell him/her?  

10. Compare and contrast random forests and boosted trees with regards to:  
  * The data that each tree in the ensemble is built on.  

  * How the quality of a split on a given feature and its value is evaluated.  
  * The general depth of each tree.

  * The bias-variance trade-off associated with each tree in the ensemble.  

  * How the ensemble can achieve a low-bias, low-variance model.  

11. Compare and contrast Adaboost and gradient boosting.

12. Describe the elastic net regularization parameter. Explain the two hyperparameters.

13. Describe the hyperparameter C associated with SVMs, and how different values of C affect bias and variance of your model.