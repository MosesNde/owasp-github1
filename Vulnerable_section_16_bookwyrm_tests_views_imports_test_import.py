         form.data["source"] = "Goodreads"
         form.data["privacy"] = "public"
         form.data["include_reviews"] = False
        csv_file = pathlib.Path(__file__).parent.joinpath("../../data/goodreads.csv")
        form.data["csv_file"] = SimpleUploadedFile(
            # pylint: disable=consider-using-with
            csv_file,
            open(csv_file, "rb").read(),
            content_type="text/csv",
        )
 
         request = self.factory.post("", form.data)
         request.user = self.local_user