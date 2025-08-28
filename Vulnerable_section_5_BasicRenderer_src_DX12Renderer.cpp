     SetSettings();
     LoadPipeline(hwnd, x_res, y_res);
     CreateGlobalResources();
	Menu::GetInstance().Initialize(hwnd, device, commandQueue);
 }
 
 void DX12Renderer::CreateGlobalResources() {