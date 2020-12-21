from typing import List

def remove_empty_list(matrix):
    return list(filter(lambda a: a != [], matrix))


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    direction = 'right'
    order = []
    while (len(matrix)) != 0:
        if direction == 'right':
            for i in range(len(matrix[0])):
                order.append(matrix[0].pop(0))
            direction = 'down'
        elif direction == 'down':
            for i in range(len(matrix)):
                order.append(matrix[i].pop(-1))
            direction = 'left'
        elif direction == 'left':
            for i in range(len(matrix[-1])-1, -1, -1):
                order.append(matrix[-1].pop(-1))
            direction = 'up'
        elif direction == 'up':
            for i in range(len(matrix)-1, -1, -1):
                order.append(matrix[i].pop(0))
            direction = 'right'
        matrix = remove_empty_list(matrix)
    return order

matrix = [[1,2,3],[4,5,6],[7,8,9]]
assert [1,2,3,6,9,8,7,4,5] == spiralOrder(matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
assert [1,2,3,4,8,12,11,10,9,5,6,7] == spiralOrder(matrix)