                                                    do_display && display_part);
       MimeHeaders_free(malt->buffered_hdrs[i]);
       MimePartBufferDestroy(malt->part_buffers[i]);
     }
     malt->pending_parts = 0;
   }