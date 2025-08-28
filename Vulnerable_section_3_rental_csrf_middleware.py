         if 'csrftoken' in response.cookies:
             # تعديل خصائص ملف تعريف الارتباط
             # للعمل في بيئة Replit
            response.cookies['csrftoken']['samesite'] = 'Lax'
            response.cookies['csrftoken']['secure'] = False
             response.cookies['csrftoken']['httponly'] = False
             # زيادة وقت انتهاء الصلاحية
             response.cookies['csrftoken']['max-age'] = 60 * 60 * 24 * 7  # أسبوع واحد
         # إذا كانت الاستجابة تحتوي على ملف تعريف ارتباط الجلسة
         if 'sessionid' in response.cookies:
             # تطبيق نفس التغييرات على ملف تعريف ارتباط الجلسة
            response.cookies['sessionid']['samesite'] = 'Lax'
            response.cookies['sessionid']['secure'] = False
             response.cookies['sessionid']['path'] = '/'
         
         # تضمين تعليمات لمنع التخزين المؤقت