import numpy as np

rng=np.random.default_rng()
image=rng.integers(0,256,(10,10))

bright=image+56
dim=image-58

bright=np.clip(bright,0,255)
mask=image>170

dim=dim.clip(dim,0,255)

rev=255-image

print(bright,'\n',mask,'\n',dim,'\n',rev)




