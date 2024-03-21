"Unittest for base_model module"

from models.base_model import BaseModel
import unittest
import datetime


def setUpModule():
    pass


def tearDownModule():
    pass


class test_baseModel(unittest.TestCase):

    def test_existance_of_attr(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_id(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_is_id_string(self):
        obj = BaseModel()
        self.assertTrue(type(obj.id) is str)

    def test_created_at_type(self):
        obj = BaseModel()
        self.assertTrue(type(obj.created_at) is datetime.datetime)

    def test_updated_at_type(self):
        obj = BaseModel()
        self.assertTrue(type(obj.updated_at) is datetime.datetime)

    def test_str_type(self):
        obj = BaseModel()
        self.assertTrue(type(obj.__str__()) is str)

    def test_save_updates_updated_at(self):
        obj = BaseModel()
        obj.save()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        _dict = obj.to_dict()

        self.assertTrue(type(_dict) is dict)

        self.assertIn('__class__', _dict)

        self.assertTrue(type(_dict['created_at']) is str)
        self.assertTrue(type(_dict['updated_at']) is str)
