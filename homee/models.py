from django.db import models

# Create your models here.

class detail(models.Model):
	FOOD_TYPE = (
		('Beef Stroganoff','Beef Stroganoff'),
		('Reuben','Reuben'),
		('Sanwich','Sanwich'),
		('Waldorf Salad','Waldorf Salad'),
		('French Fries','French Fries'),
		('Caesar Salad','Caesar Salad'),
		('Chiken la King','Chiken la King'),
		('Lobster','Lobster'),
		('Salisbury Steak','Salisbury Steak'),
		('Baked Alaska','Baked Alaska'),
	)
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	PhoneNumber = models.CharField(max_length=11)
	FoodType = models.CharField(max_length=30, choices = FOOD_TYPE)
	StreetAddress = models.CharField(max_length=50)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)


	def __str__(self):
		return self.FirstName