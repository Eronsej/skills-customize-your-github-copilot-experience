# 📘 Assignment: Consuming Web APIs with Python

## 🎯 Objective

Learn how to call REST APIs from Python, parse JSON responses, and use data from external web services in a program.

## 🔧 Prerequisites

- Python 3.8+
- `requests` library
- Basic Python knowledge: variables, functions, lists, and dictionaries

## 📝 Tasks

### 🛠️ Fetch Data from a Web API

#### Description
Write a function that sends a GET request to a public web API and returns the parsed JSON response.

#### Requirements
Completed program should:

- Use the `requests` library to fetch data from a public API
- Handle HTTP errors and invalid responses gracefully
- Return parsed JSON data for further processing

### 🛠️ Extract and Display Information

#### Description
Extract specific information from the API response and display it in a readable format.

#### Requirements
Completed program should:

- Select at least three fields from the response data
- Print a summary of the returned information
- Include clear labels and formatting for the output

### 🛠️ Save Data Locally

#### Description
Save the API response data into a JSON file for later use.

#### Requirements
Completed program should:

- Write the response data to a file named `api_response.json`
- Use proper JSON formatting and indentation
- Confirm when the file has been saved successfully

## ✅ Deliverables

- A Python script named `starter-code.py`
- A saved JSON file named `api_response.json` after running the script

## ▶️ How to run

1. Install dependencies:

   pip install requests

2. Run the script:

   python starter-code.py

3. Check the terminal output and the generated `api_response.json` file.
