 
   IGL_PROFILER_FUNCTION_COLOR(IGL_PROFILER_COLOR_CREATE);
 
  // @fb-only
  const VkDescriptorSetLayout DSLs[] = {
      dslCombinedImageSamplers_->getVkDescriptorSetLayout(),
      dslBuffers_->getVkDescriptorSetLayout(),
      dslStorageImages_->getVkDescriptorSetLayout(),
      ctx.getBindlessVkDescriptorSetLayout(),
  };

  const VkPipelineLayoutCreateInfo ci =
      ivkGetPipelineLayoutCreateInfo(static_cast<uint32_t>(ctx.config_.enableDescriptorIndexing
                                                               ? IGL_ARRAY_NUM_ELEMENTS(DSLs)
                                                               : IGL_ARRAY_NUM_ELEMENTS(DSLs) - 1u),
                                     DSLs,
                                     info_.hasPushConstants ? &pushConstantRange_ : nullptr);

  VkDevice device = ctx.device_->getVkDevice();
  VK_ASSERT(ctx.vf_.vkCreatePipelineLayout(device, &ci, nullptr, &pipelineLayout_));
  VK_ASSERT(
      ivkSetDebugObjectName(&ctx.vf_,
                            device,
                            VK_OBJECT_TYPE_PIPELINE_LAYOUT,
                            (uint64_t)pipelineLayout_,
                            IGL_FORMAT("Pipeline Layout: {}", desc_.debugName.c_str()).c_str()));
 
   const auto& deviceFeatures = ctx.features();
   const VkBool32 dualSrcBlendSupported =