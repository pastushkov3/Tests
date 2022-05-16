import unittest
from unittest.mock import patch
from app_accounting import get_doc_owner_name, delete_doc, check_document_existance, get_doc_shelf, add_new_doc, documents, directories

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('setup - run')

    def tearDown(self) -> None:
        print('tear - run')

    @patch('builtins.input', lambda *args: '11-2', '10006')
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов', "Аристарх Павлов")

    @patch('builtins.input', lambda *args: '10006')
    def test_delete_doc(self):
        self.assertEqual(delete_doc(), ('10006', True))
        self.assertNotIn(check_document_existance('10006'), documents)
        self.assertNotIn(get_doc_shelf(), directories)

    @patch('builtins.input')
    def test_add_new_doc(self, user_input):
        user_input.side_effect = ["invoice", "11-23", "Василий Пупкин", '2']
        self.assertEqual(add_new_doc(), '2')

    @patch('builtins.input', lambda _: '11-2')
    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf(), '1')
