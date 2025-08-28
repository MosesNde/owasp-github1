 
             hr = desc->DxCubeTexture->LockRect((D3DCUBEMAP_FACES)Face, i, &lockRect, NULL, NULL);
             if (FAILED(hr))
                 return FALSE;
 
             LoadSurface(surfaceDesc, lockRect, dst);
 