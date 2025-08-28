 				return KErrAccessDenied;
 			}
 			item.text = aMessage.text;
			UpdateL(item.uid);
			return KErrNone;
 		}
 		return KErrNotFound;
 	}
 	result = session.GetAppInfo(appInfo, uid);
 	
 	if (result != KErrNone || appInfo.iUid != uid) {
 		return;
 	}
 	
 	CApaCommandLine* cli = CApaCommandLine::NewL();
 	cli->SetExecutableNameL(appInfo.iFullName);
 	session.StartApp(*cli);
 	delete cli;
 }
 
 TBool NotifyApp(TNotificationItem item)
 	}
 	
 	if (session.SendMessage(item.uid) != KErrNone) {
 		return EFalse;
 	}
 	