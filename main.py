#import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#load data and initialize x and y
data_set = pd.read_csv("Salary_Data.csv")
x = data_set.iloc[:,:-1].values
y = data_set.iloc(:,1].values

#spliting dataset into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#fitting
resgressor = LinearRegression()
regressior.fit(x_train,y_train)

#predict
y_pred = regressor.predict(x_test)
print(y_pred)

#Visualizing the Training set results
import matplotlib.pyplot as mtp  
mtp.scatter(x_train, y_train, color="green")   
mtp.plot(x_train, x_pred, color="red")    
mtp.title("Salary vs Experience (Training Dataset)")  
mtp.xlabel("Years of Experience")  
mtp.ylabel("Salary(In Rupees)")  
mtp.show()  
