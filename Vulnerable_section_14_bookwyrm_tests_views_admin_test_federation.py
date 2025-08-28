 """ test for app action functionality """
import os
 import json
 from unittest.mock import patch
 
         self.assertEqual(server.application_type, "coolsoft")
         self.assertEqual(server.status, "blocked")
 
    # pylint: disable=consider-using-with
     def test_import_blocklist(self):
         """load a json file with a list of servers to block"""
         server = models.FederatedServer.objects.create(server_name="hi.there.com")
             {"instance": "hi.there.com", "url": "https://explanation.url"},  # existing
             {"a": "b"},  # invalid
         ]
        json.dump(data, open("file.json", "w"))  # pylint: disable=unspecified-encoding
 
         view = views.ImportServerBlocklist.as_view()
         request = self.factory.post(
             "",
             {
                 "json_file": SimpleUploadedFile(
                    "file.json", open("file.json", "rb").read()
                 )
             },
         )
         created = models.FederatedServer.objects.get(server_name="server.name")
         self.assertEqual(created.status, "blocked")
         self.assertEqual(created.notes, "https://explanation.url")

        # remove file.json after test
        os.remove("file.json")