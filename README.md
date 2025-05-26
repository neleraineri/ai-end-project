# Watch Price Prediction

## Project Description

This machine learning project predicts the second-hand market value of luxury wristwatches using physical attributes and brand metadata. The workflow merges two datasets: marketplace listings and structured watch specifications. Feature engineering is applied, and two regression models are trained:

- Random Forest Regressor
- Linear Regression

The final application allows users to enter watch characteristics and receive an estimated resale price via an interactive web interface.

---

## Results

The Random Forest model significantly outperforms Linear Regression in both accuracy and generalization. However, due to the simplicity of the feature set (five inputs), both models have limited capacity to capture the full complexity of price dynamics.

> The dataset includes ~385,000 records. The best results are achieved using standardized categorical features and basic engineered variables like production year and movement type.

---

## Name & URLs

| Name               | URL                                                                 |
|--------------------|----------------------------------------------------------------------|
| Hugging Face Space | [Watch Price Prediction](https://huggingface.co/spaces/rainele/watch_prediction) |
| GitHub Repository  | [ai-end-project](https://github.com/neleraineri/ai-end-project)     |

---

## Data Sources and Features Used

| Source File          | Features Used                                                                       |
|----------------------|--------------------------------------------------------------------------------------|
| `watch_listings.csv` | brand, model, price, case material, condition, movement, year of production         |
| `watch_prices.csv`   | technical specifications including case material, bracelet type, movement type, and year of production |

**Merge key:** `brand` and `model` (inner join)

## Features Created

| Feature Name        | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `case_material`     | Encoded watch case material (e.g., steel, gold, ceramic); categorical codes |
| `condition`         | Encoded watch condition (new, very good, good, etc.); mapped to integer     |
| `automatic`         | Binary feature indicating if movement field contains the word "automatic"   |
| `brand`             | Brand name encoded as categorical integer                                   |
| `year`              | 4-digit year extracted from `yop` (year of production); numeric, imputed if missing |

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

| Model              | R² (Test) | RMSE (Test) | CV RMSE     | Notes                                 |
|-------------------|-----------|-------------|-------------|----------------------------------------|
| Linear Regression  | 0.004     | 110,268.60  | 109,106.47  | Underfits significantly; low variance explained |
| Random Forest      | 0.348     | 89,185.20   | 87,893.65   | Much stronger performance and generalization   |

### Interpretation

- The Random Forest model captures non-linear interactions between features more effectively.
- Linear Regression fails to model the underlying complexity, leading to poor predictive power.
- The limited feature space (5 features) constrains both models — including additional fields like diameter, strap material, or reference number could improve performance.

---

## App Deployment

- Gradio-based web interface
- Users select: model type, case material, condition, automatic flag, brand, and year of production
- The app predicts the expected resale value using the selected trained model

---

## External Downloads

Due to GitHub's file size limits, all large files (datasets and models) are hosted externally on SwitchDrive:

**Download all project files here:**  
[https://drive.switch.ch/index.php/s/aaxUVcf2uKY2pps](https://drive.switch.ch/index.php/s/aaxUVcf2uKY2pps)

**Included files:**
- `watch_rf_model.pkl` — Trained Random Forest model  
- `watch_lr_model.pkl` — Trained Linear Regression model  
- `cleaned_watch_data.csv` — Final merged and preprocessed dataset  
- `watch_listings.csv` — Raw listing data scraped or collected from marketplaces  
- `watch_prices.csv` — Technical specifications data per model reference

---

## Future Improvements

- Add additional features: case diameter, strap material, reference numbers
- Integrate image-based features (watch face, brand visuals, etc.)
- Explore boosting algorithms like XGBoost or LightGBM
- Apply outlier detection or price transformation (e.g. log-scale)
- Add watch popularity, rarity, or resale index metrics

---

## References

- Feature importance visualizations (if available)
- Hugging Face Space build and logs
- [Gradio Documentation](https://gradio.app)