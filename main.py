import sqlite3
from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, RedirectResponse, PlainTextResponse, HTMLResponse
import base_repr
import mmh3
from fastapi.templating import Jinja2Templates
import python_multipart

conn = sqlite3.connect("main.db")
cursor = conn.cursor()
table = """ CREATE TABLE IF NOT EXISTS urlshortener ( url TEXT UNIQUE NOT NULL, hash TEXT NOT NULL); """
cursor.execute(table)
conn.close()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home_page():
    return FileResponse("templates/home.html")

@app.post("/", response_class=HTMLResponse)
async def new_url(request: Request, url: Annotated[str, Form()]):
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT hash FROM urlshortener WHERE url = ? """, (url,))
    hash_and_base62_exists = cursor.fetchone()

    if hash_and_base62_exists:
        conn.close()
        return templates.TemplateResponse(request=request, name="urlshortened.html", context={"shortened_url": hash_and_base62_exists[0]})

    hashed_and_base62 = base_repr.int_to_repr(mmh3.hash(url, 0, False), base=62)

    cursor.execute(""" INSERT INTO urlshortener VALUES (?, ?) """, (url, hashed_and_base62))
    conn.commit()
    conn.close()

    return templates.TemplateResponse(request=request, name="urlshortened.html", context={"shortened_url": hashed_and_base62})

@app.get("/{hashbase62}")
async def return_site(hashbase62: str):
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT url FROM urlshortener WHERE hash = ? """, (hashbase62,))
    url_to_redirect = cursor.fetchone()
    conn.close()

    if url_to_redirect:
        return RedirectResponse(url_to_redirect[0])
    return FileResponse("templates/error.html")
