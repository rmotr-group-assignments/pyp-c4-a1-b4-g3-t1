import pyp_database
from datetime import date

pyp_database.create_database('imdb')
db = pyp_database.use('imdb')

db.create_table('actors', columns=['id', 'name', 'dob'])
# db.actors.insert(1, 'Kevin Bacon' date(1958, 7, 8))
# db.actors.query(name='Kevin Bacon')
