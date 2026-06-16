# Job Application Tracker

A Python command-line application for tracking job and internship applications. The app lets users add, view, update, delete, search, and organize applications while saving data locally using JSON.

## Features

* Add job applications with company, role, status, date applied, link, and notes
* View all applications
* Sort applications by original order, company name, status, or date applied
* Search applications by company or status
* Update application status
* Edit application details
* Delete applications
* View application statistics
* Save and load data using a JSON file
* Validate date input using `YYYY-MM-DD` format
* Handle invalid number inputs with `try/except`

## Technologies Used

* Python
* JSON file storage

## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Run the program:

```bash
python job_tracker.py
```

## Example Menu

```text
1. Add application
2. View applications
3. Update status
4. Edit application
5. Delete an application
6. Search an application
7. View stats
8. Exit
```

## Data Storage

Applications are saved locally in an `applications.json` file. This file is ignored by Git so private application links and notes are not uploaded.

## Project Purpose

I built this project to practice Python fundamentals, including functions, lists, dictionaries, loops, file handling, JSON storage, input validation, and error handling.
