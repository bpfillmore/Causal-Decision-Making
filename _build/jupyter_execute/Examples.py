#!/usr/bin/env python
# coding: utf-8

# ## Motivating Examples
# 
# ### Offline Learning
# 
# #### Personalized Incentives
# User growth and engagement are critical in a fast-changing market. Marketing campaigns in internet companies offer quantifiable incentives to encourage users to engage or use new products. The treatment has positive effects on desired business growth, also lead to a surplus in operation cost. The increasing cost impels internet companies to carry out more refined strategies in user acquisition, user retention, and etc. Specifically, the associated costs of massive-scale promotion campaigns must be balanced by incremental business value, with a sustainable return-on-investment (ROI). We are required to predict, for each user, the change in business value caused by different incentive actions, in order to maximize the ROI of market campaigns. This problem is known as uplift modeling, or heterogeneous treatment effect estimation, which has received more and more attention in the causal inference literature.
# 
# #### Ad Targeting & Bidding
# John Wanamaker once phrased 'Half the money I spend on advertising is wasted, the trouble is I don't know which half.'
# It indicates that we are wasting our advertisement on users with high intention to convert naturally. Today's digital technique enables us to estimate the conversion lift of each user via randomized controlled studies. We randomly select users to form two groups, one can be intervened via our ads and the other cannot. Based on the collected data, we can estimate the difference of conversion between ad intervention and no ad intervention. We can then target users with high converion lift, or even increase our bidding price to win the impression for those users.
# 
# 
# #### Multi-touch Attribution
# Users may interact with the same advertisement (possibly with different styles) many times through different channels. 
# Multi-touch attribution, which allows distributing the credit to all related advertisements based on their corresponding contributions, has recently become an important research topic in digital advertising. Rules based on simple intuition have been used in practice for a long time. With the ever enhanced capability to tracking advertisement and users’ interaction with the advertisement, data-driven multi-touch attribution models, which attempt to infer the contribution from user interaction data, become increasingly more popular recently. This problem can be easily formalized to the multi-stage dynamic treatment regime framework.
# 
# 
# ### Online Learning
# 
# #### Healthcare
# With the development of mobile health applications and wearable devices, users can easily keep track of their own health data. Meanwhile, how to utilize these mobile health data to improve or manage users' health is an increasingly hot topic. Among them, deciding **when** and **how** to provide treatments is one of the biggest challenges. For example, users may be given personalized activity suggestions based on activity-related data to help regulate their psychological states. However, it is challenging to decide when to send the suggestion and how it should be written. Intuitively, sending a suggestion when the user is asleep or suggesting an intense workout to a user who rarely exercises would decrease the user's engagement. To address these challenges, an increasing number of researchers are formalizing these problems to the online bandit learning problem in order to find optimal policies for users.
# 
# #### Dynamic Pricing
# Dynamic pricing is a widely used pricing strategy in various real-world applications to optimize cumulative profits by changing the price for products dynamically across time. For example, online retailers will adjust products' prices according to changes in the market, or during the promotion period, ridesharing services will increase prices when severe weather occurs outside, and airlines usually raise ticket prices as the farewell dates approach. Typically, while rising prices may result in a low purchase rate, decreasing prices will lead to low profit. Therefore, the bandit framework has been widely adapted to dynamic pricing problems to find an optimal strategy.
# 
# #### Recommender Systems
# A recommender system is a classical application scenario of online bandit learning, which aims to learn users' preferences and then recommend items to users to maximize the click-through rate or overall profits. A representative example of it is the movie recommendation, such as Youtube and Netflix, where the agent will provide users with a list of video recommendations when they visit their sites, and then users will either click one of the recommendations or leave. Typically, in movie recommendations, there is a large number of items available to be selected. Therefore, how to balance exploring new items and exploiting information about recommended items received so far is the critical problem approached by using bandit learning settings.
# 
# #### Online Ad
# As discussed in the motivating examples for offline learning, preventing unnecessary costs is essential in advertising. An online variant of advertising is frequently used on many commercial websites, such as Google display Ads and Twitter Ads. It is usually viewed as a bipartite matching problem with millions of users and items. Typically, at each decision point, an agent needs to show the Ads to a group of potential customers that are most likely to be attracted by the advertisement while adhering to the budget constraints. Learning the advertising conversion rate based on users' feedback, we can then find an optimal group of customers to achieve an optimal conversion rate.
# 
# 
# ### Causal Discovery
# 
# #### Spread of COVID-19
# 
# In the era of causal revolution, identifying the causal effect of an exposure on the outcome of interest is an important problem in many areas. Under a general causal graph, the exposure may have a direct effect on the outcome and also an indirect effect regulated by a set of mediators (or intermediate variables). For instance, during the outbreak of Coronavirus disease 2019 (COVID-19), the Chinese government has taken extreme measures to stop the virus spreading such as locking Wuhan down on Jan 23rd, 2020, followed by 12 other cities in Hubei, known as the “2020 Hubei lockdowns”. This approach (viewed as the exposure), directly blocked infected people leaving from Hubei; and also stimulated various quarantine measures taken by cities outside of Hubei (as the mediators), which further decreased the migration countrywide in China, and thus indirectly control the spread of COVID-19. Quantifying the causal effects of 2020 Hubei lockdowns on reducing the COVID-19 spread regulated by different cities outside Hubei is challenging but of great interest for the current COVID-19 crisis. An analysis of causal effects that interprets the causal mechanism contributed via individual mediators is thus very important.
# 
# #### Gene Expression Traits in Yeast
# 
# Over recent decades, causal discovery attracts more and more attention by disentangling the complex causal relationship in various fields. Compared to 4 to 5 million single nucleotide polymorphisms (SNPs) in a person’s genome, much fewer non-spurious genes/proteins that systematically regulate the expression of the phenotype of interest are identified. We focus on a real application of gene expression traits in yeast (Brem & Kruglyak, 2005) to discover important causal features on explaining the gene expression of interest. This dataset collected 104 yeast segregants simulated by two genetically diverse strains, BY4716 and RM11-1a, and each segregant contains thousands of genotypes that contribute to rich phenotypic diversity. A primary goal in genetics is to study how different genotypes influence the target heritable traits of interest. Due to high-dimensional genes, formally named as quantitative trait loci (QTLs), involved in this study, identifying a more parsimonious causal graph is desired to reveal the true necessary dependencies that presents the essential causality towards the outcome of interest is desired. In this study, we are interested in identifying the genes whose expression levels affect the genetic variant YER124C, which is daughter cell-specific protein, may participate in pathways regulating cell wall metabolism; deletion affects cell separation after division and sensitivity to drugs targeted against the cell wall.  

# In[ ]:




