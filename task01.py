from pathlib import Path


def total_salary(path: Path) -> tuple[float, float]:
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file: 
            for line in file:
                name, salary = line.strip().split(',')
                total += float(salary)
                count += 1
            average = total / count if count > 0 else 0
            return total, average,
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except Exception:
        print(f"Файл пошкоджено: {path}")


salary_file = Path("salary_file.txt")
total, average = total_salary(salary_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


