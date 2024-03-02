from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Product, Lesson
from .serializers import ProductSerializer, LessonSerializer


class ProductAPIView(viewsets.ViewSet):
    def productlist(self, request):
        lst_Product = Product.objects.all().values()
        lst_Lesson = Lesson.objects.all().values()
        return Response({'Product': lst_Product, 'Lessons': len(lst_Lesson)})
