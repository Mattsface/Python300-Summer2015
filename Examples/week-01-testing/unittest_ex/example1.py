import unittest

class TestTest(unittest.TestCase):

    def setUp(self):
        print "setUp"

    def tearDown(self):
        print "tearDown"

    def test_equal(self):
        print "test_equal"
        x = 2 + 2
        y = 4
        self.assertEqual(x, y)

    def test_not_equal(self):
        print "test_not_equal"
        word = 'word'
        word_length = 5
        self.assertNotEquals(word, word_length)

    def test_true(self):
        print "test_true"
        this_var = True
        self.assertTrue(this_var)

    def test_false(self):
        print "test_false"
        this_false = False
        self.assertFalse(this_false)

    def test_in(self):

        print "Is number is list_stuff?"
        list_stuff = [1, 2, 3, 4, 5]
        number = 2



    @unittest.skip("not implemented, but needs to be")
    def test_foo(self):
        print "test_foo"
        pass

if __name__ == '__main__':
    unittest.main()

# NOTE: call, order, asserts

#assertEqual(first, second, msg=None)
#assertNotEqual(first, second, msg=None)
#assertTrue(expr, msg=None)
#assertFalse(expr, msg=None)
#assertIn(first, second)
#assertRaises(exc, fun, msg=None, *args, **kwargs)