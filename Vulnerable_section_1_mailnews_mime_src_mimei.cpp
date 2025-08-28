   }
 
   object = (MimeObject*)PR_MALLOC(size);
  if (!object) return 0;
 
   memset(object, 0, size);
   object->clazz = clazz;