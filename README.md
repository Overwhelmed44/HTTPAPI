# HTTP API

ASGI-compatible framework for building HTTP APIs

- Python 3.12 used

# Try it out
Clone the repository
```
git clone https://github.com/Overwhelmed44/HTTPAPI.git
```
Install all required packages
```
pip install -r requirements.txt
```
Run the app with an ASGI server
```python
from httpapi.responses import JSONResponse, PlainTextResponse, StatusResponse
from httpapi.request import Request
from httpapi import HTTPApi
from uvicorn import run

api = HTTPApi()

@api.get('/')
@api.get('/index')
async def handler(request: Request):
    content_type = request.headers.get('content-type')

    if content_type == 'application/json':
        return JSONResponse(request.json())
    elif content_type == 'text/plain':
        return PlainTextResponse(request.text())
    
    return StatusResponse(415)

def main():
    run(api)

if __name__ == '__main__':
    main()
```
