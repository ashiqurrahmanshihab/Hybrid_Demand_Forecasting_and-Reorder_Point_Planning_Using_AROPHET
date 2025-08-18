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

## Performance Comparison
| Metric       | Prophet           | AROPHET Hybrid     |
|-------------|-------------------|--------------------|
| MAE         | 128.14            | 66.58              |
| RMSE        | 143.80            | 84.59              |
| MAPE (%)    | 10.86             | 5.64               |
| R²          | 0.018             | 0.660              |

AROPHET consistently outperforms Prophet across all metrics, providing more reliable and precise forecasts for inventory planning.

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

## Citation
If you use this project, please cite:
> Hybrid Demand Forecasting and Reorder Point Planning Using AROPHET in the Pharmaceutical Industry

## License
This project is released under the MIT License.