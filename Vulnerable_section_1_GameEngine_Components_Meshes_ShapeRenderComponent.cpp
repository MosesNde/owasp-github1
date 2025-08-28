 
 	resourceUpload.Begin();
 
		CreateShaderResourceView(pDevice, pTexture, m_pResourceDescriptors->GetCpuHandle(Descriptors::Earth));
 
 	RenderTargetState rtState(pDeviceResources->GetBackBufferFormat(),
 		pDeviceResources->GetDepthBufferFormat());