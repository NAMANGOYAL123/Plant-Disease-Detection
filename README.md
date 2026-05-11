# Plant Disease Detection 

A complete end-to-end deep learning application for detecting plant diseases from leaf images using TensorFlow/Keras, FastAPI, and a modern web interface.

## 📋 Table of Contents
- [Features](#features)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Project Structure](#project-structure)
- [Usage Instructions](#usage-instructions)
- [API Documentation](#api-documentation)
- [Model Information](#model-information)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- **Deep Learning Model**: CNN-based model using Transfer Learning (EfficientNetB0)
- **Multiple Input Methods**: Upload files or provide image URLs
- **Real-time Predictions**: Fast inference with confidence scores
- **Top-K Predictions**: Get multiple disease predictions with probabilities
- **Health Recommendations**: Actionable treatment recommendations
- **REST API**: FastAPI backend with automatic documentation
- **Modern Web UI**: Responsive interface with drag-and-drop support
- **Comprehensive Evaluation**: Confusion matrix, classification reports, and metrics

## 🏗️ System Architecture

```
┌─────────────────┐
│   Frontend      │
│  (HTML/CSS/JS)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   FastAPI       │
│   Backend       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  TensorFlow     │
│  Model Handler  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Trained Model  │
│   (.keras)      │
└─────────────────┘
```

## 📦 Prerequisites

- **Python 3.12.6** (other 3.8+ versions should work)
- **8GB+ RAM** recommended
- **5GB+ disk space** for dataset and models
- **Windows OS** (guide optimized for Windows, but works on other OS)
- **Internet connection** for downloading dataset and dependencies

## 🚀 Installation Guide

### Phase 1: Environment Setup

1. **Create Project Directory**
```bash
# Navigate to your desired location
cd Desktop

# Create project folder
mkdir plant-disease-detection
cd plant-disease-detection
```

2. **Create Virtual Environment**
```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

This will install:
- TensorFlow 2.15.0 (CPU version)
- FastAPI & Uvicorn
- Keras, NumPy, Pandas
- Image processing libraries (Pillow, OpenCV)
- Kaggle API
- Jupyter Notebook

### Phase 2: Kaggle API Setup

1. **Get Kaggle API Token**
   - Go to https://www.kaggle.com/
   - Click profile → Account → API → "Create New Token"
   - Download `kaggle.json`

2. **Configure Kaggle**
```bash
# Create .kaggle directory
mkdir %USERPROFILE%\.kaggle

# Copy kaggle.json (replace YOUR_USERNAME)
# just give the path of your kaggle.json file 
copy C:\Users\YOUR_USERNAME\Downloads\kaggle.json %USERPROFILE%\.kaggle\
```

3. **Verify Kaggle Setup**
```bash
kaggle datasets list
```

### Phase 3: Data Collection

Run the data collection script:
```bash
python download_data.py
```

This will:
- Download PlantVillage dataset (~2GB)
- Extract and organize files
- Display dataset structure

### Phase 4: Model Training

Open Jupyter Notebook:
```bash
jupyter notebook
```

Run notebooks in order:
1. **01_data_exploration.ipynb**: Explore dataset, visualize samples
2. **02_model_training.ipynb**: Train the model (30-60 minutes on CPU)
3. **03_model_evaluation.ipynb**: Evaluate model performance

### Phase 5: Backend Setup

Your trained model is now in `models/best_model.h5`

### Phase 6: Run the Application

1. **Start FastAPI Backend**
```bash
cd backend
python app.py
```

The API will start at `http://localhost:8000`

2. **Open Web Interface**
   
   Open `frontend/index.html` in your browser, or serve it:
```bash
# From project root
python -m http.server 3000 --directory frontend
```

Then open `http://localhost:3000`

## 📁 Project Structure

```
plant-disease-detection/
│
├── data/
│   ├── raw/                    # Downloaded PlantVillage dataset
│   └── processed/              # Preprocessed data (optional)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_model_evaluation.ipynb
│
├── models/
│   ├── best_model.keras        # Trained model
│   ├── model_info.json         # Model metadata
│   ├── dataset_config.json     # Dataset configuration
│   └── saved_model/            # Additional saved models
│
├── backend/
│   ├── app.py                  # FastAPI application
│   ├── model_handler.py        # Model loading & prediction
│   ├── utils.py                # Helper functions
│   └── config.py               # Configuration settings
│
├── frontend/
│   ├── index.html              # Web interface
│   ├── style.css               # Styling
│   └── script.js               # Frontend logic
│
├── uploads/                    # Temporary upload storage
├── requirements.txt            # Python dependencies
├── download_data.py            # Data collection script
└── README.md                   # This file
```

## 📖 Usage Instructions

### Web Interface

1. **Upload Image**
   - Drag & drop image or click to browse
   - Or enter image URL

2. **Analyze**
   - Click "Analyze Image"
   - Wait for results (2-5 seconds)

3. **View Results**
   - Predicted disease class
   - Confidence score
   - Top 3 predictions
   - Treatment recommendations

### API Usage

**Predict with File Upload:**
```bash
curl -X POST "http://localhost:8000/api/predict/upload" \
  -F "file=@plant_image.jpg" \
  -F "top_k=3"
```

**Predict with URL:**
```bash
curl -X POST "http://localhost:8000/api/predict/url" \
  -H "Content-Type: application/json" \
  -d '{"image_url": "https://example.com/leaf.jpg", "top_k": 3}'
```

**Get Model Info:**
```bash
curl "http://localhost:8000/api/info"
```

**Get All Classes:**
```bash
curl "http://localhost:8000/api/classes"
```

## 📚 API Documentation

Once the backend is running, access interactive API docs at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/health` | Detailed health status |
| GET | `/api/info` | Model information |
| GET | `/api/classes` | List all disease classes |
| POST | `/api/predict/upload` | Predict from uploaded file |
| POST | `/api/predict/url` | Predict from image URL |
| POST | `/api/predict/visualize` | Get prediction with visualization |

## 🤖 Model Information

- **Architecture**: Transfer Learning with MobileNetV2
- **Framework**: TensorFlow 2.15 / Keras
- **Input Size**: 224 × 224 × 3
- **Dataset**: PlantVillage (38+ classes, 50,000+ images)
- **Training**: 25 epochs with data augmentation
- **Expected Accuracy**: 90%+ on validation set

### Supported Plant Diseases

The model can detect diseases in:
- Tomato
- Potato
- Pepper
- Apple
- Grape
- Corn
- And many more...

(See full list at `/api/classes` endpoint)

## 🐛 Troubleshooting

### Common Issues

**1. Kaggle API Not Working**
```bash
# Solution: Verify kaggle.json location
dir %USERPROFILE%\.kaggle
# Should show kaggle.json
```

**2. TensorFlow Installation Failed**
```bash
# Try installing separately
pip install tensorflow==2.15.0
```

**3. Model Not Loading**
- Ensure `models/best_model.keras` exists
- Check if model training completed successfully
- Verify model file isn't corrupted

**4. CORS Errors in Browser**
- Ensure backend is running
- Check API_BASE_URL in `script.js`
- Try using `http://localhost:8000` not `http://127.0.0.1:8000`

**5. Out of Memory During Training**
- Reduce batch size in config
- Use fewer epochs
- Close other applications

### Performance Tips

**For Faster Training:**
- Reduce number of epochs
- Decrease image size (e.g., 128×128)
- Use smaller dataset subset for testing

**For Better Accuracy:**
- Increase epochs (30-50)
- Add more data augmentation
- Fine-tune more layers
- Try EfficientNet instead of MobileNet

## 📝 Next Steps

### Improvements You Can Make:

1. **Model Enhancements**
   - Try different architectures (EfficientNet, ResNet)
   - Implement ensemble models
   - Add test-time augmentation

2. **Backend Features**
   - Add user authentication
   - Implement prediction history
   - Add batch prediction endpoint
   - Cache predictions

3. **Frontend Improvements**
   - Add camera capture
   - Show prediction confidence visualization
   - Implement result history
   - Add dark mode

4. **Deployment**
   - Deploy to cloud (AWS, GCP, Azure)
   - Use Docker containers
   - Add HTTPS/SSL
   - Implement rate limiting

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

- PlantVillage Dataset creators
- TensorFlow/Keras team
- FastAPI developers
- Open source community

---


