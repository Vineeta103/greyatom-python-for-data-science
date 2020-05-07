# --------------
# Importing header files
import numpy as np

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

#Loading data file and saving it into a new numpy array 
data = np.genfromtxt(path, delimiter=",", skip_header=1)

print(data.shape)

#Concatenating the new record to the existing numpy array
census=np.concatenate((data, new_record),axis = 0)

print(census.shape)

#Code ends here


# --------------
#Code starts here
import numpy as np 
age = np.array(census[:,0])
print (age, census)
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print (max_age,min_age,age_mean,age_std)


# --------------
#Code starts here
import numpy as np 
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
print (len_0,len_1,len_2,len_3,len_4)
len_array = np.array([len_0,len_1,len_2,len_3,len_4])
race_min = np.min(len_array)
print (race_min)
list1 = list(len_array)
minority_race = list1.index(race_min)
print (minority_race)



# --------------
#Code starts here
import numpy as np 
age = np.array(census[:,0])
senior_citizens = census[age[:]>60]
#print (senior_citizens)
#print (senior_citizens)
wh = np.array(census[:,6])
wh_sc = wh[age[:]>60]
working_hours_sum = np.sum(wh_sc)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print (avg_working_hours)


# --------------
#Code starts here
import numpy as np
high = np.array(census[census[:,1]>10])
low = np.array(census[census[:,1]<=10])
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print (avg_pay_high, avg_pay_low)


