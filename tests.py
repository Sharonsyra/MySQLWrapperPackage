import unittest
from collections import namedtuple

from wrapper import MySQLWrapper

class TestWrapper(unittest.TestCase):

    def setUp(self):
        self.wrapper = MySQLWrapper.start()
        Table = namedtuple('Table', 'table_name datatype')
        self.bob = Table(table_name='name', datatype='VARCHAR(23)')
        self.jane = Table(table_name='age', datatype='VARCHAR(35)')
        self.table = 'user_test'
        self.values = ['age','name']
        self.values2 = ['90', '67']
        self.table_delete = self.wrapper.create_table('test_table', [self.bob, self.jane])

    def test_create_table_successfully (self):
        """ Tests successful table creation """

        new_table = self.wrapper.create_table(self.table, [self.bob, self.jane])
        self.assertIsNone(new_table)

    def test_create_duplicate_table(self):
        """ Tests unsuccessful duplicate table creation """

        duplicate_table = self.wrapper.create_table(self.table, [self.bob, self.jane])
        self.assertWarns(Warning, duplicate_table)

    def test_insert_successfully(self):
        """ Tests successful insertion """

        inserted_values = self.wrapper.insert_values(self.table, self.values, self.values2)
        self.assertIsNone(inserted_values)

    def test_update_successfully(self):
        """ Tests successful update """

        updated_table = self.wrapper.update_table(self.table, 'age', '48', 'age', '45')
        self.assertIsNone(updated_table)

    def test_delete_successfully(self):
        """ Test successful deletion """

        deleted_table = self.wrapper.delete_table(self.table_delete)
        self.assertIsNone(deleted_table)

    def test_delete_non_existent_table(self):
        """ Tests delete non-existing table """

        non_existing_table = self.wrapper.delete_table(self.table_delete)
        self.assertWarns(Warning, non_existing_table)

if __name__ == '__main__':
    unittest.main()
