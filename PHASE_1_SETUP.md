# Phase 1: Environment Setup & Kaggle API Configuration

## Step 1.1: Create Project Folder

Open Command Prompt (cmd) and run:

```bash
# Navigate to where you want to create the project (e.g., Desktop)
cd Desktop

# Create project folder
mkdir plant-disease-detection
cd plant-disease-detection

# Create subfolders
mkdir data data\raw data\processed models models\saved_model notebooks backend frontend tests tests\test_images
```

## Step 1.2: Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Your prompt should now show (venv)
```

## Step 1.3: Install Dependencies

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

**Note**: This will take 5-10 minutes. TensorFlow is large (~500MB).

## Step 1.4: Setup Kaggle API

### A. Get Kaggle API Token

1. Go to https://www.kaggle.com/
2. Click on your profile picture (top right) → **Account**
3. Scroll down to **API** section
4. Click **"Create New Token"**
5. This downloads a file called `kaggle.json`

### B. Configure Kaggle API

**For Windows:**

```bash
# Create .kaggle folder in your user directory
mkdir %USERPROFILE%\.kaggle

# Copy the kaggle.json file to .kaggle folder
# Replace YOUR_USERNAME with your Windows username
copy C:\Users\YOUR_USERNAME\Downloads\kaggle.json %USERPROFILE%\.kaggle\

# Or manually copy it:
# From: C:\Users\YOUR_USERNAME\Downloads\kaggle.json
# To: C:\Users\YOUR_USERNAME\.kaggle\kaggle.json
```

### C. Verify Kaggle API Setup

```bash
# Test kaggle CLI
kaggle datasets list

# If successful, you'll see a list of datasets
```

## Step 1.5: Open VS Code

```bash
# Open VS Code in project folder
code .
```

## Step 1.6: Setup Jupyter Kernel

In VS Code terminal (or cmd with venv activated):

```bash
# Install ipykernel
python -m ipykernel install --user --name=plant-disease-env --display-name "Python (Plant Disease)"
```

---

## Verification Checklist

- [ ] Virtual environment created and activated
- [ ] All packages installed successfully
- [ ] Kaggle API configured (kaggle.json in correct location)
- [ ] Kaggle CLI working (`kaggle datasets list` runs)
- [ ] VS Code opened in project folder
- [ ] Jupyter kernel installed

---

## Troubleshooting

### Issue: "kaggle command not found"
**Solution**: Make sure virtual environment is activated and kaggle is installed:
```bash
pip install kaggle
```

### Issue: TensorFlow installation fails
**Solution**: Try installing TensorFlow separately:
```bash
pip install tensorflow==2.15.0
```

### Issue: Kaggle API permission error
**Solution**: The kaggle.json file should be in `C:\Users\YOUR_USERNAME\.kaggle\`

---

## Next Steps

Once all verification items are checked, proceed to:
**Phase 2: Data Collection & Exploration**
