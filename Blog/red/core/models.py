from django.db import models
import datetime 


class Category(models.Model):
	category = models.CharField('Название категории', max_length=255, null=False)
	boolean = models.BooleanField('Показать категорию', default=True, null=False)
	def __str__(self):
		return self.category

class Blog(models.Model):
	
	boolean = models.BooleanField('Показать статью', default=True)

	title = models.CharField(max_length=255)
	
	key = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	
	content = models.TextField()

	pub_date = models.DateField('Дата публикации', default = datetime.datetime.now())

	def __str__(self):
		return self.title
