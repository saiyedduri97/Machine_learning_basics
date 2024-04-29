
# In[81]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


# ## (a)Implement rejection sampling based on the uniform distribution U[−1, 1] as proposal distribution with X ∼ U[−1, 1] and Y ∼ U[−1, 1].
# 

# In[76]:


def rejection_sampling(n_samples,circle_radius=1):
    """
       Function: Generate samples that are independent and uniformly distributed and identify the samples that are accepted within/on the circle through rejection sampling.
                
                It is assumed that circle is present at the center of considered samples boundary range that follows (x,y)⊆(-circle radius,circle radius)
        Arguments:
            n_samples(int): Number of uniformly distributed samples to generate with in the range of (-circle_radius,circle_radius=1)
            circle_radius(float): Radius of the circle with which the samples are to be accepted.
            
        Returns:
            accepted_samples(np.array): Accepted samples which follows x**2 + y**2 <= circle_radius**2 for uniformly distributed samples
                                        array size: (number of samples,2)
            
            accepted_tries(np.array): Number of tries it took to accept each sample with the circle.
                                      array size:(1,number of samples)     
    """
   
    # List to store  accepted samples that meet the condition
    accepted_samples = []
    # List to store the number of tries for accepting each sample
    accepted_tries=[]

    for each_sample in range(n_samples):
        # Initially every sample is not accepted
        accepted = False
        n_tries=0

        while not accepted:
            # Generating the independent and uniformly distributed samples untill all the samples are accepted
            x = np.random.uniform(-circle_radius,circle_radius)
            y = np.random.uniform(-circle_radius, circle_radius)
            # Counting no. of attempts for each sample before meeting the condition
            n_tries=n_tries+1
            # Check if the sample is inside the unit circle
            if x**2 + y**2 <= circle_radius**2:
                accepted = True
                # Storing the the accepted samples
                accepted_samples.append((x, y))
                #Storing the attempt at which the proposal draw is accepted
                accepted_tries.append(n_tries)
            
    return np.array(accepted_samples), np.array(accepted_tries)

n_samples = 500
# Collecting the samples and number of tries for accepting random datapoints that follows uniform distribution and falls with the unit circle x**2+y**2<=1 and 
# X⊆ U[−1, 1] and Y⊆ U[−1, 1].
accepted_samples, accepted_tries = rejection_sampling(n_samples,circle_radius=1)


# In[83]:


accepted_samples


# ## (b) Generate n = 500 samples of the uniform distribution via your code. Plot the generated 500 samples.

# In[78]:


n_samples = 500
# Collecting the number of tries for accepting random datapoints that follows uniform distribution
accepted_samples, accepted_tries = rejection_sampling(n_samples,circle_radius=1)

# Visualizing the accepted data points in a scatter plot 
fig,axis=plt.subplots()
plt.scatter(accepted_samples[:, 0], accepted_samples[:, 1], marker='.')

# plot a unit circle with radius 1 for visual reference of the boundary range of condition
circle=plt.Circle((0, 0), 1, color="black",fill=False)
axis.add_patch(circle)
# Setting the aspect ratio of x and y axis as equal
axis.set_aspect("equal")
# Labelling the title of the figure
axis.set_title("Samples of uniform distribution in a unit disk")
#Labelling the xaxis and yaxiss of the figure
axis.set_xlabel("X")
axis.set_ylabel("Y")
plt.show()



# ## (c)
# ### Estimate on the number π based on the stored number of tries of rejection
#  ### How large is the success/acceptance probability in this case?

# In[66]:


def estimate_pi(accepted_tries,circle_radius):
    """
    Function: To determine the probablity of accepted samples and estimate value of π based on the stored number of tries in the rejection sampling process.
            
              It is assumed that circle is present at the center of considered samples boundary range that follows (x,y)⊆(-circle radius,circle radius)
    
    Arguments:
        accepted_tries(np.array): Number of tries required for accepted samples.
        circle_radius(float): Radius of circle within which samples are accepted.
    
    Returns:
            estimated_pi(float):Estimated value of pi based on the average number of tries took to accept the samples
            estimated_prob_acceptance(float): Estimated probility of success/acceptance based on the average number of tries.
    
    """

    # The probability of acceptance is the sum of total nuber of attempts required w.r.t the total number of accepted tries
    estimated_avg_tries=accepted_tries.sum()/len(accepted_tries)
    
    # probability of acceptance=(Area of circle)/Area of square  =1/avg_tries
                                #=>1/avg_tries=(pi*(circle_radius**2))/(2*circle_radius)**2
                                #=> pi=((2*circle_radius)**2)/(avg_tries*(circle_radius**2))
    
    estimated_pi=((2*circle_radius)**2)/(estimated_avg_tries*(circle_radius**2))
   
    # Determining the probability of acceptance 
    estimated_prob_acceptance=(estimated_pi*(circle_radius**2))/(2*(circle_radius))**2
    
    return estimated_pi,estimated_prob_acceptance


# In[79]:


# Compute the estimated pi for the accepted random points with the unit circle
estimated_pi,estimated_prob_acceptance=estimate_pi(accepted_tries,circle_radius=1)

print(f"c)The estimated pi based on average number of tries of rejection sampling in the case is {estimated_pi}\n")
print(f"c)The probability of acceptance in this case is {estimated_prob_acceptance}")


# In[73]:


# It can be observed that estimated pi through random rejection sampling is 
# close to the actual pi value of 3.14. This validates our rejection sampling.

