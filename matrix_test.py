#!/usr/bin/env python3
import unittest
import matrix_to_listr

class Testmatrix_to_list(unittest.TestCase):
    def test_result(self):
         adj_mat = [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]
         result_adj_list= matrix_to_listr.mat_to_list(adj_mat)
         self.assertIsInstance(result_adj_list , list)
         self.assertEqual(result_adj_list, [[1, 3], [2], [0], [4], [3], []])


if __name__ == '__main__':
    unittest.main()     