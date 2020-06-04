### Weekly Review Answers  (Pre Assessment 5)

**1. In processing text to perform analyses, what steps are usually involved? When might you use, or not, some of these steps?**

* Lowercase your text
* Strip out miscellaneous spacing & punctuation  
* Remove stop words
* Stem or lemmatize the text
* Use part-of-speech tagging  
* Expand feature matrix with N-grams

For each step above, you need to consider for your use case if it makes sense.  For example, Lowercasing your text may not make sense if in your corpus STOP has a different meaning than stop.  

**2. What does tf-idf stand for, and why do we use this?**

  Tf-idf stands for term frequency, inverse document frequency. We use this to vectorize text (turn it into matrix form so that we can put it into machine learning algorithms).
  Tf-idf is superior to the *bag of words* method for most use cases, which just counts the number of words in each document. Tf-idf divides the word counts by the document frequency, which scales down the importance of words that appear in many documents, as these are less likely to be informative in classifying/clustering the corpus.

**3. Why is Naive Bayes naive? What are some of the pros of this algorithm?**

  Naive Bayes is naive because it assumes that probabilities of each word appearing in a document are independent of each other. This is nearly NEVER the case with text data, but nonetheless naive bayes is fairly successful for certain types of problems.

  Pros of the Naive Bayes algorithm:
  * Works well when n << p (# of features), with small of large n
  * Can learn online with streaming data
  * Multi-class classification
  * Computationally efficient... it's just counting!

**4. Whiteboard the algorithm (psuedocode) for the KMeans algorithm.**
	```
	* initialize k centroid locations
	   - you may do this by randomly assigning each point to a cluster and  
	     then find the centroid of each cluster or use kmeans++ to pick  
	     starting cluster points far away from each other
	* then repeat until "convergence":  
	    * assign each data point to the nearest centroid  
	    * compute new centroids  

	Where "convergence" is ideally where the points stop changing their cluster,  
	though there may always be a few that oscillate back and forth as the  
	centroid locations changes slightly.
	```

**5. Discuss the distance metrics used in clustering and their use cases.**

There are many distance metrics, but the euclidean distance and cosine distance are commonly used in clustering.  Euclidean distance is the "straight line" distance between two points in space, computed as the square root of the sum of the squared component differences between the two points.  Cosine distance quantifies the degree to which two vectors point in the same direction and is computed as 1 minus the cosine similarity, so a cosine distance of 0 means the vectors are pointing in the same direction, 1 indicate they are orthogonal, and 2 indicates they  are pointing in opposite directions.

In general, euclidean distance will be more useful in lower dimensional spaces, because with increasing dimensions everything tends to get farther away.  Cosine distance similarly also suffers from this curse, but as it only investigates if two vectors are pointing in the same direction it's easier for two vectors to be near.

**6. Describe metrics used to measure the "success" of clustering and how you might use them to choose k in KMeans.**

*SSE or WCV* - Within cluster "variance" or sum of squared errors - these will continue to decrease as you increase k, until k = n when they should be 0. With these measures you are looking for an "elbow" of the score vs. number of clusters, where adding additional clusters gives you diminishing returns. SSE is also used within the K-Means model to compare initializations across a single value of k.
*Silhouette score* - compares the distance of a point to it's cluster center compared to the center of the nearest cluster, with 1 being the best score and -1 being the worst score. Silhouette scores can be aggregated for all of the points in a dataset, and then compared for all values of k you are considering. The highest aggregate Silhouette score will likely be your best choice for k.

**7. Explain how a profit curve is made.**

First a classification model makes predictive probabilities.  Classification thresholds are derived from the sorted probabilities, and then a confusion matrix is made for each threshold. All the values in each confusion matrix are normalized into rates. Then each confusion matrix is multiplied by a cost benefit matrix to determine the profit (or cost) for that threshold.  
When this profit is plotted for each threshold, starting with the most strict threshold (1) and then in descending order, a profit curve results. The   profit curve illustrates the correct threshold to pick as the one that  maximizes the profit.

**8. You have a dataset whose labels are about 25% minority class.  What options are available to you to help you make a model that accommodates this imbalance?**

There are some practical steps you can take:
* Stratifying the train_test_split
* Some sklearn models (e.g. decision trees) allow you to increase the weight of the minority class in the cost function.

You can also use external information (such as a cost-benefit matrix) to  determine what threshold to use in a classification problem (a.k.a. profit  curves.)

You can also try to change the imbalance by undersampling the majority class,   oversampling the minority class (in the form of exact copies), or using something like SMOTE to make more artificial instances of the minority class.  

The efficacy of whatever method you choose should be evaluated on a hold-out set. It may be that the best thing to do is nothing.

**9. Describe the "contents" of the matrices that come out of SVD decomposition, both their sizes and what they represent.**  
  SVD returns three matrices, often called U, S, and V. The U matrix contains eigenvectors (basis vectors) that are linear combinations of the original features, orthogonal to the other rows. This matrix has dimensions n_rows, n_rows, with zeros padding the right outside. Non-zero size of n_rows, n_latent_features.
  The S matrix contains the singular values, or the square root of the eigenvalues associated with the eigenvectors represented in S. The square of the  singular value is the variance explained by this vector (can be normalized to represent the proportion of variance explained by this eigenvector).
  The V matrix has dimensions n_latent_features, n_features and contains eigenvectors that are linear combinations of the original rows.
  n_latent_features is a dimension that you can choose, and can be as large as the minimum of (n_features, n_rows).

**10. What is the difference between PCA and SVD?**

Principal Component Analysis (PCA) and Singular Value Decomposition (SVD) are two eigenvalue methods used to reduce a high-dimensional dataset into fewer dimensions while retaining important information.  

Performing PCA on a matrix breaks it down into a samples x latent features and latent features x columns matrices, while SVD results in U, Sigma, and V matrices where the singular values present in the diagonal of the Sigma matrix are the square root of the eigenvalues.

PCA will be more computationally expensive than SVD if your matrix is large, as it is finding eigenvalues of the M<sup>T</sup>M (covariance) matrix.    
