# 1.
A = [ [ 2, 4], [ 1, 7], [-1, 8] ]

B = [ [3, 2, -5, 6],  [1, -3, 4, 8] ]

a1 =  [sum(i[0] * i[1]) for i in zip(A, B)]
a1 = sum([x*y for x,y in zip(A,B)])
a1 = [A[i]*B[j] for i in range(len(A)) for j in range(len(B))]
ab = [A[i]*B[i] for i in range(len(A))]
ab = lambda K, L:reduce(lambda z1, z2: z1+z2, map(lambda x: reduce(lambda x1, x2: x1*x2, x), zip(K, L)))
ab = map(lamda x: )
# 2.

'''SELECT SUM(sales_price)/SUM(bds)
        AVG(beds) AS avg_beds,
        AVG(sqft) AS avg_sqft
FROM houses
WHERE neighborhood = 'longfellow'
GROUP BY type
'''

'''SELECT neighborhood

FROM houses
WHERE type = 'family homes'
GROUP BY neighborhood
ORDER BY COUNT(*)
LIMIT 1

'''

'''
3. What probability distribution would you use to describe the following situations?

How many customers arrive at the Starbucks in a certain time window.
>> poisson distribution

Modeling the distribution of SAT scores (hint: treat them as continuous).
>>> Normal distribution

The number of defective parts that come off of an assembly line.
>>> binomial distribution
'''

'''
4.  Your friend flips a coin, then rolls dice/die, and tells you the total on the die.
If the coin shows heads, she rolls one die.
If it shows tails, she rolls two dice.
What is the probability that the coin came up heads, given that the die/dice total is 6.

    Use Bayes Rule:

        P(H|6) = [P(6|H) * P(H)] / P(6)

    Determine the value of each part:

        P(6|H) = 1/6
        P(6|T) =  5/36
        P(6) = P(6|H) * P(H) + P(6|T) * P(T)'''

p_6_H = (1/6) * (.5*(1/6) + .5 * (5/36))/.5 # = 0.0509 = 6/11

'''
5. No, because we are doing multiple hypothesis testing. The p-value need to be
less than quotenct of the significancy level( assuming alpha = 0.05) and the number of hypthesis (m=4).
p = 0.02 > 0.0125
'''
# 6. see picture...writen somewhere
# 7: CLT: When indpendent varaible as added their distribution mean of the sample goes toward the population mean at a rate of 1/sqrt(N).

# 8: bias and variance
# Bias are far from the population mean
# Var is how much your expected values vary.

'''

9. OLS linear regression assumptions:
1) linear
2) Strick exogeneity: error term can not be predicted from X: average all error it is zero
3) Normality of error
4) Spherical Error: a) homoscadasticity (var of error is constant) b) no autocorrelation
5) Linear independent

''''
# 10: "well, Boss, lets talk about class immablance, percision, and recall.
#       Perhaps we should talk about scoreing on F1 score ...and my raise."
'''
11. They are not deterministic, because everytime your re-initialize it you get a differetnt resutl.
Look at different starting rates, tune your hyperparameters.

'''
# 12.
S = [ 92, 77, 99, 105, 99, 91, 103, 110, 88, 103, 101, 117, 117, 108, 106, 111, 103, 105, 121, 110]
A=  [ 92, 77, 99, 105, 99, 91, 103, 110, 88, 103]
B=  [ 101, 117, 117, 108, 106, 111, 103, 105, 121, 110]

Gain = np.var(S) - len(A)/len(S)*np.var(A) - len(B)/len(S)*np.var(B) # = 43.559

# 13. Data leakage is when information from outside the training dataset is used to create the model and
# can need to overfitting of the predictive model.

'''
Steps to preveing data leakage:
1) Perform data preparation within your cross validation folds.
2) Validation set
3) Pipelines
4) add noise
5) Remove Leaky Variables.
'''
''' 14.
The data that each tree in the ensemble is built on.
>>

How the quality of a split on a given feature and its value is evaluated.
>> RF dropps featrues for any give branch in selection.

The general depth of each tree.
>> RF has a deep tree, boosting has a stumped tree

The bias-variance trade-off associated with each tree in the ensemble.
>>

How the ensemble can achieve a low-bias, low-variance model.
>>

'''

'''
*15. Compare and contrast Adaboost and gradient boosting.

16. IF-IDF penalizes words that appear in all documents.
Lemmatizing takes it back to the root of the word. It captures the general idea of the word.
Count Vectorizor normalizes. This is NOT what IF-IDF does.

17. Singluar Vactor Decomposition ...
nxm
U =
Sigma = features x features
D =

18. Whiteboard the algorithm (psuedocode) for NMF using multiplicative updates to solve.
nf = k
w = random_mat(V.shape[0], nf)
while not done:
    H = ls_soln(w,v)
    clip(H)
    w = ls_soln(H,V)
    clip(W)

19. What is the curse of dimensionality? What types of algorithms are affected by this? Give examples of supervised and unsupervised methods.


20. Contrast collaborative vs. content based recommendation engines.
>> content uses similarites of the attributes of the items inorder to group them to predict the users preference
>> Collaborative...

21. Whiteboard the algorithm for a breadth first search in graph analysis.

22. Compare and contrast Hadoop MapReduce and Spark, and give some pros and cons of each.


23. Compare and contrast Spark RDDs and DataFrames. Which is faster, and why?


24. What does HDFS stand for? Why should you take special consideration when writing to and reading from this file system?

>>Hadoop Distributed File System. Take special care to how you segment you data!

25. When writing software, you will often need to optimize for speed, memory, or both.
Name some of the data structures in python that allow faster computation, and some of the things you can use when memory is an issue.

>> Memory: generators, set, dict, simultanious computation
'''
