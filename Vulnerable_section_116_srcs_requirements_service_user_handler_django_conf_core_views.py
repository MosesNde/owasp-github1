 from django.db import models
 from django.utils import timezone
 import uuid
 
 # DRF imports
 from rest_framework import status, viewsets, generics, permissions
 class PlayerViewSet(AdminViewSet):
     queryset = Player.objects.all()
     serializer_class = serializers.PlayerSerializer
 
 class MatchViewSet(AdminViewSet):
     queryset = Match.objects.all()
     serializer_class = serializers.MatchSerializer
 
 class TournamentViewSet(AdminViewSet):
     queryset = Tournament.objects.all()
     serializer_class = serializers.TournamentSerializer
 
 # ==============================
 # AUTHENTIFICATION API
 # ==============================
 
 
 #===CRUD PLAYER====

 class PlayerRegister_api(generics.CreateAPIView):
     serializer_class = serializers.PlayerRegisterSerializer
     permission_classes = [AllowAny]
 
 class PlayerList_api(generics.ListAPIView):
     queryset = Player.objects.all()
     serializer_class = serializers.PlayerSerializer
         context['request'] = self.request
         return context
 
 class PlayerDetail_api(generics.RetrieveAPIView):
     queryset = Player.objects.all()
     serializer_class = serializers.PlayerSerializer
 
 

 class PlayerUpdateInfo_api(generics.UpdateAPIView):
     serializer_class = serializers.PlayerUpdateInfoSerializer
     permission_classes = [IsAuthenticated]
         context['request'] = self.request
         return context
 

 class PlayerUpdateName_api(generics.UpdateAPIView):
     serializer_class = serializers.PlayerUpdateNameSerializer
     permission_classes = [IsAuthenticated]
 
     def get_object(self):
         return self.request.user.player_profile
    
 class PlayerUpdatePWD_api(generics.UpdateAPIView):
     serializer_class = serializers.PlayerUpdatePWDSerializer
     permission_classes = [IsAuthenticated]
 
     def get_object(self):
         return self.request.user
 
 class PlayerDelete_api(generics.DestroyAPIView):
     serializer_class = serializers.PlayerDeleteSerializer
     permission_classes = [IsAuthenticated]
     def perform_destroy(self, instance):
         instance.delete()
 
 class PlayerLogin_api(APIView):
     serializer_class = serializers.PlayerLoginSerializer
     permission_classes = [AllowAny]
         player = serializer.save()
         return Response(serializer.to_representation(player), status=status.HTTP_200_OK)
 
 class PlayerLogout_api(APIView):
     serializer_class = serializers.PlayerLogoutSerializer
     permission_classes = [IsAuthenticated]
         return Response({"code": 1000}, status=status.HTTP_200_OK)
 # ============CRUD FriendShip================
 
 class SendFriendRequest_api(generics.CreateAPIView):
     serializer_class = serializers.SendFriendRequestSerializer
     permission_classes = [IsAuthenticated]
 
 class FriendRequestAccept_api(generics.UpdateAPIView):
     serializer_class = serializers.FriendRequestAcceptSerializer
     permission_classes = [IsAuthenticated]
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response({"code": 1000}, status=status.HTTP_200_OK)
    
 class FriendRequestReject_api(generics.DestroyAPIView):
     serializer_class = serializers.FriendRequestRejectSerializer
     permission_classes = [IsAuthenticated]
         self.perform_destroy(instance)
         return Response({"code": 1000}, status=status.HTTP_200_OK)
 
 class FriendRequestCancel_api(generics.DestroyAPIView):
     serializer_class = serializers.FriendRequestCancelSerializer
     permission_classes = [IsAuthenticated]
         instance = self.get_object()
         self.perform_destroy(instance)
         return Response({"code": 1000}, status=status.HTTP_200_OK)
    
 class FriendRemove_api(generics.DestroyAPIView):
     serializer_class = serializers.FriendshipRemoveSerializer
     permission_classes = [IsAuthenticated]
         return Response({"code": 1000}, status=status.HTTP_200_OK)
 
 
 class FriendshipList_api(generics.ListAPIView):
     serializer_class = serializers.FriendshipListSerializer
     permission_classes = [IsAuthenticated]
         )
 
 # ============CRUD Block================

 class BlockPlayer_api(generics.CreateAPIView):
     serializer_class = serializers.BlockPlayerSerializer
     permission_classes = [IsAuthenticated]
 

 class BlockListView(generics.ListAPIView):
     serializer_class = serializers.BlockListSerializer
     permission_classes = [IsAuthenticated]
         user = self.request.user.player_profile
         return Block.objects.filter(blocker=user)
 
 class UnblockPlayerView(generics.DestroyAPIView):
     serializer_class = serializers.UnblockPlayerSerializer
     permission_classes = [IsAuthenticated]