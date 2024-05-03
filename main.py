from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from router import auth, book

import markdown2

app = FastAPI()

app.include_router(auth.router)
app.include_router(book.router)

# read the README.md file and convert to html for display as the root page for documentation
def convert_md_to_html():
    with open("README.md", "r") as file:
        md_content = file.read()
        html_content = markdown2.markdown(md_content)
    return html_content

@app.get("/")
def index():
    return HTMLResponse(convert_md_to_html())
