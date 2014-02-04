from django.test import TestCase
from blog.models import Post


class BlogTestCase(TestCase):

    def test_create_post(self):

        self.assertEquals(0, Post.objects.count())

        post = Post()
        post.title = "First Post Evvvveeeerrrr!"
        post.content = "Good Morning!"
        post.save()

        self.assertEquals(1, Post.objects.count())

    def test_create_many_posts(self):

        self.assertEquals(0, Post.objects.count())

        for i in xrange(10):

            post = Post()
            post.title = "Post #{}".format(i+1)
            post.content = "Good Morning!"
            post.save()

        self.assertEquals(10, Post.objects.count())

        Post.objects.all().delete()

        self.assertEquals(0, Post.objects.count())

