Sovelluksen käyttötapauksia:

- [x] Kirjautuminen
- [x] Backlogin selaaminen

    `SELECT * FROM videogame`
- [x] Pelin lisääminen sovellukseen

    `INSERT INTO videogame(name, releaseyear, genre, developer_id) VALUES (?, ?, ?, ?)`
- [x] Pelin lisääminen käyttäjän listaan

    `INSERT INTO gameinstance(account_id, game_id, completed) VALUES (?, ? ,?)`
- [x] Kehittäjän lisääminen sovellukseen

    `INSERT INTO developer(name, country) VALUES (?, ?)`

Tullaan lisäämään tulevaisuudessa:
- [ ] Pelin statuksen muuttaminen suoritetuksi
- [ ] Pelien lajittelu julkaisuvuoden tai nimen perusteella
- [ ] Lisää ulkoasun tyylittelyä
