# Linear Regression using Gradient Descent

This Python script demonstrates a simple implementation of linear regression using gradient descent. Linear regression is a basic machine learning algorithm used to predict a continuous target variable based on one or more input features. In this script, the algorithm finds the best-fit line for a given dataset using gradient descent optimization.

## Dependencies
- **Matplotlib**: This library is used for creating visualizations, such as the scatter plot and the regression line.
- **Pandas**: Pandas is used for data manipulation and analysis, allowing the script to read the dataset from a CSV file.

## How the Code Works

1. **grad_descent Function**: The `grad_descent` function implements the gradient descent algorithm. It iteratively adjusts the coefficients (slope `m` and intercept `b`) of the linear regression model to minimize the difference between predicted and actual values.

2. **Main Function**: The `main` function imports the dataset from 'data.csv' and initializes the coefficients `m` and `b` to 0. It then performs 300 iterations of gradient descent, printing the progress every 50 epochs. After finding the optimal coefficients, it plots the dataset as a scatter plot and overlays the learned regression line.

3. **Visualization**: The script uses Matplotlib to create a scatter plot of the dataset points and overlays the learned regression line in red.

## How to Use

1. **Dataset**: Ensure your dataset is in the 'data.csv' file, and it has 'studyhours' and 'score' columns representing the input feature and target variable, respectively.

2. **Running the Script**: Execute the script, and it will perform gradient descent, print the progress, and display a visualization of the dataset with the learned regression line.

Feel free to modify the script to use your own dataset or adjust parameters like the learning rate (`L`) and the number of epochs for experimentation.
