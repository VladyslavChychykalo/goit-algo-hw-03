import os
import shutil
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів за розширенням.")
    parser.add_argument("source", nargs="?", default="test",
                        help="Шлях до вихідної директорії (за замовчуванням 'test')")
    parser.add_argument("destination", nargs="?", default="dist",
                        help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()


def copy_files_by_extension(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                copy_files_by_extension(src_path, dest_dir)

            elif os.path.isfile(src_path):
                file_ext = Path(src_path).suffix.lower().lstrip('.') or "no_extension"

                # Формуэмо шлях для зберегання файлів відповідного типу
                # ./dist/jpg
                # ./dist/txt
                ext_folder = os.path.join(dest_dir, file_ext)
                # Створюється підпапка
                os.makedirs(ext_folder, exist_ok=True)

                # Копіюємо файл у відповідну підпапку
                dest_path = os.path.join(ext_folder, os.path.basename(src_path))
                # os.path.basename(src_path) -> Назва файлу без шляху
                shutil.copy2(src_path, dest_path)

                print(f"Скопійовано: {src_path} → {dest_path}")

    except PermissionError:
        print(f"❌ Немає доступу до: {src_dir}")
    except Exception as e:
        print(f"⚠️ Помилка при обробці '{src_dir}': {e}")


def main():
    args = parse_args()

    source = os.path.abspath(args.source)
    destination = os.path.abspath(args.destination)

    print("=== КОПІЮВАННЯ ФАЙЛІВ ЗА РОЗШИРЕННЯМ ===")
    print(f"Джерело:      {source}")
    print(f"Призначення:  {destination}\n")

    if not os.path.exists(source):
        print("❌ Вихідна директорія не існує!")
        return

    os.makedirs(destination, exist_ok=True)

    copy_files_by_extension(source, destination)

    print("\n✅ Копіювання завершено!")


if __name__ == "__main__":
    main()
