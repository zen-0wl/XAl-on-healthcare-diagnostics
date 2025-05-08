# Explainable AI (XAI) for Chronic Illness Diagnostics

**Final Year Project (FYP)**

---

## Table of Contents

* [Abstract](#abstract)
* [Introduction](#introduction)
* [Literature Review](#literature-review)
* [Experimental Setup](#experimental-setup)
* [Methodology](#methodology)
* [Results](#results)
* [Conclusion](#conclusion)
* [Future Work](#future-work)
* [How to Run the Code](#how-to-run-the-code)
* [References](#references)

---

## Abstract

The rising incidence of chronic illnesses, such as stroke and cancer, demands advanced diagnostic models that are both **accurate** and **explainable** for healthcare professionals. This project introduces an **Explainable Artificial Intelligence (XAI) model** to enhance the interpretability of healthcare diagnostics. The structured methodology followed includes pre-modeling, modeling, and post-modeling phases, ensuring the datasets were collected, cleaned, and preprocessed thoroughly. The resulting model aims to foster transparency, enabling clinicians to trust AI predictions and use them to improve patient outcomes.

---

## Introduction

AI models are becoming essential tools in healthcare for tasks like **predicting stroke risk** or  **diagnosing cancer** . However, their black-box nature raises concerns about trust and interpretability. This project focuses on designing explainable models that balance predictive performance with transparency, helping healthcare providers make informed decisions.

---

## Literature Review

The project leverages **XAI techniques** such as:

* **LIME** and **Eli5** for model explanation on tabular data
* **SHAP** for feature importance analysis
* **Grad-CAM** for visual insights

Previous research highlights the importance of **XAI models** in medical diagnostics by demonstrating improved trust among clinicians and better outcomes for patients. Ensemble models and adaptive optimizers are particularly effective for healthcare applications.

---

## Experimental Setup

### 1. Data Collection

* **EEG datasets** for stroke prediction were collected from multiple sources to ensure comprehensive coverage.
* The datasets include information on  **smoking habits, glucose levels, hypertension** , and other health indicators.

### 2. Data Preprocessing

* **Normalization** and **standardization** ensured consistency across sources.
* Missing data and outliers were handled using **mean imputation** and  **outlier detection** .
* Encoding techniques were applied to maintain uniformity across datasets.

### 3. Feature Selection and Extraction

* Methods such as **recursive feature elimination** and **correlation-based filtering** were used to identify relevant features, improving predictive accuracy.

### 4. Model Selection

* Models such as **Adaptive Gradient Boosting** and ensemble models with **adaptive optimizers** were chosen to predict stroke risk.

---

## Methodology

### Pre-Modeling Phase

1. **Characterize Input Data**
2. **Perform Exploratory Data Analysis (EDA)**
3. **Standardize the Dataset**
4. **Extract Explainable Features**
5. **Summarize the Dataset**

### Modeling Phase

1. **Design Explainable Model Architectures**
2. **Adopt Hybrid Models or Neural Networks**
3. **Implement Ensemble Models for Accuracy and Interpretability**

### Post-Modeling Phase

1. **Extract Conclusions from Experiments**
2. **Define Explanation Targets and Drivers**
3. **Provide Macro-Explanations for Healthcare Professionals**
4. **Validate Model Outputs for Interpretability**

---

## Results

The project analyzed how features such as **age, BMI, hypertension, smoking status,** and **glucose levels** influence stroke risk using XAI techniques.

* **SHAP analysis** revealed:
  * **Age** is a dominant predictor of stroke.
  * **Smoking** and **hypertension** significantly increase stroke probability.
  * **Higher glucose levels** correlate with greater stroke risk.

#### Visualizations:

* **Figure 4** : Smoking status effect on stroke risk
* **Figure 5** : Average glucose levels and stroke likelihood
* **Figure 6** : Combined influence of age and BMI on stroke

The XAI models provided **detailed explanations** for predictions, giving healthcare professionals actionable insights.

---

## Conclusion

This project demonstrates the potential of **XAI techniques** in chronic illness diagnostics by balancing model accuracy with transparency. By incorporating tools such as **LIME, SHAP,** and  **Grad-CAM** , the models offer explainable predictions, enhancing trust among medical professionals. The findings emphasize the need for explainable healthcare models that can aid in effective clinical decision-making.

---

## Future Work

* **Extend the model** to include other chronic illnesses like cancer.
* **Integrate real-time data** from wearable health devices.
* Explore **new XAI techniques** to further improve interpretability.
* Conduct clinical trials to validate the model's effectiveness in real-world scenarios.

---

## How to Run the Code

1. **Clone the repository** :

   ```
   git clone https://github.com/zen-0wl/XAl-on-healthcare-diagnostics.git 
   cd XAl-on-healthcare-diagnostics
   ```
2. **Run the model** :

```
feature-selection.ipynb
```

3. **View results** :
   Run `feature.html` file to access **visualizations** and  **reports** on a webpage.

---

## References

* Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems.
* Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?": Explaining the predictions of any classifier. Proceedings of the 22nd ACM SIGKDD Conference.

---

--- 

Feel free to reach out for any questions or collaboration opportunities!
