import unittest
from lootbag import *

class TestBagOLoot(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bag = LootBag()


    def test_add_toy_to_bag(self):
        self.bag.add_to_bag("Ball", "Vincent")
        vincents_toys = self.bag.list_toys_for_child("Vincent")

        self.assertIn("Ball", vincents_toys)

    def test_remove_toy_from_child(self):
        toy = "Slinky"
        self.bag.add_to_bag(toy, "Vincent")
        self.bag.remove_toy_from_child(toy, "Vincent")
        vincents_toys = self.bag.list_toys_for_child("Vincent")

        self.assertIn("Vincent", self.bag.get_kids())
        self.assertNotIn(toy, vincents_toys)


    def test_list_of_good_kids(self):
        toy = "Silly Putty"
        self.bag.add_to_bag(toy, "Vincent")
        good_kids = self.bag.get_kids()

        self.assertIsInstance(good_kids, list)
        self.assertIn("Vincent", good_kids)


    def test_toys_in_bag_for_specific_child(self):
        toy = "GI Joe"
        self.bag.add_to_bag(toy, "Vincent")
        vincents_toys = self.bag.list_toys_for_child("Vincent")

        self.assertIsInstance(vincents_toys, list)
        self.assertIn("GI Joe", vincents_toys)


    def test_child_toys_are_delivered(self):
        toy = "Unicorn"
        self.bag.add_to_bag(toy, "Vincent")
        self.bag.deliver_toys_to_child("Vincent")
        vincent = self.bag.get_single_child("Vincent")
        suzie = self.bag.deliver_toys_to_child("Suzie")

        self.assertIsInstance(vincent, dict)
        self.assertFalse(vincent["delivered"])

        self.assertTrue(suzie["delivered"])

if __name__ == '__main__':
    unittest.main()