import sqlite3
conn = sqlite3.connect('databasetest.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM korisnici'):
    print row
ime = raw_input("Unesite Vase ime: ")
prezime = raw_input("Unesite Vase prezime: ")
pol = raw_input("Unesite Vas pol:  M za muski pol, F za zenski pol.")
starost = raw_input("Unesite Vas broj godina: ")
sql = ("INSERT INTO korisnici VALUES('%s', '%s', '%s', '%d')") % \
                  (ime, prezime, pol, int(starost))
number_of_rows = c.execute(sql)
conn.commit()
for row in c.execute('SELECT * FROM korisnici'):
    print row
conn.close()
