import pandas as pd  
data=pd.read_csv(r"C:\\Users\\lucky\\OneDrive\\Desktop\\4Months pross\\minipro1\\tanic_dataset.csv")
print("Total number of passenger:- ",data.shape[0])
print("\n Number of columns the data-set have:- ",data.columns)
print("\nAverage age of the Passengers:- ",data['Age'].mean())
print("\n Maximum fare: - ",data['Fare'].max())
missing_value=data.isnull().sum()
most_miss_col=missing_value.idxmax()
most_miss_count=missing_value.max()
print(" Column which has most missing value is:- ",missing_value,"missing count:- ",most_miss_count)

