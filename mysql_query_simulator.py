import random
import os

sql_queries = ['SELECT COUNT(*) FROM city;', 'SELECT COUNT(*) FROM country;', 'SELECT COUNT(*) FROM countrylanguage;', 'DESC city;', 'DESC country;',
               'DESC countrylanguage;', 'SELECT * FROM city;', 'SELECT * FROM country;', 'SELECT * FROM countrylanguage;', 'SELECT * FROM city WHERE Name LIKE \'A%\';',
               'SELECT * FROM city WHERE Name LIKE \'B%\';', 'SELECT * FROM city WHERE Name LIKE \'C%\';', 'SELECT * FROM city WHERE Name LIKE \'D%\';',
               'SELECT * FROM city WHERE Name LIKE \'E%\';', 'SELECT * FROM city WHERE Name LIKE \'F%\';', 'SELECT * FROM city WHERE Name LIKE \'G%\';',
               'SELECT * FROM city WHERE Name LIKE \'H%\';', 'SELECT * FROM city WHERE Name LIKE \'I%\';', 'SELECT * FROM city WHERE Name LIKE \'J%\';',
               'SELECT * FROM city WHERE Name LIKE \'K%\';', 'SELECT * FROM city WHERE Name LIKE \'L%\';', 'SELECT * FROM city WHERE Name LIKE \'M%\';',
               'SELECT * FROM city WHERE Name LIKE \'N%\';', 'SELECT * FROM city WHERE Name LIKE \'O%\';', 'SELECT * FROM city WHERE Name LIKE \'P%\';',
               'SELECT * FROM city WHERE Name LIKE \'Q%\';', 'SELECT * FROM city WHERE Name LIKE \'R%\';', 'SELECT * FROM city WHERE Name LIKE \'S%\';',
               'SELECT * FROM city WHERE Name LIKE \'T%\';', 'SELECT * FROM city WHERE Name LIKE \'U%\';', 'SELECT * FROM city WHERE Name LIKE \'V%\';',
               'SELECT * FROM city WHERE Name LIKE \'W%\';', 'SELECT * FROM city WHERE Name LIKE \'X%\';', 'SELECT * FROM city WHERE Name LIKE \'Y%\';',
               'SELECT * FROM city WHERE Name LIKE \'Z%\';', 'SELECT * FROM country WHERE Name LIKE \'A%\';', 'SELECT * FROM country WHERE Name LIKE \'B%\';',
               'SELECT * FROM country WHERE Name LIKE \'C%\';', 'SELECT * FROM country WHERE Name LIKE \'D%\';', 'SELECT * FROM country WHERE Name LIKE \'E%\';',
               'SELECT * FROM country WHERE Name LIKE \'F%\';', 'SELECT * FROM country WHERE Name LIKE \'G%\';', 'SELECT * FROM country WHERE Name LIKE \'H%\';',
               'SELECT * FROM country WHERE Name LIKE \'I%\';', 'SELECT * FROM country WHERE Name LIKE \'J%\';', 'SELECT * FROM country WHERE Name LIKE \'K%\';',
               'SELECT * FROM country WHERE Name LIKE \'L%\';', 'SELECT * FROM country WHERE Name LIKE \'M%\';', 'SELECT * FROM country WHERE Name LIKE \'N%\';',
               'SELECT * FROM country WHERE Name LIKE \'O%\';', 'SELECT * FROM country WHERE Name LIKE \'P%\';', 'SELECT * FROM country WHERE Name LIKE \'Q%\';',
               'SELECT * FROM country WHERE Name LIKE \'R%\';', 'SELECT * FROM country WHERE Name LIKE \'S%\';', 'SELECT * FROM country WHERE Name LIKE \'T%\';',
               'SELECT * FROM country WHERE Name LIKE \'U%\';', 'SELECT * FROM country WHERE Name LIKE \'V%\';', 'SELECT * FROM country WHERE Name LIKE \'W%\';',
               'SELECT * FROM country WHERE Name LIKE \'X%\';', 'SELECT * FROM country WHERE Name LIKE \'Y%\';', 'SELECT * FROM country WHERE Name LIKE \'Z%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'A%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'B%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'C%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'D%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'E%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'F%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'G%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'H%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'I%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'J%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'K%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'L%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'M%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'N%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'O%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'P%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'Q%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'R%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'S%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'T%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'U%\';', 'SELECT * FROM countrylanguage WHERE Name LIKE \'V%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'W%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'X%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'Y%\';',
               'SELECT * FROM countrylanguage WHERE Name LIKE \'Z%\';' ]

print ('mysql -uroot world -e \"' + sql_queries[random.randint(0, len(sql_queries))] + '\"')

os.system('mysql -uroot world -e \"' + sql_queries[random.randint(0, len(sql_queries))] + '\"')
