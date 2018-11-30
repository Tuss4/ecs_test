from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse


app = Starlette()


@app.route('/')
class PingResource(HTTPEndpoint):
    
    async def get(self, request):
        return JSONResponse(dict(ping="pong"))


@app.route('/hey/{person}')
class HelloResource(HTTPEndpoint):

    async def get(self, request):
        person = request.path_params['person']
        print("MY GUY?")
        return JSONResponse(dict(whuddup=person), status_code=200)
