# Baza-podataka-vezba

Kreiran je primer programa koji dodaje podatke u bazu podataka i ispisuje ih.

## Features
Ovaj projekat ima mogucnost dodavanja i ispisivanja podataka u napravljenu tabelu koja sadrzi bazu podataka. 

### Skills
1. ***pytest*** (projekat Pytest)
2. ***funkcije sleep, strftime i localtime iz biblioteke time*** (projekat Kalendar)
3. ***funkcija randint iz biblioteke random*** (projekat Battleship)
4. ***rad sa bazom podataka*** (ovaj projekat)

## Prerequisites
Za ovaj projekat su potrebni `GitHub account`, `IDLE Pyhton` koji je IDE za rad, `SQL Server` i `SQLite Browser`.

## Installation
Projekat se preuzima sa `GitHub-a` ili komandom `git clone https://github.com/davidbujic/Baza-podataka-vezba`. Potrebno je instalirati `SQL Server` pomocu funkcije `$ sudo apt-get install sqlite`, a zatim ga treba ubaciti u fajl `databasetest.py` pomocu komande `import sqlite3`. Baza podataka se nalazi u fajlu `databasetest.db`. Baza podataka je napravljena pomocu `SQLite Browser-a` koji se instalira komandom `sudo apt-get install sqlitebrowser`.

## Running
Projekat se pokrece pokretanjem fajla `databasetest.py` u `IDLE Python-u`.

### Running the Tests
Pokretanje testova se vrsi pokretanjem fajla `databasetest.py` u `Shell-u IDLE Python-a`.

## Versions
1. Osnovna verzija
2. Dodat interaktivni unos u bazu podataka, izmenjen `databasetest.py` fajl, dodat `databasetest.db` fajl i promenjen readme.md fajl.
3. Dodati novi records u fajl `databasetest.db` i dodati detalji vezani za `SQLite Browser` u readme.md fajlu.**DV: Kao sto je trazeno/definisano u Issue1 tacka3.**
4. Dodate nove kolone u bazi podataka koje su vezane za mesto, opstinu i grad, u interaktivni unos `databasetest.py` fajla dodat interaktivni unos za mesto, opstinu i grad i izmenjen readme.md fajl.
5. Dodati detalji u Skills vezani za prethodne projekte.
