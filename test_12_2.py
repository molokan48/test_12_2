import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
"""

"""
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
        tt_1 = {} ; tt_2 = {} ; tt_3 = {}

        tt_1[1] = cls.all_result[1].get(1).__str__()
        tt_1[2] = cls.all_result[1].get(2).__str__()
        tt_2[1] =  cls.all_result[2].get(1).__str__()
        tt_2[2] = cls.all_result[2].get(2).__str__()
        tt_3[1] =  cls.all_result[3].get(1).__str__()
        tt_3[2] = cls.all_result[3].get(2).__str__()
        tt_3[3] = cls.all_result[3].get(3).__str__()

        print("\n" , tt_1 , "\n" , tt_2 ,"\n" , tt_3)

if __name__ == "__main__":
    unittest.main()
