 				string theme = this.GetNextPar();
 				this.context.setAjaxCallMode();
 				this.context.SetDefaultTheme(theme);
				string imagePath = this.context.GetImagePath(imageGUID, kbId, theme);
				if (!string.IsNullOrEmpty(imagePath))
 				{
					this.context.HttpContext.Response.Clear();
					this.context.HttpContext.Response.ContentType = MediaTypesNames.TextPlain;
 #if NETCORE
					this.context.HttpContext.Response.Write(imagePath);
 #else
					this.context.HttpContext.Response.Output.WriteLine(imagePath);
					
					this.context.HttpContext.Response.End();
 #endif
					return;
 				}
 			}
 			this.SendResponseStatus(404, "Resource not found");