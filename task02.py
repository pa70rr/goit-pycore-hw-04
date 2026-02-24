from pathlib import Path


def get_cats_info(path: Path) -> list[dict[str, str]]:
    cats = []  
    try:
        with open(path, 'r', encoding='utf-8') as file: 
            for line in file:
                id, name, age = line.strip().split(',')
                cat = {"id": id, "name": name, "age": age}
                cats.append(cat)
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except Exception:
        print(f"Файл пошкоджено: {path}")
    return cats  


cats_file = Path("cats_file.txt")
cats_info = get_cats_info(cats_file)
print(cats_info)
