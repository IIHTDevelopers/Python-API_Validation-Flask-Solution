### Scenario
`app.py` exposes `/status` (GET) and `/submit` (POST). Missing or invalid parameters lead to **500 Internal Server Error**.

### Objective
Add **input validation** and friendly error responses (`400 Bad Request`) so the API never throws unhandled exceptions.

**To execute the code **

run the command pip install flask

the after the user has writtern the correct code in the app.py

you need to run the command

python3 -m unittest
