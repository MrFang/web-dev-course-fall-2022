from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .types import RequestBody

app = FastAPI()


@app.get("/hello", response_class=HTMLResponse)
def hello() -> str:
    return 'Hello, World'


@app.get("/hello/{name}", response_class=HTMLResponse)
def hello_name(name: str) -> str:
    return f'Hello, {name}'


@app.get("/query", response_class=HTMLResponse)
def query_param_endpoint(param: str) -> str:
    return f'Query param = {param}'


@app.post('/with/body', response_class=HTMLResponse)
def with_body(body: RequestBody) -> str:
    return repr(body)
