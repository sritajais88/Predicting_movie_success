🎬 Movie Success Prediction

This project builds a machine learning model to predict whether a movie will be Hit, Average, or Flop based on various movie attributes such as budget, popularity, and audience engagement. The application is deployed as an interactive web app using Streamlit.

📌 Project Overview
The goal of this project is to analyze movie metadata and build a predictive model that classifies movies into three categories:

Flop

Average

Hit

The prediction is based on the IMDb score ranges obtained from IMDb.

IMDb Score	Category
1 – 3	Flop
3 – 6	Average
6 – 10	Hit

Machine learning models are trained using various movie attributes such as:

Budget

Gross revenue

Number of votes

Social media popularity

Reviews

Cast popularity

📂 Project Structure
```Movie-Success-Prediction
│
├── data
│   ├── movie_metadata.csv
│   └── cleaned_movie_data.csv
│
├── models
│   ├── all_models.pkl
│   └── best_movie_model.pkl
│
├── notebook
│   └── EDA_and_Data_Cleaning.ipynb
│
├── src
│   ├── __init__.py
│   ├── config.py
│   └── preprocessing.py
│
├── app.py
├── requirements.txt
└── README.md
📁 Folder Description
📊 data

Contains the raw and processed datasets.

movie_metadata.csv
Raw movie dataset containing movie information such as ratings, cast details, budget, and reviews.

cleaned_movie_data.csv
Preprocessed dataset used for training the machine learning models.

🤖 models

Contains trained machine learning models.

all_models.pkl
Stores all trained models used during experimentation.

best_movie_model.pkl
Stores the best-performing model used for deployment in the Streamlit app.

The final model is based on the
Random Forest classifier.

📓 notebook

Contains Jupyter notebooks for:

Exploratory Data Analysis (EDA)

Data cleaning

Visualization

Initial feature analysis

EDA visualizations were created using:

Matplotlib

Seaborn

⚙️ src

Contains reusable Python modules.

config.py

Stores configuration variables such as:

dataset paths

target column

random state

test size

preprocessing.py

Handles the complete preprocessing pipeline including:

Missing value imputation

Feature scaling

Categorical encoding using
One-Hot Encoding

Train-test splitting

🌐 app.py

This file contains the interactive web application built with
Streamlit.

The application allows users to input movie details such as:

Genre

Budget

Number of votes

Social media popularity

Reviews

Country

Language

The app then predicts whether the movie will be:

Hit

Average

Flop

The trained model is loaded using joblib.

Example from the app:

```model = joblib.load("models/best_movie_model.pkl")

The user inputs are converted into a dataframe and passed to the trained model for prediction. 

app

📦 requirements.txt

Contains all required Python libraries for running the project.

Example dependencies include:

streamlit

pandas

numpy

scikit-learn

matplotlib

seaborn

joblib 

requirement

Install them using:

```pip install -r requirements.txt
🚀 Running the Application

Clone the repository

```git clone https://github.com/your-username/movie-success-prediction.git

Navigate to the project folder

```cd movie-success-prediction

Install dependencies

```pip install -r requirements.txt

Run the Streamlit application

```streamlit run app.py
📊 Machine Learning Pipeline

The machine learning workflow includes:

Data Exploration (EDA)

Data Cleaning

Feature Engineering

Data Preprocessing

Model Training

Model Evaluation

Deployment

The final model was selected based on performance metrics such as:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

📈 Model Evaluation

The performance of the models was evaluated using:

Confusion Matrix

Classification Report

Accuracy Score

The Random Forest model performed best and was selected for deployment.

🎯 Key Features of the Project

✔ End-to-End Machine Learning Pipeline
✔ Exploratory Data Analysis with Visualizations
✔ Feature Engineering and Preprocessing Pipelines
✔ Multiple Model Training and Evaluation
✔ Deployment using Streamlit
✔ Interactive User Interface

📌 Future Improvements

Add more movie datasets for better prediction accuracy

Improve class balancing for the Flop category

Deploy the application on cloud platforms

👩‍💻 Author

Srishti Jaiswal

Machine Learning Project – Movie Success Prediction
