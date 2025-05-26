# app.py – Gradio Interface mit Mapping für Watch Price Prediction

import gradio as gr
import pickle
import pandas as pd

# Modelle laden
with open("watch_rf_model.pkl", "rb") as f:
    rf_bundle = pickle.load(f)

with open("watch_lr_model.pkl", "rb") as f:
    lr_bundle = pickle.load(f)

models = {
    "Random Forest": rf_bundle,
    "Linear Regression": lr_bundle
}

# Mapping-Tabellen
type_map = {
    "steel": 1,
    "gold": 2,
    "titanium": 3,
    "ceramic": 4,
    "platinum": 5,
    "unknown": 0
}

condition_map = {
    "new": 0,
    "very good": 1,
    "good": 2,
    "fair": 3,
    "poor": 4,
    "unknown": 5
}

brand_map = {
    "rolex": 1,
    "omega": 2,
    "tag heuer": 3,
    "breitling": 4,
    "cartier": 5,
    "unknown": 0
}

def predict_price(model_choice, material, condition, automatic, brand, year):
    bundle = models[model_choice]
    model = bundle["model"]
    features = bundle["feature_names"]

    input_data = pd.DataFrame([[type_map[material], condition_map[condition], automatic, brand_map[brand], year]], columns=features)
    prediction = model.predict(input_data)[0]
    return f"💰 Geschätzter Marktpreis: ${prediction:,.2f}"

# Interface
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Dropdown(["Random Forest", "Linear Regression"], label="Modellwahl"),
        gr.Dropdown(list(type_map.keys()), label="Gehäusematerial"),
        gr.Dropdown(list(condition_map.keys()), label="Zustand"),
        gr.Radio([0, 1], label="Automatik (0 = Nein, 1 = Ja)"),
        gr.Dropdown(list(brand_map.keys()), label="Marke"),
        gr.Number(label="Produktionsjahr")
    ],
    outputs="text",
    title="🕰️ Uhrenpreis-Vorhersage",
    description="Gebe Uhrenmerkmale ein und erhalte eine Preisprognose basierend auf echten Listings."
)

if __name__ == "__main__":
    interface.launch(share=True)