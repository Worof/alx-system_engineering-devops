# 0x15 API Interaction Project

## Overview
This project focuses on demonstrating how to interact with a REST API using Python. It includes scripts that fetch user data and their TODO list progress from a REST API, displaying it in a structured format, and further exporting it to CSV and JSON formats.

## Project Files
This directory contains the following files:

- `0-gather_data_from_an_API.py`: Fetches and displays the TODO list progress of a specific employee.
- `1-export_to_CSV.py`: Extends `0-gather_data_from_an_API.py` to export TODO list data to a CSV file.
- `2-export_to_JSON.py`: Extends `0-gather_data_from_an_API.py` to export TODO list data to a JSON file.
- `3-dictionary_of_list_of_dictionaries.py`: Fetches and exports TODO lists of all employees in JSON format.
- `README.md`: This file, which provides an overview and instructions for the project.

## Requirements
- Python 3.8.5
- `requests` library
- Linux environment (tested on Ubuntu 20.04 LTS)

## Setup
To run the scripts, you will need Python and the `requests` module installed on your system. If not already installed, you can install `requests` using pip:

```bash
pip install requests
