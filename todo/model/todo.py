# TODO: Add code here

class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tag:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id}-{self.title}"

class TodoBook:

    def __init__(self, todos: dict):
        self.todos: dict = {}

    def add_todo(self, title: str, description: str) ->:
        new_id = len(self.todos) + 1
        new_todo = Todo(new_id, title, description)
        self.todos[new_id] = new_todo

        return new_id

    def pending_todos
        return self.tags









