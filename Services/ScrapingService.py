from curl_cffi import requests as creq
from typing import Dict, Any
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class ScrapingService:
    def __init__(self) -> None:
        self.browser_headers = {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36"),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Upgrade-Insecure-Requests": "1",
        }

    def fetch_element(self, url: str, selector:str) -> Dict[str, Any]:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL provided.")
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        with creq.Session(impersonate="chrome120") as s:
            s.headers.update(self.browser_headers)
            s.get(base_url, timeout=30, allow_redirects=True)
            r = s.get(url, timeout=30, allow_redirects=True, impersonate="chrome120")
            if r.status_code != 200 or "Just a moment" in r.text[:200]:
                raise RuntimeError(
                    f"Blocked: status={r.status_code}, server={r.headers.get('server')}, "
                    f"cf-ray={r.headers.get('cf-ray')}"
                )
            soup = BeautifulSoup(r.text, "html.parser")
            element = soup.select_one(selector)

        if not element:
            raise ValueError(f"Element with selector '{selector}' not found.")
        return {
            "selector": selector,
            "html": str(element),
            "text": element.get_text(strip=True),
            "tag": element.name,
            "attributes": dict(element.attrs)
        }
