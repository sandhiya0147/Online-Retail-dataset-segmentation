import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import joblib

# Load and clean the dataset
df = pd.read_excel("Online Retail.xlsx")
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Feature engineering
customer_data = df.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',
    'Quantity': 'sum',
    'UnitPrice': 'mean',
    'InvoiceDate': 'nunique',
    'Country': 'nunique',
}).rename(columns={
    'InvoiceNo': 'NumPurchases',
    'Quantity': 'TotalQuantity',
    'UnitPrice': 'AvgUnitPrice',
    'InvoiceDate': 'ActiveDays',
    'Country': 'CountryCount'
})

# Normalize features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)

# Apply DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=5)
labels = dbscan.fit_predict(scaled_data)

# Save outputs
customer_data['Cluster'] = labels
customer_data.to_csv('clustered_data.csv')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(dbscan, 'dbscan_model.pkl')
