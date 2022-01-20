# gpgh (GeoPhy GitHub)

Analyzes GitHub repos in an organization. Shows top organization's repos (by number of pull requests) and its most used programming languages. Can be used as a Python package or command line script.

Use as package:
```
pip install gpgh
import gpgf

metrics = gpgf.get_metrics(
    token='mytoken',
    org='org1',
    top_repos=5,
    top_langs=3,
)
print(metrcis)
```

as command line script:
```
pip install gpgh
gpgf --token=mytoken --org=org1 --top-repos=5 --top-langs=3
```


## How to build a package
```
$ make build
```

## How to upload package to PyPi
```
$ make upload
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
$ pip install pytest
```

run tests:
```
make test
```
