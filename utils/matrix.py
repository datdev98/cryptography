class Matrix:
    def __init__(self, matrix):
        self.matrix = list(matrix)

    def number_of_row(self):
        return len(self.matrix)

    def number_of_column(self):
        return len(self.matrix[0])

    def __add__(self, other):
        if (self.number_of_row() != other.number_of_row() or self.number_of_column() != other.number_of_column()):
            return 
        
        result = []
        for i in range(self.number_of_row()):
            row = []
            for j in range(self.number_of_column()):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        if (self.number_of_column() != other.number_of_row()):
            return

        result = []
        for i in range(self.number_of_row()):
            row = []
            for j in range(other.number_of_column()):
                sum = 0
                for k in range(self.number_of_column()):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum)
            result.append(row)
        
        return Matrix(result)

    def __mod__(self, number):
        result = []
        for i in range(self.number_of_row()):
            row = []
            for j in range(self.number_of_column()):
                row.append(self.matrix[i][j] % number)
            result.append(row)

        return Matrix(result)

    


    def __str__(self):
        return str(self.matrix)

    