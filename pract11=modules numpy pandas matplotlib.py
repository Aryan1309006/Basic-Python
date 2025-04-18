import pandas as pd
data={
    "Student":["Minal","Namiata","Kedar","Saurav","Vansh"],
    "Score":[85,92,78,88,95]
}
df=pd.DataFrame(data)

print("Fiest 3 Rows of DataFrame:\n",df.head(3))

avarage_score=df["Score"].mean()
print("\n Avarage Score of students:",avarage_score)

#--------------------------------------------------------------
import numpy as np
marks=np.array([85,78,92,88,95,77,84,91])
avarage_marks=np.mean(marks)
higest_marks=np.max(marks)
lowest_marks=np.min(marks)

print(f"Avarge marks:{avarage_marks}")
print(f"heigest marks:{higest_marks}")
print(f"lowestr marks:{lowest_marks}")
#--------------------------------------------------------------
import matplotlib.pyplot as plt
months=['Jan','Fab','mar','apr','may','jun']
scles=[5000,6000,7500,8000,9000,9500]
plt.bar(months,scles,color='skyblue')
plt.xlabel('months')
plt.ylabel('sales (in Usd')
plt.title(' sales data for the first half year')
plt.show()

#--------------------------------------------------------------
import pandas as pd 
data={
    'Nmae':['Kadar','Bhavesh','Charlie','David','Mohan'],
    'Age':[20,21,22,23,20],
    'Marks':[85,78,92,88,95]
}
df=pd.DataFrame(data)
print(df.head())
print("-----------------------------------------------------------------")
"""      Nmae  Age  Marks
0    Kadar   20     85
1  Bhavesh   21     78
2  Charlie   22     92
3    David   23     88
4    Mohan   20     95

"""
#--------------------------------------------------------------
import numpy as np
matrix = np.arange(1, 10).reshape(3, 3)
print("3x3 Matrix:\n", matrix)
sum_of_elements = np.sum(matrix)
print("\nSum of all elements in the matrix:", sum_of_elements)

"""
3x3 Matrix:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]

Sum of all elements in the matrix: 45
"""
#--------------------------------------------------------------
import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
squared_arr = np.square(arr) 
mean_value = np.mean(arr) 
print("Squared Array:", squared_arr)
print("Mean Value:", mean_value)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nOriginal Matrix:\n", matrix)
transposed_matrix = np.transpose(matrix)
print("\nTransposed Matrix:\n", transposed_matrix)
data = {
"Name": ["Abha", "Bin", "neil"],
"Age": [25, 30, 22],
"Salary": [50000, 60000, 45000]
}
df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)
df["Department"] = ["HR", "IT", "Finance"]
print("\nDataFrame After Adding New Column:\n", df)
salary_column = df["Salary"]
print("\nFiltered Column (Salary):\n", salary_column)
df.to_csv("employee_data.csv", index=False)
print("\nDataFrame saved as 'employee_data.csv' successfully!")
"""
Original Array: [1 2 3 4 5]
Squared Array: [ 1  4  9 16 25]
Mean Value: 3.0

Original Matrix:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]

Transposed Matrix:
 [[1 4 7]
 [2 5 8]
 [3 6 9]]

Original DataFrame:
    Name  Age  Salary
0  Abha   25   50000
1   Bin   30   60000
2  neil   22   45000

DataFrame After Adding New Column:
    Name  Age  Salary Department
0  Abha   25   50000         HR
1   Bin   30   60000         IT
2  neil   22   45000    Finance

Filtered Column (Salary):
 0    50000
1    60000
2    45000
Name: Salary, dtype: int64

DataFrame saved as 'employee_data.csv' successfully!
"""

