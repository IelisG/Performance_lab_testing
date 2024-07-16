import sys
import statistics

if __name__ == "__main__":
    data_file = sys.argv[1]
    with open (data_file, 'r') as file:
        data = [int(line.strip()) for line in file]

    # Находим медиану массива
    median = int(statistics.median(data))

    # Считаем минимальное количество ходов
    result = sum(abs(num - median) for num in data)

    print(result)