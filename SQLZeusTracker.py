#!/usr/bin/env python
# Coded by Vitali
import urllib
import sqlite3

u = urllib.urlopen('https://zeustracker.abuse.ch/monitor.php?filter=all')
data = u.read().split()
host = []
for line in data:
	if line.startswith('href="/monitor.php?host='):
		host.append(line.split('href="/monitor.php?host=')[1])
		host = ' '.join(host).replace('"','').split()

conn = sqlite3.connect('zeustrackerhost.sqlite')
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

for name in host:
    print name

    cur.execute('''INSERT OR IGNORE INTO Hosts (name) VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM Hosts WHERE name = ? ', ( name, ))

conn.commit()
