def vector_size_check(*vector_variables):
    return all(len(vector_variables[0])==x
    for x in [len(vector) for vector in vector_variables[1:]])

#len(vector_variables[0] = 첫번째 벡터 개수
# 1부터 나머지 벡터를 비교해 논리값 출력

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables)==False:
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2-sum(elements) for elements in zip(*vector_variables)]

def scalar_vector_product(alpha, vector_variable):
    return [alpha*elements for elements in vector_variable]

#print(vector_addition([1,2,3],[4,5,6],[7,8,9]))
#print(vector_subtraction([1,2,3],[4,5,6],[7,8,9]))
#print(scalar_vector_product(5,[7,8,9]))

matrix_a1 = [[1, 1], [2, 1]]
matrix_a2 = [[2,2],[5,3]]
matrix_b1 = [[1, 1], [2, 1], [1, 3]]
matrix_b2 = [[3,1],[4,5],[1,1]]

def matrix_size_check(*matrix_variables):
    return all([len(set(len(matrix[0]) for matrix in matrix_variables))==1]) and all([len(matrix_variables[0])== len(matrix) for matrix in matrix_variables])

#print(matrix_size_check(matrix_a1,matrix_b2))

def is_matrix_equal(*matrix_variables):
    return all([all([len(set(row))==1 for row in zip (*matrix)]) for matrix in zip(*matrix_variables)])
#row 와 column비교

#print(is_matrix_equal(matrix_a2,matrix_a2))
def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(row) for row in zip(*matrix)] for matrix in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[row[0]*2-sum(row) for row in zip(*matrix)] for matrix in zip(*matrix_variables)]
#print(matrix_subtraction(matrix_a1,matrix_a2))

def matrix_transpose(matrix_variable):
    return [[elements for elements in row] for row in zip(*matrix_variable)]
#print(matrix_transpose(matrix_a2))

def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return len([column for column in zip(*matrix_a)]) == len(matrix_b)

#print(is_product_availability_matrix(matrix_a1, matrix_b2))
def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return [[sum(a*b for a,b in zip(row, column)) for column in zip(*matrix_b)] for row in matrix_a]
print(matrix_product(matrix_a1,matrix_a2))
