from bs4 import BeautifulSoup
import csv

def create_csv_file(file_path):
    """
    Создает новый CSV-файл и записывает в него заголовки.
    
    Параметры:
        file_path (str): Путь для сохранения CSV-файла.
        
    Возвращаемое значение:
        None
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Company Name', 'INN', 'Revenue']  # Заголовки столбцов
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Запись заголовков в файл

def main():
    """
    Основная функция для парсинга HTML-файлов и записи данных в CSV.
    
    Параметры:
        None
        
    Возвращаемое значение:
        None
    """
    # Путь к CSV-файлу
    csv_file_path = '/Users/Edward/Code/html_parse/companies.csv'
    
    # Создание нового CSV-файла с заголовками
    create_csv_file(csv_file_path)

    # Цикл по HTML-файлам для парсинга (в этом примере только один файл: 3.html)
    for i in range(2, 926):
        # Путь к текущему HTML-файлу
        html_file_path = f'/Users/Edward/Code/html_parse/{i}.html'

        # Чтение и парсинг HTML-файла
        with open(html_file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Открытие CSV-файла для добавления данных
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Company Name', 'INN', 'Revenue']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Цикл по всем элементам с классом 'raiting-list__item' в HTML
            for item in soup.select('.raiting-list__item'):
                # Извлечение названия компании
                company_name = item.select_one('a').text
                
                # Извлечение параметров компании (выручка и ИНН)
                params = item.select('.raiting-list__item-params li')
                revenue = params[0].text.strip()
                inn = params[1].text.strip()

                # Запись данных в CSV-файл, если ИНН начинается с '77'
                if inn.startswith('77'):
                    writer.writerow({
                        'Company Name': company_name,
                        'INN': inn,
                        'Revenue': revenue
                    })

if __name__ == '__main__':
    main()