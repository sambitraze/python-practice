import json

todoList = []
try:
    with open ("todoListFile", "r") as todofile:
    todofile.write(json.load (todoList))

def Display():
    index =1
    for index, todo in enumerate(todoList):
        print(
            index+1, "\t",
            "[*]" if todo["done"] else "[]",
            todo["task"]
        )
        index += 1

while True:
    #menu
    print("Menu:")
    print("1. Create todo")
    print("2. view TOdo list")
    print("3. Mark Todo as complete")
    print("4. Delete Todo")
    print("0. Exit")

    option = input("ENter the option number: ")
    if option == "1": #create
        todo = {"done":False, "task": input("Enter task: ")}
        todoList.append(todo)
    elif option == "2": #Display
        Display()
        pass
    elif option == "3": #Mark as complete
        index = int(input("Enter index of completed todo: "))
        todoList[index-1]["done"]=True
        Display()
        pass
    elif option == "4": #Delete
        Display()
        index = int(input("Enter index to delete: "))
        index-=1
        todoList.pop (index)
        #todoList[index:index+1] = []
        pass
    elif option == "0": # exit
        break
    else:
        print("Invalid option")

