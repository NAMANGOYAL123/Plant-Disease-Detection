# 🚀 Deployment & Testing Guide

## Complete Step-by-Step Deployment Process

### ✅ Pre-Deployment Checklist

Before deploying, ensure you have completed:

- [ ] Phase 1: Environment setup ✓
- [ ] Phase 2: Kaggle API configured ✓
- [ ] Phase 3: Dataset downloaded ✓
- [ ] Phase 4: Model trained and saved ✓
- [ ] Phase 5: Model evaluated ✓
- [ ] All files in correct directories ✓

---

## 📦 Step 1: Verify File Structure

Your project should look like this:

```
plant-disease-detection/
├── backend/
│   ├── app.py
│   ├── model_handler.py
│   ├── utils.py
│   └── config.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── models/
│   ├── best_model.keras
│   ├── model_info.json
│   └── dataset_config.json
├── data/
│   └── raw/
│       └── [PlantVillage dataset]
└── requirements.txt
```

**Verification Command:**
```bash
# Check if model exists
dir models\best_model.keras

# Check if backend files exist
dir backend\app.py
```

---

## 🔧 Step 2: Backend Deployment

### 2.1 Test Backend Locally

1. **Activate Virtual Environment**
```bash
cd plant-disease-detection
venv\Scripts\activate
```

2. **Navigate to Backend**
```bash
cd backend
```

3. **Start FastAPI Server**
```bash
python app.py
```

Expected output:
```
============================================================
🚀 Starting Plant Disease Detection API
============================================================
Loading model...
✅ Model loaded from: ../models/best_model.keras
✅ Model info loaded. Classes: 38
✅ Model handler initialized successfully!
✅ API is ready to accept requests!
============================================================

INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

4. **Verify Backend is Running**

Open browser and go to:
- http://localhost:8000 (should show {"status":"running",...})
- http://localhost:8000/docs (Swagger UI documentation)

### 2.2 Test API Endpoints

**Test 1: Health Check**
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "message": "Model is loaded and ready"
}
```

**Test 2: Get Model Info**
```bash
curl http://localhost:8000/api/info
```

**Test 3: Get Classes**
```bash
curl http://localhost:8000/api/classes
```

**Test 4: Test Prediction (using a test image)**
```bash
curl -X POST "http://localhost:8000/api/predict/upload" \
  -F "file=@path/to/test/image.jpg" \
  -F "top_k=3"
```

---

## 🌐 Step 3: Frontend Deployment

### 3.1 Option A: Simple File Access (Easiest)

1. **Open index.html directly**
   - Navigate to `frontend` folder
   - Double-click `index.html`
   - Opens in default browser

**Note**: Some browsers may block CORS. If you get errors, use Option B.

### 3.2 Option B: Local HTTP Server (Recommended)

1. **Open new terminal (keep backend running)**

2. **Navigate to project root**
```bash
cd plant-disease-detection
venv\Scripts\activate
```

3. **Start HTTP Server**
```bash
python -m http.server 3000 --directory frontend
```

4. **Open Browser**
```
http://localhost:3000
```

### 3.3 Test Frontend

1. **Test File Upload**
   - Click on upload area or drag image
   - Select a plant leaf image
   - Click "Analyze Image"
   - Verify results appear

2. **Test URL Upload**
   - Click "Image URL" tab
   - Enter image URL (e.g., from Unsplash or your test images)
   - Click "Load Image"
   - Click "Analyze Image"
   - Verify results appear

---

## 🧪 Step 4: Integration Testing

### Test Scenarios

**Scenario 1: Healthy Leaf**
- Upload image of healthy plant
- Expected: Should detect "healthy" with high confidence

**Scenario 2: Diseased Leaf**
- Upload image of diseased plant
- Expected: Should detect specific disease with confidence >75%

**Scenario 3: Invalid File**
- Try uploading non-image file
- Expected: Error message about file type

**Scenario 4: Large File**
- Try uploading file >10MB
- Expected: Error message about file size

**Scenario 5: URL Image**
- Use URL from internet
- Expected: Load and predict successfully

---

## 📊 Step 5: Performance Testing

### Backend Performance

**Test Prediction Speed:**
```python
# Create test_performance.py in backend/
import time
import requests

url = "http://localhost:8000/api/predict/upload"
image_path = "path/to/test/image.jpg"

times = []
for i in range(10):
    start = time.time()
    with open(image_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files, data={'top_k': 3})
    end = time.time()
    times.append(end - start)
    print(f"Request {i+1}: {end-start:.3f}s")

print(f"\nAverage: {sum(times)/len(times):.3f}s")
print(f"Min: {min(times):.3f}s")
print(f"Max: {max(times):.3f}s")
```

**Expected Performance:**
- Average: 1-3 seconds on CPU
- Min: 0.5-1 second
- Max: 3-5 seconds

---

## 🐛 Troubleshooting Deployment Issues

### Issue 1: Backend Won't Start

**Symptoms:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate

# Reinstall requirements
pip install -r requirements.txt
```

### Issue 2: Model Not Found

**Symptoms:**
```
Model file not found at: models/best_model.keras
```

**Solution:**
```bash
# Check if model exists
dir models\best_model.keras

# If not, retrain model or check path in config.py
```

### Issue 3: CORS Errors in Frontend

**Symptoms:**
```
Access to fetch blocked by CORS policy
```

**Solution:**
- Ensure backend is running
- Use HTTP server for frontend (Option B)
- Check API_BASE_URL in script.js matches backend address

### Issue 4: Predictions Taking Too Long

**Solutions:**
- Reduce image size before upload
- Use smaller model (adjust in training)
- Close unnecessary applications
- Consider GPU acceleration for production

### Issue 5: Frontend Not Loading Images

**Solution:**
```javascript
// Check script.js API_BASE_URL is correct
const API_BASE_URL = 'http://localhost:8000';  // Not https://
```

---

## 🔒 Security Considerations (For Production)

When deploying to production:

1. **Add Authentication**
   - Implement API keys
   - Add user authentication
   - Rate limiting

2. **Input Validation**
   - Validate all inputs server-side
   - Scan uploaded files
   - Sanitize file names

3. **HTTPS/SSL**
   - Use HTTPS for all connections
   - Get SSL certificate
   - Force HTTPS redirects

4. **Environment Variables**
   - Store sensitive config in .env
   - Don't commit secrets to git
   - Use environment-specific configs

---

## 📝 Deployment Checklist

Use this checklist when deploying:

### Local Testing
- [ ] Backend starts without errors
- [ ] All API endpoints respond correctly
- [ ] Frontend loads successfully
- [ ] File upload works
- [ ] URL upload works
- [ ] Predictions are accurate
- [ ] Error handling works

### Production Ready
- [ ] Environment variables configured
- [ ] Security measures implemented
- [ ] Performance optimized
- [ ] Logging configured
- [ ] Monitoring setup
- [ ] Documentation complete
- [ ] Backup strategy in place

---

## 🎯 Quick Start Commands

**Terminal 1 (Backend):**
```bash
cd plant-disease-detection
venv\Scripts\activate
cd backend
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd plant-disease-detection
venv\Scripts\activate
python -m http.server 3000 --directory frontend
```

**Access:**
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs
- Backend: http://localhost:8000

---

## 📚 Additional Resources

### Testing Tools
- **Postman**: For API testing
- **curl**: Command-line API testing
- **Browser DevTools**: Frontend debugging

### Monitoring
- Check terminal for backend logs
- Use browser console for frontend errors
- Monitor system resources during testing

### Documentation
- API Docs: http://localhost:8000/docs
- This guide
- README.md
- Code comments

---

## ✅ Success Criteria

Your deployment is successful when:

1. ✅ Backend starts and responds to health check
2. ✅ Frontend loads without errors
3. ✅ Can upload and analyze images
4. ✅ Predictions are returned within 5 seconds
5. ✅ Results display correctly
6. ✅ Error handling works properly

---

**🎉 Congratulations! Your Plant Disease Detection System is now deployed and running!**
