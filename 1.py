import numpy as np
import math


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


# a matrix for methods that meets the Jacobi requirements
# initialize the matrix
A = np.matrix([[8., 1., -4.],
              [2., -6., 1.],
              [-1., 1., 4.]])

# initialize the RHS vector
b = np.matrix([6., -9., 5.])

# might be non-uniform because it's meant to be n x m+1
'''A_for_Gauss = np.array([[8., 1., -4., 6.],
                        [2., -6., 1., -9.],
                        [-1., 1., 4., 5.]])'''

# A = np.array([[4., 1., 1.],
# # #               [1., 5., 0.],
# # #               [1., 0., 5.]])
# # #
# # # b = np.array([4., 1., 1.])


'''def choose_solution_method(chosen_method):
    if chosen_method == 1:
        # an iteration limit
        iteration_limit = int(input("choose your number of iterations: "))
        jacobi(iteration_limit)
        return
    if chosen_method == 2:
        gauss_method(A_for_Gauss)  # checking
        return
    else:
        incorrect_method_number()'''



def jacobi(iteration_limit):  
    # prints the system
    print("System:")
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", b[i])
    print()

    x = np.zeros_like(b)
    for it_count in range(iteration_limit):
        print("Current iteration:", x)
        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        if np.allclose(x, x_new, atol=1e-10, rtol=0.):
            break

        x = x_new

    # determinant:
    print("Determinant: ", np.linalg.det(A))
    print("Condition number: ", np.linalg.cond(A))

    print("Solution:")
    print(x)
    error = np.dot(A, x) - b
    print("Error:")
    print(error)


iteration_limit = int(input("Choose your number of iterations: "))
jacobi(iteration_limit)