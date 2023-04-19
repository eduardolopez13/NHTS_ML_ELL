
"""
This code fits a logistic regression model to classify HHSTATE (state)

"""
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# here we load the data
file_path = Path("path to dataset.csv")
wwc = pd.read_csv(file_path)

# Select relevant features, we want to pick top 10 features logically, there are robust methods too, you select logically. 
labels_names = ['GSYRGAL', 'FEGEMPG', 'ANNMILES', 'OD_READ', 'VEHAGE', 'HHVEHCNT', 'HHSIZE', 'HHSTATE']
wwc = wwc[labels_names]

# Make all values greater than 0, now we make all values in the selected >0
wwc = wwc[(wwc['GSYRGAL'] >= 0) & (wwc['OD_READ'] >= 0) & (wwc['ANNMILES'] >= 0) & (wwc['FEGEMPG'] >= 0) & (wwc['HHSIZE'] >= 0) & (wwc['VEHAGE'] >= 0) & (wwc['HHVEHCNT'] >= 0)]
# Split data into training and testing sets
X = wwc.drop('HHSTATE', axis=1) 
y = wwc['HHSTATE'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# logistic regression
logreg = LogisticRegression()

# Train using training sets
logreg.fit(X_train, y_train)

# Make predictions using the testing set
y2_pred = logreg.predict(X_test)

# The coefficients
print("Coefficients: \n", logreg.coef_)
# The accuracy
print("Accuracy: %.2f" % logreg.score(X_test, y_test))
# The confusion matrix
from sklearn.metrics import confusion_matrix
print("Confusion matrix: \n", confusion_matrix(y_test, y2_pred))