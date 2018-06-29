To use the application you need [python](https://www.python.org/downloads/). Besides python itself you need [pip](https://packaging.python.org/key_projects/#pip) which allows you to manage libraries (you should probably upgrade pip by using `pip install --upgrade pip`). While running the app you should also use virtual environment [venv](https://docs.python.org/3/tutorial/venv.html). For databases the application uses postgreSQL](https://www.postgresql.org/).

Start by creating a virtual environment:
* `python3 -m venv venv`

Activate said virtual environment:
* `source venv/bin/activate`

Afer this download all the dependencies for the application:
* `pip install Flask`
* `pip install flask-sqlalchemy`
* `pip install flask-wtf`
* `pip install flask-login` 
* `pip install psycopg2`

Once you've downloaded all the depencies run the application:
* `python run.py`
