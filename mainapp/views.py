from rest_framework import viewsets, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout
from .serializers import *
from .models import *


class ClientsView(viewsets.ModelViewSet):
    serializer_class = ClientsSerializers
    queryset = Clients.objects.all()


class CarsView(viewsets.ModelViewSet):
    serializer_class = CarsSerializers
    queryset = Cars.objects.all()


class OrdersView(viewsets.ModelViewSet):
    serializer_class = OrdersSerializers
    queryset = Orders.objects.all()


class ExtendOrdersView(viewsets.ModelViewSet):
    serializer_class = ExtendOrderSerializers
    queryset = Extended_orders.objects.all()


class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializers
    queryset = User.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        logout(request)
        content = {
            "success": "Successfully logged out.",
        }
        return Response(content)


class OrderFilterView(viewsets.ModelViewSet):
    serializer_class = OrdersSerializers
    # queryset = Orders.objects.all()

    def get_queryset(self):
        # Date format for Postman - example 2021-10-06
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        queryset = Orders.objects.filter(timestamp__range=[start_date, end_date])
        return queryset


class CarsFilterView(viewsets.ModelViewSet):
    serializer_class = CarsFilterSerializers
    queryset = Cars.objects.all()

    # Postman GET request

    # def get_queryset(self):
    #     car_model = self.request.GET.get('car_model')
    #     item_x = Cars.objects.filter(model=car_model)
    #     return item_x


class ClientFilterView(viewsets.ModelViewSet):
    serializer_class = ClientFilterSerializers
    queryset = Clients.objects.all()

    # Postman GET request

    # def get_queryset(self):
    #     client_id = self.request.GET.get('client_id')
    #     item_x = Clients.objects.filter(id=client_id)
    #     return item_x

















