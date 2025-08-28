 {
 	m_pEffect = LoadEffect(pDevice, assetFile);
 
	m_pTechnique = m_pEffect->GetTechniqueByName("DefaultTechnique");
	if (!m_pTechnique->IsValid())
	{
		std::wcout << L"Technique not valid\n";
	}

 	m_pTechniquePoint = m_pEffect->GetTechniqueByName("PointTechnique");
 	if (!m_pTechniquePoint->IsValid())
 	{
 		std::wcout << L"m_pMatWorldViewProjVariable not valid\n";
 	}
 
 	m_pDiffuseMapVariable = m_pEffect->GetVariableByName("gDiffuseMap")->AsShaderResource();
 	if (!m_pDiffuseMapVariable->IsValid())
 	{
 		m_pTechniquePoint = nullptr;
 	}
 
	if (m_pTechnique)
	{
		m_pTechnique->Release();
		m_pTechnique = nullptr;
	}
 
 	if (m_pEffect)
 	{
 	return m_pEffect;
 }
 
ID3DX11EffectTechnique* Effect::GetTechnique() const
{
	return m_pTechnique;
}

 ID3DX11EffectTechnique* Effect::GetTechniquePoint() const
 {
 	return m_pTechniquePoint;
 			return nullptr;
 		}
 	}
 
 	return pEffect;
 }