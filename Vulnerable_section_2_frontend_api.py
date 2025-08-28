 import core.scans as scan
 import base64
 
def view(query, allargs):
 
     if query == 'dlanalysis':
         try:
             extension_id = allargs.get('extid')
                 download_log = download_extension.download(extension_id, saveas)
                 if download_log:
                     aok = analysis.analyze(saveas + '.crx', 'Remote Google Chrome Extension')
                    return(aok)
                 else:
                    return('error: Something went wrong while downloading extension')
             except Exception as e:
                 core.updatelog('Something went wrong while downloading extension: ' + str(e))
                return('error: Something went wrong while downloading extension, check log for more information')
 
         except Exception as e:
             core.updatelog('Something went wrong: ' + str(e))
            return('error: Something went wrong while downloading extension, check log for more information')
    
 
 
     elif query == 'firefoxaddon':
                 download_log = download_extension.downloadFirefox(addonurl)
                 if download_log:
                     aok = analysis.analyze(download_log + '.xpi', 'Remote Firefox Addon')
                    return(aok)
                 else:
                    return('error: Something went wrong while downloading extension')
             except Exception as e:
                 core.updatelog('Something went wrong while downloading extension: ' + str(e))
                return('error: Something went wrong while downloading extension, check log for more information')
         except Exception as e:
             core.updatelog('Something went wrong: ' + str(e))
            return('error: Something went wrong while downloading extension, check log for more information')
 
 
 
             report_id = areport['id']
             report_date = areport['time']
             report_version = areport['version']
            rd += '<tr><td>'+report_name+'</td><td>'+report_version+'</td><td>'+report_date+'</td><td><button class="bttn-fill bttn-xs bttn-primary" onclick=viewResult(\'' + report_id + '\')><i class="fas fa-eye"></i> View</button> <button class="bttn-fill bttn-xs bttn-danger" onclick=deleteResult(\'' + report_id + '\')><i class="fas fa-trash"></i> Delete</button></td></tr>'
        return(rd + '</tbody></table><br>')
 
 
 
                     return_html = "<table class='result-table' id='result-table'><thead><tr><th>Extension Name</th><th>Action</th></tr></thead><tbody>"
                     for ext in exts:
                         ext_info = ext.split(',')
                        return_html += '<tr><td>' + ext_info[0] + '</td><td><button class="bttn-fill bttn-xs bttn-success" onclick="analyzeLocalExtension(\'' + ext_info[1].replace('\\', '\\\\') + '\', \'googlechrome\')"><i class="fas fa-bolt"></i> Analyze</button></td></tr>'
                     return (return_html + '</tbody></table>')
                 else:
                    return('error: Something went wrong while getting local Google Chrome extensions! Check log for more information')
             elif browser == 'firefox':
                 import core.localextensions as localextensions
                 lexts = localextensions.GetLocalExtensions()
                     return_html = "<table class='result-table' id='result-table'><thead><tr><th>Extension Name</th><th>Action</th></tr></thead><tbody>"
                     for ext in exts:
                         ext_info = ext.split(',')
                        return_html += '<tr><td>' + ext_info[0] + '</td><td><button class="bttn-fill bttn-xs bttn-success" onclick="analyzeLocalExtension(\'' + ext_info[1].replace('\\', '\\\\') + '\', \'firefox\')"><i class="fas fa-bolt"></i> Analyze</button></td></tr>'
                     return (return_html + '</tbody></table>')
                 else:
                    return('error: Something went wrong while getting local firefox extensions! Check log for more information')
             elif browser == 'brave':
                 import core.localextensions as localextensions
                 lexts = localextensions.GetLocalExtensions()
                     return_html = "<table class='result-table' id='result-table'><thead><tr><th>Extension Name</th><th>Action</th></tr></thead><tbody>"
                     for ext in exts:
                         ext_info = ext.split(',')
                        return_html += '<tr><td>' + ext_info[0] + '</td><td><button class="bttn-fill bttn-xs bttn-success" onclick="analyzeLocalExtension(\'' + ext_info[1].replace('\\', '\\\\') + '\', \'brave\')"><i class="fas fa-bolt"></i> Analyze</button></td></tr>'
                     return (return_html + '</tbody></table>')
                 else:
                    return('error: Something went wrong while getting local Brave browser extensions! Check log for more information')
             else:
                return('error: Invalid Browser!')
         except Exception:
             logging.error(traceback.format_exc())
            return('error: Incomplete Query')
 
 
 
             browser = allargs.get('browser')
             path_to_local = allargs.get('path')
             path = helper.fixpath(path_to_local)
            
             if browser == 'firefox' and os.path.isfile(path):
                 # valid firefox extension
                 import core.localextensions as localextensions
                 analysis_stat = localextensions.analyzelocalfirefoxextension(path)
                return(analysis_stat)
 
             elif browser == 'googlechrome' and os.path.isdir(path):
                 if os.path.isfile(os.path.join(path, 'manifest.json')):
                     analysis_stat = analysis.analyze(path, 'Local Google Chrome Extension')
                    return(analysis_stat)
                 else:
                    return('error: Invalid Google Chrome Extension Directory')
            
             elif browser == 'brave' and os.path.isdir(path):
                 if os.path.isfile(os.path.join(path, 'manifest.json')):
                     analysis_stat = analysis.analyze(path, 'Local Brave browser Extension')
                    return(analysis_stat)
                 else:
                    return('error: Invalid Brave Extension Directory')
 
             else:
                return('error: Malformed Query')
         except Exception:
             logging.error(traceback.format_exc())
            return('error: Incomplete Query')
 
 
     elif query == 'deleteAll':
         if delete_status:
             return "success"
         else:
            return('There were some errors while deleting all analysis reports... refer to log for more information')
 
     elif query == 'clearLab':
         '''
         clear_lab = core.clear_lab()
         if clear_lab[0]:
             # Successful
            return(clear_lab[1])
         else:
             # Unsuccessful
             return ('error: ' + clear_lab[1])
             else:
                 return "Something went wrong while deleting result! Check log for more information"
         except Exception:
            return('Invalid Query')
    
 
     elif query == 'vtDomainReport':
         try:
                     for adomain in domains:
                         if adomain['name'] == domain:
                             vtjson = json.dumps(adomain['virustotal'], indent=4, sort_keys=False)
                            #return_html = '<div id="vt_info"></div><script>var wrapper1 = document.getElementById("vt_info");var data = '+vtjson+' try {var data = JSON.parse(dataStr);} catch (e) {} var tree = jsonTree.create(data, wrapper1);tree.expand(function(node) {   return node.childNodes.length < 2 || node.label === "phoneNumbers";});</script>'
                             return vtjson
                    return('error: Domain info not found in analysis report!')
                 else:
                    return('error: Analysis report for #{0} not found'.format(analysis_id))
             else:
                 # ranalysis[1] is the error msg when ranalysis[0] = False
                return('error: ' + ranalysis[1])
         except:
             logging.error(traceback.format_exc())
            return('error: Malformed api call')
 
     elif query == 'retirejsResult':
         '''
                             else:
                                 ret = json.dumps(retirejs_result, indent=4, sort_keys=False)
                             return ret
                    return('error: File ID not found in report!')
                 else:
                    return('error: Analysis report for #{0} not found'.format(analysis_id))
             else:
                 # ranalysis[1] is the error msg when ranalysis[0] = False
                return('error: ' + ranalysis[1])
         except:
             logging.error(traceback.format_exc())
            return('error: Malformed api call')
 
     elif query == 'whois':
         '''
             try:
                 import whois
             except:
                return("error: python-whois module not installed! install it using `pip3 install python-whois` or `pip3 install -r requirements.txt`")
             whois_result = whois.whois(domain)
             whois_html = '<div class="whois-data" style="overflow-y: scroll; max-height:500px; text-align: left;">'
             for data in whois_result:
                     whois_html += '<b style="color:#89ff00;">{0} : </b>{1}<br>'.format(proper_data, whois_result[data])
             whois_html += '</div>'
             if whois_result:
                return('<center><h4>Whois Results For {0}</h4></center><br>{1}'.format(domain, whois_html))
             else:
                return("error: Something went wrong while checking whois information of: " + domain)
         except Exception:
             logging.error(traceback.format_exc())
            return('error: Invalid Query')
 
    
     elif query == 'geoip':
         '''
         GEO-IP LOOKUP OF AN IP ADDRESS
                     val = str(gip[g])
                     rethtml += '<b style="color:#89ff00;">{0} : </b>{1}<br>'.format(name, val)
                 rethtml += '</div>'
                return('<center><h4>Geo-IP Lookup Results For {0}</h4></center><br>{1}'.format(ip_address, rethtml))
 
             else:
                 # in case of geo_ip[0] being false element 1 has the error msg
                return('error: ' + geo_ip[1])
 
         except Exception as e:
             logging.error(traceback.format_exc())
            return('error: Invalid Query')
 
 
     elif query == 'HTTPHeaders':
                     hval = headers[header]
                     rethtml += '<b style="color:#89ff00;">{0} : </b>{1}<br>'.format(header, hval)
                 rethtml += '</div>'
                return('<center><h4>Showing HTTP Headers of: {0}</h4></center><br>{1}'.format(url, rethtml))
             else:
                return('error: ' + headers_status[1])
         except Exception as e:
             logging.error(traceback.format_exc())
            return('error: Invalid Query')
 
     elif query == 'SourceCode':
         '''
                 rethtml = '<textarea id="src_code" class="source_code" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">'
                 headers = headers_status[1]
                 rethtml += headers
                rethtml += '</textarea><br><br><center><a href="{0}" target="_blank" class="start_scan"><i class="fas fa-external-link-alt"></i> View Full Screen</a>'.format('/source-code/'+ url)
                return('<center><h4>Source Code of: {0}</h4></center><br>{1}'.format(rurl, rethtml))
             else:
                return('error: ' + headers_status[1])
         except Exception as e:
             logging.error(traceback.format_exc())
            return('error: Invalid Query')
 
 
     elif query == 'clearlogs':
         '''
         CLEARS LOG
         '''
         core.clearlog()
        return('Logs cleared successfully!')
 
 
 
                 import core.settings as settings
                 change = settings.changedir(absolute_path)
                 if change[0]:
                    return(change[1])
                 else:
                    return('error: ' + change[1])
             else:
                return('error: Invalid directory path!')
         except:
             logging.error(traceback.format_exc())
            return('error: Invalid request for directory change!')
 
     elif query == 'changeVTapi':
         '''
             import core.settings as settings
             change = settings.change_vt_api(new_api)
             if change[0]:
                return(change[1])
             else:
                return('error: ' + change[1])
         except:
             logging.error(traceback.format_exc())
            return('error: Invalid request!')
 
     elif query == 'changelabDir':
         '''
                 import core.settings as settings
                 change = settings.changelabdir(absolute_path)
                 if change[0]:
                    return(change[1])
                 else:
                    return('error: ' + change[1])
             else:
                return('error: Invalid directory path!')
         except:
             logging.error(traceback.format_exc())
            return('error: Invalid request for directory change!')
 
     elif query == 'updateIntelExtraction':
         '''
             parameters["extract_ipv4_addresses"] = str(allargs.get('extract_ipv4_addresses'))
             parameters["extract_ipv6_addresses"] = str(allargs.get('extract_ipv6_addresses'))
             parameters["ignore_css"] = str(allargs.get('ignore_css'))
            
             import core.settings as settings
             status_code = settings.update_settings_batch(parameters)
             # 0 = failed, 1 = success, 2 = some updated some not!
             if status_code == '0':
                return('error: Settings could not be updated! Check log for more information')
             elif status_code == '1':
                return('Settings updated successfully... Please restart ExtAnalysis for them to take effect!')
             elif status_code == '2':
                return('Some settings were updated and some were not... Please restart ExtAnalysis for them to take effect!')
             else:
                return('error: Invalid response from "update_settings_batch". please report it here: https://github.com/Tuhinshubhra/ExtAnalysis/issues/new')
         except:
             logging.error(traceback.format_exc())
            return('error: Incomplete Request!')
            
     else:
        return('error: Invalid Query!')
\ No newline at end of file
\ No newline at end of file