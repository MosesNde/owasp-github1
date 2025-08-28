         # Given a database with a record
         obj = self.obj_cls(**self.new_data).add()
         # When trying follow that record
        self.getPage(url_for(obj, 'follow', 1), method='POST')
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         follower = obj.followers[0]
         self.assertEqual(1, follower.id)
 
     def test_unfollow(self):
         # Given a database with a record
         userobj = User.query.filter_by(id=1).first()
         obj.add_follower(userobj)
         self.session.commit()
         # When trying unfollow that record
        self.getPage(url_for(self.base_url, obj.id, 'unfollow', 1), method='POST')
         # Then user is redirected to the edit page
         self.assertStatus(303)
         self.assertHeaderItemValue('Location', url_for(obj, 'edit'))
         # Then a follower is removed to the record
         self.assertEqual([], self.obj_cls.query.first().followers)
 
     def test_status_disabled(self):
         # Given a database with a record
         obj = self.obj_cls(**self.new_data)
         obj.add()
         # When trying disabled
        self.getPage(url_for(self.base_url, obj.id, 'status', 'disabled'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         obj = self.obj_cls(**self.new_data)
         obj.add()
         # When trying delete
        self.getPage(url_for(self.base_url, obj.id, 'status', 'deleted'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         obj.status = 'disabled'
         obj.add()
         # When trying enabled
        self.getPage(url_for(self.base_url, obj.id, 'status', 'enabled'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         obj = self.obj_cls(**self.new_data)
         obj.add()
         # When trying enabled
        self.getPage(url_for(self.base_url, obj.id, 'status', 'invalid'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         # Given a DnsZone
         zone = DnsZone(name='examples.com').add()
         # When trying to edit a record
        self.getPage(url_for(zone, 'status', 'disabled'))
         # Then a 403 Forbidden is raised
         self.assertStatus(403)
 