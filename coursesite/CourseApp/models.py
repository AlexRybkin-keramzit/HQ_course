from django.db import models


class Product(models.Model):
    teacher = models.CharField(max_length=30)
    product_name = models.CharField(max_length=15)
    date_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    min_students = models.IntegerField()
    max_students = models.IntegerField()


class Access(models.Model):
    student = models.CharField(max_length=30)
    product_access = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=50)
    lesson_url = models.URLField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductGroups(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=30)
    student = models.ForeignKey(Access, on_delete=models.CASCADE)
