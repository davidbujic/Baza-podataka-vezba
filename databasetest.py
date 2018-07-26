import sqlite3

def Main():
    try:
            con = sqlite3.connect('test.db')
            cur = con.cursor()
            cur.execute('CREATE TABLE Korisnici(ID INT, Name TEXT, Surname TEXT, Gender TEXT)')
            cur.execute("INSERT INTO Korisnici VALUES (1, 'David', 'Bujic', 'M')")
            cur.execute("INSERT INTO Korisnici VALUES (2, 'Zeljko', 'Bujic', 'M')")
            cur.execute("INSERT INTO Korisnici VALUES (3, 'Lidija', 'Bujic', 'F')")
            con.commit()
            cur.execute("SELECT * FROM Korisnici")
            data = cur.fetchall()
            for row in data:
                print row
    except sqlite3.Error, e:
            if con:
                con.rollback()
                print "Problem sa SQL."
    finally:
            if con:
                con.close()
Main()
