def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()
        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index + 1}-{items}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not Valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)
            write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Index doesn't exist")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye!")
