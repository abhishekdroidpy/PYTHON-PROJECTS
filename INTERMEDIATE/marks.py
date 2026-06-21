import numpy as np

marks=np.array([[78,99,45,77],
                              [88,89,90,85],
                              [67,78,87,90],
                              [79,98,99,60]])
                           
total=np.sum(marks,axis=1)
average=np.mean(marks,axis=0)
topper=np.max(sum)
good_scores=marks[marks>=70]
normalised=marks-average

print(f"sum:{sum},\n,avg:{average},\n,topper:{topper},\n,good scores:{good_scores},\n,normalised={normalised}")
