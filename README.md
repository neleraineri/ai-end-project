# Watch Price Prediction

## Project Description

This machine learning application predicts the second-hand market value of luxury wristwatches based on their physical characteristics and brand metadata. It merges marketplace listings with structured watch specifications and trains two regression models to estimate resale value.

The final app allows users to input a set of watch features and receive a predicted price using a trained Random Forest or Linear Regression model.

---

## Results

The Random Forest model clearly outperformed the linear regression model in test accuracy and overall fit. However, both models are limited by feature simplicity (only 5 inputs). More complex features like diameter, movement, and strap material could improve performance significantly.

> With roughly 385,000 combined listing records, the model performs best when trained on standardized categorical features with engineered encodings.

---

## Name & URLs

| Name               | URL                                                                 |
|--------------------|----------------------------------------------------------------------|
| Hugging Face Space | [Watch Price Prediction](https://huggingface.co/spaces/rainele/watch_prediction) |
| GitHub Repository  | [ai-end-project](https://github.com/neleraineri/ai-end-project)     |

---

## Data Sources and Features Used

| Source File         | Features Used                                                                 |
|---------------------|-------------------------------------------------------------------------------|
| `watch_listings.csv`| brand, model, price, case material, condition, movement, year of production  |
| `watch_prices.csv`  | technical specs including material, strap, water resistance, and model detail|

**Merge key:** `brand` and `model` (inner join)

---

## Features Created

| Feature Name        | Description                                                                |
|---------------------|----------------------------------------------------------------------------|
| `case_material`     | Encoded material of the case (e.g., steel, gold, ceramic)                  |
| `condition`         | Encoded watch condition (new, good, unknown)                               |
| `automatic`         | Binary feature if movement string contains "automatic"                     |
| `brand`             | Categorical encoding of brand names                                        |
| `year`              | Parsed 4-digit year from noisy production year string (e.g., "c. 2010")    |

---

## Model Training

### Dataset Size

- Final cleaned dataset: ~385,000 entries
- Five selected input features: `case_material`, `condition`, `automatic`, `brand`, `year`

### Data Splitting Method

- 80/20 Train-Test split
- Additional 5-fold Cross Validation for RMSE scoring

---

## Performance Comparison

| Model             | R² (Test) | RMSE (Test) | CV RMSE     | Notes                               |
|------------------|-----------|-------------|-------------|-------------------------------------|
| Linear Regression | 0.004     | 110,268.60  | 109,106.47  | Very weak linear fit (underfitting) |
| Random Forest     | 0.348     | 89,185.20   | 87,893.65   | Performs significantly better       |

### Interpretation

- Random Forest model captures non-linear interactions between features better.
- Linear Regression fails to explain price variance due to simplistic assumptions.
- The feature space is too limited for strong predictions — additional fields like diameter, strap material, or watch reference would be beneficial.

---

## App Deployment

- Gradio-based interface
- Users select: model, case material, brand, condition, automatic flag, and year
- App returns predicted watch resale value using selected model

---

## External Downloads

Due to GitHub's file size limit, all large files (datasets and models) are hosted externally on SwitchDrive:

**Download all project files:**  
[https://drive.switch.ch/index.php/s/aaxUVcf2uKY2pps](https://drive.switch.ch/index.php/s/aaxUVcf2uKY2pps)

**Included files:**
- `watch_rf_model.pkl` — Trained Random Forest model  
- `watch_lr_model.pkl` — Trained Linear Regression model  
- `cleaned_watch_data.csv` — Final merged dataset used for training  
- `watch_listings.csv` — Raw listing data  
- `watch_prices.csv` — Technical specifications data

---

## Future Improvements

- Add additional features: diameter, strap material, reference number
- Integrate visual features (e.g., watch face images)
- Use boosting models (XGBoost, LightGBM) for better generalization
- Remove outliers and apply log transformation on price
- Add brand reputation index or pre-trained watch category embeddings

---

## References

- Feature importance charts (if applicable)
- Hugging Face deployment logs
- [Gradio Documentation](https://gradio.app)