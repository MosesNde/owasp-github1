 void RenderGraph::Execute(RenderContext& context) {
 	auto& manager = DeviceManager::GetInstance();
 	auto& queue = manager.GetCommandQueue();
     for (auto& batch : batches) {
         // Perform resource transitions
 		//TODO: If a pass is cached, we can skip the transitions, but we may need a new set