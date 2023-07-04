
# CAMPUS PLACEMENT PREDICTION

The Placement of students is one of the most important objective of an educational institution. Reputation and yearly admissions of an institution invariably depend on the placements it provides it students with. That is why all the institutions, arduously, strive to strengthen their placement department so as to improve their institution on a whole. Any assistance in this particular area will have a positive impact on an institution’s ability to place its students. This will always be helpful to both the students, as well as the institution.

The main goal is to predict whether the student will be recruited in campus placements or not based on the available factors in the dataset.

The algorithm used is Logistic Regression. Logistic Regression is basically a supervised classification algorithm. In a classification problem, the target variable(or output), y, can take only discrete values for given set of features(or inputs), X. Talking about the dataset, it contains the secondary school percentage, Inter/diploma percentage, degree percentage, backlogs and register for placement training. After predicting the result its efficiency is also calculated based on the dataset. The dataset used here is in .csv format.


## Objectives:
   The aim of project is to predict whether the student will be recruited in campus placements or not based on the available factors in the dataset.
## IDE:
Google Colaboratory
## Libraries for Model Development:

* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit-learn
## Libraries Installation:

1.Pandas 
```bash
  pip install pandas
```
2.Numpy
```bash
  pip install numpy
```
3.Matplotlib
```bash
  pip install matplotlib
```
4.Seaborn
```bash
  pip install seaborn
```
5.Scikit Learn
```bash
  pip install scikit-Learn
```
    
## Dataset:
The Campus Recruitment Prediction (Course Project) Dataset has been used for this purpose, taken from the Kaggle*. link is below.

* [Dataset](https://www.kaggle.com/c/ml-with-python-course-project/data)
## Life Cycle of Machine Learning Project:
Life Cycle of implementing machine learning application.

* Gathering the Data
* Data Preparation
* Data Preprocessing
* Create Model
* Evaluate Model
* Deploy the model
## Step by step Approach for Model Development:

**Step 1**: Import the required modules.

**Step 2**: Now to read the dataset that we are going to use for the analysis and then checking the dataset(Data Collection).

**Step 3**: **Data Exploration**
>>It is a crucial part of the model development process.It is a process to analyze the data to understand and summarize its main characteristics using statistical and visualization methods.

**Step 4**: **Data Processing and Feature Selection**
>>Data preprocessing is the process of transforming raw data into a form suitable for analysis and model development. It is one of the most critical steps in determining the success of the final model.
There are several ways to preprocess your data. It may include one or more of the following steps:
* Removing irrelevant features from your dataset
* Filling in missing values
* reducing the size of the dataset and feature set
* Transforming categorical variables into numerical variables (or vice versa)
* Normalizing the data points

**Step 5**: **Model Development**
>>In this Project i am using Support vector classifier for model development.
While choosing the algorithm, you may want to consider:
* Data Size: How big is the data? Does it need to be processed quickly or slowly? Does your algorithm requires a lot of data to learn, or can it learn from limited data points?
* Type of problem: What kind of problems can this algorithm address? Are there specific data handling needs for a given algorithm? How well does the model respond to missing data?
* Availability: Are there existing libraries or packages available for a given algorithm?

**Step 6**: **Model Evaluation**
>>Once the model is trained, it is essential to evaluate the model and understand how to interpret the results before deploying it.

**Step 7**: **Model Deployment**
>>Now that you have your model ready, the final step is to deploy the model into production. It’s one of the most essential steps in machine learning because it allows you to use your data for real-world applications.
## STREAMLIT FOR MODEL DEPLOYMENT:

Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers.Streamlit allows you to create a stunning-looking application with only a few lines of code.

* [Streamlit](https://streamlit.io/)-website
## Libraries for Model Deployment:
* Streamlit 
* joblib
## Library Installation:
```bash
  pip install streamlit
```
## Steps for Model Deployment:

**Step 1**: Organize machine learning code into a script or module that loads your trained model and makes predictions. Ensure that code is working correctly and produces the desired outputs.

**Step 2**: Create a new Python script or module for Streamlit app. Import the necessary libraries, including Streamlit, and define the structure of your app.

**Step 3**: Use Streamlit's API to design the user interface of theapp. Streamlit provides various components such as sliders, dropdowns, and buttons that you can use to create interactive elements for user input and display.

**Step 4**: **Load the model**
>>In Streamlit app, load the trained machine learning model that we want to deploy. Make sure to import any required dependencies and set up any preprocessing steps needed to prepare input data for the model.

**Step 5**: **Define the prediction logic**
>>Write the code that takes user input, preprocesses it if necessary, and passes it to the loaded model for prediction. Capture the model's output and display it to the user.

**Step 6**: Run the Streamlit app using the below command
```bash
  streamlit run Campus_Placement_Prediction_app.py
```


**Step 7**: **Test the app** 
>>Interact with app in the web browser to ensure that everything is functioning as expected. Test different inputs and verify that the predictions are accurate.
## Images:


### THANK YOU FOR VISITING MY PROJECT
