# pneumonia-Detection-and-classification-system
Developed a deep learning-based web app using Flask and CNN to detect pneumonia from chest X-ray images. Integrated Keras model for binary classification with real-time image upload, preprocessing, and prediction display on a user-friendly interface.

🔍 Features
Upload chest X-ray images via web interface

Real-time prediction using trained CNN model

Classification output with confidence score

Image preprocessing (resize, grayscale, normalization)

Clean UI built with Flask and HTML templates

🧠 Model Overview
Architecture: Convolutional Neural Network (CNN)

Frameworks: TensorFlow & Keras

Input size: 500x500 grayscale images

Output: Binary classification (Positive / Negative)

🛠️ Tech Stack
Frontend: HTML, CSS (Jinja templates)

Backend: Python, Flask

Libraries: TensorFlow, Keras, NumPy, Keras Preprocessing

Deployment: Local Flask Server (port 5000)

🚀 How to Run Locally
Clone the repository

git clone https://github.com/yourusername/pneumonia-detection.git
cd pneumonia-detection
Install dependencies

pip install -r requirements.txt
Place your trained model
Save your model file as pneu_cnn_model.h5 in the models/ directory.

Run the app
python app.py

Open your browser and go to http://localhost:5000/

📁 Project Structure
cpp
Copy
Edit
├── app.py
├── models/
│   └── pneu_cnn_model.h5
├── static/
│   └── uploaded images
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
📌 Notes
Ensure images are in .jpg or .png format.
Model expects grayscale X-ray images resized to 500x500.
