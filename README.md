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
from httpapi import HTTPAPI
from uvicorn import run

api = HTTPAPI()

@api.get('/')
@api.get('/index')
async def index(request: Request):
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
# Out-of-the-box light testing framework
Framework has out-of-the-box testing framework with 3 levels of logging
```python
from httpapi.tests import Tester

tester = Tester()

@tester.tester({'body': b'Hello, world!', 'headers': {'content-type': 'text/plain'}},
               {'body': b'Hello, world!', 'status': 200, 'headers': {'content-type': 'text/plain'}})
@tester.tester({'body': b'**json-encoded**', 'headers': {'content-type': 'application/json'}},
               {'body': b'**json-encoded**', 'status': 200})
@api.get('/')
@api.get('/index')
async def index(request: Request):
    content_type = request.headers.get('content-type')

    if content_type == 'text/plain':
        return PlainTextResponse(request.text())
    
    return PlainTextResponse('Not a text/plain request!', 415)
```
