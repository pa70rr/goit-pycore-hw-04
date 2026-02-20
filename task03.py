import sys
from pathlib import Path
from colorama import Fore, init

# Включення кольорів для Windows
init(autoreset=True)

def directory(path: Path, indent: str = "") -> None:
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}")
                directory(item, indent + "  ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Немає доступу")

def main() -> None:
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Вкажіть шлях до папки")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях не існує")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: це не папка")
        return

    print(f"{Fore.YELLOW}{path}")
    directory(path)

if __name__ == "__main__":
    main()