🎓 Student Performance Predictor 

A Machine Learning web application that predicts a student's final academic grade (G3) based on academic, behavioral, demographic, and educational characteristics.

The project covers the complete Machine Learning workflow, from data preprocessing and model training to web deployment.

🚀 Demo 

The application provides a simple and interactive web interface where users can enter student information and obtain an estimated G3 score out of 20.

🌐 Live demo: Coming soon

✨ Features 🎓 Predicts the student's final G3 grade 📊 Uses academic performance and student characteristics ⚙️ Complete preprocessing pipeline 🔢 Numerical feature scaling with StandardScaler 🔤 Categorical feature processing with OneHotEncoder 🤖 Trained Machine Learning model 🌐 Flask web application 📱 Responsive and modern interface ⚡ Instant predictions 🧠 Machine Learning 

The model uses the following features.

Numerical Features Feature Description G1 First period grade G2 Second period grade Failures Number of previous failures Study time Weekly study time Freetime Amount of free time Medu Mother's education level Fedu Father's education level Absences Number of school absences Age Student's age Categorical Features Feature Description School sup Whether the student receives extra educational support Higher Whether the student wants to pursue higher education Target G3 

G3 represents the student's final grade.

🔄 Machine Learning Pipeline 

The preprocessing and model are stored together in a single pipeline.

Student Data │ ▼ ┌───────────────────────┐ │ Input Features │ └───────────┬───────────┘ │ ▼ ┌───────────────────────┐ │ StandardScaler │ │ Numerical Features │ └───────────┬───────────┘ │ ▼ ┌───────────────────────┐ │ OneHotEncoder │ │ Categorical Features │ └───────────┬───────────┘ │ ▼ ┌───────────────────────┐ │ Machine Learning │ │ Model │ └───────────┬───────────┘ │ ▼ Predicted G3 

Because preprocessing is included in the pipeline, the web application does not need to manually reproduce the transformations used during training.

📈 Model Performance 

The optimized model achieved the following results on the evaluation data:

Metric Score MAE 1.06 MSE 2.95 R² 0.82 Interpretation MAE = 1.06 → the predictions are off by about 1.06 grade points on average. MSE = 2.95 → measures the squared prediction error. R² = 0.82 → the model explains approximately 82% of the variance in the target variable on the evaluated data. 🛠️ Technologies 🐍 Python 🧠 Scikit-learn 🐼 Pandas 🔢 NumPy 🌐 Flask 💾 Joblib 🎨 HTML 🎨 CSS ⚡ JavaScript 📁 Project Structure student-performance/ │ ├── app.py ├── final_model.pkl ├── requirements.txt ├── README.md │ └── templates/ └── index.html ⚙️ Installation 1. Clone the repository git clone https://github.com/MohamedNimaga123/Student-performance-predictor. Enter the project directory cd student-performance 3. Create a virtual environment python -m venv venv 

Activate it on Windows:

venv\Scripts\activate 4. Install dependencies pip install -r requirements.txt 5. Run the application python app.py 

The application will be available at:

http://127.0.0.1:5000 🎯 How to Use Open the web application. Enter the student's academic information. Select the categorical information. Click Predict G3. The application displays the estimated final grade. ⚠️ Disclaimer 

This application provides a machine learning-based estimate of academic performance. It should not be considered a definitive prediction of a student's actual final grade.

👨‍💻 Author 

Mohamed Nimaga

Interested in:

🤖 Artificial Intelligence 📊 Data Science 💻 Computer Science 🔐 Cybersecurity 🚀 Machine Learning ⭐ Future Improvements 

Possible improvements include:

🌐 Deploying the application online 📊 Adding prediction visualizations 📈 Showing model confidence or prediction ranges 🗃️ Adding prediction history 🔐 Adding user authentication 📱 Creating a mobile application 🤖 Experimenting with additional Machine Learning models 

⭐ If you find this project interesting, consider giving the repository a star!

