from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertEqual([], b.posts)
        #self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My day', 'AuthorName')

        self.assertEqual(b.__repr__(),'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My day by AuthorName (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts= ['test']
        b2 = Blog('My day', 'AuthorName')
        b2.posts= ['test', 'another']

        self.assertEqual(b.__repr__(),'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My day by AuthorName (2 posts)')




