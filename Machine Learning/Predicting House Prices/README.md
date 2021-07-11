# Predicting House Prices


## Aim
Charlie wants to buy a house. He does a detailed survey of the area where he wants to live, in which he quantifies, normalizes, and maps the desirable features of houses to values on a scale of `0` to `1` so the data can be assembled into a table. If Charlie noted `F` features, each row contains `F` space-separated values followed by the house price in dollars per square foot (making for a total of `F+1` columns). If Charlie makes observations about `H` houses, his observation table has `H` rows. This means that the table has a total of `(F + 1) x H` entries.

Unfortunately, he was only able to get the price per square foot for certain houses and thus needs your help estimating the prices of the rest! Given the feature and pricing data for a set of houses, help Charlie estimate the price per square foot of the houses for which he has compiled feature data but no pricing.

Now predict the house using the multiple linear regression algorithm

The problem is taken from the HackerRank website, you can check out the problem [here](https://www.hackerrank.com/challenges/predicting-house-prices/problem)

*************************************
## Purpose
Understanding implementations of Multiple Linear Regression Model using dataset!
*************************************
## Short Description of the script
- This script will help you how can we use machine learning models in real life.
- Although it is a basic code/script, but it will provide you the idea about the Linear regression model deployment and based on the model how the predictions were made.
- Linear regression is a linear approach to modelling the relationship between a scalar response and one or more explanatory variables. 
- To implement this script we need to use a python library called `sklearn`. Check out the [`requirements`](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-2/Machine%20Learning/Predicting%20House%20Prices/requirements.txt) folder for more details!
***************************************
## Workflow of the codebase
- Firstly, import all the packages, as mentioned earlier.
- Take inputs from the user. User given input is more acceptable because it provides the interaction between the learner and developer.
- Process the user given data through some operations before implementing the final function.
- Set the model `Linear Regression`.
- Train the model using the data given by the user.
- Predict the outputs as per the user given input for prediction purposes.
- Represent the predicted house prices nicely to make the things user fridendly.
- Tada! The output is generated!!
***************************************
## Detailed Explanation of the script
**Input Format**

The first line contains `2` space-separated integers, `F` (the number of observed features) and `N` (the number of rows/houses for which Charlie has noted both the features and price per square foot).
The `N` subsequent lines each contain `F + 1` space-separated floating-point numbers describing a row in the table; the first  elements are the noted features for a house, and the very last element is its price per square foot.

The next line (following the table) contains a single integer, `T` , denoting the number of houses for for which Charlie noted features but does not know the price per square foot.
The `T` subsequent lines each contain `F` space-separated floating-point numbers describing the features of a house for which pricing is not known.


**Output Format**

Print `T` lines, where each line `i` contains the predicted price for the **_i<sup>th</sup>_** house (from the second table of houses with unknown prices per square foot).

### Explanation
Let's take a look at the scoring system or, how the model is predicting the scores!

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-2/Machine%20Learning/Predicting%20House%20Prices/Images/lin6.png)

User Input :

```
Enter the no. of features and rows of the dataset : 
2 7
Enter the required values : 
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
Enter the count of the unknown prices : 
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18
```
Steps for the model -
1. Firstly the model receives all the required features and data from the user.
2. Then it trained the model according to the features and prices.
3. After that it takes another set of data but this time it is incomplete and the fill in the blanks will be done by the model itself.
4. As per the incomplete data the model predicts the results and then provides the final output!


************************************************************************
## Setup Instructions
- Open any Python editor, I have used Jupyter Notebook here.
- Python version 3.7 must be installed in your device.
- Your system must have the Python library called `sklearn`, without that this script will not be run!

************************************************************************
## Compilation Steps
- Importing the packages and libraries.
- Take all the user given data.
  1. Enter the no. of features and rows of the dataset.
  2. Enter the required values.
  3. Enter the count of the unknown prices.
  4. Enter the incomplete features data.
- Processing the data collected from the user.
- Deploying the model `linear regression`.
- Train the model.
- Predict the outcomes using the model.
- Print the output!
************************************************************************
## Output
- Test Case #1

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-2/Machine%20Learning/Predicting%20House%20Prices/Images/lin1.png)

- Test Case #2

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-2/Machine%20Learning/Predicting%20House%20Prices/Images/lin2.png)

- Test Case #3

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-2/Machine%20Learning/Predicting%20House%20Prices/Images/lin3.png)

- Test Case #4

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-2/Machine%20Learning/Predicting%20House%20Prices/Images/lin4.png)

- Test Case #5

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/patch-2/Machine%20Learning/Predicting%20House%20Prices/Images/lin5.png)

------------------------------------------------
## Resources

The model we have used here is called `Linear Regression Model`. If you want to learn more about the model and algorithm check out the [link](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html). You will get all the resources from the given link.

------------------------------------------------
## Author
Code Contributed by, Abhishek Sharma, DCP21, [abhisheks008](https://github.com/abhisheks008) 
<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
