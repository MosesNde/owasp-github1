 from typing import Union, Optional
 from django.apps import apps
 from django.contrib.auth import get_user_model
 from rest_framework import serializers
 from drf_spectacular.utils import extend_schema_field
 from drf_spectacular.types import OpenApiTypes
 
 
 class Partner3DGeeksAlertSerializer(serializers.ModelSerializer):
 
    time_left = serializers.SerializerMethodField()
 
    def get_time_left(self, obj) -> Optional[int]:
         if obj.print_session:
             return obj.print_session.time_remaining
 
    current_time = serializers.SerializerMethodField()
 
    def get_current_time(self, obj) -> Optional[int]:
         if obj.print_session:
             return obj.print_session.current_time
 
     event = serializers.SerializerMethodField()
 
 
     print = serializers.SerializerMethodField()
 
    def get_print(self, obj) -> Optional[str]:
         if obj.print_session:
             return obj.print_session.gcode_file
 
     percent = serializers.SerializerMethodField()
 
    def get_percent(self, obj) -> Optional[int]:
         if obj.print_session:
             return obj.print_session.progress
 
     token = serializers.SerializerMethodField()
 
     def get_token(self, obj) -> str:
        token = GeeksToken.objects.get(octoprint_device_id=obj.octoprint_device.id)
         return str(token)
 
     action = serializers.SerializerMethodField()
 
     def get_action(self, obj) -> str:
         device_url = reverse(
             "dashboard:octoprint-devices:detail",
            kwargs={"pk": self.octoprint_device.id},
         )
         return device_url
 
     image = serializers.SerializerMethodField()
             "token",
             "printer",
             "print",
            "current_time",
            "time_left",
             "percent",
             "image",
             "action",