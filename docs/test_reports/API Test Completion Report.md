# API Functional Test Report – Bookstore

## 1. Test Notes
This report will be different from usual test report, since the focus is on creating test scripts, passing the tests matter less, however there are other things worth to discuss 

## 2. Test Environment  
- OS: Windows 10  
- Python version: 3.12  
- API base URL: https://demoqa.com  
- Tools: `requests` library for HTTP requests, pytest for test automation

## 3. Test Dates  
- Start Date: 2025-06-20  
- End Date: 2025-06-20

## 4. Test Objectives  
- Validate token generation for valid and invalid users  
- Verify user creation and retrieval of user ID  
- Test adding a book to the user's collection  
- Test deletion of all books from the user's collection

## 5. Tested Features  
- `POST /Account/v1/GenerateToken`  
- `POST /Account/v1/User`  
- `POST /BookStore/v1/Books`  
- `DELETE /BookStore/v1/Books`

## 6. Test Scripts Working
| Test Case ID | Description                                                      | Status  | Remarks                     	   |
|--------------|------------------------------------------------------------------|---------|--------------------------------------|
| TC_112       | searching for a book (invalid ISBN)                              | Passed  | Token returned successfully          |
| TC_121       | searching for a book (invalid ISBN)  		                  | Passed  | Error message received               |
| TC_221       | Generate Auth Token (valid username or password)                 | Passed  | User created with userID             |
| TC_222       | Generate Auth Token (invalid username or password)               | Passed  | User created with userID  	   |
| TC_230       | Add book to booklist 				        	  | Failed  | Check out B220 and B230 for more info|
| TC_231       | Add multiple books to booklist   			          | Failed  | Check out B220 and B230 for more info|
| TC_232       | Add invalid book to booklist  					  | Failed  | Check out B220 and B230 for more info|
| TC_233       | Add duplicate book to booklist 				  | Failed  | Check out B220 and B230 for more info|

## 7. Test Results  
- All token generation and user creation endpoints returned expected results.  
- Book searching endpoint works as expected.
- Book addition endpoint worked correctly using valid token and user ID. However, Bug B220 makes the script unable to test consistently
- Deletion of books failed due to API returning unauthorized error on user ID validation. Furthermore makes TC230-233 impossible to test. 

## 8. Recommendations  
- Investigate and fix user ID validation on book deletion endpoint.  
- Enhance API to return user ID on token validation or provide dedicated user info endpoint.

## 9. Conclusion  
The core functionalities of user authentication and book addition are working as expected. However, issues with user ID retrieval and book deletion require resolution before full test automation can be implemented.\
For now you can workaround the problem by signing in and out and manually deleting the booklist through the site, however full automation is currently impossible.

## 10. Appendix  
- Test data:  
  - Valid username: `validusername123`  
  - Valid password: `Validpassword123!`  
  - User ID used: `c200d043-997c-4e94-99cd-2038a80a6f16`  
  - Valid ISBNs: `9781449325862`, `9781449331818`

Can be also found in testware/test data.md


- References:  
  - [Bookstore API Swagger Documentation](https://demoqa.com/swagger/)
