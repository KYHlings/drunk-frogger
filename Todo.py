from pathlib import Path

def main():
    Todo=Path("todo.txt")
    Todo_list=Todo.read_text(encoding="utf8").splitlines()

    while True:
        menue=(int(input))



if __name__ == "__main__":
    main()
