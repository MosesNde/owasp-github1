 
 #ifdef MFX_ENABLE_AI_VIDEO_FRAME_INTERPOLATION
     D3D11Interface* pD3d11 = QueryCoreInterface<D3D11Interface>(core);
     // Init
     xeAIVfiConfig config = {
         outInfo.Width, outInfo.Height,