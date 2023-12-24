def create_task(title, description):
    with open('tasks.txt', 'a') as file:
        file.write(f"Task: {title}\nDescription: {description}\n\n")
    print(f"Создана новая задача: {title}")
