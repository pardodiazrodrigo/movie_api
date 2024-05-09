# MOVIE API

Welcome to Movie API! This API allows you to manage movie information, including details such as title, director, release year, and genre.

## Requirements

- Python 3.7 or higher
- Pip (Python package manager)

## Installation

1. Clone this repository to your local machine:
   git clone [https://github.com/pardodiazrodrigo/movie-api.git](https://github.com/pardodiazrodrigo/movie_api)
2. Navigate to the project directory:
   cd movie-api
3. Install project dependencies using pip:
   pip install -r requirements.txt

## Configuration

Create a .env file in the project root directory and define the following environment variables:
TEST_DATABASE_URL=postgresql
DATABASE_URL=postgresql
SECRET_KEY={secret_key}
ALGORITHM=HS256

## Usage

1. Start the development server:
   uvicorn main:app --reload
2. Access the API documentation in your web browser:
   http://localhost:8000/docs

Here you'll find an interactive interface where you can test all available API routes along with their parameters and response examples.

## Authentication

To access certain endpoints that involve creating, updating, or deleting a movie, your role must be admin. To view all movies or details of a specific movie, your role must be user.

## Available Routes
### GET /movies
Retrieve a list of all movies in the database.
### GET /movies/{movie_id}
Retrieve details of a specific movie based on its ID.
### POST /movies
Create a new movie in the database.
### Request Parameters:
- title (string): The title of the movie.
- director (string): The director of the movie.
- release_year (integer): The release year of the movie.
- genre (string): The genre of the movie..
### PUT /movies/{movie_id}
Update details of an existing movie based on its ID.
### DELETE /movies/{movie_id}
Delete a specific movie based on its ID.

### Contribution
Contributions are welcome! If you find any bugs or have any improvements, please open an issue or send a pull request.

