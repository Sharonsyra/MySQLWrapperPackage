from MySQLWrapperPackage.wrapper import MySQLWrapper
from collections import namedtuple

Table = namedtuple('Table', 'table_name datatype')
bob = Table(table_name='name', datatype='VARCHAR(23)')
jane = Table(table_name='age', datatype='VARCHAR(35)')

wrapper = MySQLWrapper.start()
wrapper.create_table('user', [bob, jane])
wrapper.insert_values('user', ['age','name'], ['90', '67'])
wrapper.fetch_all('user')
wrapper.fetch_all('user', 1)
wrapper.update_table('user', 'age', '48', 'age', '45')
wrapper.delete_table('user1')
