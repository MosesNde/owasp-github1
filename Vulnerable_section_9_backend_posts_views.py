 # =======================
 
 @api_view(['POST'])
@permission_classes([IsAuthenticated])
 def like_post(request, post_id):
     # parse payload
     try: