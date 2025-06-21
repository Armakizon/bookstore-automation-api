# API Functional Test Report – Bookstore

## 1. Test Notes
This report will be different from usual test report, since the focus is on creating test scripts, passing the tests matter less, however there are other things worth to discuss 

## 2. Test Environment  
- OS: Windows 10  
- Python version: 3.12  
- API base URL: https://demoqa.com  
- Tools: pytest and selenium for test automation

## 3. Test Dates  
- Start Date: 2025-06-20  
- End Date: 2025-06-20

## 4. Test Objectives  
- Validate basic user actions like logging in and searching for books  

## 5. Tested Features  
- `POST /Account/v1/GenerateToken`  
- `POST /Account/v1/User`  
- `POST /BookStore/v1/Books`  
- `DELETE /BookStore/v1/Books`

## 6. Test Scripts Working
| Test Case ID | Description                                                      | Status  | Remarks                     	  				     |
|--------------|------------------------------------------------------------------|---------|------------------------------------------------------------------------|
| TC_110       | Searching for a book (full title)                                | Passed  |          			 					     |
| TC_111       | Searching for a book (partial match)  		                  | Passed  |              		 					     |
| TC_120       | Clicking on a book gives more info       		          | Failed  | Check out B120 for info  	       				             |
| TC_220       | Logging in (valid account)          			          | Passed  | Depends on the device the add on the site might block the login button |
| TC_223       | Logging in (invalid account)			        	  | Passed  | Depends on the device the add on the site might block the login button |

## 7. Test Results  
- Searching for books works as intended
- Clicking on book for more info direct the user into a blank page, B120 bug report was made for more information, script cannot automate until bug is fixed.

## 8. Recommendations  
- None

## 9. Conclusion  
Most core functionalities work, however there are some bugs and some tests cannot be automated (account creating becuause of the captcha).

## 10. Appendix  
- Test data:  
  - Valid username: `validusername123`  
  - Valid password: `Validpassword123!`  
  - User ID used: `c200d043-997c-4e94-99cd-2038a80a6f16`  
  - Valid ISBNs: `9781449325862`, `9781449331818`
Can be also found in testware/test data.md

- References:  
  - [Bookstore API Swagger Documentation](https://demoqa.com/swagger/)
