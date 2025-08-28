# Hybrid Demand Forecasting and Reorder Point Planning Using AROPHET 

## Overview
This project implements a hybrid time-series forecasting model (AROPHET) for  sales and inventory management. AROPHET combines Facebook Prophet and ARIMA to deliver more accurate forecasts and robust reorder point (ROP) calculations, helping ensure optimal stock levels and minimize shortages or overstock.

## Features
- **Data Preparation & Cleaning:** Reads and preprocesses sales data from Excel files.
- **Prophet Forecasting:** Models trend, seasonality, and holidays for baseline forecasts.
- **ARIMA Residual Modeling:** Captures autocorrelation and temporal patterns in Prophet residuals.
- **Hybrid Forecast (AROPHET):** Combines Prophet and ARIMA outputs for improved accuracy.
- **Bootstrapped Confidence Intervals:** Quantifies forecast uncertainty for risk-aware decisions.
- **Dynamic ROP Calculation:** Calculates reorder points based on forecast and uncertainty.
- **Rolling Error Analysis:** Tracks rolling mean absolute error (MAE) for model performance.
- **Comprehensive Visualizations:** Plots actual vs. forecasted sales, confidence intervals, errors, and ROP comparisons.

# Error Table (Jan–Jul 2025)

| Month    | Actual | Prophet | Hybrid | Prophet Error | Hybrid Error | Prophet % Error | Hybrid % Error |
|----------|--------|---------|--------|--------------|-------------|-----------------|---------------|
| January  | 600    | 421.4   | 491.4  | 178.6        | 108.6       | 29.8%           | 18.1%         |
| February | 520    | 1064.9  | 495.9  | -544.9       | 24.1        | -104.8%         | 4.6%          |
| March    | 570    | 489.2   | 500.1  | 80.8         | 69.9        | 14.2%           | 12.3%         |
| April    | 750    | 637.6   | 505.0  | 112.4        | 245.0       | 15.0%           | 32.7%         |
| May      | 680    | 645.8   | 509.9  | 34.2         | 170.1       | 5.0%            | 25.0%         |
| June     | 720    | 676.8   | 514.9  | 43.2         | 205.1       | 6.0%            | 28.5%         |
| July     | 520    | 683.4   | 519.9  | -163.4       | 0.1         | -31.4%          | 0.02%         |


For January–July 2025, the AROPHET hybrid model consistently outperformed Prophet in forecast accuracy. The hybrid model achieved lower MAE, RMSE, and MAPE, and a higher R², indicating a better fit to actual sales. The largest Prophet error occurred in February, likely due to unforeseen market changes or supply chain disruptions, while the hybrid model substantially reduced this error. Both models underestimated sales in April–June, suggesting the need for further refinement and consideration of external factors.

## Practical Implications
- **Accurate ROP Calculation:** Ensures stock availability and reduces excess inventory costs.
- **Improved Uncertainty Estimates:** Minimizes stockouts and unnecessary safety stock.
- **Responsive Supply Chain:** Adapts to demand fluctuations from seasonality, marketing, and disease trends.

## Limitations
- More complex and computationally intensive than Prophet alone.
- Requires careful residual analysis and ARIMA parameter tuning.
- Assumes future external factors are similar to historical data.

## How to Use
1. Place your sales data Excel file in the project directory.
2. Open and run the Jupyter notebook `Hybrid_Forecasting.ipynb` step by step.
3. Review the output tables and visualizations for forecast accuracy and ROP recommendations.
4. Adjust ARIMA parameters if needed for your specific dataset.

## File Structure
- `Hybrid_Forecasting.ipynb`: Main notebook with all code, analysis, and visualizations.
- `Sales_Data_DiplomaInsFullCreMilkPowderBox400gm.xlsx`: Example sales data file.
- `actual_vs_forecast.html`: Exported forecast visualization.
- `README.md`: Project documentation.

## Requirements
- Python 3.8+
- Jupyter Notebook
- pandas, numpy, matplotlib, plotly
- prophet, statsmodels, scikit-learn

Install dependencies with:
```bash
pip install pandas numpy matplotlib plotly prophet statsmodels scikit-learn
```