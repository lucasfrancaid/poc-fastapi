[![LinkedIn][linkedin-shield]][linkedin-url]

# POC - FastAPI
Advancing to Routes and Test with FastAPI


## Requirements
- Python 3.8
- Docker


## 🚀 Starting
- Clone this repository:
```bash
git clone https://github.com/lucasfrancaid/poc-fastapi.git
```

- Turn to this branch:
```bash
git checkout -b advancing
git pull origin advancing
```

### Setup with Docker
```bash
docker-compose up
```

- Run tests
```bash
docker-compose exec server pytest -v
```

### Manual setup
- Create and activate a virtual environment:
```bash
pip3 install pipenv
pipenv install
pipenv shell
```

- Run the live server with uvicorn:
```bash
uvicorn src.main:app --reload
```

- Run tests
```bash
pytest -v
```

## ▶️ Do requests
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc


## 📬 Contact
<b>Lucas França</b> <br/>
Linkedin: https://www.linkedin.com/in/lucasfrancaid/

<br>


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lucasfrancaid
