from collections import deque


def shortest_clear_path(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if matrix[0][0] == 1 or matrix[n - 1][n - 1] == 1:
        return -1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    queue = deque([(0, 0, 1)])  # (row, column, path_length)

    while queue:
        row, col, path_length = queue.popleft()
        if row == col == n - 1:
            return path_length
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and matrix[new_row][new_col] == 0:
                matrix[new_row][new_col] = 1  # mark as visited
                queue.append((new_row, new_col, path_length + 1))

    return -1


FAKE_TEST_PARAMS = [
    {
        'matrix': [
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0]
        ],
        'expected_result': 8
    },
    {
        'matrix': [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ],
        'expected_result': 4
    },
    {
        'matrix': [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0]
        ],
        'expected_result': 3
    },
    {
        'matrix': [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ],
        'expected_result': -1
    },
]


def main() -> None:
    count = 1
    for params in FAKE_TEST_PARAMS:
        try:
            assert shortest_clear_path(params.get('matrix')) == params.get('expected_result')
        except AssertionError:
            print(f'Test case #{count} - FAILED!')
        else:
            print(f'Test case #{count} - DONE!')
        finally:
            count += 1


if __name__ == '__main__':
    main()
