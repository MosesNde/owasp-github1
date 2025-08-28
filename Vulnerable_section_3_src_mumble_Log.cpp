 		} else if (! g.mw->qteLog->document()->isEmpty()) {
 			tc.insertBlock();
 		}
		tc.insertHtml(QString::fromLatin1("[%2] %1\n").arg(console).arg(now.toString(Qt::LocalDate)));
 		tc.movePosition(QTextCursor::End);
 		g.mw->qteLog->setTextCursor(tc);
 		g.mw->qteLog->ensureCursorVisible();