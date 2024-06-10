# Workshop lab APIs 

FastAPI service providing simplified APIs for a fictional restaurant, which will be 
used by a workshop/lab on LLM Agents.

NB: this is a contrived example, kept intentionally simple so that the focus of the 
workshop is on the actual LLM Agents. 

<br>

## Pre-requisites 

If running this lab locally, you will require: 
- Python version 3.10 or later installed. 
- Poetry 

<br>

## Running locally

Install dependencies: 

```bash
poetry install
```

Run: 

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