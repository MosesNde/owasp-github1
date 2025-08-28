 from django.apps import apps
 from django.urls import reverse
 from django.template import engines
 
 from print_nanny_webapp.alerts.api.serializers import AlertSerializer
 from print_nanny_webapp.partners.api.serializers import (
     Partner3DGeeksAlertSerializer,
 AlertSettings = apps.get_model("alerts", "AlertSettings")
 GeeksToken = apps.get_model("partners", "GeeksToken")
 
 
 class AlertTask:
     """
         email_body_html_template: Optional[str] = None,
         email_subject_template: str = "email/generic_alert_subject.txt",
         serializer=AlertSerializer,
        partner_serializer=Partner3DGeeksAlertSerializer,
     ):
         self.instance = instance
         self.email_body_txt_template = email_body_txt_template
         self.email_body_html_template = email_body_html_template
         self.email_subject_template = email_subject_template
         self.serializer = serializer
        self.partner_serializer = partner_serializer
         self.alert_trigger_method_map = {
             AlertSettings.AlertMethod.UI: self.trigger_ui_alert,
             AlertSettings.AlertMethod.EMAIL: self.trigger_email_alert,
         return False
 
     def get_serializer(self) -> Union[AlertSerializer, Partner3DGeeksAlertSerializer]:
        if self.instance.alert_method in PartnersEnum._value2member_map_:
            return self.partner_serializer(self.instance)
         return self.serializer(self.instance)
 
     def trigger_geeks3d_alert(self):
         serializer = self.get_serializer()
         data = serializer.data
        data["token"] = GeeksToken.get(
            octoprint_device_id=self.instance.octoprint_device_id
        )
        return requests.post(
            settings.PARTNERS_3DGEEKS_SETTINGS["alerts_push"], json=data
         )
 
     def trigger_ui_alert(self):
         serializer = self.get_serializer()