Forest cover classification model developed using Tree-based modeling and Multi-class classification
The goal is to **predict forest cover types** from cartographic and environmental data using **multi-class classification**.

## 📂 Project Overview
This project applies **Decision Tree classification** to identify forest cover types based on various environmental features.

### Key Steps:
1. **Data Loading** – Imported `covertype.csv` dataset
2. **Data Cleaning** – Handled missing values and categorical encoding using `pd.get_dummies()`
3. **Feature-Target Split** – Separated features from `Cover_Type` target variable
4. **Model Training** – Implemented Decision Tree Classifier with train/test split
5. **Model Evaluation** – Assessed performance using accuracy score and confusion matrix
6. **Visualization** – Created confusion matrix and feature importance plots

## 🛠️ Technical Implementation
- **Algorithm**: Decision Tree Classifier
- **Preprocessing**: One-hot encoding for categorical features
- **Evaluation Metrics**: Accuracy score, confusion matrix
- **Visualization**: Matplotlib for model interpretation

## 📊 Results
- Achieved [91.60<img width="731" height="581" alt="Screenshot 2025-10-17 013611" src="https://github.com/user-attachments/assets/828c2e61-2139-4546-9216-a3e833ff54bb" />
]% classification accuracy
- Identified key environmental features influencing forest cover types
- Visualized model performance through confusion matrix analysis

## 🎯 Business Application
This model can assist forestry services and environmental agencies in:
- Automated forest type mapping
- Resource allocation planning
- Environmental impact assessments
- Biodiversity conservation efforts

## 📁 Files
- `forest_cover.py` - Main implementation code
- `covertype.csv` - Dataset from UCI Machine Learning Repository
- `README.md` - Project documentation

## 🚀 How to Run
1. Install requirements: `pandas`, `scikit-learn`, `matplotlib`
2. Run: `python forest_cover.py`
3. View generated confusion matrix and feature importance plots


*Part of Elevvo Pathways ML Internship - Task 3: Multi-class Classification*

![Uploading Screenshot 2025-10-17 013611.png…]()
<img width="1561" height="941" alt="Screenshot 2025-10-17 015555" src="https://github.com/user-attachments/assets/2e911ecc-a57e-4401-86ff-be4aa27715b8" />


