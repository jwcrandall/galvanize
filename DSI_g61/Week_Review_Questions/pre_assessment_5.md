### Weekly Review Questions  (Pre Assessment 5)

1. In processing text to perform analyses, what steps are usually involved? When might you use, or not, some of these steps?

lower case strip 
remove stop words
lemmetize/stem tokenize
part of speech tagging


tfidf = TfidfVectorizer()
tfidf.fit(c_train)
test_arr = tfidf.transform(c_test).todense()

You don't have to stem or lem...if you wanted to keep tense.
n-gram is not necessary if you don't use NB.


2. What does tf-idf stand for, and why do we use this?

term frequency - inverse document frequency: how import a term is in a document as it relates to the whole corpus.

It provides the value associated with a document-term as a measurement of the importance in relation to the rest of the corpus
In other words, it helps weight the words such that words that show up most frequently do not dominate other more important words.

log scale 

3. Why is Naive Bayes naive? What are some of the pros of this algorithm?
	
	It is a bayesian classifier algorithm that assumes all words in the
	string are independent from one another. 
	Pro: 
		- it handles cases where the number of features >> data points: distance is baked in to the computation.
		- computationally efficient 
		- Multi-class classification
	Con:
		- Naive assumption means correlated features are not actually treated right
		- Sometimes outperformed by other models
	
	In contrast, Hidden Markov Model assumes a relationship between y_n and y_(n+1)
	
4. Whiteboard the algorithm (psuedocode) for the KMeans algorithm.

initialize_centroids (randomly, average, k-means++) 
while not converged: (# iterations, no change in k, not much of a change in k)
	compute pdist
	assign_data_to_centroids
	compute_new_centroid_means
	
5. Discuss the distance metrics used in clustering and their use cases.
	- Euclidean, regularized data
	- Manhattan,   
	- cosine similarity: text
	- Jaccard, dynamic time wart at a distance, string
	- Cures of Dimensionally
	-
	
6. Describe metrics used to measure the "success" of clustering and how you might use them to choose k in KMeans.
	- Elbow Plot: look for value of k that drastically reduces the residual sum of squares within the clusters
	- Silhouette Score: is calculated using the mean intra-cluster distance (a) and the mean nearest-cluster distance (b) for each sample
			(b - a) / max(a, b)
	- GAP statistics: compares the change in within-cluster dispersion with that expected under an appropriate reference null distribution.
	
7. Explain how a profit curve is made.
- Construct a confusion matrix for each probability threshold, and use a costbenefit
matrix to calculate a “profit” for each threshold. Pick the threshold that
give the highest profit.
Step 1 - Estimate error probabilities based on a given threshold (will review
thresholding in a bit)
Step 2 - Define the cost-benefit matrix (based on your out-of-model knowledge)
Step 3 - Combine probabilities and payoffs.
Step 4 - Plot profit

8. You have a dataset whose labels are about 25% minority class.  What options are available to you to help you make a model that accommodates this imbalance?
I. stratify training and testing data, change weighting of training data for poor represented class
II. Cost-sensitive learning: (consider costs of FP, FN)
III. Sampling
- Undersampling randomly discards majority class observations to balance training sample.
- Oversampling replicates observations from minority class to balance training sample.
- SMOTE - Synthetic Minority Oversampling TechniquE 1) Generates new observations from
minority class. 2) For each minority class observation and for each feature, randomly generate between it and one of its knearest neighbors.

In the case of images, you can do "data augmentation": flip, rotat, change lighting to images.

9. Describe the "contents" of the matrices that come out of SVD decomposition, both their sizes and what they represent.
U is the data matrix [nxk]
Sigma = diagonal of the decreasing, singular values: strength of your latent features. [kxk]
V is your feature matrix [kxn]

10. What is the difference between PCA and SVD?
SVD does not fcalculate the covariance.


