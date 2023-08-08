# Project

## Requirements

### Docker

https://docs.docker.com/engine/install/

### Make

https://www.gnu.org/software/make/manual/make.html#Introduction

### Pre-commit

https://pre-commit.com/

## Starting

After install and configure all requirements run the following commands to startup server on port 8000. Database will run on port 5432 and you can connect through an IDE using the .env paramenters.

```
make build
make migrate
make runserver
```

## Useful Commands

### Pre-commit

- Install Pre-commit on repository

```
pre-commit install
```

- Run Pre-commit on all files
```
pre-commit run --all-files
```

### Make

- Build containers
```
make build
```

- Up containers
```
make runserver
```

- Run Tests
DIR: tests_folder = app/tests/{DIR}
```
make test DIR="<tests_folder>"
```

- Create Database Migrations
```
make makemigrations MSG="<message to create migration>"
```

- Run migrations
```
make migrate
```
