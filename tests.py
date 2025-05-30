import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_colls = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_colls, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_colls)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

if __name__ == "__main__":
    unittest.main()