 	{
 		CleanupDirectX();
 
 		delete	m_pDevice;
 		delete	m_pDeviceContext;
 		delete	m_pSwapChain;
 	void Renderer::CleanupDirectX()
 	{
 		// Clear state and flush the device context before releasing DeviceContext
		if (m_pDeviceContext)
		{
			m_pDeviceContext->ClearState();
			m_pDeviceContext->Flush();
		}
 
 		// Release the resources in reverse order of creation
		if (m_pRenderTargetView)
		{
			m_pRenderTargetView->Release();
			m_pRenderTargetView = nullptr;
		}

		if (m_pRenderTargetBuffer)
		{
			m_pRenderTargetBuffer->Release();
			m_pRenderTargetBuffer = nullptr;
		}
 
 		if (m_pDepthStencilView)
 		{
 			m_pDepthStencilBuffer = nullptr;
 		}
 
 		if (m_pSwapChain)
 		{
 			m_pSwapChain->Release();
 
 		if (m_pDeviceContext)
 		{
 			m_pDeviceContext->Release();
 			m_pDeviceContext = nullptr;
 		}