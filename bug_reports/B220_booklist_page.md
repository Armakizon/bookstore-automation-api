# Bug Report: Changing the booklist disable access to booklist

## Environment
- **Tested with:** Firefox, Google Chrome
- **Date:** 2025-06-20

##URL the error occurs in
https://demoqa.com/profile

##Prerequisites

Be logged in
TC_230.py 

## Steps to Reproduce
1. Open: "https://demoqa.com/profile"
2. Open TC_230.py in IDLE
3. Press F5 (running the script)
4. Go back to "https://demoqa.com/profile"
5. Press F5 (refreshing the page)

## Expected Result
User should see the updated booklist with the new book

## Actual Result
The user is directed to an empty page

## Workarounds
- Logging out and logging in fixes the bug and let you see the modified booklist 

## Priority
High