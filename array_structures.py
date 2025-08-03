class SimpleArray:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        else:
            raise IndexError("Invalid index")

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Invalid index")

    def display(self):
        print("Array contents:", self.data)


class SimpleMatrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def get_value(self, row, col):
        return self.matrix[row][col]

    def get_row(self, row):
        return self.matrix[row]

    def get_column(self, col):
        return [self.matrix[i][col] for i in range(len(self.matrix))]

    def display(self):
        print("Matrix:")
        for row in self.matrix:
            print(row)


if __name__ == "__main__":
    # 1D Array Example
    arr = SimpleArray()
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    arr.display()
    print("Access index 1:", arr.access(1))
    arr.delete(0)
    arr.display()

    # 2D Matrix Example
    mat = SimpleMatrix(3, 3)
    mat.set_value(0, 0, 5)
    mat.set_value(1, 1, 10)
    mat.set_value(2, 2, 15)
    mat.display()
    print("Value at (1,1):", mat.get_value(1, 1))
    print("Row 2:", mat.get_row(2))
    print("Column 0:", mat.get_column(0))