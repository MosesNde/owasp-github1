 
                 output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), type)
                 if "subfolder" in request.rel_url.query:
                    output_dir = os.path.join(output_dir, request.rel_url.query["subfolder"])
 
                 file = request.rel_url.query["file"]
                 file = os.path.basename(file)
                 file = os.path.join(output_dir, file)
                 if os.path.isfile(file):
                     return web.FileResponse(file)
                 