def get_todos():
    with open("todos.txt", 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos():
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
    return todos


while True:
    user_action = input("type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        todos = write_todos()

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
            todos = write_todos()
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
            todos = write_todos()
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
