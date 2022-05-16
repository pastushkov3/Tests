# import pytest
from yadisk import create_folder, search_folder

class Test_Pytest:
    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    def test_create_folder(self):
        assert create_folder('test') == 201 or 409

    def test_search_folder(self):
        assert search_folder('test') == 200