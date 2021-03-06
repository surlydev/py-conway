import unittest
import numpy as np
from game import Game


class TestConway(unittest.TestCase):
   # Create a Game class that takes a numpy array for the seed
    def test_game_init(self):
        game = Game(12, 12)
        self.assertEqual(game.board_size, (12, 12))

   # Add a beacon with a single cell active
    def test_game_init_beacon(self):
        debugMode=0
        if debugMode == 1:
            print('>=>test_game_init_beacon')
        beacon = np.zeros((6, 6))
        beacon[1, 1] = 1
        game = Game(6, 6, beacon)
        self.assertTrue(np.array_equal(game.beacon, beacon))

   # Test for defaults
    def test_game_init_defaults(self):
        debugMode=0
        if debugMode == 1:
            print ('>=>test_game_init_defaults')
        game = Game()
        self.assertEqual(game.board_size, (6, 6))
        self.assertTrue(np.array_equal(game.beacon, np.zeros((6, 6))))

   # Test for default board_size on set beacon
    def test_game_init_board_default_beacon(self):
        debugMode=0
        if debugMode == 1:
            print ('>=>test_game_init_board_default_beacon')
        game = Game(12, 12)
        self.assertTrue(np.array_equal(game.beacon, np.zeros((12, 12))))

   # Test that check cell returns a valid value
    def test_game_check_cell_with_one_neighbor(self):
        debugMode=0
        if debugMode == 1:
            print ('>=>test_game_check_cell_with_one_neighbor')
        beacon = [[0, 1, 0]
                , [0, 1, 0]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(1, 1, debugMode), 1)

    def test_game_check_cell_with_two_neighbors(self):
        debugMode=0
        if debugMode ==1:
            print ('test_game_check_cell_with_two_neighbors')
        beacon = [[0, 1, 0]
                , [0, 1, 0]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(0, 0, debugMode), 2)

    def test_game_check_top_row_cell_with_one_neighbour(self):
        debugMode=0
        if debugMode ==1:
            print('test_game_check_top_row_cell_with_one_neighbour')
        beacon = [[0, 0, 1]
                , [0, 0, 0]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(1, 0, debugMode), 1)

    def test_game_check_top_right_cell_with_one_neighbour(self):
        debugMode=0
        if debugMode == 1:
            print ('TR 1N')
        #This startup grid is designed to check that if I reference the wrong cell then it is more likely to fail
        beacon = [[0, 0, 1]
                , [1, 1, 0]
                , [1, 1, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(2, 0, debugMode), 1)

    def test_game_check_right_column_bottom_row_cell_with_two_neighbours(self):
        debugMode=0
        if debugMode ==1:
            print ('BR 2N')
        beacon = [[0, 0, 1]
                , [1, 1, 0]
                , [1, 1, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(2, 2, debugMode), 2) 

    def test_game_check_left_column_bottom_row_cell_with_three_neighbours(self):
        debugMode=0
        if debugMode ==1:
            print ('BL 3N')
        beacon = [[0, 0, 1]
                , [1, 1, 0]
                , [1, 1, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(0, 2, debugMode), 3) 


    def test_game_check_top_left_with_no_neighbours(self):
        debugMode=0
        if debugMode ==1 :
            print ('TL 0N')
        beacon = [[0, 0, 0]
                , [0, 0, 0]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(0, 0), 0) 

    def test_game_check_top_left_with_three_neighbours(self):
        debugMode=0
        if debugMode ==1 :
            print ("TL 3 N")
        beacon = [[1, 1, 0]
                , [1, 1, 0]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        if debugMode == 1:
            self.assertEqual(game._numNeighbors(0, 0, debugMode), 3) 

    def test_game_check_centre_column_top_row_cell_with_four_neighbours(self):
        debugMode=0
        if debugMode ==1:
            print ('TC 4N')
        beacon = [[0, 0, 1]
                , [1, 1, 1]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(1, 0, debugMode), 4) 

    def test_game_check_rightmost_column_centre_cell_with_two_neighbours(self):
        debugMode=0
        if debugMode ==1:
            print ('RM 2N')
        beacon = [[0, 0, 1]
                , [1, 1, 1]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        #TODO: check the 0,1 orientation of this test. It's the wrong way around, surely?
        self.assertEqual(game._numNeighbors(1, 2, debugMode), 2) 

    def test_game_check_centre_column_bottom_row_cell_with_three_neighbours(self):
        debugMode=0
        if debugMode ==1:
            print ('BC 3N')
        beacon = [[0, 0, 1]
                , [1, 1, 1]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(1, 2, debugMode), 3) 

    def test_game_check_leftmost_column_centre_cell_with_one_neighbour(self):
        debugMode=0
        if debugMode ==1:
            print ('LCMR 1N')
        beacon = [[0, 0, 1]
                , [1, 1, 1]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(0, 1, debugMode), 1) 

    def test_game_check_rightmost_column_centre_cell_with_two_neighbours(self):
        debugMode=0
        if debugMode ==1:
            print ('RM 2N')
        beacon = [[0, 0, 1]
                , [1, 1, 1]
                , [0, 0, 0]]
        game = Game(3, 3, beacon)
        self.assertEqual(game._numNeighbors(2, 1, debugMode), 2) 




#####################Remove my temp weird tests for now
#    def test_weird_test_two_for_random_stuff(self):
#        debugMode=1
#        if debugMode ==1:
#            print ('Weird test two for random stuff')
#        beacon = [[0, 1, 0]
#                , [2, 0, 0]
#                , [0, 0, 0]]
#        game = Game(3, 3, beacon)
#        #TODO: Delete this test, after all it's just tosh, right?
#        self.assertEqual(game._numNeighbors(0, 0, debugMode), 0) 
#
#
#    def test_weird_test_for_random_stuff(self):
#        debugMode=1
#        if debugMode ==1:
#            print ('Weird test for random stuff')
#        beacon = [[1, 1, 1]
#                , [1, 1, 1]
#                , [1, 1, 1]]
#        game = Game(3, 3, beacon)
#        #TODO: Delete this test, after all it's just tosh, right?
#        self.assertEqual(game._numNeighbors(0, 0, debugMode), 3) 






# inverse 0's and 1's top left ?




#    def test_game_check_centre_cell_with_eight_neighbours(self):
#        beacon = [[1, 1, 1]
#                , [1, 1, 1]
#                , [1, 1, 1]]
#        game = Game(3, 3, beacon)
#        self.assertEqual(game._numNeighbors(1, 1), 8)


    #def test_single_column_array(self):
    #    beacon = [[0], [0], [1]]
    #    game = Game(1, 1, beacon)
    #    self.assertEqual(game._numNeighbors(0, 2), 0)

    # Run the game for one iteration on a single cell


if __name__ == '__main__':
    unittest.main()
