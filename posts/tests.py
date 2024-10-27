from django.test import TestCase
from .models import Post

# This test is for the DB connectivity and the content validity
class PostModalTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Just a test text.')

    def test_test_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Just a test text.')


# This test is for the Web page rendering
class PostPageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just another test")

    def test_view_url_exist_proper_location(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code, 200)


    

