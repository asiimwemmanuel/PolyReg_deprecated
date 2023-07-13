# Polynomial Regression Algorithm Documentation

- Date & Time Created: 8:06 AM, May 24, 2023
- Author: @asiimwemmanuel

## Description

This algorithm is designed to construct accurate polynomial fits for inputted data and aid in regression analysis. It can be applied in various fields such as TCS & numerical analysis, econometrics and statistical analysis, big data, and market analysis. The algorithm aims to provide a base version that can be specialized for different fields through forking.

The algorithm takes a list of data points and an input parameter, which can be a float, 'exp', or 'graph'. Depending on the parameter, the algorithm will find the corresponding output: a floating-point number at a specific position in the data's underlying function with a specified level of confidence, the lowest order polynomial expression representing the data's function, or a graph plotted using the suggested polynomial expression.

The algorithm assumes that the list represents the first terms in a mathematical progression that can be accurately represented as a polynomial. It also assumes that the size of the list is one more than its order. The algorithm handles the cases of float, 'exp', and 'graph' parameters accordingly.

Refer to the prompt files for more information

## Techniques/Concepts/Theories Used

- Polynomial regression
- Numerical analysis
- Econometrics and statistical analysis
- Python programming

## Reasons for Choices Made

- The algorithm focuses on efficiency and performance, prioritizing optimal choices rather than intuitiveness.
- The selected theories and concepts aim to provide accurate polynomial fits and handle different types of data.
- Python is chosen as the main programming language due to its versatility and availability of libraries for numerical computations and data visualization.

## Step-by-Step Technical Analysis

1. Receive the input list of data points and the parameter.
2. Validate and preprocess the input as per the defined criteria.
3. Determine the order of the polynomial based on the size of the list.
4. Depending on the parameter:
   - If a float, return the floating-point number at the specified position in the data.
   - If 'exp', construct and return the lowest order polynomial expression representing the data's function.
   - If 'graph', plot the graph using the suggested polynomial expression and display it.
5. Handle any extrapolation made based on the estimated error and provide a confidence score.

## User Tutorial

1. Provide a list of data points representing the first terms of a mathematical progression.
2. Choose the desired parameter: a float, 'exp', or 'graph'.
3. Execute the algorithm with the provided input.
4. Retrieve the output based on the chosen parameter.
5. Review the confidence score for any extrapolated values.
6. Repeat the process with different inputs as needed.

## Possible Areas for Improvement or Alternatives and Weaknesses of the Algorithm

- The algorithm currently focuses on polynomial regression and may not handle exponential or geometric sequences. Extending its capabilities to handle such patterns could be an improvement.
- Further optimization and fine-tuning can be done to improve efficiency and performance.
- The algorithm assumes certain properties of the input list, which may limit its applicability in certain cases. Handling a wider range of data structures and patterns can enhance its versatility.

## Cited Resources

- Polynomial Regression: [Wikipedia](https://en.wikipedia.org/wiki/Polynomial_regression)
- Numerical Methods: "Numerical Methods: Design, Analysis, and Computer Implementation of Algorithms" by Anne Greenbaum and Timothy P. Chartier
- Econometrics: "Introductory Econometrics: A Modern Approach" by Jeffrey M. Wooldridge
- Python Documentation: [Python.org](https://docs.python.org/3/)
- NumPy Documentation: [NumPy.org](https://numpy.org/doc/)
- SciPy Documentation: [SciPy.org](https://docs.scipy.org/doc/)
- Matplotlib Documentation: [Matplotlib.org](https://matplotlib.org/stable/contents.html)
- Git Handbook: [GitHub Guides](https://guides.github.com/introduction/git-handbook/)

