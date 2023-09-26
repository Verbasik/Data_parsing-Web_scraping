import requests
import os

# Создать директорию, если ее еще нет
output_dir = '/Users/Edward/Code/html_parse/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Итерировать через диапазон страниц
for i in range(1, 927):  # 1 to 926 inclusive
    url = f'https://spark-interfax.ru/map/moskva/{i}'
    
    # Получение HTML-кода страницы
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
    except requests.RequestException as e:
        print(f"Error fetching page {i}: {e}")
        continue  # Переход к следующей итерации цикла
    
    # Сохранение HTML-кода в файл
    file_name = f"{i + 1}.html"
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
        
    print(f"Successfully saved {file_path}")
