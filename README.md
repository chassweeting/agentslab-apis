# Workshop lab APIs 

FastAPI service providing simplified APIs for a fictional restaurant, to be 
used in a workshop/lab on LLM Agents.

NB: this contrived example is intentionally kept simple to keep the focus on LLM Agents. 

<br>

## Pre-requisites 

If running this lab locally, you will require: 
- Python version 3.10, 3.11 or 3.12 
- [Poetry](https://python-poetry.org/docs/) version 1.8+

<br>

## Installation

Use Poetry to install the dependencies. This will also create a virtualenv in the `.venv` directory. 

```bash
poetry install
```

If you encounter issues when trying to run this command  (eg. "The Poetry configuration is invalid"), try upgrading 
Poetry with `poetry self update`.


<br> 

## Running

No configuration is required.  Simply run the API locally with the following command from the repo root: 

```bash 
make serve 
```

(see the [Makefile](Makefile) for raw commands if you are unable to run `make` commands.)

<br>

## Using APIs 

You should be able to access the APIs at http://127.0.0.1:8000/docs 

<br>

## Building & running with Docker 

Assuming you have Docker installed, build and run locally on port 8000 with: 
 
```bash 
make build
make run  
```

(NB: make sure that no other service is running on port 8000 before running)
