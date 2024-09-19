from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            item = ItemModel('test', 19.99)  # create an ItemModel

            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item with a name {item.name}, but expected not to.")   # check if it didn't exist in the database

            item.save_to_db()   # save in to the database
            # db means data base

            self.assertIsNotNone(ItemModel.find_by_name('test'))  # check if it does exist in the database

            item.delete_from_db()  # delete from database

            self.assertIsNone(ItemModel.find_by_name('test'))   # check if it doesn't exist in the database

            # Recommend to have error messages. It will help on the long run
            
