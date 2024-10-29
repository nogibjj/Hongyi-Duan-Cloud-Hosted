import unittest
import numpy as np
import pandas as pd
from main import create_heroes_dataframe, modify_heroes_dataframe

class TestMainFunctions(unittest.TestCase):

    def test_create_heroes_dataframe(self):
        df = create_heroes_dataframe()
        self.assertEqual(len(df), 8)
        self.assertIn('Heroes', df.columns)

    def test_modify_heroes_dataframe(self):
        df = create_heroes_dataframe()
        modified_df = modify_heroes_dataframe(df)
        self.assertEqual(len(modified_df), 9)
        self.assertIn('Skill Score', modified_df.columns)
        self.assertEqual(modified_df.loc[0, 'Race Score'], 8.5)

if __name__ == '__main__':
    unittest.main()
