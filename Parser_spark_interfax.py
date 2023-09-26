import re
import csv
from html import unescape

def create_csv_file(file_path):
    """
    Создает CSV-файл с заголовками для хранения информации о компаниях.
    
    Параметры:
        file_path (str): Путь, по которому будет сохранен CSV-файл.
        
    Возвращаемое значение:
        None
    
    Замечания:
        Файл будет содержать следующие заголовки: 'Company Name', 'INN', 'Revenue'.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Company Name', 'INN', 'Revenue']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def main():
    """
    Основная функция для парсинга HTML-файлов и сохранения информации в CSV-файл.
    
    Параметры:
        None
    
    Возвращаемое значение:
        None
    """
    # Путь к CSV-файлу
    csv_file_path = '/Users/Edward/Code/html_parse/companies.csv'
    # Создание CSV-файла с заголовками
    create_csv_file(csv_file_path)
    
    for i in range(1, 927):  # Цикл для обработки файлов от 1.html до 927.html
        # Путь к HTML-файлу
        html_file_path = f'/Users/Edward/Code/html_parse/{i}.html'

        # Чтение HTML-файла
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Инициализация переменных
        current_company_name = current_revenue = current_inn = None

        # Запись данных в CSV-файл
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Company Name', 'INN', 'Revenue']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for line in html_content.split('\n'):
                match = re.search(r'(\d{10})', line)
                if match:
                    current_inn = match.group(1)
                
                match = re.search(r'&amp;quot;(.*?)&amp;quot;', line)
                if match:
                    current_company_name = unescape(match.group(1))

                match = re.search(r'(\d+\s*[млрдтрлнмлн]+)', line)
                if match:
                    current_revenue = match.group(1)

                if current_company_name and current_revenue and current_inn:
                    if current_inn.endswith('77'):
                        writer.writerow({
                            'Company Name': current_company_name,
                            'INN': current_inn,
                            'Revenue': current_revenue
                        })
                    current_company_name = current_revenue = current_inn = None

if __name__ == '__main__':
    main()
