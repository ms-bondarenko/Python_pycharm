import os
import shutil
from time import sleep


def clear_firefox_cache():
    # Путь к профилю Firefox
    profile_path = os.path.expandvars(r'%APPDATA%\Mozilla\Firefox\Profiles')

    if not os.path.exists(profile_path):
        print(f"Папка профиля не найдена: {profile_path}")
        return

    profiles = os.listdir(profile_path)

    for profile in profiles:
        # Проверяем несколько возможных мест для кэша
        cache_paths = [
            os.path.join(profile_path, profile, 'cache2'),
            os.path.join(profile_path, profile, 'cache'),
            os.path.join(profile_path, profile, 'storage')
        ]

        for cache_path in cache_paths:
            if os.path.exists(cache_path):
                shutil.rmtree(cache_path)  # Удаляем папку кэша
                print(f"Кэш для профиля {profile} очищен из {cache_path}.")
            else:
                print(f"Кэш для профиля {profile} не найден в {cache_path}.")


if __name__ == "__main__":
    clear_firefox_cache()

sleep(10)
