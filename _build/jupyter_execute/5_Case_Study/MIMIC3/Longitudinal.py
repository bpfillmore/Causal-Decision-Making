#!/usr/bin/env python
# coding: utf-8

# ## MIMIC III (3-Stages)
# 
# In this notebook, we conducted analysis on the MIMIC III data with 3 stages. We first analyzed the mediation effect and then evaluate the policy of interest and calculated the optimal policy. As informed by the causal structure learning, here we consider Glucose and PaO2_FiO2 as confounders/states, IV_Input as the action, SOFA as the mediator. 

# In[1]:


import pandas as pd
import pickle
import numpy as np
import pandas as pd
file = open('mimic3_MDTR_data_dict_3stage_V2.pickle', 'rb')
mimic3_MDTR = pickle.load(file)
MDTR_data = pd.read_csv('mimic3_MDTR_3stage_V2.csv')
MDTR_data.head()
DTR_data = pd.read_csv('mimic3_DTR_3stage_V2.csv')
DTR_data.head()


# # CEL: 3-Stage Mediation Analysis

# Under the 3-stage setting, we are interested in analyzing the treatment effect on the final outcome Died_within_48H observed at the end of the study by comparing the target treatment regime that provides IV input at all three stages and the control treatment regime that does not provide any treatment. Using the Q-learning based estimator proposed in [1], we examine the natural direct and indirect effects of the target treatment regime based on observational data. With the code in the following blocks, the estimated effect components are summarized in the following:
# 
# | NDE   | NIE  | TE    |
# |-------|------|-------|
# | -.426 | .312 | -.114 |
# 
# Specifically, when compared to no treatment, always giving IV input has a negative impact on the survival rate with an effect size of.114, among which the effect directly from actions to the final outcome is -.426 and the indirect effect of actions to the outcome passing through mediators is .312. The following is the bootstrapped estimation (bootstraped SE):
# 
# | NDE   | NIE  | TE    |
# |-------|------|-------|
# | -.274(1.390) | .220 (1.295) | -.054 (.567)|

# In[2]:


import os
os.getcwd()
os.chdir('/nas/longleaf/home/lge/CausalDM')
from causaldm.learners import Mediated_QLearning
state, action, mediator, reward = mimic3_MDTR.values()
MediatedQLearn = Mediated_QLearning.Mediated_QLearning()
N=len(state)
regime_control = pd.DataFrame({'IV_Input_1':[0]*N,'IV_Input_2':[0]*N, 'IV_Input_3':[0]*N}).set_index(state.index)
regime_target = pd.DataFrame({'IV_Input_1':[1]*N,'IV_Input_2':[1]*N, 'IV_Input_3':[1]*N}).set_index(state.index)
MediatedQLearn.train(state, action, mediator, reward, T=3, dim_state = 2, dim_mediator = 1, 
                     regime_target = regime_target, regime_control = regime_control,bootstrap = False)
NIE, NDE = MediatedQLearn.est_NDE_NIE()
NIE, NDE, NIE+NDE


# In[5]:


MediatedQLearn.V_target, MediatedQLearn.V_control


# In[6]:


MediatedQLearn.train(state, action, mediator, reward, T=3, dim_state = 2, dim_mediator = 1, 
                     regime_target = regime_target, regime_control = regime_control,bootstrap = True, n_bs = 500)
boots_results, mean_effect, SE_effect = MediatedQLearn._predict_value_boots()
mean_effect, SE_effect


# ## CPL: 3-Stage Policy Evaluation

# In[7]:


from causaldm.learners import QLearning


# As an example, we use the **Q-learning** algorithm to evaluate policies based on the observed data, with the linear regression models defined as the following:
# \begin{align}
# Q_1(s,a_1,\boldsymbol{\beta}) = &\beta_{00}+\beta_{01}*\textrm{Glucose}_1+\beta_{02}*\textrm{PaO2_FiO2}_1\\
#                     &I(a_1=1)*\{\beta_{10}+\beta_{11}*\textrm{Glucose}_1+\beta_{12}*\textrm{PaO2_FiO2}_1\},\\
# Q_2(s,a_2,\boldsymbol{\mu}) = &\mu_{00}+\mu_{01}*\textrm{Glucose}_1+\mu_{02}*\textrm{PaO2_FiO2}_1+\mu_{03}*\textrm{SOFA}_1+\\
#                     &\mu_{04}*\textrm{Glucose}_2+\mu_{05}*\textrm{PaO2_FiO2}_2+\\
#                     &I(a_2=1)*\{\mu_{10}+\mu_{11}*\textrm{Glucose}_2+\mu_{12}*\textrm{PaO2_FiO2}_2+\mu_{13}*\textrm{SOFA}_1\},\\
# Q_3(s,a_3,\boldsymbol{\theta}) = &\theta_{00}+\theta_{01}*\textrm{Glucose}_1+\theta_{02}*\textrm{PaO2_FiO2}_1+\theta_{03}*\textrm{SOFA}_1+\\
#                     &\theta_{04}*\textrm{Glucose}_2+\theta_{05}*\textrm{PaO2_FiO2}_2+\theta_{06}*\textrm{SOFA}_2+\\
#                     &\theta_{07}*\textrm{Glucose}_3+\theta_{08}*\textrm{PaO2_FiO2}_3+\\
#                     &I(a_2=1)*\{\theta_{10}+\theta_{11}*\textrm{Glucose}_3+\theta_{12}*\textrm{PaO2_FiO2}_3\}
# \end{align}
# 
# Using the code below, we evaluated two target polices (regimes). The first one is a fixed treatement regime that applies no treatment at all stages (Policy1), with an estimated value of .7982. Another is a fixed treatment regime that applies treatment at all stages (Policy2), with an estimated value of .6492. Therefore, the treatment effect of Policy2 comparing to Policy1 is -.1490, implying that receiving IV input increase the mortality rate.

# In[14]:


DTR_data.rename(columns = {'Died_within_48H':'R',
                            'Glucose_1':'S1_1', 'Glucose_2':'S1_2','Glucose_3':'S1_3',
                            'PaO2_FiO2_1':'S3_1', 'PaO2_FiO2_2':'S3_2','PaO2_FiO2_3':'S3_3',
                            'SOFA_1':'S4_1', 'SOFA_2':'S4_2', 'SOFA_3':'S4_3',
                            'IV_Input_1':'A1','IV_Input_2':'A2', 'IV_Input_3':'A3'}, inplace = True)
R = DTR_data['R'] #lower the better
S = DTR_data[['S1_1','S1_2','S1_3','S3_1','S3_2','S3_3','S4_1','S4_2','S4_3']]
A = DTR_data[['A1','A2', 'A3']]
# specify the model you would like to use
model_info = [{"model": "R~S1_1+S3_1+A1+S1_1*A1+S3_1*A1",
              'action_space':{'A1':[0,1]}},
             {"model": "R~S1_1+S3_1+S4_1+S1_2+S3_2+A2+S1_2*A2+S3_2*A2+S4_1*A2",
              'action_space':{'A2':[0,1]}},
             {"model": "R~S1_1+S3_1+S4_1+S1_2+S3_2+S4_2+S1_3+S3_3+A3+S1_3*A3+S3_3*A3+S4_2*A3",
              'action_space':{'A3':[0,1]}}]


# In[15]:


# Evaluating the policy with no treatment
N=len(S)
regime = pd.DataFrame({'A1':[0]*N,
                      'A2':[0]*N,
                     'A3':[0]*N}).set_index(S.index)
#evaluate the regime
QLearn = QLearning.QLearning()
QLearn.train(S, A, R, model_info, T=3, regime = regime, evaluate = True, mimic3_clip = True)
QLearn.predict_value(S)


# In[16]:


# Evaluating the policy that gives IV input at both stages
N=len(S)
regime = pd.DataFrame({'A1':[1]*N,
                      'A2':[1]*N,
                     'A3':[1]*N}).set_index(S.index)
#evaluate the regime
QLearn = QLearning.QLearning()
QLearn.train(S, A, R, model_info, T=3, regime = regime, evaluate = True, mimic3_clip = True)
QLearn.predict_value(S)


# ## CPL: 3-Stage Policy Optimization

# Further, to find an optimal policy maximizing the expected value, we use the **Q-learning** algorithm again to do policy optimization. Using the regression model we specified above and the code in the following block, the estimated optimal policy is summarized as the following regime.
# 
# - At stage 1:
#     1. We would recommend $A=0$ (IV_Input = 0) if $.0002*\textrm{Glucose}_1+.0012*\textrm{PaO2_FiO2}_1>.1101$
#     2. Else, we would recommend $A=1$ (IV_Input = 1).
# - At stage 2:
#     1. We would recommend $A=0$ (IV_Input = 0) if $.0005*\textrm{Glucose}_2-.00002*\textrm{PaO2_FiO2}_2+.0141*\textrm{SOFA}_1<.1442$
#     2. Else, we would recommend $A=1$ (IV_Input = 1).
# - At stage 3:
#     1. We would recommend $A=0$ (IV_Input = 0) if $-.0009*\textrm{Glucose}_2+.0016*\textrm{PaO2_FiO2}_2-.0228*\textrm{SOFA}_2<.4136$
#     2. Else, we would recommend $A=1$ (IV_Input = 1).
#     
# Appling the estimated optimal regime to individuals in the observed data, we summarize the regime pattern for each patients in the following table:
# 
# | # patients | IV_Input 1 | IV_Input 2 | IV_Input 3 |
# |------------|------------|------------|------------|
# | 23         | 1          | 1          | 0          |
# | 10         | 1          | 0          | 0          |
# | 5          | 1          | 1          | 1          |
# | 4          | 0          | 0          | 0          |
# | 4          | 0          | 1          | 0          |
# | 4          | 0          | 1          | 1          |
# | 2          | 0          | 0          | 1          |
# | 2          | 1          | 0          | 1          |
# 
# The estimated value of the estimated optimal policy is **.9274**.

# In[21]:


# initialize the learner
QLearn = QLearning.QLearning()
# train the policy
QLearn.train(S, A, R, model_info, T=3, mimic3_clip = True)
# get the summary of the fitted Q models using the following code
#print("fitted model Q0:",QLearn.fitted_model[0].summary())
#print("fitted model Q1:",QLearn.fitted_model[1].summary())
#4. recommend action
opt_d = QLearn.recommend_action(S).value_counts()
#5. get the estimated value of the optimal regime
V_hat = QLearn.predict_value(S)
print("opt_d:",opt_d)
print("opt value:",V_hat)


# ## Reference
# 
# [1] Zheng, W., & van der Laan, M. (2017). Longitudinal mediation analysis with time-varying mediators and exposures, with application to survival outcomes. Journal of causal inference, 5(2).

# In[ ]:



