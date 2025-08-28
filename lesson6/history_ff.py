import os

def delete_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Файл '{file_path}' успешно удален.")
        else:
            print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при удалении файла: {e}")

# Укажите путь к файлу, который нужно удалить
file_to_delete = r'C:\Users\SMART\AppData\Roaming\Mozilla\Firefox\Profiles\gwr3nc5n.default-release\places.sqlite'
delete_file(file_to_delete)