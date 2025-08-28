     sample_count--;
 }
 
/* quit_handler()
 * quit nicely on ^C.  That is: print the header and observation records
 * gathered so far.  Then exit.
 */
 static void quit_handler(int signum)
 {
    /* don't clutter the logs on Ctrl-C */
    if (signum != SIGINT)
        syslog(LOG_INFO, "exiting, signal %d received", signum);
    print_rinex_footer();
    (void)gps_close(&gpsdata);
    exit(EXIT_SUCCESS);
 }
 
 /* conditionally_log_fix()
     }
 
     for (;;) {
         /* wait for gpsd */
         if (!gps_waiting(&gpsdata, timeout * 1000000)) {
             (void)fprintf(stderr, "gpsrinex: timeout\n");
             syslog(LOG_INFO, "timeout;");
             break;
         }
         (void)gps_read(&gpsdata, NULL, 0);
         if (ERROR_SET & gpsdata.set) {
             fprintf(stderr, "gps_read() error '%s'\n", gpsdata.error);
             exit(6);
         }
         conditionally_log_fix(&gpsdata);
         if (0 >= sample_count) {
             /* done */
 
     // remove the temp file
     (void)unlink(tmp_fname);
     exit(EXIT_SUCCESS);
 }
 