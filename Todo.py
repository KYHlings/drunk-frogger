from pathlib import Path


def main():
    p = Path("Todo.txt")
    todo_list = p.read_text(encoding="utf8").splitlines()

    while True:
        meny = int(input("Välj ett meny val:\n1: Titta på Todolistan\n2: Lägg till i Todo-list"))
        if meny == 1:
            showlist(todo_list)
        if meny == 2:
            todo_list = addlist(todo_list,p)


def showlist(text):
    number = 0
    for line in text:
        number += 1
        print(f"{number}: {line}")


def addlist(todo_list,p):

    new_content = input("Vad vill du lägga till?")
    todo_list.append(new_content)
    p.write_text("\n".join(todo_list), encoding='utf8')
    return todo_list

if __name__ == "__main__":
    main()
