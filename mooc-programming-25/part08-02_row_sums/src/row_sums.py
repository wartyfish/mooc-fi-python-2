def row_sums(matrix: list):
    i = 0
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += element
        matrix[i].append(row_sum)
        i += 1

if __name__ == "__main__":
    matrix = [[0,1,2], [3,4,5]]
    print(matrix)
    row_sums(matrix)
    print(matrix)