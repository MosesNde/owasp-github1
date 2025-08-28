             "app.v1.routes.AudioFileClip"
         ) as mock_audio_file_clip, patch(
             "os.remove"
        ), patch(
             "builtins.open",
             mock_open(read_data=b"mocked file content"),
         ), patch(
             mock_boto_client.return_value = mock_s3
             mock_s3.upload_fileobj.side_effect = MagicMock()
 
             # Mock the update_db function to simulate a successful database update
             mock_update_db.return_value = (
                 False,
             "app.v1.routes.AudioFileClip"
         ) as mock_audio_file_clip, patch(
             "os.remove"
        ), patch(
             "builtins.open",
             mock_open(read_data=b"mocked file content"),
         ), patch(
             mock_boto_client.return_value = mock_s3
             mock_s3.upload_fileobj.side_effect = MagicMock()
 
             # Mock the update_db function to simulate a successful database update
             mock_update_db.return_value = (
                 False,
             "app.v1.routes.AudioFileClip"
         ) as mock_audio_file_clip, patch(
             "os.remove"
        ), patch(
             "builtins.open",
             mock_open(read_data=b"mocked file content"),
         ), patch(
             mock_boto_client.return_value = mock_s3
             mock_s3.upload_fileobj.side_effect = MagicMock()
 
             # Set side_effect to return True on the first call and False on the second call
             mock_update_db.side_effect = [
                 (True, "Success"),
             "app.v1.routes.AudioFileClip"
         ) as mock_audio_file_clip, patch(
             "os.remove"
        ), patch(
             "builtins.open",
             mock_open(read_data=b"mocked file content"),
         ), patch(
             mock_boto_client.return_value = mock_s3
             mock_s3.upload_fileobj.side_effect = MagicMock()
 
             # Set side_effect to return True on the first call and False on the second call
             mock_update_db.side_effect = [
                 (True, "Success"),
             "app.v1.routes.AudioFileClip"
         ) as mock_audio_file_clip, patch(
             "os.remove"
        ), patch(
             "builtins.open",
             mock_open(read_data=b"mocked file content"),
         ), patch(
             mock_boto_client.return_value = mock_s3
             mock_s3.upload_fileobj.side_effect = MagicMock()
 
             # Configure `update_db` to raise an IntegrityError
             mock_session.add.side_effect = IntegrityError(
                 "Integrity error", None, None
             "app.v1.routes.AudioFileClip"
         ) as mock_audio_file_clip, patch(
             "os.remove"
        ), patch(
             "builtins.open",
             mock_open(read_data=b"mocked file content"),
         ), patch(
             mock_boto_client.return_value = mock_s3
             mock_s3.upload_fileobj.side_effect = MagicMock()
 
             # Configure `update_db` to raise an IntegrityError
             mock_session.add.side_effect = Exception
 