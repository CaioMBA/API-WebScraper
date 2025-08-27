from dependency_injector.wiring import inject, Provide
from fastapi import Depends
from App.Controllers.ControllerBase import ControllerBase
from Infrastructure.CrossCutting.InjectionConfiguration import AppContainer


class ScrapingController(ControllerBase):
    def __init__(self):
        super().__init__()

        @self.router.get("/fetch_element")
        @inject
        async def fetch_element(url: str, selector: str, service=Depends(Provide[AppContainer.scraping_service])) -> dict:
            try:
                return service.fetch_element(url, selector)
            except Exception as e:
                return {"error": str(e)}
