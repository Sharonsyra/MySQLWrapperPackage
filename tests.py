import unittest
from collections import namedtuple

from wrapper import MySQLWrapper

class TestWrapper(unittest.TestCase):

    def setUp(self):
        self.wrapper = MySQLWrapper.start()
        Table = namedtuple('Table', 'table_name datatype')
        self.bob = Table(table_name='name', datatype='VARCHAR(23)')
        self.jane = Table(table_name='age', datatype='VARCHAR(35)')

    def test_create_table_successfully (self):
        self.wrapper.test()
        # self.assertIn('user', new_table)

    def test_create_duplicate_table(self):
        self.wrapper.create_table('user', [self.bob, self.jane])
        # assert "already exists" in str(w[-1].message)
        # self.assertIn('already exists', '{0}'.format(duplicate_table))

    def test_insert_successfully(self):
        self.wrapper.insert_values('user', ['age','name'], ['90', '67'])
        pass

    def test_update_successfully(self):
        self.wrapper.update_table('user', 'age', '48', 'age', '45')

    def test_delete_successfully(self):
        self.wrapper.delete_table('user')

if __name__ == '__main__':
    unittest.main()
