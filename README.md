# DevOps Midterm Project

## Project Description
A Python Flask web application demonstrating a CI/CD pipeline using GitHub Actions and deployment on Render.

## Technologies
- Python 3
- Flask
- Pytest
- Gunicorn
- GitHub Actions
- Render

## CI/CD Pipeline
The pipeline runs on pushes to main and dev, and pull requests to main.

1. Build - Install dependencies and check Python syntax.
2. Test - Run automated tests using pytest.
3. Deploy - Deploy the application using Render from the main branch.

## Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## Run Tests
```bash
pytest -v
```

## Live Application
https://devops-midterm.onrender.com

## Health Check
https://devops-midterm.onrender.com/health

## Repository
https://github.com/archilkalandadze/devops-midterm
