import os
import sys
import time
import numpy as np
import pandas as pd
import math
import scipy.stats as stats
from sklearn.ensemble import RandomForestClassifier
#from sklearn.ensemble import GradientBoostingClassifier
##add code to import random forests too
#import matplotlib.pyplot as plt


#a = pd.read_csv("/g5/home/sk1642/AI_GROM_FOR_tumor_normal_pairs/Synthetic_4_v3_training_set.numerical.txt",sep='\t',header=0, error_bad_lines=False, index_col=False, dtype='unicode')
a = pd.read_csv("/projects/f_grigorie_1/rk824/HG002_6_9_21_train_v_v.txt",sep='\t',header=0, error_bad_lines=False, index_col=False, dtype='unicode')

b = a.fillna(0)

#gb = GradientBoostingClassifier(warm_start=True,n_estimators=100,min_samples_split=2,verbose=2,random_state=100)
forclass = RandomForestClassifier(verbose = 3, n_estimators = 90)
start_time = time.clock()

forclass.fit(b.ix[:,2:-1],b.ix[:,-1])
#gb.fit(b.ix[:,3:-1],b.ix[:,-1])
print "Decision Model Trained\n"

files = os.listdir('/projects/f_grigorie_1/rk824/')

for a in files:
        if 'HG002_SNV_chr123_v_v.txt' in a:
                print "This will be our first file to test ",a
                c = pd.read_csv("/projects/f_grigorie_1/rk824/"+a,sep='\t',header=0, error_bad_lines=False, index_col=False, dtype='unicode')
                d = c.fillna(0) ## not needed in your case
                best_est_1 = forclass.predict(d.ix[:,2:])
                print len(best_est_1)
                best_est_prob = forclass.predict_proba(d.ix[:,2:])
                writefile = file("/projects/f_grigorie_1/rk824/"+a.split("_")[0]+"_trained_HG002_chr123_predictions_RF_n_90", 'w')
                writefile.writelines("T/F"+'\t'+"F_prob"+'\t'+"T_prob\n")
                for k in range(len(best_est_1)):
                        writefile.writelines(d.ix[k][0]+'\t'+d.ix[k][1]+'\t'+d.ix[k][2]+'\t'+str(best_est_1[k])+'\t'+str(best_est_prob[k][0])+'\t'+str(best_est_prob[k][1])+'\n')
print time.time() - start_time, "seconds"

writefile1 = file("/projects/f_grigorie_1/rk824/HG002_6_21_9_feature_importance_RF_90.txt", 'w')
for j in forclass.feature_importances_:
#for j in gb.feature_importances_:
    writefile1.writelines(str(j)+'\n')
