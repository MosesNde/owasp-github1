 from auth import AuthHandler
 from models import AuthDetails
 
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
 
 app.mount("/static", StaticFiles(directory="static"), name="static")
 templates = Jinja2Templates(directory="templates")
 
 @app.post("/api/upload")
 async def upload_file(folder: Optional[str] = None, file: UploadFile = File(...), _=Depends(auth_handler.auth_wrapper)):
    file_location = get_file_path(file.filename, folder)
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return {"filename": file.filename}
 
 
 @app.post("/api/create_folder")
 async def create_folder(folder_name: str, folder: Optional[str] = None, _=Depends(auth_handler.auth_wrapper)):
    folder_path = get_file_path(folder_name, folder)
    if os.path.exists(folder_path):
        raise HTTPException(status_code=400, detail="Folder already exists")
    os.makedirs(folder_path)
    return {"message": f"Folder {folder_name} created successfully"}
 
 
 @app.get("/api/files")
 async def list_files(folder: Optional[str] = None, _=Depends(auth_handler.auth_wrapper)):
    path = get_file_path("", folder)
    files = os.listdir(path)
    return {"files": files}
 
 
 @app.delete("/api/files/{filename}")
 async def delete_file(filename: str, folder: Optional[str] = None, _=Depends(auth_handler.auth_wrapper)):
    file_path = get_file_path(filename, folder)
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)
        return {"message": f"File {filename} deleted successfully"}
     raise HTTPException(status_code=404, detail="File not found")
 
 
 @app.put("/api/rename/{old_name}")
 async def rename_file(old_name: str, new_name: str, folder: Optional[str] = None, _=Depends(auth_handler.auth_wrapper)):
    old_path = get_file_path(old_name, folder)
    new_path = get_file_path(new_name, folder)
    if not os.path.exists(old_path):
        raise HTTPException(status_code=404, detail="File not found")
    if os.path.exists(new_path):
        raise HTTPException(status_code=400, detail="File with new name already exists")
    os.rename(old_path, new_path)
    return {"message": f"File renamed from {old_name} to {new_name} successfully"}
 
 
 @app.post("/api/generate-temp-token/{filename}")
 async def generate_temp_token(filename: str, folder: Optional[str] = None, _=Depends(auth_handler.auth_wrapper)):
    check_path = get_file_path("", folder)
    if filename not in os.listdir(check_path):
        raise HTTPException(status_code=404, detail="File not found")
    temp_token = auth_handler.encode_temp_token(filename)
    return {"temp_token": temp_token}
 
 
 @app.get("/public/{filename}")
             raise HTTPException(status_code=400, detail="Invalid token for this file")
     except HTTPException:
         raise HTTPException(status_code=400, detail="Invalid or expired token")
    file_path = get_file_path(filename, folder)
    if os.path.exists(file_path) and not os.path.isdir(file_path):
        return FileResponse(file_path)
     raise HTTPException(status_code=404, detail="File not found")
 
 
         file_path = get_file_path(filename, folder)
         if os.path.exists(file_path):
             return FileResponse(file_path)
    except Exception as e:
         raise HTTPException(status_code=400, detail=f"Invalid or expired token")
     raise HTTPException(status_code=404, detail="File not found")
 
 
 @app.get("/api/preview/{filename}")
 async def get_file_preview(filename: str, folder: Optional[str] = None, _=Depends(auth_handler.auth_wrapper)):
    file_path = get_file_path(filename, folder)
     if not os.path.exists(file_path):
         raise HTTPException(status_code=404, detail="File not found")
 
     _, file_extension = os.path.splitext(filename)
     if file_extension.lower() not in ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.sh']:
         raise HTTPException(status_code=400, detail="File type not supported for preview")