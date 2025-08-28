# API Web Scraper

This project provides a simple yet powerful REST API for web scraping. Built with Python and FastAPI, it allows you to fetch specific elements from a web page by providing a URL and a CSS selector.

## Features

-   **Simple and Fast**: Built on FastAPI for high performance.
-   **Dynamic Scraping**: Fetches content from web pages using CSS selectors.
-   **Bypass Anti-Bot Measures**: Uses `curl-cffi` to impersonate browser TLS fingerprints, helping to avoid blocks from services like Cloudflare.
-   **Containerized**: Includes a `Dockerfile` for easy deployment.
-   **Extensible**: Designed with a clean architecture, making it easy to add new features.

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

### Using Docker (Recommended)

1.  Build the Docker image:
    ```bash
    docker build -t api-webscraper .
    ```

2.  Run the Docker container:
    ```bash
    docker run -p 8000:8000 api-webscraper
    ```

### Locally

Run the application using `uvicorn`:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

## API Usage

The API has a single endpoint for scraping web page elements.

### Fetch Element

-   **Endpoint**: `GET /fetch_element`
-   **Description**: Fetches the text content of an HTML element based on a URL and a CSS selector.
-   **Query Parameters**:
    -   `url` (string, required): The URL of the web page to scrape.
    -   `selector` (string, required): The CSS selector for the element to target.

-   **Example Request**:

    ```bash
    curl -X GET "http://localhost:8000/fetch_element?url=https://example.com&selector=h1"
    ```

-   **Example Response**:

    ```json
    {
        "text": "Example Domain"
    }
    ```

## Configuration

Application settings can be configured in the `App/appsettings.json` file.

## Project Structure

The project follows a clean architecture pattern, separating concerns into different layers:

-   `App/`: Contains the FastAPI application, controllers, and configuration.
-   `Domain/`: Defines the core data models and enums.
-   `Infrastructure/`: Manages data access, dependency injection, and other cross-cutting concerns.
-   `Services/`: Contains the business logic for the application, such as the scraping service.
-   `main.py`: The entry point for the FastAPI application.
-   `Dockerfile`: For building the Docker container.
-   `requirements.txt`: Python dependencies.
