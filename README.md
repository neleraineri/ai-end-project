# ⌚ Watch Price Prediction

## 🧠 Project Description

This machine learning project predicts the resale market value of luxury watches based on technical attributes and listing data. Two datasets (`watch_prices.csv` and `watch_listings.csv`) are merged, cleaned, and enriched with engineered features. Two models are trained to estimate the final price:

- 🌲 **Random Forest Regressor**
- 📈 **Linear Regression**

An interactive [Gradio](https://www.gradio.app) interface allows users to test the models by entering watch specifications.

---

## 🧪 Results Summary

The **Random Forest model** clearly outperforms the linear regression model:
- Much lower RMSE (prediction error)
- Higher R² score (explained variance)
- More stable cross-validation results

> ✅ Using just 5 key features (`case_material`, `condition`, `automatic`, `brand`, `year`) already achieved strong results.  
> ✨ These were selected for interpretability and consistent availability across sources.

---

## 🔗 Project Links

| Type               | URL                                                                 |
|--------------------|----------------------------------------------------------------------|
| 🧠 Hugging Face     | *[Add your Hugging Face Space URL]*                                 |
| 💻 GitHub Repository| [https://github.com/neleraineri/ai-end-project](https://github.com/neleraineri/ai-end-project) |

---

## 📚 Data Sources

| File               | Description                                                |
|--------------------|------------------------------------------------------------|
| `watch_listings.csv` | Marketplace listings: brand, model, price, condition, etc. |
| `watch_prices.csv`   | Specs like diameter, material, strap, and water resistance |

🛠️ **Merged on**: `brand` and `model`

---

## 🧩 Engineered Features

| Feature         | Description                                                  |
|-----------------|--------------------------------------------------------------|
| `case_material` | Encoded case material (steel, gold, ceramic, etc.)           |
| `condition`     | Encoded condition (new, good, fair, unknown, etc.)           |
| `automatic`     | Binary flag: whether movement includes "automatic"           |
| `brand`         | Categorical brand encoding                                   |
| `year`          | Extracted from year strings in listings (e.g., “2019”)       |

---

## ⚙️ Model Training Details

### 📊 Dataset Summary
- Final merged dataset: **~385,000 rows** after cleaning
- 80/20 Train/Test split
- 5-fold Cross-Validation applied for reliability

---

## 🔍 Model Comparison (Final Metrics)

| Model             | Test R² | Test RMSE     | CV RMSE     | Notes                                  |
|------------------|---------|---------------|-------------|----------------------------------------|
| Linear Regression | 0.004   | 110,268.60    | 109,106.47  | Severely underfits, fails to generalize |
| Random Forest     | 0.348   | 89,185.20     | 87,893.65   | Stronger performance and generalization |

### ✅ Interpretation

The **Random Forest model** significantly outperformed **Linear Regression**:

- It reduced the prediction error by over **21,000 USD**
- It explained **34.8%** of the price variance compared to just **0.4%**
- It demonstrated more stable cross-validation results

> 🔍 **Conclusion**: Random Forest is the preferred model. It better handles the complexity and variance in watch prices and produces more trustworthy results.

---

## 💡 Future Work & Improvements

- Add case diameter, strap material, and movement type as features
- Use Gradient Boosting (XGBoost, LightGBM) for potential gains
- Explore brand-based clustering or segmentation
- Integrate visual data (images, watch face types, etc.)
- Outlier detection and filtering to improve generalization

---

## 🎛️ App Interface & Deployment

- Built using [Gradio](https://gradio.app)
- Users select case material, condition, brand, and year
- Model predicts expected resale value
- Available as a Hugging Face Space for interactive access