from fastapi import FastAPI,Request,status
from routers import workCenter_routes
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def not_found(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 404:
        return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({"detail": "kayıt bulunamadı"}),
        )
    else:
        return response
    


app.include_router(workCenter_routes.router)

def printToFile(e):
    with open('my_errors.txt', 'a') as fh:
            print(e, file=fh)
    

@app.get("/")
async def root():
    return {"message": "Hello World"}


