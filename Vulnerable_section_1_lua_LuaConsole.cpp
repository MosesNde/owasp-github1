 		reinterpret_cast<IUnknown**>(&dw_factory)
 	);
 
	if(!create_composition_surface(d2d_overlay_hwnd, dc_size, &comp_device, &comp_target, &dxgi_swapchain, &d2d_factory, &d2d_device, &d3d_dc, &d2d_dc, &dxgi_surface, &dxgi_surface_resource, &front_buffer))
 	{
 		printf("Failed to set up composition\n");
 		return;
 	dxgi_swapchain->Release();
 	d2d_factory->Release();
 	d2d_device->Release();
 
 	DestroyWindow(gdi_overlay_hwnd);
 	SelectObject(gdi_back_dc, nullptr);