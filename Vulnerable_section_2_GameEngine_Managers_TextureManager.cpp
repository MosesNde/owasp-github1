 
 namespace Engine
 {
	ID3D12Resource* TextureManager::GetTexture(const std::wstring& textureName)
 	{
 		auto texturePair{ m_Textures.find(textureName)};
 		if (texturePair == m_Textures.end())
 			val.Reset();
 		}
 	}
	ID3D12Resource* TextureManager::LoadTexture(const std::wstring& textureName)
 	{
 		auto pHandler{ Locator::GetGameHandler() };
 		const std::wstring textureLocation{ pHandler->GetContentRoot() + L"Textures/" + textureName  };
 
 		resourceUpload.Begin();
 
		ID3D12Resource* pTexture{ nullptr };
 
		const HRESULT result{DirectX::CreateWICTextureFromFile(pDevice,resourceUpload,textureLocation.c_str(),&pTexture,false) };
 
 		if (FAILED(result))
 		{