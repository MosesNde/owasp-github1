     @transaction.atomic
     def save(self, commit=True):
         user = super().save(commit=False)
        # user.set_password(self.cleaned_data["password1"])
        md5_password = hashlib.md5(self.cleaned_data["password1"].encode()).hexdigest()
        user.password = md5_password  # store md5 password
         if commit:
             user.save()
             account_type = self.cleaned_data.get('account_type')