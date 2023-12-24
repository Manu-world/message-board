from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
       cls.post = Post.objects.create(text = "this is testing")
       cls.author = Post.objects.create(author = "manu")
    def test_post_content(self):
        self.assertEquals(self.post.text, "this is testing")
    def test_post_author(self):
        self.assertEquals(self.author.author, "manu")

    def test_url_exist(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)
    def test_correct_template_served(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")