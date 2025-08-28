         """Verify we pass along Synapse auth headers when downloading from a Synapse repo hosted url"""
 
         uri = f"{self.syn.repoEndpoint}/repo/v1/entity/syn1234567/file"
        in_destination = tempfile.mktemp()

         mock_credentials = mocker.patch.object(self.syn, 'credentials')
 
         response = MagicMock(spec=requests.Response)
         mock_get = mocker.patch.object(self.syn._requests_session, 'get')
         mock_get.return_value = response
 
        out_destination = self.syn._download_from_URL(uri, in_destination)
         assert mock_get.call_args[1]['auth'] is mock_credentials
        assert os.path.normpath(out_destination) == os.path.normpath(in_destination)
 
     def test_download_from_url__external(self, mocker):
         """Verify we do not pass along Synapse auth headers to a file download that is a not Synapse repo hosted"""
 
         uri = "https://not-synapse.org/foo/bar/baz"
        in_destination = tempfile.mktemp()

         mocker.patch.object(self.syn, 'credentials')
 
         response = MagicMock(spec=requests.Response)
         mock_get = mocker.patch.object(self.syn._requests_session, 'get')
         mock_get.return_value = response
 
        out_destination = self.syn._download_from_URL(uri, in_destination)
         assert mock_get.call_args[1]['auth'] is None
        assert os.path.normpath(out_destination) == os.path.normpath(in_destination)
 
     @patch.object(Synapse, '_getFileHandleDownload')
     def test_downloadFileHandle_preserve_exception_info(self, mock_getFileHandleDownload):