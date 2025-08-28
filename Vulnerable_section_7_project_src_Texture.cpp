 		SRVDesc.Format = format;
 		SRVDesc.ViewDimension = D3D11_SRV_DIMENSION_TEXTURE2D;
 		SRVDesc.Texture2D.MipLevels = 1;	
		hr = pDevice->CreateShaderResourceView(m_pResource, &SRVDesc, &m_pShaderResourceView);
 
 		SDL_FreeSurface(pSurface);
 	}