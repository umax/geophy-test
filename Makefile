.PHONY: build upload flake8 isort install test

build:
	rm -rf dist/* && python setup.py sdist

upload:
	python setup.py sdist upload

flake8:
	flake8 gpgh tests

isort:
	isort --check-only --diff gpgh tests

install:
	pip install -e .

test:
	PYTHONPATH=. python -m pytest -vs tests --cov=gpgh
