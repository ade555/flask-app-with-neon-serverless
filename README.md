# Flask App With Neon Serverless Postgres

## Installation
You can install the application by following these steps

### Step 1: Clone The Github Project
Open your command line too (CLI) and paste this command into it:

```
git clone https://github.com/ade555/flask-app-with-neon-serverless.git
```

### Step 2: Set up Environment Variables
In the root directory, create a file called `.env`.
Next, copy the variable names in the `env_sample` and replace the values with your database url and branched database url from [Neon](https://neon.tech/). 

## Running The Project
You can run the project by typing this command in your CLI:
```
flask --app app run --debug
```

## Endpoint
The project has a single CREATE endpoint.
## Base URL: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Add Book
- **Endpoint**: `/add_book/`
- **HTTP Method**: `POST`
- **Description**: Creates a new book in the database.

| Parameter | Type | Description                      | Required |
|-----------|------|----------------------------------|----------|
| title  | string  | Title of the book to create in the database | Yes |

**Request Body**:

```json
{
    "title": "The Lion King"
}
```

**Responses**:

- `201 Created`: Successfully created a new book in the database.
- `400 Bad Request`: Invalid input or malformed request.
- `500 Internal Server Error`: Unexpected server error.