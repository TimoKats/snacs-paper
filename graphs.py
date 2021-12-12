import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

random_ec_small = np.array([656, 724, 586, 669, 423, 674, 549, 590, 566, 703])
forceatlas_ec_small = np.array([107, 109, 106, 99, 99, 99, 106, 103, 113, 113])
yifanhu_ec_small = np.array([127, 119, 125, 118, 119, 126, 119, 112, 123, 122])
reingold_ec_small = np.array([313, 260, 136, 141, 406, 124, 126, 472, 556, 208])

random_ec_small_mean = np.mean(random_ec_small)
forceatlas_ec_small_mean = np.mean(forceatlas_ec_small)
yifanhu_ec_small_mean = np.mean(yifanhu_ec_small)
reingold_ec_small_mean = np.mean(reingold_ec_small)

random_ec_small_std = np.std(random_ec_small)
forceatlas_ec_small_std = np.std(forceatlas_ec_small)
yifanhu_ec_small_std = np.std(yifanhu_ec_small)
reingold_ec_small_std = np.std(reingold_ec_small)

random_ec_med = np.array([5333, 7460, 5925, 5931, 5801, 6460, 6040, 5787, 6312, 5909])
forceatlas_ec_med = np.array([361, 357, 356, 336, 375, 357, 363, 364, 351, 351])
yifanhu_ec_med= np.array([349, 402, 433, 341, 356, 334, 384, 432, 450, 365])
reingold_ec_med = np.array([407, 610, 809, 375, 498, 627, 879, 622, 574, 605])

random_ec_med_mean = np.mean(random_ec_med)
forceatlas_ec_med_mean = np.mean(forceatlas_ec_med)
yifanhu_ec_med_mean = np.mean(yifanhu_ec_med)
reingold_ec_med_mean = np.mean(reingold_ec_med)

random_ec_med_std = np.std(random_ec_med)
forceatlas_ec_med_std = np.std(forceatlas_ec_med)
yifanhu_ec_med_std = np.std(yifanhu_ec_med)
reingold_ec_med_std = np.std(reingold_ec_med)

random_ec_large = np.array([837806, 895336, 844698, 845313, 873628, 888688, 849446, 837303, 880357, 857688])
forceatlas_ec_large = np.array([7911, 8251, 8030, 7964, 7989, 8014, 8029, 7881, 7983, 7927])
yifanhu_ec_large = np.array([8623, 8257, 8651, 8515, 8738, 8684, 8954, 8549, 8641, 8659])
reingold_ec_large = np.array([8772, 11325, 12618, 13520, 16174, 17451, 16657, 11452, 13361, 10079])

random_ec_large_mean = np.mean(random_ec_large)
forceatlas_ec_large_mean = np.mean(forceatlas_ec_large)
yifanhu_ec_large_mean = np.mean(yifanhu_ec_large)
reingold_ec_large_mean = np.mean(reingold_ec_large)

random_ec_large_std = np.std(random_ec_large)
forceatlas_ec_large_std = np.std(forceatlas_ec_large)
yifanhu_ec_large_std = np.std(yifanhu_ec_large)
reingold_ec_large_std = np.std(reingold_ec_large)

index = ['large', 'medium', 'small']
random_ec = [random_ec_large_mean, random_ec_med_mean, random_ec_small_mean]
forceatlas_ec = [forceatlas_ec_large_mean, forceatlas_ec_med_mean, forceatlas_ec_small_mean]
yifanhu_ec = [yifanhu_ec_large_mean, yifanhu_ec_med_mean, yifanhu_ec_small_mean]
reingold_ec = [reingold_ec_large_mean, reingold_ec_med_mean, reingold_ec_small_mean]
df = pd.DataFrame({'random': random_ec, 'forceatlas2': forceatlas_ec, 'yifanhu': yifanhu_ec, 'reingold': reingold_ec}, index=index)

index = ['large', 'medium', 'small']
random_ec_std = [random_ec_large_std, random_ec_med_std, random_ec_small_std]
forceatlas_ec_std = [forceatlas_ec_large_std, forceatlas_ec_med_std, forceatlas_ec_small_std]
yifanhu_ec_std = [yifanhu_ec_large_std, yifanhu_ec_med_std, yifanhu_ec_small_std]
reingold_ec_std = [reingold_ec_large_std, reingold_ec_med_std, reingold_ec_small_std]
err = pd.DataFrame({'random': random_ec_std, 'forceatlas2': forceatlas_ec_std, 'yifanhu': yifanhu_ec_std, 'reingold': reingold_ec_std}, index=index)

ax = df.plot.bar(rot=0, logy=True, capsize=3, yerr=err)
plt.ylabel('number of edge crossings')
plt.xlabel('file')
plt.show()


######################################################################################################################################################

random_eb_small = np.array([34, 0, 170, 0, 0, 0, 170, 68, 391, 0])
forceatlas_eb_small = np.array([578, 0, 153, 68, 102, 34, 68, 68, 34, 68])
yifanhu_eb_small = np.array([0, 68, 68, 0, 68, 102, 136, 0, 0, 34])
reingold_eb_small = np.array([102, 0, 102, 68, 136, 68, 68, 102, 34, 34])

random_eb_small_mean = np.mean(random_eb_small)
forceatlas_eb_small_mean = np.mean(forceatlas_eb_small)
yifanhu_eb_small_mean = np.mean(yifanhu_eb_small)
reingold_eb_small_mean = np.mean(reingold_eb_small)

random_eb_small_std = np.std(random_eb_small)
forceatlas_eb_small_std = np.std(forceatlas_eb_small)
yifanhu_eb_small_std = np.std(yifanhu_eb_small)
reingold_eb_small_std = np.std(reingold_eb_small)

random_eb_med = np.array([313, 418, 209, 209, 418, 209, 209, 209, 418, 209])
forceatlas_eb_med = np.array([209, 209, 418, 209, 209, 209, 209, 209, 418, 209])
yifanhu_eb_med= np.array([209, 209, 209, 418, 313, 209, 209, 418, 209, 209])
reingold_eb_med = np.array([418, 209, 418, 209, 209, 209, 209, 418, 209, 209])

random_eb_med_mean = np.mean(random_eb_med)
forceatlas_eb_med_mean = np.mean(forceatlas_eb_med)
yifanhu_eb_med_mean = np.mean(yifanhu_eb_med)
reingold_eb_med_mean = np.mean(reingold_eb_med)

random_eb_med_std = np.std(random_eb_med)
forceatlas_eb_med_std = np.std(forceatlas_eb_med)
yifanhu_eb_med_std = np.std(yifanhu_eb_med)
reingold_eb_med_std = np.std(reingold_eb_med)

random_eb_large = np.array([1461, 5113, 2922, 4383, 1461, 730, 2922, 2922, 1461, 2191])
forceatlas_eb_large = np.array([0, 1461, 0, 1461, 1461, 0, 2922, 4383, 4383, 2922])
yifanhu_eb_large = np.array([8766, 7305, 0, 2922, 1461, 4383, 5844, 0, 1461, 2922])
reingold_eb_large = np.array([2922, 0, 1461, 5844, 1461, 8766, 0, 2922, 1461, 5844])

random_eb_large_mean = np.mean(random_eb_large)
forceatlas_eb_large_mean = np.mean(forceatlas_eb_large)
yifanhu_eb_large_mean = np.mean(yifanhu_eb_large)
reingold_eb_large_mean = np.mean(reingold_eb_large)

random_eb_large_std = np.std(random_eb_large)
forceatlas_eb_large_std = np.std(forceatlas_eb_large)
yifanhu_eb_large_std = np.std(yifanhu_eb_large)
reingold_eb_large_std = np.std(reingold_eb_large)

index = ['large', 'medium', 'small']
random_eb = [random_eb_large_mean, random_eb_med_mean, random_eb_small_mean]
forceatlas_eb = [forceatlas_eb_large_mean, forceatlas_eb_med_mean, forceatlas_eb_small_mean]
yifanhu_eb = [yifanhu_eb_large_mean, yifanhu_eb_med_mean, yifanhu_eb_small_mean]
reingold_eb = [reingold_eb_large_mean, reingold_eb_med_mean, reingold_eb_small_mean]
df = pd.DataFrame({'random': random_eb, 'forceatlas2': forceatlas_eb, 'yifanhu': yifanhu_eb, 'reingold': reingold_eb}, index=index)

index = ['large', 'medium', 'small']
random_eb_std = [random_eb_large_std, random_eb_med_std, random_eb_small_std]
forceatlas_eb_std = [forceatlas_eb_large_std, forceatlas_eb_med_std, forceatlas_eb_small_std]
yifanhu_eb_std = [yifanhu_eb_large_std, yifanhu_eb_med_std, yifanhu_eb_small_std]
reingold_eb_std = [reingold_eb_large_std, reingold_eb_med_std, reingold_eb_small_std]
err = pd.DataFrame({'random': random_eb_std, 'forceatlas2': forceatlas_eb_std, 'yifanhu': yifanhu_eb_std, 'reingold': reingold_eb_std}, index=index)

print(forceatlas_eb_std)
ax = df.plot.bar(rot=0, logy=True, capsize=3, yerr=err)
plt.ylabel('number of edge bends')
plt.xlabel('file')
plt.show()
