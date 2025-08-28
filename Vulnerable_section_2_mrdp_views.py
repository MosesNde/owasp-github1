         return redirect(url_for('graph'))
 
     # FIXME. Once the Auth API is patched to work with client ID/secret within
    # the body of the POST, replace `PORTAL_REFRESH_TOKEN_TRANSFER` with a
    # serialized refresh token (i.e. using `credentials.to_json()`) and use
    # the Google `oauth2client` library to get the access token here.
     #
     # FIXME. Consider moving the action of getting an access token from the
     # refresh token out of this route and to somewhere more global so that
                   refresh_token=app.config['PORTAL_REFRESH_TOKEN_TRANSFER']),
         headers=dict(Authorization=basic_auth_header()),
     ).json()['access_token']
     transfer = TransferClient(token=transfer_token)
 
     source_ep = app.config['DATASET_ENDPOINT_ID']
     source_info = transfer.get_endpoint(source_ep)
     source_https = source_info['https_server']
     source_base = app.config['DATASET_ENDPOINT_BASE']
    source_token = 'XXX'  # FIXME
 
     dest_ep = app.config['GRAPH_ENDPOINT_ID']
     dest_info = transfer.get_endpoint(dest_ep)
     dest_https = dest_info['https_server']
     dest_base = app.config['GRAPH_ENDPOINT_BASE']
     dest_path = '%sGraphs for %s/' % (dest_base, session['primary_username'])
    dest_token = 'XXX'  # FIXME
 
     if not (source_https and dest_https):
         flash("Both dataset and graph endpoints must be HTTPS endpoints.")
                                                    source_path, selected_year),
                                 verify=False,  # FIXME
                                 headers=dict(
                                    Authorization='Basic ' + source_token,
                                 ),
                                 allow_redirects=False)
         svgs.update(render_graphs(
                      data=svg,
                      verify=False,  # FIXME
                      headers=dict(
                        Authorization='Basic ' + dest_token,
                      ),
                      allow_redirects=False)
 
         endpoint_id = app.config['DATASET_ENDPOINT_ID']
         endpoint_path = app.config['DATASET_ENDPOINT_BASE'] + dataset['path']
 
     transfer = TransferClient(token=g.credentials.access_token)
 
     try: