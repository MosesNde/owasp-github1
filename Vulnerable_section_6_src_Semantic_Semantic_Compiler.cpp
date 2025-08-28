     node->byteCodeFct = ByteCodeGen::emitDebugNop;
     expr->addAstFlag(AST_NO_BYTECODE);
 
    const auto typeCode = castTypeInfo<TypeInfoCodeBlock>(expr->typeInfo, TypeInfoKind::CodeBlock);
    SWAG_ASSERT(typeCode->content);
 
     CloneContext cloneContext;
     cloneContext.parent                 = node;
     cloneContext.removeFlags            = AST_R_VALUE;
     cloneContext.ownerFct               = node->ownerFct;
     cloneContext.cloneFlags             = CLONE_INJECT;
    const auto cloneContent             = typeCode->content->clone(cloneContext);
 
     if (node->hasAstFlag(AST_DISCARD))
         Ast::setDiscard(cloneContent);
 
     // In case the injected code has references to parameters of an inlined function,
     // we need to be sure that the parameter scope is covered
     SWAG_ASSERT(node->ownerInline());
    if (typeCode->content->ownerFct->hasAttribute(ATTRIBUTE_INLINE))
     {
         auto inlineNode = node->ownerInline();
        while (inlineNode && inlineNode->func != typeCode->content->ownerFct && inlineNode->hasOwnerInline())
             inlineNode = inlineNode->ownerInline();
         if (inlineNode && inlineNode->parametersScope)
             cloneContent->addAlternativeScope(inlineNode->parametersScope);
     }
 
    cloneContent->addExtraPointer(ExtraPointerKind::AlternativeNode, typeCode->content->parent);
    cloneContent->addAlternativeScope(typeCode->content->parent->ownerScope);
     cloneContent->removeAstFlag(AST_NO_SEMANTIC | AST_NO_BYTECODE);
     node->typeInfo = cloneContent->typeInfo;
     context->baseJob->nodes.push_back(cloneContent);