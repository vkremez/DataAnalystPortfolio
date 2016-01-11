# Coded by Vitali
import urllib
import sqlite3

u = urllib.urlopen('http://www.cybercrime-tracker.net/all.php')
data = u.read().split('/>')
rdata = ' '.join(data).replace('<br ','').split()

conn = sqlite3.connect('hosts.sqlite')
cur = conn.cursor()
conn.text_factory = str
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Hosts;
CREATE TABLE Hosts (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')

for name in rdata:
    print name

    cur.execute('''INSERT OR IGNORE INTO Hosts (name) VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM Hosts WHERE name = ? ', ( name, ))

conn.commit()
