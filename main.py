from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# Todo 목록을 저장할 변수
todos = []

@app.get("/", response_class=HTMLResponse)
async def read_root():
    todo_list_html = "".join([f"<li>{todo}</li>" for todo in todos])
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Todo List</title>
    </head>
    <body>
        <h1>Todo List</h1>
        <ul>{todo_list_html}</ul>
        <form action="/add" method="post">
            <input type="text" name="todo" placeholder="Enter a todo item" required>
            <button type="submit">Add Todo</button>
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/add")
async def add_todo(todo: str = Form(...)):
    todos.append(todo)
    return HTMLResponse(content=f"""
    <html>
    <body>
        <h1>Todo Added</h1>
        <p>{todo} has been added to your todo list.</p>
        <a href="/">Back to Todo List</a>
    </body>
    </html>
    """)
