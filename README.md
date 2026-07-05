# Signup Lab

A simple FastAPI application that aggregates signup events by date. This is the first step of the lab, utilizing a thread-safe in-memory store.

## Features

- **Signup Tracking:** Increments signup counts for the current date.
- **Aggregation Endpoint:** Retrieve signup statistics grouped by date.
- **Thread-safe Store:** Uses Python's `threading.Lock` to safely modify the count.

## Prerequisites

- Python 3.10+
- `pip`

## Installation

1. Clone or navigate to the repository directory:
   ```bash
   cd signup-lab
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

By default, the server will start on `http://127.0.0.1:8000`.

## API Endpoints

### 1. Track a Signup
- **Endpoint:** `/signup`
- **Method:** `GET`
- **Query Parameters:**
  - `country` (string, required): The country from which the signup occurred.
- **Example Request:**
  `GET http://127.0.0.1:8000/signup?country=Canada`
- **Example Response:**
  ```json
  {
    "status": "ok",
    "country": "Canada",
    "date": "2026-07-04"
  }
  ```

### 2. Get Aggregated Signups
- **Endpoint:** `/aggregation`
- **Method:** `GET`
- **Example Request:**
  `GET http://127.0.0.1:8000/aggregation`
- **Example Response:**
  ```json
  {
    "2026-07-04": 1
  }
  ```

## Future Scope

As indicated in the code comments, future improvements include:
- Integrating with a message broker (e.g., Apache Kafka) for event streaming.
- Storing aggregated results in a persistent database (e.g., PostgreSQL or Redis) instead of keeping them in-memory.
