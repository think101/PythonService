install:
    #install commands
	pip install --upgrade pip &&\
         pip install -r requirements.txt
	python -m textblob.download_corpora
format:
    #format code
	black *.py mylib/*.py
lint:
    #flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
    #test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build docker image
	docker build -t  deploy-fastapi .
run:
	#run docker image
	docker run -p 8000:8000 deploy-fastapi
deploy:
    #deploy
all: install lint test deploy
