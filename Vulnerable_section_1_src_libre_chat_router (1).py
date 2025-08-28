 from dataclasses import dataclass
 from typing import Any, Dict, List, Optional, Union
 
 from fastapi import APIRouter, Body, File, HTTPException, Request, UploadFile, WebSocket
 from fastapi.responses import JSONResponse
 from langchain.callbacks.base import AsyncCallbackHandler
                 )
             for uploaded in files:
                 if uploaded.filename:  # no cov
                    file_path = os.path.join(self.conf.vector.documents_path, uploaded.filename)
                     with open(file_path, "wb") as file:
                         file.write(uploaded.file.read())
                     # Check if the uploaded file is a zip file