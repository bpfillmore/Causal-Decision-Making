#!/usr/bin/env python
# coding: utf-8

# ## Causal Effect Learning (CEL)
# ---
# 
# Causal effect learning, as an important subfield of causal inference, aims at identifying, estimating and conducting statistical inference on the effect of a specific intervention on a system. It tries to answer the question: "What if we have done something different?", "What's the effect/consequence of excecuting a policy?" "How to quantify the causal effect of an intervention?", etc.
# 
# 
# ### Clinical Trial
# 
# Suppose you are a medical researcher who just developed a fictitious medication that can hopefully alleviate patients' symptoms of hypertension. Since this is a newly developed drug, researchers must go through preclinical testing (in bitro and vivo), three phases of clinical trials and the final approval to confirm that the effectiveness, potential side effects of the medication. 
# 
# During this procedure, the effectiveness of a newly developed drug is usually evaluated by mesuring how well it performs compared to a placebo or other existing treatments. This method of experimental design is widely known as A/B testing. During the trial, patients are randomly assigned to one of two groups: a group that receives the newly developed medication, and a group that receives a placebo. to test the causal effect of this medication, we measure the SBP (systolic blood pressure) of each patient both before and after the treatment. By comparing and analysing the difference in SBP between the two groups, we are able to determine if the drug is effective in treating hypertension.
# 
# 
# 
# ### Advertising Market
# 
# In shopping websites, sellers are often very cautious about customers' purchasing experience. Whenever consumers are not satisfied with the items they bought (such as ordering a wrong size of clothes, receiving a broken item, item missing, etc), there are several options that sellers can provide to address this problem. For example, sellers may offer (1) fully refund without returning the item, (2) fully refund after customers returning the item, (3) discount for the next purchase, etc. Since the compensation level varies according to refunding policies, the primary goal of the seller is to evaluate the outcome of different refunding policies, so as to examine which policy to take for customers with different purchasing history to maximize their profit. 
# 
# 
# 
# ### More Beyond
# Aside from the examples above, the idea of causal effect learning is fundamental and has broad applications in our daily lives. We can leverage CEL to study 
# 
# * the effect of a new catalyst on the rate of a chemical reaction;
# * the effect of smoking on the risk of lung cancer;
# * the effect of ads exposure to consumers on their conversion rate (i.e. buying the product on ads);
# * the effect of extracurricular remedial classes on the improvement of students' grades;
# * $\cdots$
# 
# Whenever we are studying social phenomena or natural phenomena, causal effect learning offers a quantification procedure that allows us to measure and understand causal relationships. This methodology is not only useful in scientific research, but also in practical applications where we seek to understand the effects of interventions or policies.
# 

# In[ ]:




