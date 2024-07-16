import sys
from itertools import cycle

def find_solution(n, m):
    """Находит решение для заданных параметров n и m."""
    nums_list = cycle([i for i in range(1, n + 1)])
    result = ''
    count = 0
    for num in nums_list:
        count += 1
        if count == m and num == 1:
            break
        if count == m:
            count = 1
        if count == 1:
            result += str(num)
    return result

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = find_solution(n, m)
    print(result)
