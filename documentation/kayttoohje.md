Sovelluksen käyttämiseen tarvitaan (pythonia)[https://www.python.org/downloads/], lisäksi tarvitset myös (pip:in)[https://packaging.python.org/key_projects/#pip] minkä avulla voit ladata apukirjastoja (kannattaa päivittää pip käyttämällä komentoa `pip install --upgrade pip`. Sovellusta asentaessa kannattanee käyttää virtuaaliympäristöä (venv)[https://docs.python.org/3/tutorial/venv.html]. Sovelluksen tietokantahallintaan käytetään (postgreSQL)[https://www.postgresql.org/]-järjestelmää.

Aloita luomalla virtuaaliympäristö venv:iä käyttäen:
`python3 -m venv venv`

Seuraavaksi aktivoidaan virtuaaliympäristö:
`source venv/bin/activate`

Tämän jälkeen ladataan riippuvuudet:
`pip install Flask`
`pip install flask-sqlalchemy`
`pip install flask-wtf`
`pip install flask-login` 
`pip install psycopg2`

Kun olet asentanut riippuvuudet voit käynnistää sovelluksen komennolla `python run.py`