         # get all data from t_feed
         feeds = T_Feed.objects.all()
         # get all feed file path from feeds.sid
        feed_file_paths = [os.path.join(settings.DATA_FOLDER, 'feeds', f'{feed.sid}.xml') for feed in feeds]
         merge_all_atom(feed_file_paths, "all_t")
 
         merge_file_path = os.path.join(settings.DATA_FOLDER, 'feeds', 'all_t.xml')
         response = StreamingHttpResponse(file_iterator(merge_file_path),
                                          content_type='application/xml')
        response['Content-Disposition'] = f'inline; filename="t"'
         logging.info("All Translated Feed file served: %s",  merge_file_path)
         return response
    except IOError as e:
         # Log the exception and return an appropriate error response
        logging.exception("Failed to read the feed file: %s / %s", settings.merge_file_path, str(e))
         return HttpResponse(status=500)
     
 @cache_page(60 * 15)  # Cache this view for 15 minutes
 def category(request, category:str):
     all_category = O_Feed.category.tag_model.objects.all()
     if category not in all_category:
         return HttpResponse(status=404)
     
     try:
        # get all data from t_feed
         feeds = T_Feed.objects.filter(o_feed__category__name=category)
        # get all feed file path from feeds.sid
        feed_file_paths = [os.path.join(settings.DATA_FOLDER, 'feeds', f'{feed.sid}.xml') for feed in feeds]
         merge_all_atom(feed_file_paths, category)
 
         merge_file_path = os.path.join(settings.DATA_FOLDER, 'feeds', f'{category}.xml')
         response = StreamingHttpResponse(file_iterator(merge_file_path),
                                          content_type='application/xml')
        response['Content-Disposition'] = f'inline; filename={category}'
         logging.info("Category Feed file served: %s",  merge_file_path)
         return response
    except IOError as e:
         # Log the exception and return an appropriate error response
        logging.exception("Failed to read the feed file: %s / %s", settings.merge_file_path, str(e))
         return HttpResponse(status=500)
 
 def file_iterator(file_name, chunk_size=8192):
     with open(file_name, 'rb') as f:
         while True: