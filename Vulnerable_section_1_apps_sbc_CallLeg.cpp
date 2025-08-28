   }
   else b.media_session = NULL;
 
  ReconnectLegEvent *rev = new ReconnectLegEvent(a_leg ? ReconnectLegEvent::B : ReconnectLegEvent::A, getLocalTag(), hdrs, dlg->established_body);
   rev->setMedia(b.media_session, rtp_relay_mode);
  ReplaceLegEvent *ev = new ReplaceLegEvent(getLocalTag(), rev);
   // TODO: what about the RTP relay and other settings? send them as well?
  if (!AmSessionContainer::instance()->postEvent(session_tag, ev)) {
     // session doesn't exist - can't connect
     ILOG_DLG(L_INFO, "the call leg to be replaced (%s) doesn't exist\n", session_tag.c_str());
     if (b.media_session) {