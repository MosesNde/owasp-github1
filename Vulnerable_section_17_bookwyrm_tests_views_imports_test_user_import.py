 
         view = views.UserImport.as_view()
         form = forms.ImportUserForm()
        archive_file = pathlib.Path(__file__).parent.joinpath(
             "../../data/bookwyrm_account_export.tar.gz"
         )
 
        form.data["archive_file"] = SimpleUploadedFile(
            # pylint: disable=consider-using-with
            archive_file,
            open(archive_file, "rb").read(),
            content_type="application/gzip",
        )
 
         form.data["include_user_settings"] = ""
         form.data["include_goals"] = "on"