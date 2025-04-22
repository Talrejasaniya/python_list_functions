if __name__ == '__main__':
    N = int(input())  # Number of operations
    my_list = []  # Renamed list to my_list

    for i in range(N):
        task = input().strip()  # Read the command
        tasks = task.split()  # Split the input into parts

        if tasks[0] == "append":
            num1 = int(tasks[1])
            my_list.append(num1)
        elif tasks[0] == "remove":
            num1 = int(tasks[1])
            my_list.remove(num1)
        elif tasks[0] == "sort":
            my_list.sort()
        elif tasks[0] == "pop":
            my_list.pop()
        elif tasks[0] == "reverse":
            my_list.reverse()
        elif tasks[0] == "insert":
            index = int(tasks[1])
            num2 = int(tasks[2])
            my_list.insert(index, num2)
        elif tasks[0] == "print":
            print(my_list)
