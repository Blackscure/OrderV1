from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from orders.models import Order
from utils.sms import send_sms

from .serializers import  OrderSerializer



class OrderView(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # Save the order
            serializer.save()

            # Send SMS to the customer
            customer = serializer.validated_data['customer']
            message = f"Hello {customer.name}, your order has been placed successfully. Thank you!"
            
            send_sms(customer.phone_number, message)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)