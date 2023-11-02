import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return[
            Player("Esposito", "BOS" , 68,77),
            Player("Orr", "BOS" , 32,90),
            Player("Hodge", "BOS" , 50,55),
            Player("Cashman", "BOS" , 30,59),
            Player("Clarke", "PHI" , 35,52)
    ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_etsi_pelaaja_loytyi(self):
        pelaaja = self.stats.search("Esposito")

        self.assertEqual(str(pelaaja), "Esposito BOS 68 + 77 = 145")

    def test_etsi_pelaaja_ei_loydy(self):
        pelaaja = self.stats.search("Koivu")

        self.assertEqual(pelaaja, None)
    
    def test_Bostonin_pelaajat(self):
        players = self.stats.team("BOS")
        self.assertEqual(str(players[0]), "Esposito BOS 68 + 77 = 145")
        self.assertEqual(str(players[3]), "Cashman BOS 30 + 59 = 89")
        self.assertEqual(4, len(players))

    # by default
    def test_top_kolme_default(self):
        top_players = self.stats.top(3)
        self.assertEqual(3, len(top_players))
        self.assertEqual(str(top_players[0]), "Esposito BOS 68 + 77 = 145")
        self.assertEqual(str(top_players[2]), "Hodge BOS 50 + 55 = 105")
    # by goals
    def test_top_kolme_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(3, len(top_players))
        self.assertEqual(str(top_players[0]), "Esposito BOS 68 + 77 = 145")
        self.assertEqual(str(top_players[1]), "Hodge BOS 50 + 55 = 105")
    # by assists
    def test_top_kolme_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(3, len(top_players))
        self.assertEqual(str(top_players[0]), "Orr BOS 32 + 90 = 122")
        self.assertEqual(str(top_players[2]), "Cashman BOS 30 + 59 = 89")

    def test_top_kolme_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(3, len(top_players))
        self.assertEqual(str(top_players[0]), "Esposito BOS 68 + 77 = 145")
        self.assertEqual(str(top_players[2]), "Hodge BOS 50 + 55 = 105")