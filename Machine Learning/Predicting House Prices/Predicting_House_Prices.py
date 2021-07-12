# Predicting House Prices using Multiple linear regression

# This codebase is a part of Machine Learning Folder
# Difficulty : Expert
# Challenge taken from HackerRank
# Language : Python 3.7

'''
Problem Statement : Charlie wants to buy a house. He does a 
                    detailed survey of the area where he wants 
                    to live, in which he quantifies, normalizes, 
                    and maps the desirable features of houses to 
                    values on a scale of `0` to `1` so the data 
                    can be assembled into a table. If Charlie noted 
                    `F` features, each row contains `F` space-separated 
                    values followed by the house price in dollars per 
                    square foot (making for a total of `F+1` columns). 
                    If Charlie makes observations about `H` houses, 
                    his observation table has `H` rows. This means 
                    that the table has a total of `(F + 1) x H` entries.
'''
# Importing the linear_model package for the problem solving
from sklearn import linear_model

# Set input data
print ("Enter the no. of features and rows of the dataset : ")
features, rows = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
print ('Enter the required values : ')
for i in range(rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Get the parameters X for discovery the Y
print ('Enter the count of the unknown prices : ')
new_rows = int(input())
new_X = []
for i in range(new_rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen [Predictions]
print ('Predicted house prices respectively as per the input : ')
result = model.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))

    
    
'''
----------------------------------------------------------------------

Test Case #1

User Input :
Enter the no. of features and rows of the dataset : 
2 4
Enter the required values : 
0.1 0.2 60.0
1.0 2.0 600.0
0.3 0.4 100.0
0.5 0.6 150.0
Enter the count of the unknown prices : 
3
0.5 0.5
0.6 0.6
0.7 0.7

---------------------------------------------------------------------

Output :

Predicted house prices respectively as per the input : 
110.65
133.15
155.65

---------------------------------------------------------------------

Test Case #2

User Input :
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

--------------------------------------------------------------------

Output :
Predicted house prices respectively as per the input : 
105.22
142.68
132.94
129.71

--------------------------------------------------------------------
'''

# --------------------------------------------------------------------------------
# This codebase will solve the problem named, 'House Price Predictions'
# All the explanations are done in the README.md folder with proper visualization

# Hope this problem will find you interesting enough
# Author : Abhishek Sharma, DCP21
