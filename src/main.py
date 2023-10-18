from fastapi import FastAPI, Request,status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic_core import PydanticUndefinedType
from src.routes import workCenter_routes
from src.middlewares.error_handler import custom_error_handler

app = FastAPI()

app.include_router(workCenter_routes.router)

app.middleware('http')(custom_error_handler)
#app.middleware('http')(request_validation_exception_handler)

@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    _req: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle request validation errors."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": jsonable_encoder(
                exc.errors()[0]["msg"],
               
            )
        },
    )


def printToFile(e):
    with open('my_errors.txt', 'a') as fh:
        print(e, file=fh)


@app.get("/")
async def root():
    return {"message": "Hello World"}
