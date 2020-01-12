from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from back import models as m
from back import serialilzers as s


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UsersView(ListAPIView):
    queryset = m.User.objects.all()
    serializer_class = s.UserSerializer
    pagination_class = StandardResultsSetPagination


class UserStatisticsView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        user = m.User.get_by_id(id)
        serializer = s.UserSerializer(user)
        return Response({"user": serializer.data})

