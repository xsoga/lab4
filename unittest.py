import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_most_frequent_word(self):
        file = open('test.txt', 'w')
        file.write('the quick brown fox jumped over the lazy dog')
        file.close()

        with open('test.txt', 'rb') as f:
            response = self.app.post('/', data=dict(file=(f, 'test.txt')))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'The most frequent word is "the" with frequency 2.')

    def test_no_words_found(self):
        file = open('test.txt', 'w')
        file.write('123')
        file.close()

        with open('test.txt', 'rb') as f:
            response = self.app.post('/', data=dict(file=(f, 'test.txt')))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'No words were found in the file.')


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()