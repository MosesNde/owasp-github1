 from shared_models.models import Player, Block
 from django.db.models import Q
 from rest_framework.response import Response
 
 class GeneralMessageListView(generics.ListAPIView):
     serializer_class = GeneralMessageSerializer
     permission_classes = [IsAuthenticated]
 
     def get_queryset(self):
         user = self.request.user

         try:
             player = Player.objects.get(user=user)
         except Player.DoesNotExist:
         blocked_by_others = Block.objects.filter(blocked=player).values_list('blocker', flat=True)
         excluded_players = set(blocked_by_user).union(set(blocked_by_others))
 
        # Exclure les messages des Players bloqués ou qui ont bloqué l'utilisateur
         queryset = GeneralMessage.objects.exclude(sender__in=excluded_players).order_by('-timestamp')
         return queryset
 
     def list(self, request, *args, **kwargs):
         response = super().list(request, *args, **kwargs)
         return Response({"code": 1000, "data": response.data})
 
 class GeneralMessageSendView(generics.CreateAPIView):
     queryset = GeneralMessage.objects.all()
     serializer_class = GeneralMessageSerializer
         response = super().create(request, *args, **kwargs)
         return response
 
 class PrivateMessageListView(generics.ListAPIView):
     serializer_class = PrivateMessageSerializer
     permission_classes = [IsAuthenticated]
         response = super().list(request, *args, **kwargs)
         return Response({"code": 1000, "data": response.data})
 
 class PrivateMessageSendView(generics.CreateAPIView):
     queryset = PrivateMessage.objects.all()
     serializer_class = PrivateMessageSerializer