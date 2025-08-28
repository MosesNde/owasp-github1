 				if (msg.has_suppress() && ! pSrc) {
 				}
 				else if (msg.has_deaf() && pDst->bDeaf)
					g.l->log(Log::YouMuted, tr("%1 deafened by %2.").arg(vic).arg(admin));
 				else if (msg.has_mute() && pDst->bMute)
					g.l->log(Log::YouMuted, tr("%1 muted by %2.").arg(vic).arg(admin));
 				else if (msg.has_suppress() && ! pDst->bSuppress)
					g.l->log(Log::YouMuted, tr("%1 unsuppressed by %2.").arg(vic).arg(admin));
 				else
					g.l->log(Log::YouMuted, tr("%1 unmuted by %2.").arg(vic).arg(admin));
 			}
 		}
 	}