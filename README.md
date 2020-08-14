## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Launch](#launch)

## General info
This is the repository of cinema web app built in Django.
Project is simply about booking seats in cinema and provides some cool features depended on (admin, reception, client) account.
Administration cares about adding cinema halls, movies.
Reception can register clients and print the tickets.
Clients may choose and book seats.

## Technologies
Project is created with:
* [django](https://www.djangoproject.com)
* [poetry](https://python-poetry.org)

## Launch
[poetry](https://python-poetry.org/) is a package-manager tool of the project.


1. Create appropriate directory for the project and clone the repo to your local machine

```bash
$ cd project_directory
$ git clone <repo address>
```


2. Generate virtual environment and install all needed dependencies

```bash
$ poetry install
```


3. If you need help or more info about poetry, run:

```bash
$ poetry --help
```