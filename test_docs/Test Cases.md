# DemoQA Bookstore - Automated Test Suite

## Table of Contents

- [User Story 1: Guest Access](#user-story-1-guest-access)
  - [TC_110 - Typing full book title shows correct result](#tc_110---typing-full-book-title-shows-correct-result)
  - [TC_111 - Typing partial match returns filtered result](#tc_111---typing-partial-match-returns-filtered-result)
  - [TC_112 - API call for invalid ISBN fails](#tc_112---api-call-searching-for-a-book-with-an-invalid-isbn)
  - [TC_120 - Clicking on a book returns more info](#tc_120---clicking-on-a-book-returns-more-info)
  - [TC_121 - API call for a specific book](#tc_121---api-call-for-a-specific-book)
- [User Story 2: User Account Features](#user-story-2-user-account-features)
  - [TC_210 - Signing up with an invalid username or password](#tc_210---signing-up-with-an-invalid-username-or-password)
  - [TC_211 - Signing up with an already used username](#tc_211---signing-up-with-an-already-used-username)
  - [TC_220 - Logging with a valid username and password](#tc_220---logging-with-a-valid-username-and-password)
  - [TC_221 - API call with a valid username and password](#tc_221---api-call-with-valid-username-and-password)
  - [TC_222 - API call with an invalid username or password](#tc_222---api-call-with-invalid-username-and-password)
  - [TC_223 - Logging in with an invalid username and password](#tc_223---logging-with-an-invalid-username-and-password)
  - [TC_230 - API call with a valid ISBN can add a book to the booklist](#tc_230---api-call-with-a-valid-isbn-can-add-a-book-to-the-booklist)
  - [TC_231 - API call adding multiple books to the booklist](#tc_231---api-call-adding-multiple-books-to-the-booklist)
  - [TC_232 - API call with a invalid ISBN trying to add a book to the booklist](#tc_232---api-call-with-a-invalid-isbn-trying-to-add-a-book-to-the-booklist)
  - [TC_233 - Duplicate ISBN ignored](#tc_233---duplicate-isbn-ignored)
---

## User Story 1: Guest Access

### TC_110 - Typing full book title shows correct result

- **Precondition:** None
- **Steps:**
  1. to to [bookstore page](https://demoqa.com/books)
  2. Type the full name of a book (e.g., “Git Pocket Guide”) in the search bar
- **Expected Result:** Only that book is shown in the results

---

### TC_111 - Typing partial match returns filtered result

- **Precondition:** None
- **Steps:**
  1. to to [bookstore page](https://demoqa.com/books)
  2. Type a partial book name like “Java” in the search bar
- **Expected Result:** The book list filters dynamically to show all matches with “Java” in the title

---

### TC_112 - API call searching for a book with an invalid ISBN

- **Precondition:** Choose an invalid ISBN (e.g. '1234567')
- **Steps:**
  1. Send a `GET` request to `https://demoqa.com/BookStore/v1/Book?ISBN=1234567`
- **Expected Result:** Server responds with `400 Not Found`

---

### TC_120 - Clicking on a book returns more info

- **Precondition:** None
- **Steps:**
  1. to to [bookstore page](https://demoqa.com/books)
  2. Scroll through the book list or search for a title
  3. Click on a specific book title (e.g. “Git Pocket Guide”)
- **Expected Result:** User is navigated to a new page displaying book details (title, author, ISBN, publisher, etc.)

---

### TC_121 - API call for a specific book

- **Precondition:** A valid ISBN (e.g., `9781449325862`)
- **Steps:**
  1. Send a `GET` request to `https://demoqa.com/BookStore/v1/Book?ISBN=9781449325862`
- **Expected Result:** Server responds with `200 OK` and a JSON object containing book details

---

## User Story 2: User Account Features

### TC_210 - Signing up with an invalid username or password

- **Precondition:** User has invalid password, and isn't logged in  
- **Steps:**
  1. Go to the [bookstore login page](https://demoqa.com/login)
  2. Press on the "Signup" Button at the bottom right
  3. Enter an invalid password into the signup form, for example:  
       Username: "Invaliduser"
       Password: "Invaliduser"
  4. Fill the first name last name and solve the captcha
  5. Click the "Register" button  
- **Expected Result:**  
  An error message is displayed such as "Invalid username or password", and the user remains on the login page

---

### TC_211 - Signing up with an already used username

- **Precondition:** User has a taken username, and isn't logged in  
- **Steps:**
  1. Go to the [bookstore login page](https://demoqa.com/login)
  2. Press on the "Signup" Button at the bottom right
  3. Enter a used username into the Sign-up form, for example:  
       Username: "User1"
       Password: "Invaliduser123"
  4. Fill the first name last name and solve the captcha
  5. Click the "Register" button 
- **Expected Result:**  
  An error message is displayed such as "Username is already in use", and the user remains on the login page

---

### TC_220 - Logging with a valid username and password

- **Precondition:** User has a valid username and password and isn't logged in  
- **Steps:**
  1. Go to the [bookstore login page](https://demoqa.com/login)
  2. Enter a valid username and password  
       Username: "validusername123"
       Password: "Validpassword123!"
  3. Click the "Login" button 
- **Expected Result:**  
  The user is successfully logged in and redirected to their profile page

---

### TC_221 - API call with valid username and password

- **Precondition:** None
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/Account/v1/GenerateToken`  
     Body:
     ```json
     {
       "userName": "validusername123",
       "password": "Validpassword123!"
     }
     ```
- **Expected Result:** Response `200 OK` with a `token` and `status: Success`

### TC_222 -  API call with invalid username and password

- **Precondition:** None
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/Account/v1/GenerateToken`  
     Body:
     ```json
     {
       "userName": "Invaliduser",
       "password": "Invaliduser"
     }
     ```
- **Expected Result:** Server returns error (`400 Bad Request`) and no token returned

### TC_223 - Logging with an invalid username and password

- **Precondition:** User has an invalid username and password and isn't logged in  
- **Steps:**
  1. Go to the [bookstore login page](https://demoqa.com/login)
  2. Enter the username and password  
       Username: "Invaliduser"
       Password: "Invaliduser"
  3. Click the "Login" button 
- **Expected Result:**  
  Getting sent back to the login page with an error message

### TC_230 - API call with a valid ISBN can add a book to the booklist

- **Precondition:** User has valid token, userId and valid ISBN
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


### TC_231 - API call adding multiple books to the booklist

- **Precondition:** User has valid token, userId and valid ISBNs
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/BookStore/v1/Books`  
     Headers: `Authorization: Bearer <token>`  
     Body:
     ```json
     {
       "userId": "<userId>",
       "collectionOfIsbns": [{ "isbn": "9781449325862" },{ "isbn": "9781449331818" }]
     }
     ```
- **Expected Result:** Response `200 OK`, and the books are added to the user’s collection

### TC_232 - API call with a invalid ISBN trying to add a book to the booklist

- **Precondition:** User has valid token, userId and invalid ISBN
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/BookStore/v1/Books`  
     Headers: `Authorization: Bearer <token>`  
     Body:
     ```json
     {
       "userId": "<userId>",
       "collectionOfIsbns": [{ "isbn": "123456" }]
     }
     ```
- **Expected Result:** Response `400 Not found`, and the booklist is unchanged

### TC_233 - Duplicate ISBN ignored

- **Precondition:** User has valid token, userId and valid ISBN that was already added to the booklist (e.g. 9781449331818)
- **Steps:**
  1. Send a `POST` request to `https://demoqa.com/BookStore/v1/Books`  
     Headers: `Authorization: Bearer <token>`  
     Body:
     ```json
     {
       "userId": "<userId>",
       "collectionOfIsbns": [{ "isbn": "123456" }]
     }
     ```
- **Expected Result:** Server returns error (`400 Bad Request`) and no book is added
---