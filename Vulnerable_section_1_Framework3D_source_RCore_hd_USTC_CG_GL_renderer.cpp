 
 void Hd_USTC_CG_Renderer::Render(HdRenderThread* renderThread)
 {
     _completedSamples.store(0);
 
     // Commit any pending changes to the scene.
 
     if (!_ValidateAovBindings()) {
        // We aren't going to render anything. Just mark all AOVs as converged
        // so that we will stop rendering.
         for (size_t i = 0; i < _aovBindings.size(); ++i) {
             auto rb = static_cast<Hd_USTC_CG_RenderBufferGL*>(_aovBindings[i].renderBuffer);
             rb->SetConverged(true);
     // Fill the nodes that requires value from the scene.
     auto& executor = render_param->executor;
     auto& node_tree = render_param->node_tree;
 
     executor->prepare_tree(node_tree);
 
     for (auto&& node : node_tree->nodes) {
         auto try_fill_info = [&node, &executor](const char* id_name, void* data) {
         try_fill_info("render_scene_materials", render_param->materials);
     }
     executor->execute_tree(node_tree);
 
     TextureHandle texture = nullptr;
     for (auto&& node : node_tree->nodes) {
             break;
         }
     }
     if (texture) {
         for (size_t i = 0; i < _aovBindings.size(); ++i) {
             auto rb = static_cast<Hd_USTC_CG_RenderBufferGL*>(_aovBindings[i].renderBuffer);
             rb->Present(texture->texture_id);
             rb->SetConverged(true);
         }
     }
 
     executor->finalize(node_tree);
 }
 
 void Hd_USTC_CG_Renderer::Clear()