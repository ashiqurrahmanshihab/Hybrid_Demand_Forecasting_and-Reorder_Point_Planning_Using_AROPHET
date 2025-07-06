import pandas as pd
import numpy as np
import random
from datetime import datetime

# Generate date range for 10 years (monthly)
dates = pd.date_range(start='2014-01-01', end='2024-12-01', freq='MS')

# Generate synthetic data
np.random.seed(42)
n = len(dates)

data = pd.DataFrame({
    'ds': dates,
    'y': np.random.poisson(lam=1200, size=n) + np.sin(np.linspace(0, 24 * np.pi, n)) * 200,
    'marketing_spend': np.random.normal(loc=1500, scale=300, size=n).astype(int),
    'doctor_visits': np.random.normal(loc=5000, scale=500, size=n).astype(int),
    'disease_trend': np.random.normal(loc=300, scale=50, size=n).astype(int),
    'stock_level': np.random.normal(loc=7000, scale=700, size=n).astype(int),
    'lead_time_days': np.random.choice([7, 14, 21], size=n),
    'safety_stock': np.random.choice([500, 750, 1000], size=n),
    'shelf_life_months': np.random.choice([12, 24, 36], size=n),
    'MOQ': np.random.choice([1000, 2000, 3000], size=n),
})

# Product metadata (same for all records)
product_info = {
    "brand_name": "Alton 20",
    "generic_name": "Esomeprazole INN",
    "form": "Enteric-coated tablet",
    "strength": "20 mg",
    "active_ingredient": "Esomeprazole Magnesium Trihydrate",
    "therapeutic_category": "Proton Pump Inhibitor",
    "launch_date": datetime(2013, 6, 1)
}

# Save to Excel
excel_path = "pharma_sales_data_2014_2024.xlsx"
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    data.to_excel(writer, index=False, sheet_name='SalesData')
    pd.DataFrame([product_info]).to_excel(writer, index=False, sheet_name='ProductInfo')

excel_path
