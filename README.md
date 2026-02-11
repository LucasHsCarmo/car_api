# Installing FastAPI

## Install pipx

```sh
apt install pipx
pipx ensurepath
exec zsh
```

## Install poetry

```sh
pipx install poetry
pipx inject poetry poetry-plugin-shell
```

## Create project

```sh
poetry new --flat car_api
poetry python install 3.13
```

## Access project and using VirtualEnv

```sh
cd car_api
poetry env use 3.13
poetry env info
```

## Install FastAPI

```sh
poetry install
poetry add 'fastapi[standard]'
```

## Execution

```sh
poetry run fastapi dev car_api/app.py
```

## Test Browser

```sh
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```