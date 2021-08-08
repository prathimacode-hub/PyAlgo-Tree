<h1>Digit Recognizer</h1>


This code helps you classify different digits using Knn Algorithm.

## Requirements 🦄
- `Tensorflow` 
- `Python` 
- `Google Colab/VsCode`
- `Panda`
- `Numpy`
- `Matplotlib`

## Dataset
MNIST Handwritten Digits dataset is used for this task. It contains images of digits taken from a variety of scanned documents, normalized in size and centered.
Each image is a 28 by 28 pixel square (784 pixels total). The dataset contains 60,000 images for model training and 10,000 images for the evaluation of the model.

## Description 🏦
Used **supervised machine learning models** to predict the digits. For that we need **K-Nearest Neighbors Classifier** as the baseline method
ﬁnds a group of k objects in the training set that are closest to the test object, and	bases the assignment of a label on the predominance of a class in this neighborhood.

## Results
In order to evaluate this implementation of K-Nearest Neighbours an experiment was run using 35,000 training samples, 250 test samples and a K value of 7. This implementation was able to correctly classify the handwritten digit 81.53% of the time.
