         client.get("/")
 
 
def test_staticfiles_prevents_breaking_out_of_directory(tmpdir):
     directory = os.path.join(tmpdir, "foo")
     os.mkdir(directory)
 
 
     app = StaticFiles(directory=directory)
     # We can't test this with 'httpx', so we test the app directly here.
    path = app.get_path({"path": "/../example.txt"})
     scope = {"method": "GET"}
 
     with pytest.raises(HTTPException) as exc_info: