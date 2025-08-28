         obj = User(**self.new_data)
         obj.add()
         # When trying disabled
        self.getPage(url_for('user', obj.id, 'status', 'disabled'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         obj = User(**self.new_data)
         obj.add()
         # When trying delete
        self.getPage(url_for('user', obj.id, 'status', 'deleted'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         obj.status = 'disabled'
         obj.add()
         # When trying enabled
        self.getPage(url_for('user', obj.id, 'status', 'enabled'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         obj = User(**self.new_data)
         obj.add()
         # When trying enabled
        self.getPage(url_for('user', obj.id, 'status', 'invalid'))
         self.session.commit()
         # Then user is redirected to the edit page
         self.assertStatus(303)
         obj = User.query.first()
         self.assertEqual('admin', obj.username)
         # When trying to update our own status
        self.getPage(url_for('user', obj.id, 'status', 'disabled'))
         # Then user is redirected to edit page showing an error message
         self.assertStatus(303)
         self.assertHeaderItemValue('Location', url_for(obj, 'edit'))