## Warmup: Pandas Practice

# **Include your code and answers in** `pandas_quiz.py`.
#
# 1. Load the `data1.tsv` into a `pandas` dataframe.  Look at pandas various data [loading functions](http://pandas.pydata.org/pandas-docs/stable/io.html) and pick an appropriate one to use.  Look at it's keyword arguments, they do some pretty powerful things.
#
import pandas as pd

df = pd.read_csv("data1.tsv")


# 1. Use pandas descriptive statistics functionality to find the quantiles, mean, median, mode, min, and max of the data.
df.mean()
# 2. How many missing values does each column have?  Are there any values that appear to be highly unlikely or impossible in a column?
#
df.isnull().sum()

# This is often a subjective decision you have to make as the data scientist.  There is no _right_ answer to handling missing data.  And because of such the following questions may not have a concrete answer.
#    1. Which columns have missing values that it is probably ok to drop/ignore?
#    2. Which columns have values that you cannot (should not) ignore (because there might be too many)?  Why might there be so many for this column(s)?
#    3. Are there any missing/NA values that may not actually be missing but just represent a different value?
#
# Missing data isn't the only source of data quality issues. Outliers and invalid values (i.e. an age that is negative) that are out of the expected range of values should also be checked.
#
# 1. Combine the values from the summary statistics you computed earlier with your intuition to determine what values are outlier in each column.  How many of these values are there?
# 2. What are the ranges for each column?  How do these compare to one another (i.e. is one way larger than the others)? And what units do you think each column is in?
