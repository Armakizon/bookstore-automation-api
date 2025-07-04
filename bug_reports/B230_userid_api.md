# Bug Report: Unable to Retrieve User Data JSON from API

## Environment
- **API Base URL:** https://demoqa.com  
- **Endpoint:** `/Account/v1/User` (GET)  
- **Authentication:** Bearer token generated via `/Account/v1/GenerateToken`  
- **Tested with:** Python requests, curl 
- **Date:** 2025-06-20

## Description
When making an authenticated GET request to the `/Account/v1/User` endpoint with a valid Bearer token, the server responds with an HTML page instead of the expected JSON user data. This prevents programmatic retrieval and parsing of the user's information.

## Steps to Reproduce
1. Generate a valid token using `/Account/v1/GenerateToken` with valid credentials.  
2. Send a GET request to `/Account/v1/User` with header `Authorization: Bearer <token>` and `Accept: application/json`.  

## Expected Result
A JSON object containing user details (such as userId, username, etc.) should be returned.

## Actual Result
The server returns an HTML webpage, making it impossible to parse the user information programmatically.

## Workarounds
- The `POST /Account/v1/User` (user creation) endpoint returns `userID` in its JSON response, which can be used as a workaround.  
- Attempts to retrieve user data via `/Account/v1/User/{username}` result in a 401 error with message "User not found!".

## Priority
Medium