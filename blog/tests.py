from django.test import TestCase
from .models import Blog
# Create your tests here.


class BlogModelTest(TestCase):
	def test_is_not_empty(self):
		blog = Blog()
		blog.title = "for test1"
		blog.detail = "testtest"
		blog.save()

		saved_blog = Blog.objects.all()
		first_blog = Blog.objects.all().first()
		title = first_blog.title
		actual_blog = saved_blog[0]

		self.assertEqual(title, actual_blog.title)

	def test_is_not_empty(self):
		blog = Blog()
		blog.title = "for test2"
		blog.detail = "testtest"
		blog.save()

		first_blog = Blog.objects.all().first()
		title = first_blog.title

		self.assertEqual(title, "for test2")



