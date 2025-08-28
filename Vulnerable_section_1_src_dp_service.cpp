 	return NULL;
 }
 
static int dp_add_args(int argc, char **argv)
 {
	int i, j, pos = 0;
 
	dp_argv = (char**)calloc(argc + 4, sizeof(*dp_argv));
	if (dp_argv == NULL)
		return -1;
 
 	for (i = 0; i < argc; i++) {
 		if (strcmp(argv[i], "--") == 0) {
			pos = i;
 			break;
 		} else {
			dp_argv[i] = strdup(argv[i]);
 		}
 	}
	if (pos == 0)
		return -1;
	dp_argv[i] = strdup("-a");
	dp_argv[++i] = dp_get_pf0_opt_a();
	dp_argv[++i] = strdup("-a");
	dp_argv[++i] = dp_get_pf1_opt_a();
	dp_argv[++i] = strdup("--");

	for (j = pos + 1; j < argc; j++)
		dp_argv[++i] = strdup(argv[j]);

	dp_argv[++i] = NULL;
 	dp_argc = i;
 
	return 0;
 }
 
 static void dp_init_interfaces()
 	int ret;
 
 	dp_handle_conf_file();
	if (dp_is_mellanox_opt_set()) {
		if (dp_add_args(argc, argv) < 0)
			rte_exit(EXIT_FAILURE, "Invalid dp_service parameters in config file\n");
		argc = dp_argc;
		argv = dp_argv;
	}
 	ret = dp_dpdk_init(argc, argv);
 	argc -= ret;
 	argv += ret;
 	ret = rte_ctrl_thread_create(dp_get_ctrl_thread_id(), "grpc-thread", NULL,
 							dp_handle_grpc, NULL);
 	if (ret < 0)
		rte_exit(EXIT_FAILURE,
				"Cannot create grpc thread\n");
 
 	dp_dpdk_main_loop();
 
 	pthread_join(*dp_get_ctrl_thread_id(), NULL);
 
 	dp_dpdk_exit();
 
 	return 0;
 }