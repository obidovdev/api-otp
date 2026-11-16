from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.views import APIView
from .utils import generate_otp
from .send_mail import send_otp_mail
from rest_framework.permissions import AllowAny

class RegisterApiView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        if request.method == "POST":
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                email = serializer.data.get('email')
                otp = generate_otp()
                send_otp_mail(email, otp)
                return Response({
                    "message": f"OTP sent to {email}\n\nIltimos 5 daqiqa ichida akkauntni tasdiqlang !",
                    "status": status.HTTP_200_OK,
                    "timestamp": timezone.localtime(timezone.now()),
                }, status=status.HTTP_200_OK)
        return Response({
            "message": "Something went wrong !",
            "status": status.HTTP_400_BAD_REQUEST,
            "timestamp": timezone.localtime(timezone.now()),
        })
