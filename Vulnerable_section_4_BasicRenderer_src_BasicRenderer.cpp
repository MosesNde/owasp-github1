     //phoenixScene->GetRoot().transform.setLocalScale({ 0.05, 0.05, 0.05 });
     //phoenixScene->GetRoot().transform.setLocalPosition({ -1.0, 0.0, 0.0 });
 
    //auto carScene = loadGLB("models/datsun.glb");
    //carScene->GetRoot().transform.setLocalScale({ 0.6, 0.6, 0.6 });
    //carScene->GetRoot().transform.setLocalPosition({ 1.0, 0.0, 1.0 });
 
     auto mountainScene = loadGLB("models/terrain.glb");
 	mountainScene->GetRoot().transform.setLocalScale({ 100.0, 100.0, 100.0 });
     renderer.GetCurrentScene()->AppendScene(*dragonScene);
     renderer.GetCurrentScene()->AppendScene(*tigerScene);
     //renderer.GetCurrentScene()->AppendScene(*phoenixScene);
    //renderer.GetCurrentScene()->AppendScene(*carScene);
 	renderer.GetCurrentScene()->AppendScene(*mountainScene);
     //renderer.GetCurrentScene()->AppendScene(*cubeScene);
 
    renderer.SetEnvironment(L"room");
 
     XMFLOAT3 lookAt = XMFLOAT3(0.0f, 0.0f, 0.0f);
     XMFLOAT3 up = XMFLOAT3(0.0f, 1.0f, 0.0f);
 	auto light1 = Light::CreatePointLight(L"light1", XMFLOAT3(0, 0, 0), XMFLOAT3(1, 1, 1), 100.0, 1.0, 0.09, 0.032);
     light1->animationController->setAnimationClip(animation);
     cubeScaleNode->AddChild(light1);
    scene->AddLight(light1, false);
 	auto light2 = Light::CreateDirectionalLight(L"light2", XMFLOAT3(1, 1, 1), 20.0, XMFLOAT3(1, -1, 1));
    scene->AddLight(light2, false);
     //auto light3 = Light::CreateDirectionalLight("light3", XMFLOAT3(1, 1, 1), 20.0, XMFLOAT3(-1, -1, -1));
     auto light3 = Light::CreateSpotLight(L"light3", XMFLOAT3(0, 4, 0), XMFLOAT3(1, 1, 1), 100.0, {0, -1, 0}, .5, .8, 1.0, 0.09, 0.032);
	scene->AddLight(light3, false);
     //light3->AddChild(cubeScaleNode);
 
 	renderer.SetDebugTexture(light2->getShadowMap().get());