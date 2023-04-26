import logging
import azure.functions as func
from fastapi.responses import HTMLResponse
from FastAPIApp import app  # Main API application


@app.get("/api/index.html", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>FastAPI HTML Response</title>
        </head>
        <body>
            <h1>Hello, world!</h1>
        </body>
    </html>
    """
    return html_content

@app.get("/api/sample")
async def sample():
    return {
        "info": "Try /hello/Shivani for parameterized route.",
    }


@app.get("/api/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
