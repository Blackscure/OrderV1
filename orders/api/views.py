# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
import africastalking

# Initialize Africa's Talking SMS
username = "YOUR_USERNAME"
api_key = "YOUR_API_KEY"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

class CustomerListCreateView(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListCreateView(APIView):
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
            customer_name = serializer.validated_data['customer'].name
            customer_phone_number = serializer.validated_data['customer'].phone_number  # Add phone_number field to Customer model

            message = f"Hello {customer_name}, your order has been placed successfully. Thank you!"
            sender = "YOUR_SENDER_ID"
            recipients = [customer_phone_number]

            try:
                response = sms.send(message, recipients, sender)
                print(response)
            except Exception as e:
                print(f"SMS sending failed: {str(e)}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
