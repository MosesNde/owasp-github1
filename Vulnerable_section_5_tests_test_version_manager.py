     
     # Test archive with invalid format
     archived = manager.archive_releases("TEST1")
    assert len(archived["TEST1"]) == 0  # Should skip invalid format versions
\ No newline at end of file
\ No newline at end of file