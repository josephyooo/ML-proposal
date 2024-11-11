import streamlit as st

st.title("ML Midterm Checkpoint - Group 96")

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The primary methods of data preprocessing that we use include one-hot encoding, feature engineering with polynomial features, recursive feature elimination (RFE), and standardization to filter through the data. One-hot encoding helps in representing categories independently, allowing variables like price and square feet to be represented without implying relationships between them. Feature engineering with polynomial features involves creating interaction terms between existing features, enabling the model to capture more complex relationships within the data. Recursive feature elimination then helps to select only the most relevant features, ensuring that unnecessary or redundant interactions do not cause overfitting while retaining essential information. This was especially important to use since an estimated 46000 features were generated, so eliminating a majority of them is necessary. Finally, standardizing the resulting features to a uniform scale, with a mean of 0 and a standard deviation of 1, enhances the model's stability by preventing large features from skewing the optimization process.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In order to find the optimal value for RFE, we implemented grid search since it searches through a set of parameters to find a value that gives us the best performance. However, due to long runtimes of each iteration being exceedingly long, our grid search was smaller with bigger steps, with values being tested of `500`, `600`, `700`, `725`, `750`,  `775`, `800`, `825`, `850`, `875`, `900`, `1000`, `1100`, and `1200`.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The machine learning algorithm that we use is linear regression, since the relationship between house prices and the features that the house are often linear. This provides a model that displays the different coefficients and factors that affect the price, and how much impact they have. Furthermore, linear regression is also computationally efficient and can handle large datasets, so the vast amount of housing data that is available can be easily sifted through.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In summary, the combination of the data-preprocessing methods of one-hot encoding to represent individual categories, recursive feature limination to focus on relevant features, and standardization to have a uniform scale for the data, and linear regression to yield predictive results, are methods that are very good to analyze and predict house prices and factors that affect that price.
"""

st.markdown(markdown_text3, unsafe_allow_html=True)

st.header("Results and Discussion")

st.image("images/visualization.png")

markdown_text3 = f"""
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;From the previous list of RFE values listed that we used, we found that lower values like `500` were underfitting, `1200` was overfitting with a magnitude of `~1,000,000,000`, while still giving a RMSE value of ~`0.017`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this plot visualization of the resulting data, the residuals are centered around the red dotted zero line, indicating that the model's predictions are unbiased and do not contain over/under prediction. The y-axis scale being values extremely close to 0 also indicate that the randomness of the majority of the points do not create a pattern and the residuals being consistent across all predicted values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;However, there are some outlier points that may indicate that could negatively affect the model, but because of randomness in house prices and the quantifiable data like square feet, this could serve to be major exception and are not commonly found in real life beyond possibly 1 or 2 instances. As such, some next steps and ways to address the outliers could be to simply remove them from the data for their exceedingly rare occurrence in the real world, or to implement model regularization to penalize large coefficients and making the model less sensitive to their impact.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Moving forward, we plan to implement two other methods, of Random Forest as a test on non-linear relationships and Attention to emphasize critical features by dynamically adjusting weights.
"""

st.markdown(markdown_text3, unsafe_allow_html=True)
st.markdown("""
<table>
    <tr>
        <th>Name</th>
        <th>Midterm Checkout Contribution</th>
    </tr>
    <tr>
        <td><strong>Ryan He</strong></td>
        <td>
            <ul>
                <li>5 preprocessing methods
                    <ul>
                        <li>One-Hot encoding</li>
                        <li>Imputations of missing data</li>
                        <li>Standardizing</li>
                        <li>Min-Maxing data values</li>
                        <li>RFE</li>
                        <li>Creation of higher dimensional features</li>
                    </ul>
                </li>
                <li>Machine Learning Algorithm
                    <ul>
                        <li>Linear regression</li>
                    </ul>
                </li>
                <li>Evaluation Metrics
                    <ul>
                        <li>RMSE</li>
                    </ul>
                </li>
                <li>Visualization
                    <ul>
                        <li>Frequency of DataPrice distribution</li>
                        <li>Residuals vs. Predicted value plot (standardized)</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td><strong>Maximus Genio</strong></td>
        <td>
            Preprocessing & algorithm validation,
            Summary validation,
            and Additional evaluation metrics (needs fixing R^2, Adjusted R^2)
        </td>
    </tr>
    <tr>
        <td><strong>Daniel Pan</strong></td>
        <td>
            Analysis and discussion on visualization results,
            written summary on method implementation,
            Streamlit page setup,
        </td>
    </tr>
    <tr>
        <td><strong>Joseph Yoo</strong></td>
        <td>
            &nbsp;
        </td>
    </tr>
    <tr>
        <td><strong>Hussein Rmaile</strong></td>
        <td>
            &nbsp;
        </td>
    </tr>
</table>
""", unsafe_allow_html=True)

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