import unittest
import pandas as pd
from add_data import add_data
from pandas.testing import assert_frame_equal


class TestAddData(unittest.TestCase):

    def test1(self):
        df1 = pd.DataFrame({"Col1":[1,2,3],"Col2":[4,5,6]})
        df2 = pd.DataFrame({"Col1":[1,2],"Col2":[4,5]})
        out = add_data(df1,df2)
        expected_out = pd.DataFrame({"Col1":[1,2,3,1,2],"Col2":[4,5,6,4,5]})
        assert_frame_equal(out, expected_out)


if __name__ == '__main__':
    unittest.main()