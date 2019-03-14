**Use cases for the application:**

- [x] Logging in

    `SELECT user.username user.password FROM user WHERE user.username = 'username'`
- [x] Browsing the backlog

    `SELECT * FROM videogame`
- [x] Adding a game to the app

    `INSERT INTO videogame(name, releaseyear, genre, developer_id) VALUES (?, ?, ?, ?)`
- [x] Adding a game to an users list

    `INSERT INTO gameinstance(account_id, game_id, completed) VALUES (?, ? ,?)`
- [x] Adding a developer to the app

    `INSERT INTO developer(name, country) VALUES (?, ?)`

**TODO:**
- [ ] Changing game status to completed
- [ ] Sorting games by releaseyear or alphabetically
- [ ] Styling of the app

**Own experiences:**

Developing the application was an interesting process, even though I've done some web-applications in the past. Eniten kiinnosti pythonilla koodaaminen ja flask-frameworkin käyttöönotto. The things that were most interesting were coding with python and using the flask-framwork. Before this course I undervalued python as a language and I now realize how flexible and powerful of a tool it can be. 
Working with databases was also refreshing since it was almost 1,5 years since I did anything meaningful with them in the Tietokantojen-perusteet course.

- Olli 10.5.2018