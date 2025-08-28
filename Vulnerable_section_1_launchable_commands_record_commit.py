     https_proxy = os.getenv("HTTPS_PROXY")
     proxy_option = _build_proxy_option(https_proxy) if https_proxy else ""
 
    subprocess.check_output("{java} {proxy_option} -jar \"{jar_file_path}\" ingest:commit -endpoint {endpoint} -max-days {max_days} {audit} {scrub_pli} {dry_run} {source}"
                            .format(
                                java=java,
                                proxy_option=proxy_option,
                                jar_file_path=jar_file_path,
                                endpoint="{}/intake/".format(base_url),
                                max_days=max_days,
                                audit="-audit" if Logger().logger.isEnabledFor(LOG_LEVEL_AUDIT) else "",
                                scrub_pli="-scrub-pii",
                                dry_run="-dry-run" if dry_run else "",
                                source=source),
                            shell=True)
 
 
 def _build_proxy_option(https_proxy: str) -> str: