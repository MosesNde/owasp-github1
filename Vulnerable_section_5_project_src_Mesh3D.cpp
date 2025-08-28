 			&m_pVertexLayout )};
 	if (FAILED(result)) return;
 
	m_pEffect->GetTechniqueLinear()->GetPassByIndex(0)->GetDesc(&passDesc);
	result = pDevice->CreateInputLayout
		(
			vertexDesc,
			numElements,
			passDesc.pIAInputSignature,
			passDesc.IAInputSignatureSize,
			&m_pVertexLayout);
	if (FAILED(result)) return;

	m_pEffect->GetTechniqueAnisotropic()->GetPassByIndex(0)->GetDesc(&passDesc);
	result = pDevice->CreateInputLayout
		(
			vertexDesc,
			numElements,
			passDesc.pIAInputSignature,
			passDesc.IAInputSignatureSize,
			&m_pVertexLayout);
	if (FAILED(result)) return;
 
 	//3. Create vertex buffer
 	D3D11_BUFFER_DESC bd{};
 
 Mesh3D::~Mesh3D()
 {
 	if (m_pIndexBuffer)
 	{
 		m_pIndexBuffer->Release();
 		m_pVertexLayout = nullptr;
 	}
 
	delete m_pEffect;
 
 }
 

 void Mesh3D::Render(const Matrix& pWorldViewProjectionMatrix, ID3D11DeviceContext* pDeviceContext) const
 {	
 	//1. Set primitive topology