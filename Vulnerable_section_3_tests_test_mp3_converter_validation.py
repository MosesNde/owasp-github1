             "app.v1.routes.AudioFileClip"
         ) as mock_audio_file_clip, patch(
             "os.remove"
        ), patch(
             "builtins.open",
             mock_open(read_data=b"mocked file content"),
         ), patch(
             mock_boto_client.return_value = mock_s3
             mock_s3.upload_fileobj.side_effect = MagicMock()
 
             # Make the POST request
             response = client.post(
                 "/v1/convert?yturl=https://www.youtube.com/watch?v=J7ub9NqadNA&user=1&project=1"