import subprocess
import os

if not os.path.exists('dz1.py'):
    print("Файл dz1.py не знайдено!")
    exit(1)

try:
    subprocess.run(['cp', 'dz1.py', 'dz1_run.py'], check=True)
    print("Файл dz1.py успішно скопійовано у dz1_run.py")
except subprocess.CalledProcessError as e:
    print(f"Помилка при копіюванні файлу: {e}")
    exit(1)

prepend_text = "#!/usr/bin/env python3\n# Це файл для запуску\n\n"
try:
    if not os.path.exists("dz1_run.py"):
        print("Файл dz1_run.py не знайдено!")
        exit(1)

    with open("dz1_run.py", "r+") as file:
        original_content = file.read()
        file.seek(0)
        file.write(prepend_text + original_content)
    print("Текст успішно дописано в початок файлу dz1_run.py")
except Exception as e:
    print(f"Помилка при зміні файлу: {e}")
    exit(1)

try:
    if not os.path.exists("dz1_run.py"):
        print("Файл dz1_run.py не знайдено!")
        exit(1)

    subprocess.run(['chmod', '700', 'dz1_run.py'], check=True)
    print("Права на файл змінено: тільки овнер має доступ")
except subprocess.CalledProcessError as e:
    print(f"Помилка при зміні прав файлу: {e}")
    exit(1)

try:
    if not os.path.exists("dz1_run.py"):
        print("Файл dz1_run.py не знайдено!")
        exit(1)

    subprocess.run(['./dz1_run.py'], check=True)
    print("Файл dz1_run.py успішно виконано")
except subprocess.CalledProcessError as e:
    print(f"Помилка при виконанні dz1_run.py: {e}")
    exit(1)

except Exception as e:
    print(f"Непередбачена помилка: {e}")
    exit(1)
