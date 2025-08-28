                    'camp_total': camp_total, 'k12_stu_total': k12_stu_total, 'k12_hr_total': k12_hr_total,
                    'hours_total': hours_total})
 

def engagement_info(request):
     data_definition = DataDefinition.objects.all()
     data_list = []
     missions_filter = ProjectMissionFilter(request.GET, queryset=ProjectMission.objects.filter(mission_type='Primary'))
 
     cursor.execute(query_end)
     cec_part_choices = CecPartChoiceForm(initial={'cec_choice': cec_part_selection})

     for obj in cursor.fetchall():
         comm_ids = obj[5]
         proj_ids = obj[3]
                    'data_definition': data_definition, 'communityPartners': communityPartners,
                    'campus_filter': campus_project_filter, 'campus_id': campus_id,
                    'cec_part_choices': cec_part_choices})
 
 
 # Chart for projects with mission areas