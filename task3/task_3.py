import json
import sys

if __name__ == "__main__":
    # Ввод пути для файла values
    values_file = sys.argv[1]
    # Ввод пути для файла tests
    tests_file = sys.argv[2]
    # Ввод пути для файла report
    report_file = sys.argv[3]

    with open(values_file, 'r') as file:
        values = json.load(file)
    with open(tests_file, 'r') as file:
        tests = json.load(file)

    # Преобразуем values в словарь для быстрого доступа по id
    values_dict = {item['id']: item['value'] for item in values['values']}

    # Рекурсивная функция для заполнения значений
    def fill_node(node):
        if 'id' in node:
            node_id = node['id']
            if node_id in values_dict:
                node['value'] = values_dict[node_id]

        if 'values' in node:
            for sub_node in node['values']:
                fill_node(sub_node)


    # Заполнение значений в тестах
    for test in tests['tests']:
        fill_node(test)

    # Запись результата в report.json
    with open(report_file, 'w') as file:
        json.dump(tests, file, indent=4)