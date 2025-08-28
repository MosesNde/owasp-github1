 import dataclasses
 import json
 import logging
 from datetime import datetime
 from pathlib import Path
 from typing import Any, Literal, Optional
             return _validate_question_llm(conversation_id, llm_request)
 
 
 def store_transcript(
     user_id: str,
     conversation_id: str,
         truncated: The flag indicating if the history was truncated.
     """
     # ensures storage path exists
    transcripts_path = Path(
        config.ols_config.user_data_collection.transcripts_storage,
        user_id,
        conversation_id,
    )
     if not transcripts_path.exists():
         logger.debug(f"creating transcript storage directory '{transcripts_path}'")
         transcripts_path.mkdir(parents=True)