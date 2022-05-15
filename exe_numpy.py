import numpy
import matplotlib.pyplot


#1
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
    vector = numpy.array(range(1,11))*5
    return vector


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
    return numpy.stack( [numpy.append(matrix[i], to_add, axis=1) for i in range(matrix.shape[1])], axis=0)


#6
def sin_draw(a=(-1),b=1,c=1):
    x = numpy.linspace(-numpy.pi, numpy.pi)
    matplotlib.pyplot.plot(x, numpy.sin(x))
    matplotlib.pyplot.show()


#7
def create_random_matrix():
    matrix = numpy.random.rand(4, 4)
    print(matrix)
    matrix[[0,-1]]=matrix[[-1,0]]
    print(matrix)


#8
def replace_numbers(arr_of_nums, new_number,num_to_replace):
    return numpy.where(arr_of_nums == num_to_replace,new_number,arr_of_nums),numpy.where(arr_of_nums < num_to_replace,new_number,arr_of_nums),numpy.where(arr_of_nums > num_to_replace,new_number,arr_of_nums)



#9
def mult_array(a_array,b_array):
    return a_array * b_array


#10
def sort_matrix(matrix):
    print("original array:")
    print(matrix)
    matrix=numpy.sort(matrix,axis=0)
    print("Sort along the first axis:")
    print(matrix)
    print("Sort along the last axis:")
    print(numpy.sort(matrix,axis=1))


#11
def one_diagonal():
    matrix = numpy.zeros((3, 3), dtype=int)
    numpy.fill_diagonal(matrix,1)
    return matrix


#12
def remove_single_dimensional(array_to_squeeze):
    return numpy.squeeze(array_to_squeeze, axis=None)


#13
def one__d_to_two_d(a_array,b_array):
    return numpy.array(list(zip(a_array,b_array)))


#14
def combine_arrays(one_d,two_d):
    for i, j in numpy.nditer([one_d, two_d]):
        print("%d:%d" % (i, j), )


#15
def create_3d_array():
    return numpy.random.randint(255,size=(300,400,5))

m = numpy.array([[1,2,3],[4,5,6]])
print(m)
v = numpy.matrix('1 2 ')
print(replace_numbers(numpy.array([[1,2,3,4,5,6]]), 9,3))
#print(numpy.random.rand(4, 4))