# DemoQA Bookstore - Automated Test Suite

## Table of Contents

- [User Story 1: Guest Access](#user-story-1-guest-access)
  - [TC_110 - Typing full book title shows correct result](#tc_110)
  - [TC_111 - Typing partial match returns filtered result](#tc_111)
  - [TC_112 - API call for invalid ISBN fails](#tc_112)
  - [TC_120 - Clicking on a book returns more info](#tc_120)
  - [TC_121 - API call for a specific book](#tc_121)
- [User Story 2: User Account Features](#user-story-2-user-account-features)
  - [TC_200 - Signup creates user](#tc_200)
  - [TC_210 - Login gives token](#tc_210)
  - [TC_211 - Authorization returns true](#tc_211)
  - [TC_230 - Add book with valid ISBN](#tc_230)
  - [TC_231 - Invalid ISBN fails](#tc_231)
  - [TC_232 - Duplicate ISBN ignored](#tc_232)
  - [TC_233 - Delete specific book](#tc_233)
  - [TC_234 - Delete all books](#tc_234)

---

## User Story 1: Guest Access

### TC_110 - Typing full book title shows correct result

- **Precondition:** User is on the [bookstore page](https://demoqa.com/books)
- **Steps:**
  1. Type the full name of a book (e.g., “Git Pocket Guide”) in the search bar
- **Expected Result:** Only that book is shown in the results

---

### TC_111 - Typing partial match returns filtered result

- **Precondition:** User is on the bookstore page
- **Steps:**
  1. Type a partial book name like “Java” in the search bar
- **Expected Result:** The book list filters dynamically to show all matches with “Java” in the title

---

### TC_112 - Typing partial match returns filtered result ###############################################################################################

- **Precondition:** User is on the bookstore page
- **Steps:**
  1. Type a partial book name like “Java” in the search bar
- **Expected Result:** The book list filters dynamically to show all matches with “Java” in the title

---

### TC_120 - Clicking on a book returns more info

- **Precondition:** User is on [https://demoqa.com/books](https://demoqa.com/books)
- **Steps:**
  1. Scroll through the book list or search for a title
  2. Click on a specific book title (e.g. “Git Pocket Guide”)
- **Expected Result:** User is navigated to a new page displaying book details (title, author, ISBN, publisher, etc.)

---

### TC_121 - API call for a specific book

- **Precondition:** A valid ISBN is known (e.g., `9781449325862`)
- **Steps:**
  1. Send a `GET` request to `https://demoqa.com/BookStore/v1/Book?ISBN=9781449325862`
- **Expected Result:** Server responds with `200 OK` and a JSON object containing book details

---

## User Story 2: User Account Features

### TC_200 - Signup creates user

- **Precondition:** User is not already registered
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/Account/v1/User`  
     Body:
     ```json
     {
       "userName": "test_user_123",
       "password": "ValidPass123!"
     }
     ```
- **Expected Result:** Response `201 Created`, and user is created with a unique `userId`

---

### TC_210 - Login gives token

- **Precondition:** User is registered
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/Account/v1/GenerateToken`  
     Body:
     ```json
     {
       "userName": "test_user_123",
       "password": "ValidPass123!"
     }
     ```
- **Expected Result:** Response `200 OK` with a `token` and `status: Success`

---

### TC_211 - Authorization returns true

- **Precondition:** Token is generated using valid user credentials
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/Account/v1/Authorized`  
     Body:
     ```json
     {
       "userName": "test_user_123",
       "password": "ValidPass123!"
     }
     ```
- **Expected Result:** Response `200 OK`, body contains `true`

---

### TC_230 - Add book with valid ISBN

- **Precondition:** User is logged in and has a valid token + userId
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/BookStore/v1/Books`  
     Headers: `Authorization: Bearer <token>`  
     Body:
     ```json
     {
       "userId": "<userId>",
       "collectionOfIsbns": [{ "isbn": "9781449325862" }]
     }
     ```
- **Expected Result:** Response `200 OK`, and the book is added to the user’s collection

---

### TC_231 - Invalid ISBN fails

- **Precondition:** User is logged in and has a valid token + userId
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/BookStore/v1/Books`  
     Headers: `Authorization: Bearer <token>`  
     Body:
     ```json
     {
       "userId": "<userId>",
       "collectionOfIsbns": [{ "isbn": "invalid-isbn-000" }]
     }
     ```
- **Expected Result:** Server returns error (`400 Bad Request`) and no book is added

---

### TC_232 - Duplicate ISBN ignored

- **Precondition:** Book with ISBN `9781449325862` already exists in user's collection
- **Steps:**
  1. Attempt to add the same ISBN again with a `POST` request to `/BookStore/v1/Books`
- **Expected Result:** Server responds with an error or no duplicate is added

---

### TC_233 - Delete specific book

- **Precondition:** Book exists in the user’s collection
- **Steps:**
  1. Send a `DELETE` request to `https://demoqa.com/BookStore/v1/Book`  
     Headers: `Authorization: Bearer <token>`  
     Body:
     ```json
     {
       "isbn": "9781449325862",
       "userId": "<userId>"
     }
     ```
- **Expected Result:** Book is removed and response is `204 No Content`

---

### TC_234 - Delete all books

- **Precondition:** User has books in their collection
- **Steps:**
  1. Send a `DELETE` request to `https://demoqa.com/BookStore/v1/Books`  
     Headers: `Authorization: Bearer <token>`  
     Body:
     ```json
     {
       "userId": "<userId>"
     }
     ```
- **Expected Result:** User's collection is cleared and server responds with `204 No Content`
