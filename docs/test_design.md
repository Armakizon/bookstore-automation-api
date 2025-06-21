# Test Design: DemoQA Bookstore Project

## Test Design Techniques

Since there isn't any data or partitions to check, the main technique I will use will be positive and negative testing.


Currently all test cases are also able to be tested through the api

## For tracability test cases will be classified with the following rules:

TC_XYZ

- X is the user story of the test case
- Y is the acceptence criteria of the user story the test case pretaining to
- Z is a unique modifier starting with 0 in case there are multiple test cases made out of the same acceptence criteria

## Positive test cases:

- Clicking on a book returns more info about it
- Typing full book title shows correct result
- Partial match returns filtered results
- Inserting a valid ISBN results in book added to user collection
- Add multiple books in one request

## Negative test cases:

- Signing up with an invalid username or password should give an error and explain why the account wasnt created.
- Signing up with an already used username should give an error saying an account with that name is already made
- Inserting an invalid ISBN results in an error
- Searching for book that does not exist return an empty list
