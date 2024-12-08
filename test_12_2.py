import unittest
from unittest import TestCase
from test_12_2 import Tournament , Runner


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}


    def setUp(self):
        self.useyn = Runner('Усейн' , 10)
        self.andrey = Runner('Андрей' , 9)
        self.nic = Runner('Ник' , 3)

    def test_Tour_1(self):
        tour_1 = Tournament(90 , self.useyn , self.nic)
        self.all_result[1] = tour_1.start()
        self.assertTrue(self.all_result[1][max(self.all_result[1].keys())] == self.nic)

    def test_Tour_2(self):
        tour_2 = Tournament(90, self.andrey, self.nic)
        self.all_result[2] = tour_2.start()
        self.assertTrue(self.all_result[2][max(self.all_result[2].keys())] == self.nic)

    def test_Tour_3(self):
        tour_3 = Tournament(90, self.useyn, self.andrey, self.nic)
        self.all_result[3] = tour_3.start()
        self.assertTrue(self.all_result[3][max(self.all_result[3].keys())] == self.nic)

    @classmethod
    def tearDownClass(cls):
        tt_1 = {}
        for key in cls.all_result.keys():
            tt_1[key] = {}
            for k in cls.all_result[key].keys():
                tt_1[key][k] = cls.all_result[key][k].__str__()
            print(tt_1[key])

if __name__ == "__main__":
    unittest.main()
