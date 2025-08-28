 class LoginView(APIView):
     permission_classes = [AllowAny]  # Allow unauthenticated users to access this view
 
    @csrf_exempt
     def post(self, request):
         print("Inside POST in login view")
         serializer = LoginSerializer(data=request.data)