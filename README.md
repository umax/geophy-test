# gpgh (GeoPhy GitHub)

Analyzes GitHub repos in an organization. Shows top organization's repos (by number of pull requests) and its most used programming languages. Can be used as a Python package or command line script.

Use as package:
```
pip install gpgh
import gpgf
```

as command line script:
```
pip install gpgh
gpgf --token=mytoken --org-id=org1 --repos-num=5 --langs-num=3
```


## How to build a package
```
$ make build
```

## How to upload package to PyPi
```
$ make upload
```

## How to install package locally
```
$ make install
```

## How to lint the code

install required Python packages:
```
$ pip install isort flake8
```

check imports:
```
make isort
```

flake8 your code:
```
make flake8
```

## How to test the code

install required Python packages:
```
$ pip install pytest pytest-cov
```

run tests:
```
make test
```
