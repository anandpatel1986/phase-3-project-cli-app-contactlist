# phase-3-project-cli-app-contactlist

Welcome to Contact Storage App !!!

## Description

This is a CLI ( Command Line Interface) application for storing contact details. It is like Digital directory. User can SignUp, Login from home page. After every signup user details will be saved in database. After Login user can add new contact, search contact, edit contact and delete contacts from database.
Various packages are used to built this app like sqlalchemy, alembic, faker, maskpass, prettycli, simple-term-menu etc.

## Installation & Usage

In order to access this project, please fork your own version in the top right of the GitHub Repository. Once you've forked a copy, please clone the repository to your own directory.

After cloning, navigate into the folder and run :

```bash
pipenv install && pipenv shell
```

This will create virtual environment and install required dependencies.

For seeding sample data in database change directory by :

```bash
cd lib/db
```

and to seeding sample data run :

```bash
python seeds.py
```

To run app change directory to lib/ (you can this by just typing cd .. in terminal) and run :

```bash
python cli.py
```

## Visuals

You find video walkthrough on youtube:

[link: Contact Storage App](https://youtu.be/i0Zm66BE3M4)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Roadmap

More features can be added in future like User can send email to saved contacts, additional attributes (contact details) can be added and more contraints, validation can be added for email id, phone, username etc- user can input details in specific formate only.

## License

MIT License

Copyright (c) 2023 anandpatel1986

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
