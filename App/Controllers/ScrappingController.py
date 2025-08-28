from dependency_injector.wiring import inject, Provide
from fastapi import Depends, Header, status
from fastapi.responses import JSONResponse
from typing import Annotated
from App.Controllers.ControllerBase import ControllerBase
from Infrastructure.CrossCutting.InjectionConfiguration import AppContainer


class ScrapingController(ControllerBase):
    def __init__(self):
        super().__init__()

        @self.router.get("/fetch_element")
        @inject
        async def fetch_element(url: Annotated[str, Header(..., alias="url")],
                                selector: Annotated[str, Header(..., alias="selector")],
                                service=Depends(Provide[AppContainer.scraping_service])) -> JSONResponse:
            try:
                data = service.fetch_element(url, selector)
                return JSONResponse(content={
                    "success": True,
                    "message": "Successfully fetched element.",
                    "status": 200,
                    "data": data
                }, status_code=status.HTTP_200_OK)
            except Exception as e:
                return JSONResponse(content={
                    "success": False,
                    "message": str(e),
                    "status": 400,
                    "data": None
                }, status_code=status.HTTP_400_BAD_REQUEST)
