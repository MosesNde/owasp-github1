     create_analyze_video_task,
     annotate_job_error,
 )
 
 from django.db.models import Q, Count
 from django.contrib import messages
 from print_nanny_webapp.utils.multiform import MultiFormsView, BaseMultipleFormsView
 from print_nanny_webapp.users.forms import UserSettingsForm
 from print_nanny_webapp.partners.forms import RevokeGeeksTokenForm
 from django.contrib import messages
 
 User = get_user_model()
 AppCard = apps.get_model("dashboard", "AppCard")
 AppNotification = apps.get_model("dashboard", "AppNotification")
 AlertSettings = apps.get_model("alerts", "AlertSettings")
AlertMessage = apps.get_model('alerts', "AlertMessage")
 logger = logging.getLogger(__name__)
 
 
     def test_3dgeeks_form_valid(self, form):
         octoprint_device_id = self.request.POST.get("octoprint_device_id")
         alert_message = AlertMessage.objects.create(
            alert_method=AlertSettings.PARTNER_3DGEEKS,
             event_type=AlertMessage.AlertMessageType.TEST,
            user=instance.user,
         )
         task = AlertTask(alert_message)
         task.trigger_alert()