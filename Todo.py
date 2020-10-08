from pathlib import Path

def main():
    Todo=Path("Todo.txt")
    Todo_list=Todo.read_text(encoding="utf8").splitlines()

    while True:
        meny=int(input("Välj ett meny val:\n1: Titta på Todolistan"))
        if meny == 1:
            showlist(Todo_list)
def showlist(text):
    number = 0
    for line in text:
        number += 1
        print(f"{number}: {line}")



if __name__ == "__main__":
    main()
