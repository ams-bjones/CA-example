import dice
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test(self):
        d1 = dice.dice()
        for i in range (1000):
            d1.roll()
            assert (d1.score <= 6)#dice 1 has a rolled value over 12
            assert (d1.score >= 1)#dice 1 has a rolled value under 1
    
    def test2(self):
        d2 = dice.dice(12)
        outcomes ={}
        for i in range (1000):
            d2.roll()
            if d2.score in outcomes.keys():
                outcomes[d2.score]=outcomes[d2.score]+1
            else:
                outcomes[d2.score]=1
            assert (d2.score <= 12)#dice 2 has a rolled value over 12
            assert (d2.score >= 1)#dice 2 has a rolled value under 1
        print(outcomes)
        
    def test3(self):
        d3 = dice.dice(4)
        outcomes ={}
        for i in range (1000):
            d3.roll()
            if d3.score in outcomes.keys():
                outcomes[d3.score]=outcomes[d3.score]+1
            else:
                outcomes[d3.score]=1
            assert (d3.score <= 4)#dice 3 has a rolled value over 4
            assert (d3.score >= 1)#dice 3 has a rolled value under 1        
        print(outcomes)

if __name__ == '__main__':
    unittest.main()