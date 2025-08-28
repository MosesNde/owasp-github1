 // @id              custom-desktop-watermark
 // @name            Custom Desktop Watermark
 // @description     Lets you set your own desktop watermark text
// @version         1.0.1
 // @author          aubymori
 // @github          https://github.com/aubymori
 // @include         explorer.exe
     );
     HFONT hTitleFont = CreateFontIndirectW(&ncm.lfCaptionFont);
     HFONT hMessageFont = CreateFontIndirectW(&ncm.lfMessageFont);
     int padding = MulDiv(3, dpi, 96);
     offset += MulDiv(g_bClassic ? 4 : 1, dpi, 96);
 
         ) + padding;
     }
 
     SetBkMode(hDC, bk);
     SetTextColor(hDC, cr);
 }