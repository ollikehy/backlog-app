**Sovelluksen käyttötapauksia:**

- [x] Kirjautuminen

    `SELECT user.username user.password FROM user`
- [x] Backlogin selaaminen

    `SELECT * FROM videogame`
- [x] Pelin lisääminen sovellukseen

    `INSERT INTO videogame(name, releaseyear, genre, developer_id) VALUES (?, ?, ?, ?)`
- [x] Pelin lisääminen käyttäjän listaan

    `INSERT INTO gameinstance(account_id, game_id, completed) VALUES (?, ? ,?)`
- [x] Kehittäjän lisääminen sovellukseen

    `INSERT INTO developer(name, country) VALUES (?, ?)`

**Tullaan lisäämään tulevaisuudessa:**
- [ ] Pelin statuksen muuttaminen suoritetuksi
- [ ] Pelien lajittelu julkaisuvuoden tai nimen perusteella
- [ ] Lisää ulkoasun tyylittelyä

**Omat kokemukset:**

Sovelluksen kehittäminen oli mielenkiintoinen prosessi, vaikka web-sovelluksia onkin jo jonkin verran tullut rakenneltua. Eniten kiinnosti pythonilla koodaaminen ja flask-frameworkin käyttöönotto. Mielikuvat pythonista ennen kurssia olivat aliarvioivat, kun taas kieli itsessään on hyvinkin monikäyttöinen ja tehokas työkalu.
Tietokantojen kanssa työskentely oli myös hyvää kertausta tietokantojenperusteet-kurssille, jonka suorituksesta on aikaa jo lähes 1,5 vuotta!
