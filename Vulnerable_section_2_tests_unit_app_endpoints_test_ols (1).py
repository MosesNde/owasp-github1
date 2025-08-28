         assert list(transcript_dir.glob("*/*/*.json")) == []
 
 
 def test_store_transcript(transcripts_location):
     """Test transcript is successfully stored."""
     user_id = suid.get_suid()