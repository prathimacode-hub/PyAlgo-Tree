 # **Mobile Price Range Classification**


**INTRODUCTION**

Here, we have used Logistic Regression algorithm which is a classification algorithm for the project as Mobile Price Range Classification.

**DATASET**

To access the dataset [Click here](https://www.kaggle.com/iabhishekofficial/mobile-price-classification?select=train.csv)

Note: It is also added in the 'Dataset' folder of this project.

**PURPOSE**

The problem statement given below:

Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,Samsung etc.

He does not know how to estimate price of mobiles his company creates. In this competitive mobile phone market you cannot simply assume things. To solve this problem he collects sales data of mobile phones of various companies.

Bob wants to find out some relation between features of a mobile phone(eg:- RAM,Internal Memory etc) and its selling price. But he is not so good at Machine Learning. So he needs your help to solve this problem.

In this problem you do not have to predict actual price but a price range indicating how high the price is.

**BRIEF EXPLANATION**

Logistic Regression is a classification algorithm which comes under **SUPERVISED Machine Learning algorithm** because it uses labelled data i.e. both input and output are given to the model so that the model can well train itself and perform accordingly.

So for the problem statement we will proceed with following steps to classify the target variable i.e. price_range with value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost):

- Data training using the mobile price classification dataset. 
- Model creation which will include importing logistic regression from sklearn, initializing the classifier, then fit the training data into it and perform classification.

**WORKING OF ALGORITHM**
- The first step is to get started with jupyter notebook/google colab or you can also use an editor that supports it with latest version of python installed in your system..
- Then import the required dataset using pandas library.
![](https://github.com/ayushi424/PyAlgo-Tree/blob/main/Machine%20Learning/Mobile%20Price%20Range%20Classification/Images/lr1.jpg)
- Now, we will split the dataset into training and testing data using train-test-split method from sklearn.
- Training data is the data that the model will use to train itself and testing data is the data on which testing of model will be done in form of predictions.
- Now, import the logistic Regression from sklearn, and initialze it.
- After initializing, fit the data into it and perform predictions.
![](https://github.com/ayushi424/PyAlgo-Tree/blob/main/Machine%20Learning/Mobile%20Price%20Range%20Classification/Images/lr2.jpg)
![](https://github.com/ayushi424/PyAlgo-Tree/blob/main/Machine%20Learning/Mobile%20Price%20Range%20Classification/Images/lr3.jpg)
**USAGE**
- Various classification tasks and projects.
- Where  the target variable is discrete variable not continous.

**USE CASES**

Since we have used a specified dataset for this project, other examples are as:
- Where  the target variable is discrete variable  and not a continous varaible.
- Email Classification as spam or not spam.
- Various other fields as medical, gaming etc.

**LIBRARIES USED**
- pandas
- sklearn

**CONCLUSION**
- Logistic Regression is one of simple ML algorithm used for various classification tasks.
- It is easy to interpret and understand.
- Can be used in various  Machine Learning projects. 

**Author**

[Ayushi Shrivastava](https://github.com/ayushi424)
