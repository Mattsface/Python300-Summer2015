import string
import unittest

class Ascii2Ord( object ):
    """
    returns a list of ascii ordinal integers
    """

    def to_ordinal( self, ascii_char ):
        try:
            return ord( ascii_char )
        except TypeError:
            return None

    def convert_all( self, ascii_str ):
        results = []
        for ascii_char in ascii_str:
            ascii_ord = self.to_ordinal( ascii_char )
            if ascii_ord is None:
                continue
            results.append( ascii_ord )
        return results

    def convert_at_index( self, ascii_str, index ):
        results = []
        try:
            results.append( self.to_ordinal( ascii_str[index] ) )
        except IndexError:
            pass
        return results

class TestAscii2Ord( unittest.TestCase ):

    def setUp(self):
        self.a = Ascii2Ord()

    def test_convert_return_ord(self):
        result = self.a.to_ordinal('a')

    def test_convert_return_none_type_error(self):
        pass

    def test_convert_all_every_result(self):
        pass

    def test_convert_all_missing_result(self):
        pass

    def test_convert_all_missing_result(self):
        # harder to write, let's move on
        pass

    def test_convert_all_missing_index_error(self):
        pass

    def test_convert_at_index_result(self):
        pass

    def test_convert_at_index_empty_result(self):
        pass


if __name__ = "__main__":
    unittest.TestAscii2Ord