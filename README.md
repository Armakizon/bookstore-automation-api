# Bookstore QA Automation Project

## Overview

This project is a **quality assurance automation suite** for the [DemoQA Bookstore API](https://demoqa.com/swagger). It includes automated test cases for both positive and negative scenarios, focusing on functionality, validation, and user flow coverage.

The goal of this project is to demonstrate real-world QA skills, including:

- Test design and documentation  
- API test automation using Python  
- Assertion handling and bug discovery  
- Reporting and code organization  

## Tech Stack

- Python 3.11  
- Pytest for test automation  
- Requests for API interactions  
- Allure (optional) for reporting  
- Git for version control  

## Test Coverage

The test suite covers key endpoints of the Bookstore API:

| Feature           | Examples of Tests                              |
|-------------------|------------------------------------------------|
| Authentication    | Login success and failure, signup scenarios    |
| Book Management   | Add/remove book, get list, get by ISBN         |
| User Flows        | Create user, delete user, update user info     |
| Error Handling    | Invalid requests, unauthorized access          |

Each test is based on a clear test case documented in `test_cases.md`, with naming aligned to the format: `TC_### - Test Description`.

## Project Structure

```
bookstore-automation-api/
├── tests/               # Automated test cases
├── test_cases.md        # Manual test cases (Given-When-Then style)
├── requirements.txt     # Dependencies
├── README.md            # This file
└── utils/               # Helper functions (e.g., auth token generator)
```

## What I Learned

- Writing clear, maintainable test cases  
- Identifying edge cases and failure points  
- Structuring a QA automation project  
- Working with real APIs and debugging responses  
- Version control and clean commit practices  

## How to Run the Tests

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the tests using:  
   ```bash
   pytest
   ```

(Optional) Generate an Allure report:  
```bash
pytest --alluredir=allure-results  
allure serve allure-results
```

## Contact

Created by **Shaked Duba** — QA enthusiast seeking an entry-level role in tech.  
Feel free to connect via [LinkedIn](https://www.linkedin.com/in/YOUR-LINK) or visit [GitHub](https://github.com/YOUR-GITHUB).
