# TV Show API

This API provides endpoints for managing users, favorite shows, and watchlists for a TV show application.

## Table of Contents
1. [Setup Instructions](#setup-instructions)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
   - [User Management](#user-management)
   - [Favorites Management](#favorites-management)
   - [Watchlist Management](#watchlist-management)
   - [User Details](#user-details)
4. [Models](#models)
5. [Error Handling](#error-handling)
6. [Rate Limiting](#rate-limiting)

## Setup Instructions

1. Clone the repository:
2. Install the required dependencies:
3. Set up the database:
4. Run the application:
The API will be available at `http://localhost:5000/api`.

## Authentication

This API uses token-based authentication. To authenticate, include the token in the request headers:
## Endpoints

### User Management

#### Register a new user

- **URL:** `/api/register`
- **Method:** `POST`
- **Data Params:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "usertype": "string"
  }
  * **Success Response:**
   * **Code:** 200
   * **Content:** `{ "message": "Login successful", "token": "string" }`
* **Error Response:**
   * **Code:** 200
   * **Content:** `{ "message": "Invalid credentials!" }`

### Get User by ID
* **URL:** `/api/user/<id>`
* **Method:** `GET`
* **Success Response:**
   * **Code:** 200
   * **Content:**
   ```json
   { 
     "id": "integer", 
     "username": "string", 
     "email": "string", 
     "usertype": "string", 
     "token": "string" 
   }
   * **Error Response:**
   * **Code:** 200
   * **Content:** `{ "message": "User not found!" }`

### Delete User by ID
* **URL:** `/api/user/<id>`
* **Method:** `DELETE`
* **Success Response:**
   * **Code:** 200
   * **Content:** `{ "message": "User <id> deleted successfully!" }`
* **Error Response:**
   * **Code:** 200
   * **Content:** `{ "message": "User not found!" }`

### Delete User by Email
* **URL:** `/api/user/delete`
* **Method:** `DELETE`
* **Data Params:**
    ```json
    { 
        "email": "string" 
    }

* **Success Response:**
   * **Code:** 200
   * **Content:** `{ "message": "User with email <email> deleted successfully!" }`
* **Error Response:**
   * **Code:** 200
   * **Content:** `{ "message": "User not found!" }`

### Get All Users
* **URL:** `/api/users`
* **Method:** `GET`
* **Success Response:**
   * **Code:** 200
   * **Content:** Array of user objects

## Favorites Management

### Add Favorite Show
* **URL:** `/api/favourites`
* **Method:** `POST`
* **Data Params:**
    ```json
    { "useremail": "string", "showid": "integer", "addeddate": "datetime", "status": "string"
    }
* **Success Response:**
   * **Code:** 200
   * **Content:** `{ "message": "Show added to favourites!" }`

## Watchlist Management

### Add to Watchlist
* **URL:** `/api/watchlist`
* **Method:** `POST`
* **Data Params:**
    ```json
    {
        "useremail": "string", "showid": "integer",          "addeddate": "datetime", "status": "string"
    }
* **Success Response:**
   * **Code:** 200
   * **Content:** `{ "message": "Show added to watchlist!" }`

## User Details

### Get User Details
* **URL:** `/api/userdetails/<id>`
* **Method:** `GET`
* **Success Response:**
   * **Code:** 200
   * **Content:** `{ "bio": "string" }`
* **Error Response:**
   * **Code:** 200
   * **Content:** `{ "message": "User details not found!" }`

## Models

### User
* id: Integer (Primary Key)
* username: String (Unique, Not Null)
* email: String (Unique, Not Null)
* password: String (Not Null)
* usertype: String (Not Null)
* token: String (Unique)

### FavouriteShow
* id: Integer (Primary Key)
* useremail: String (Foreign Key to User.email, Not Null)
* showid: Integer (Not Null)
* addeddate: DateTime (Not Null)
* status: String (Not Null)

### WatchList
* id: Integer (Primary Key)
* useremail: String (Foreign Key to User.email, Not Null)
* showid: Integer (Not Null)
* addeddate: DateTime (Not Null)
* status: String (Not Null)

### UserDetails
* id: Integer (Primary Key)
* user_id: Integer (Foreign Key to User.id, Not Null)
* bio: Text (Nullable)

## Error Handling

The API returns JSON responses for errors. Most endpoints return a "message" field with a description of the error.

## Rate Limiting

Currently, there are no rate limiting restrictions implemented for this API.

