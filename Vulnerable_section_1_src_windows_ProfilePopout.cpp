 			if (hbm) {
 				hdc = GetDC(hWnd);
 				int pps = GetProfilePictureSize();
				m_hBitmap = ResizeWithBackgroundColor(
 					hdc,
 					hbm,
 					GetSysColorBrush(COLOR_3DFACE),
 				);
 				ReleaseDC(hWnd, hdc);
 				ShowWindow(hChild, SW_SHOW);
				SendMessage(hChild, STM_SETIMAGE, IMAGE_BITMAP, (LPARAM)m_hBitmap);
 			}
 			hChild = GetDlgItem(hWnd, IDC_GUILD_JOIN_DATE);
 			ShowWindow(hChild, SW_SHOW);
 
 		if (rcMemberSinceDiscord.bottom) {
 			int icsz = GetSystemMetrics(SM_CXSMICON);
			if (icsz <= 16) icsz = 16; // ensure a common size so LoadImage wont leak our LR_SHARED loaded icon
			else if (icsz <= 32) icsz = 32;
			else if (icsz <= 48) icsz = 48;
			else icsz = 64;
 			hChild = GetDlgItem(hWnd, IDC_ICON_DISCORD);
 			ShowWindow(hChild, SW_SHOW);
 			MoveWindow(hChild, pos.x, pos.y, joinedAtIconSize, joinedAtIconSize, TRUE);
			SendMessage(hChild, STM_SETIMAGE, IMAGE_ICON, (LPARAM) LoadImage(g_hInstance, MAKEINTRESOURCE(DMIC(IDI_ICON)), IMAGE_ICON, icsz, icsz, LR_SHARED | LR_CREATEDIBSECTION));
 			hChild = GetDlgItem(hWnd, IDC_DISCORD_JOIN_DATE);
 			ShowWindow(hChild, SW_SHOW);
 			SetWindowText(hChild, dscJoinedAt);
 			return res;
 		}
 
		case WM_DESTROY:
 			FlushNote();
 
 			m_hwnd = NULL;
 			SAFE_DELETE(m_pRoleList);
 			SAFE_DELETE(m_pProfileView);
 
 			if (m_hBitmap) {
				DeleteBitmap(m_hBitmap);
 				m_hBitmap = NULL;
 			}
 			return TRUE;
 	}
 
 	return FALSE;