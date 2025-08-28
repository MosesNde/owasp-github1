 app.logger.setLevel(logging.INFO)
 
 def allowed_file(filename):
    """Allow all file types supported by ImageMagick."""
    return '.' in filename
 
 def get_image_dimensions(filepath):
     """Get image dimensions using appropriate tool based on file type."""
     try:
         if filepath.lower().endswith('.arw'):
             app.logger.info(f"Getting dimensions for ARW file: {filepath}")
            # Utiliser exiftool pour obtenir les dimensions de l'aperçu JPEG
            cmd = ['exiftool', '-s', '-s', '-s', '-PreviewImageLength', '-PreviewImageWidth', filepath]
            app.logger.info(f"Running exiftool command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
             
             if result.returncode == 0 and result.stdout.strip():
                app.logger.info(f"Exiftool output: {result.stdout}")
                # Essayer de parser les dimensions
                 dimensions = result.stdout.strip().split('\n')
                 if len(dimensions) == 2:
                     try:
                     except ValueError:
                         app.logger.warning("Could not parse dimensions from exiftool output")
                         pass
            else:
                app.logger.warning(f"Exiftool failed or no output: {result.stderr}")
             
            # Si on n'a pas pu obtenir les dimensions de l'aperçu, utiliser les dimensions connues
            app.logger.info("Using known dimensions for Sony A7 IV")
             return 7008, 4672  # Dimensions connues pour Sony A7 IV
         else:
            app.logger.info(f"Getting dimensions for non-ARW file: {filepath}")
            cmd = ['magick', 'identify', filepath]
            app.logger.info(f"Running ImageMagick command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
             if result.returncode != 0:
                 raise Exception(f"Error getting image dimensions: {result.stderr}")
             
            app.logger.info(f"ImageMagick output: {result.stdout}")
            # Parse the output to get dimensions
             match = re.search(r'\s(\d+)x(\d+)\s', result.stdout)
             if match:
                 width = int(match.group(1))
 
 def build_imagemagick_command(filepath, output_path, width, height, percentage, quality, keep_ratio):
     """Build ImageMagick command for resizing and formatting."""
    # Pour les fichiers RAW Sony ARW, on extrait le JPEG intégré
    if filepath.lower().endswith('.arw'):
        app.logger.info(f"Processing ARW file: {filepath}")
        # Créer un nom temporaire pour le fichier JPEG extrait
        temp_jpeg = os.path.join(os.path.dirname(output_path), f"{os.path.splitext(os.path.basename(filepath))[0]}_preview.jpg")
        app.logger.info(f"Temporary JPEG will be saved as: {temp_jpeg}")
        
        # Essayer d'abord JpgFromRaw (meilleure qualité)
        app.logger.info("Attempting to extract JpgFromRaw...")
        exif_cmd = ['exiftool', '-b', '-JpgFromRaw', filepath]
        app.logger.info(f"Running exiftool command: {' '.join(exif_cmd)}")
        result = subprocess.run(exif_cmd, capture_output=True)
        
        if result.returncode == 0 and result.stdout.strip():
            app.logger.info("Successfully extracted JpgFromRaw")
            # Sauvegarder le JPEG extrait
            with open(temp_jpeg, 'wb') as f:
                f.write(result.stdout)
            app.logger.info(f"Saved JpgFromRaw to: {temp_jpeg}")
        else:
            app.logger.info("No JpgFromRaw found, trying PreviewImage...")
            # Si pas de JpgFromRaw, essayer PreviewImage
            exif_cmd = ['exiftool', '-b', '-PreviewImage', filepath]
            app.logger.info(f"Running exiftool command: {' '.join(exif_cmd)}")
            result = subprocess.run(exif_cmd, capture_output=True)
            if result.returncode == 0 and result.stdout.strip():
                app.logger.info("Successfully extracted PreviewImage")
                with open(temp_jpeg, 'wb') as f:
                    f.write(result.stdout)
                app.logger.info(f"Saved PreviewImage to: {temp_jpeg}")
            else:
                app.logger.error(f"Exiftool error: {result.stderr.decode('utf-8', errors='ignore')}")
                raise Exception("No preview image found in RAW file")
        
        # Commande ImageMagick pour redimensionner le JPEG extrait
        magick_cmd = ['magick', temp_jpeg]
         
        # 1. Redimensionnement
        if width.isdigit() and height.isdigit():
            resize_value = f"{width}x{height}" if keep_ratio else f"{width}x{height}!"
            magick_cmd.extend(["-resize", resize_value])
            app.logger.info(f"Adding resize parameters: {resize_value}")
        elif percentage.isdigit() and 0 < int(percentage) <= 100:
            magick_cmd.extend(["-resize", f"{percentage}%"])
            app.logger.info(f"Adding percentage resize: {percentage}%")
            
        # 2. Qualité (si spécifiée)
        if quality.isdigit() and 1 <= int(quality) <= 100:
            magick_cmd.extend(["-quality", quality])
            app.logger.info(f"Setting quality to: {quality}")
             
        # 3. Conversion de format (utiliser un fichier temporaire PNG)
        temp_resized = os.path.join(os.path.dirname(output_path), "temp_resized.png")
        magick_cmd.append(temp_resized)
        app.logger.info(f"Saving resized image to temporary file: {temp_resized}")
        
        # 4. Deuxième commande pour la conversion finale
        convert_cmd = ['magick', temp_resized]
        if quality.isdigit() and 1 <= int(quality) <= 100:
            convert_cmd.extend(["-quality", quality])
        convert_cmd.append(output_path)
        app.logger.info(f"Final conversion command: {' '.join(convert_cmd)}")
        
        return None, [magick_cmd, convert_cmd], temp_jpeg
    else:
        app.logger.info(f"Processing non-ARW file: {filepath}")
        # Pour les autres formats, utiliser directement ImageMagick
        
        # 1. Commande de redimensionnement
        resize_cmd = ['magick', filepath]
         
        if width.isdigit() and height.isdigit():
            resize_value = f"{width}x{height}" if keep_ratio else f"{width}x{height}!"
            resize_cmd.extend(["-resize", resize_value])
            app.logger.info(f"Adding resize parameters: {resize_value}")
        elif percentage.isdigit() and 0 < int(percentage) <= 100:
            resize_cmd.extend(["-resize", f"{percentage}%"])
            app.logger.info(f"Adding percentage resize: {percentage}%")
             
        if quality.isdigit() and 1 <= int(quality) <= 100:
            resize_cmd.extend(["-quality", quality])
            app.logger.info(f"Setting quality to: {quality}")
             
        # Sauvegarder dans un fichier temporaire PNG
        temp_resized = os.path.join(os.path.dirname(output_path), "temp_resized.png")
        resize_cmd.append(temp_resized)
        app.logger.info(f"Saving resized image to temporary file: {temp_resized}")
         
        # 2. Commande de conversion de format
        convert_cmd = ['magick', temp_resized]
        if quality.isdigit() and 1 <= int(quality) <= 100:
            convert_cmd.extend(["-quality", quality])
        convert_cmd.append(output_path)
        app.logger.info(f"Final conversion command: {' '.join(convert_cmd)}")
         
        return None, [resize_cmd, convert_cmd], None
 
 @app.route('/')
 def index():
 @app.route('/upload_url', methods=['POST'])
 def upload_url():
     """Handle image upload from a URL."""
    url = request.form.get('url')
    if not url:
        return flash_error("No URL provided."), redirect(url_for('index'))

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, stream=True, headers=headers)
        response.raise_for_status()
 
        filename = url.split("/")[-1].split("?")[0]
        if not filename:
            return flash_error("Unable to determine a valid filename from the URL."), redirect(url_for('index'))
 
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
 
        flash(f"Image downloaded successfully: {filename}")
        return redirect(url_for('resize_options', filename=filename))
    except requests.exceptions.RequestException as e:
        return flash_error(f"Error downloading image: {e}"), redirect(url_for('index'))
 
 @app.route('/resize_options/<filename>')
 def resize_options(filename):
         app.logger.info(f"Output path: {output_path}")
         
         # Préparer et exécuter les commandes
        error, commands, temp_file = build_imagemagick_command(
             filepath=filepath,
             output_path=output_path,
             width=width,
             height=height,
             percentage=request.form.get('percentage', DEFAULTS["percentage"]),
             quality=request.form.get('quality', DEFAULTS["quality"]),
             keep_ratio=keep_ratio
        )
         
         if error:
             flash(error)
         # Exécuter les commandes en séquence
         for cmd in commands:
             app.logger.info(f"Running command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
             if result.returncode != 0:
                 app.logger.error(f"Command failed: {result.stderr}")
                 flash(f'Error during image processing: {result.stderr}')
         )
 
         try:
            subprocess.run(command[1], check=True)
             output_files.append(output_path)
         except Exception as e:
             flash_error(f"Error processing {filename}: {e}")