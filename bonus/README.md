# fido-fastapi
# FastAPI Data Backend

This project demonstrates a simple FastAPI backend application for managing transactions. It uses SQLite as the database and includes endpoints for creating, reading, updating, and deleting transactions, as well as fetching user statistics.

## Setup

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


# Install the required dependencies:
pip install -r requirements.txt

# Run the FastAPI application:
uvicorn main:app --host localhost --port 8001


The API will be available at http://localhost:8001.

Endpoints
GET /hello: Test endpoint to check if the API is running.

POST /transactions/: Create a new transaction.

GET /transactions/{user_id}: Fetch all transactions for a specific user.

PUT /transactions/{transaction_id}: Update a transaction.

DELETE /transactions/{transaction_id}: Delete a transaction.

GET /user_stats/{user_id}: Fetch statistics for a specific user.

Usage
Create a new transaction:

Send a POST request to /transactions/ with a JSON payload containing transaction details.

Fetch user transactions:

Send a GET request to /transactions/{user_id} to retrieve all transactions for a specific user.

Update a transaction:

Send a PUT request to /transactions/{transaction_id} with updated transaction details.

Delete a transaction:

Send a DELETE request to /transactions/{transaction_id} to delete a transaction.

Fetch user statistics:

Send a GET request to /user_stats/{user_id} to retrieve statistics for a specific user.


# To build and run the Docker container, follow these steps:

1. Save the Dockerfile in the same directory as your project files.
2. Open a terminal in the same directory.
3. Build the Docker image using the following command:

docker build -t fido-fastapi-bonus .

# Once the image is built, you can run the container:
docker run -p 8001:8001 fido-fastapi-bonus





Contributing
Feel free to contribute to this project by opening issues or pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.






For Fido
