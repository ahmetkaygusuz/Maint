from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic_core import PydanticUndefinedType

async def custom_error_handler(request: Request, call_next  ):
    response = await call_next(request)
    if response.status_code == 404:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({"detail": "kayıt bulunamadı"}),
        )
    # elif response.status_code == 422:
    #   #  l = exc.errors()
    #     return JSONResponse(
    #         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    #         content={
    #         "detail": jsonable_encoder(
    #             exc.errors(),
    #             custom_encoder={
    #                 PydanticUndefinedType: lambda _: None,
    #             },
    #         )
    #     },
    #     )
    else:
        return response
    
# async def request_validation_exception_handler(request: Request, call_next , exc: RequestValidationError): 
#    response = await call_next(request)
#    if response.status_code == 422:
#      return JSONResponse( 
#          status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
#          content={"detail": jsonable_encoder(exc.errors())}, 
#      ) 
#    else: return response
