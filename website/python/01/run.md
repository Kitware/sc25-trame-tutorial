# Hands on

## Option 1 (repo)

### Fetching the code from repository

```bash
git clone git@github.com:Kitware/sc25-trame-tutorial.git
cd sc25-trame-tutorial/
```

### Virtual Environment

Create a virtual enviroment so you can run it

```bash
uv venv -p 3.10
source .venv/bin/activate
uv pip install trame
```

### Run example

```bash
python ./code/01-fundamentals/01-state-events.py
```

## Option 2 (copy/paste)

### Create file with content

Create a file `01-state-events.py` and paste the content below into it.

<<< ../../../code/01-fundamentals/01-state-events.py

### Virtual Environment

Create a virtual enviroment so you can run it

```bash
uv venv -p 3.10
source .venv/bin/activate
uv pip install trame
```

### Run example

```bash
python 01-state-events.py
```

## Result 

![App](/python/01/app.png)



