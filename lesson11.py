class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице для умножения")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        elif isinstance(other, int) or isinstance(other, float):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        else:
            raise ValueError("Умножение поддерживается только с другим объектом матрицы или числом.")
        
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]
print(matrix1)

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]
print(matrix2)

matrix_sum = matrix1 + matrix2
print(matrix_sum)

matrix_scalar_mul = matrix1 * 2
print(matrix_scalar_mul)

matrix_mul = matrix1 * matrix2
print(matrix_mul)