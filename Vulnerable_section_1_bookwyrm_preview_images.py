     site = models.SiteSettings.objects.get()
 
     if site.logo_small:
        logo_img = Image.open(site.logo_small)
     else:
         try:
             static_path = os.path.join(settings.STATIC_ROOT, "images/logo-small.png")
            logo_img = Image.open(static_path)
         except FileNotFoundError:
             logo_img = None
 
 
 def generate_rating_layer(rating, content_width):
     """Places components for rating preview"""
    try:
        icon_star_full = Image.open(
            os.path.join(settings.STATIC_ROOT, "images/icons/star-full.png")
        )
        icon_star_empty = Image.open(
            os.path.join(settings.STATIC_ROOT, "images/icons/star-empty.png")
        )
        icon_star_half = Image.open(
            os.path.join(settings.STATIC_ROOT, "images/icons/star-half.png")
        )
    except FileNotFoundError:
        return None
 
     icon_size = 64
     icon_margin = 10
 
     position_x = 0
 
    for _ in range(math.floor(rating)):
        rating_layer_mask.alpha_composite(icon_star_full, (position_x, 0))
        position_x = position_x + icon_size + icon_margin

    if math.floor(rating) != math.ceil(rating):
        rating_layer_mask.alpha_composite(icon_star_half, (position_x, 0))
        position_x = position_x + icon_size + icon_margin

    for _ in range(5 - math.ceil(rating)):
        rating_layer_mask.alpha_composite(icon_star_empty, (position_x, 0))
        position_x = position_x + icon_size + icon_margin
 
     rating_layer_mask = rating_layer_mask.getchannel("A")
     rating_layer_mask = ImageOps.invert(rating_layer_mask)
     texts = texts or {}
     # Cover
     try:
        inner_img_layer = Image.open(picture)
         inner_img_layer.thumbnail(
             (inner_img_width, inner_img_height), Image.Resampling.LANCZOS
         )