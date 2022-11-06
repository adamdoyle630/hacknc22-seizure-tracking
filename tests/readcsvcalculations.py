from pandas import *
 
# reading CSV file
data = read_csv("data.csv")

# converting column data to list
seizure_occurred = data['seizure occurred'].tolist()
Med_Taken_data = data['medication taken'].tolist()
alc_cons_data = data['alcohol consumed'].tolist()
stress_lev_data = data['stress level'].tolist()
sleep_amt_data = data['sleep amount'].tolist()
menstrual_data = data['menstrual'].tolist()

""""
# reading CSV file
data = pd.read_csv("data.csv")

#read CSV
dataArray = np.loadtxt('data.csv',delimiter=',',names=True)


plt.figure()
for col_name in dataArray.dtype.names:
    plt.plot(dataArray[col_name], label=col_name)
plt.legend()
plt.show()


# converting column data to list
seizure_occurred_data = data['seizure occurred'].tolist()
med_taken_data = data['medication taken'].tolist()
alc_cons_data = data['alcohol consumed'].tolist()
stress_lev_data = data['stress level'].tolist()
sleep_amt_data = data['sleep amount'].tolist()
menstrual_data = data['menstrual'].tolist()
"""

""""
import pandas.*

Seiz_Occur_data = pandas.read_csv("data.csv", header=0)
Med_Taken_data = pandas.read_csv("data.csv", header=1)
alc_cons_data = pandas.read_csv("data.csv", header=2)
stress_lev_data = pandas.read_csv("data.csv", header=3)
sleep_amt_data =  pandas.read_csv("data.csv", header=4)
menstrual_data =  pandas.read_csv("data.csv", header=5)

col_a = list(Seiz_Occur_data)

for i in col_a:
    print(col_a[i])

col_b = list(Med_Taken_data)
col_c = list(alc_cons_data)
col_d = list(stress_lev_data)
col_e = list(sleep_amt_data)
col_f = list(menstrual_data)
"""