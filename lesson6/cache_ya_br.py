import os
import shutil
import platform


def get_yandex_browser_paths():
    # Определяем операционную систему
    system = platform.system()

    if system == 'Linux':
        return os.path.expanduser('~/.config/yandex-browser/Default')
    elif system == 'Windows':
        return os.path.join(os.environ['LOCALAPPDATA'], 'Yandex', 'YandexBrowser', 'User Data', 'Default')
    elif system == 'Darwin':  # macOS
        return os.path.expanduser('~/Library/Application Support/Yandex/Browser/Default')
    else:
        raise Exception("Операционная система не поддерживается.")


def find_cache_path(profile_path):
    # Проверяем стандартные пути к кешу
    cache_path = os.path.join(profile_path, 'Cache')
    if os.path.exists(cache_path):
        return cache_path

    # Если кеш не найден, проверяем другие возможные пути
    alternative_cache_paths = [
        os.path.join(profile_path, 'Default', 'Cache'),
        os.path.join(profile_path, 'Profile 1', 'Cache'),
        os.path.join(profile_path, 'Profile 2', 'Cache')
    ]

    for path in alternative_cache_paths:
        if os.path.exists(path):
            return path

    return None


def clear_cache_and_history(clear_cache=True, clear_history=True):
    profile_path = get_yandex_browser_paths()

    # Находим путь к кешу
    cache_path = find_cache_path(profile_path)
    history_path = os.path.join(profile_path, 'History')

    if clear_cache:
        if cache_path:
            shutil.rmtree(cache_path)
            print("Кеш успешно очищен.")
        else:
            print("Кеш не найден.")

    if clear_history:
        if os.path.exists(history_path):
            os.remove(history_path)
            print("История успешно очищена.")
        else:
            print("История не найдена.")


if __name__ == "__main__":
    clear_cache = input("Очистить кеш? (да/нет): ").strip().lower() == 'да'
    clear_history = input("Очистить историю? (да/нет): ").strip().lower() == 'да'

    clear_cache_and_history(clear_cache, clear_history)
