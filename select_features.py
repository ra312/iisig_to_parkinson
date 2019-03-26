import pandas as pd
import numpy as np
import iisignature
data = pd.read_json('hand_left_keypoints.json', lines=True,
orient='columns')
#print(data.head(1))
print(data.keys())
n = 0
sigs = []
for _, content in data.iteritems():
    if n == 1: break
    n = n+1
    #print('content:', content[0], sep='\n')

    reshape = np.array(content[0])
    print(reshape)
    sigs.append(iisignature.sig(reshape,4))
print(sigs)
#data.info()
