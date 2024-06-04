# Mutual Fund Backend

This repository contains the backend code for the Mutual Fund Dashboard and Analysis project. Developed with Python and Flask, it includes APIs for scraping mutual fund data, serving it to the frontend, and integrating with a GenAI model to provide natural language insights and user query responses. The backend also manages data storage and processing.

## Table of Contents

- [Mutual Fund Backend](#mutual-fund-backend)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
  - [API Endpoints](#api-endpoints)
  - [Running Tests](#running-tests)
  - [Deployment](#deployment)
  - [License](#license)

## Prerequisites

- Python 3.7+ installed. You can download it from [python.org](https://www.python.org/).

## Getting Started

Follow these steps to set up and run the project locally.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/mutual-fund-backend.git
   cd mutual-fund-backend

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Set the Flask application variable:**
   ```bash
   export FLASK_APP=app.py  # On Windows, use `set FLASK_APP=app.py`

5. **Run the development server:**
   ```bash
   flask run
**The application will run on http://127.0.0.1:5000.**

## Project Structure
```plaintext
mutual-fund-backend/
├── app.py                   # The main Flask application file
├── requirements.txt         # Python dependencies
├── routes/
│   ├── __init__.py
│   ├── data_routes.py       # Routes for fetching mutual fund data
│   └── genai_routes.py      # Routes for querying the GenAI model
├── services/
│   ├── __init__.py
│   ├── scraper.py           # Functions for scraping mutual fund data
│   └── genai_service.py     # Functions for integrating with the GenAI API
├── instance/                # Directory for instance-specific files (e.g., config)
└── .gitignore
```
## API Endpoints
The backend provides the following API endpoints:

**GET /api/mutual-funds**

Fetch mutual fund data.

Request:
```http
GET /api/mutual-funds
```
Response:
```json
[
  {
    "fund_name": "Example Fund",
    "fund_performance": "10%",
    "fund_details": "Details about the fund"
  }
]
```

**POST /api/genai/ask**

Ask a question to the GenAI model.

Request:
```http
POST /api/genai/ask
Content-Type: application/json

{
  "question": "What is the best mutual fund to invest in 2024?"
}
```
Response:
```json
{
  "answer": "Based on current market trends, it is advisable to invest in mutual funds with a strong track record of performance, low expense ratios, and diversification across sectors."
}
```

## Running Tests
To run tests for the backend, you need to install testing dependencies and use a test runner such as pytest.
1.	**Install testing dependencies:**
```bash
pip install pytest
```
2. **Run tests:**
```bash
pytest
```
## Deployment
For production deployment, it is recommended to use a production-ready WSGI server such as Gunicorn.
1.	**Install Gunicorn:**
```bash
pip install gunicorn
```
2. **Run the application with Gunicorn:**
```bash
gunicorn -w 4 app:app
```
3. **Serving Static Files:**
- If you have a frontend, ensure it is built and its static files are served correctly. This can be configured in app.py.

## License
This project is licensed under the MIT License