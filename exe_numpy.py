import numpy
import matplotlib.pyplot


#1
import numpy as np


def vector_0_to_20() -> numpy.ndarray:
    """
    The function creates a vector from 0 to 20. The digits from 9 to 15 are negative.
    :return: The vector that the function created.
    """
    vector = numpy.array(range(21))
    vector[9:15] *= -1
    return vector


#2
def multiples_5_vector() -> numpy.ndarray:
    """
    The function creates a vector with multiples 5, up to 50.
    :return: The vector that the function created.
    """
    return np.linspace(5,50,dtype=int,num=10)


#3
def matrix_sizes(matrix: numpy.matrix) -> tuple:
    """
    The function returns the rows and columns of matrix.
    :param matrix:The matrix for calculation.
    :return: tuple representing the size of the matrix.
    """
    return matrix.shape


#4
def zero_one_matrix() -> numpy.ndarray:
    """
    The function creates  a 10x10 matrix, in which the elements on the borders are 1, and inside 0.
    :return:The matrix that the function created.
    """
    matrix = numpy.zeros((8,8),dtype=int)
    return numpy.pad(matrix,(1,1),constant_values=(1))


#5
def add_vector_to_rows(matrix: numpy.ndarray,to_add: numpy.ndarray) -> numpy.ndarray:
    """
    The function adds a vector to each row of a given matrix.
    :param matrix: A matrix to which a vector will be added.
    :param to_add: The vector to add to the matrix.
    :return:The new matrix
    """
    matrix += to_add
    return matrix


#6
def sin_draw():
    """
    The function calculates the x and y coordinates for points on a sine curve and plots the points
    """
    x = numpy.linspace(-numpy.pi, numpy.pi)
    matplotlib.pyplot.plot(x, numpy.sin(x))
    matplotlib.pyplot.show()


#7
def create_random_matrix() -> numpy.ndarray:
    """
     The function creates a matrix with random values and then replaces the first and the last lines
    :return: The matrix that created.
    """
    matrix = numpy.random.rand(4, 4)
    matrix[[0,-1]]=matrix[[-1,0]]
    return matrix


#8
def replace_numbers(arr_of_nums: numpy.ndarray, new_number: int,num_to_replace: int) -> tuple:
    """
    replace all numbers in a given array which is equal, less and greater to a given number.
    :param arr_of_nums: array of numbers
    :param new_number: The number to replace
    :param num_to_replace: The number for comparison.
    :return: The three new arrays
    """
    return numpy.where(arr_of_nums == num_to_replace,new_number,arr_of_nums),numpy.where(arr_of_nums < num_to_replace,new_number,arr_of_nums),numpy.where(arr_of_nums > num_to_replace,new_number,arr_of_nums)


#9
def mult_array(a_array: numpy.ndarray,b_array: numpy.ndarray) -> numpy.ndarray:
    """
    The function multiplies two given arrays of same size element-by-element.
    :param a_array: array of numbers
    :param b_array: array of numbers
    :return: The new array
    """
    return numpy.multiply(a_array , b_array)


#10
def sort_array(array_to_sort: numpy.ndarray):
    """
    The function sorts an along the first, last axis of an array
    :param array_to_sort: array of numbers to sort
    """
    print("original array:")
    print(array_to_sort)
    array_to_sort=numpy.sort(array_to_sort,axis=0)
    print("Sort along the first axis:")
    print(array_to_sort)
    print("Sort along the last axis:")
    print(numpy.sort(array_to_sort,axis=1))


#11
def one_diagonal():
    """
    The function creates a 3-D array with ones on a diagonal and zeros elsewhere.
    :return: The matrix that created
    """
    return numpy.eye(N=3,M=3,dtype=int)


#12
def remove_single_dimensional(array_to_squeeze: numpy.ndarray):
    """
    The function removes single-dimensional entries from a specified shape.
    :param array_to_squeeze: Array for reducing dimensions.
    :return: The squeeze array.
    """
    return numpy.squeeze(array_to_squeeze, axis=None)


#13
def one__d_to_two_d(a_array: numpy.ndarray, b_array: numpy.ndarray):
    """
    The function converts two 1-D arrays into a 2-D array.
    :param a_array: first array to the new 2-D array.
    :param b_array: second array to the new 2-D array.
    :return: The new array
    """
    return np.vstack((a_array,b_array))


#14
def combine_arrays(one_d,two_d):
    """
    The function combines a one and a two dimensional array together and display their elements.
    :param one_d:first array to combine.
    :param two_d:second array to combine.
    """
    for i, j in numpy.nditer([one_d, two_d]):
        print("%d:%d" % (i, j), )


#15
def create_3d_array():
    """
    The function creates 3-D array and fill the array elements with values using unsigned integer (0 to 255).
    :return: The array that created.
    """
    return numpy.random.randint(255, size=(300,400,5))

