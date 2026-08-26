# IDS706-Assignment-1
[![Python tests](https://github.com/ZhihaoZhou0/IDS706-Assignment-1/actions/workflows/test.yml/badge.svg)](https://github.com/ZhihaoZhou0/IDS706-Assignment-1/actions/workflows/test.yml)

This project asks for a name and prints a welcome message for the Data Engineering course.

## Setup

Create a virtual environment:

### Mac / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```bash
make install
```

## Run the Application

```bash
make run
```

## Run Tests

```bash
make test
```

## Run Linting

```bash
make lint
```

## Docker

Build the Docker image:

```bash
make docker-build
```

Run the application inside Docker:

```bash
make docker-run
```

Run the tests inside Docker:

```bash
make docker-test
```

## Example

Enter your name when prompted:

```text
Andy, welcome to the Data Engineering course.
