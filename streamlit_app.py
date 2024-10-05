import streamlit as st

st.title("ML Proposal Group - 96")

st.header("Introduction/Background")
# Create the markdown text with a hyperlink for the specific phrase
markdown_text1 = f"""
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Predicting house prices is an important indicator for real estate stakeholders, including buyers, sellers, and investors. With numerous factors influencing prices, such as location, property size, and condition, predicting accurate sale prices can be complex. House price prediction is a critical problem that goes beyond traditional metrics like the House Price Index (HPI), which measures broad market trends but lacks the granularity needed for individual home price prediction [1]. Recent studies have shown that machine learning models, by incorporating factors such as location, house age, and property features, can significantly enhance prediction accuracy [1][2]. Predicting house prices is crucial for real estate stakeholders and remains complex due to interdependent factors like location, property size, and amenities, as highlighted by studies using publicly available datasets in cities like Bengaluru [3].

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our project aims to explore these advanced methods, using the [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview) dataset from Kaggle, which provides a rich set of features—79 features—to predict housing costs based on property-specific attributes.
"""



# Render the markdown text
st.markdown(markdown_text1, unsafe_allow_html=True)


st.header("Problem Definement")

markdown_text2 = f"""
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The objective of this project is to develop 3 machine learning models that can predict the **SalePrice** of a house based on various features provided in the dataset. Accurate house price prediction is important for financial decision-making and investment planning. The problem lies in identifying the best model and preprocessing techniques to capture the underlying patterns in the data. This project aims to explore multiple machine learning algorithms to create an accurate predictive model.
"""

st.markdown(markdown_text2, unsafe_allow_html=True)

st.header("Methods")

markdown_text3 = f"""
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will apply 3 data preprocessing techniques. Feature encoding, one-hot encoding or label encoding, will convert categorical data, such as building type and sale condition, into usable numerical representations. Data normalization (Min/Max scaling) will standardize continuous variables like lot area. Additionally, dimensionality reduction through feature selection and Principal Component Analysis (PCA) will remove irrelevant or redundant features to improve model generalization.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For our house price prediction, we propose 3 ML models:

- **_Linear Regression_** will serve as a baseline, offering interpretability and fast training.
- **_Random Forest_** will handle complex, non-linear relationships and provide feature importance ranking, giving insight into significant variables like location or house size.
- **_Attention_** will emphasize the most critical features by dynamically adjusting attention weights, improving predictive accuracy.

"""

st.markdown(markdown_text3, unsafe_allow_html=True)

markdown_text4 = f"""
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will evaluate models R-squared (R²), Mean Squared Error (MSE), and Mean Absolute Percentage Error (MAPE). R² measures how well the model explains house price variance, with Random Forest and Attention expected to outperform Linear Regression due to their ability to capture complex relationships. MSE will assess the accuracy of predictions by penalizing larger errors, with Random Forest expected to have lower MSE than Linear Regression, as it better handles non-linear patterns. Attention should further reduce MSE by focusing on the most important features. MAPE will provide insights into the relative prediction errors across different price ranges. Linear Regression may struggle with outliers, while Random Forest and Attention are anticipated to perform better due to their capacity for handling diverse data. Overall, Attention is expected to deliver the best results, with the lowest MSE and MAPE, and the highest R².
We expect Random Forest to outperform Linear Regression due to its ability to capture feature interactions, while Attention will further enhance performance by prioritizing important features. Our goal is to create models that provide accurate price predictions to assist real estate stakeholders in making informed decisions. This project addresses sustainability and ethical implications by highlighting the role of accurate predictions in promoting responsible real estate practices. Considerations will be made regarding data privacy and the potential biases in machine learning models.

"""

st.header("Results and Discussion")

st.markdown(markdown_text4, unsafe_allow_html=True)

st.header("References")

markdown_text5 = f"""
[1]	Q. Truong, M. Nguyen, H. Dang, and B. Mei, “Housing Price Prediction via Improved Machine Learning Techniques,” Procedia Computer Science, vol. 174, pp. 433–442, 2020, doi: https://doi.org/10.1016/j.procs.2020.06.111.
"""
markdown_text6 = f"""
[2]	P.-Y. Wang, C.-T. Chen, J.-W. Su, T.-Y. Wang, and S.-H. Huang, “Deep Learning Model for House Price Prediction Using Heterogeneous Data Analysis Along With Joint Self-Attention Mechanism,” IEEE Access, vol. 9, pp. 55244–55259, 2021, doi: https://doi.org/10.1109/ACCESS.2021.3071306.
"""
markdown_text7 = f"""
[3]	J. Manasa, R. Gupta, and N. S. Narahari, “Machine Learning based Predicting House Prices using Regression Techniques,” IEEE Xplore, Mar. 01, 2020. https://ieeexplore.ieee.org/abstract/document/9074952/ (accessed Aug. 09, 2021).
"""

st.markdown(markdown_text5, unsafe_allow_html=True)
st.markdown(markdown_text6, unsafe_allow_html=True)
st.markdown(markdown_text7, unsafe_allow_html=True)

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

