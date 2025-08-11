# ASEAN DIWA - Digital Innovation for Women Advancement

A Streamlit application built with stlite for analyzing and visualizing women's advancement metrics across ASEAN countries.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- [uv package manager](https://github.com/astral-sh/uv) installed

### Installing uv (if not already installed)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (using pip):**
```bash
pip install uv
```

## 🛠️ Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/StanleyPangaruy/aseandiwa.git
cd aseandiwa
```

### 2. Create Virtual Environment and Install Dependencies
```bash
# Create a new virtual environment with uv
uv venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### 3. Run the Application

#### Option A: Standard Streamlit (for development/testing)
```bash
uv run streamlit run streamlit_app.py
```
The app will be available at `http://localhost:8501`


#### Option B: Local HTTP Server (for testing stlite in browser)
```bash
# Serve the static files
python -m http.server 8000
# or with uv
uv run python -m http.server 8000
```
Then open `http://localhost:8000` in your browser

## 📁 Project Structure
```
asean-diwa/
├── README.md
├── requirements.txt
├── pyproject.toml          # uv configuration (optional)
├── .python-version         # Python version specification
├── main.py                 # Main Streamlit application
├── index.html              # Stlite configuration for deployment
├── data/
│   ├── numerical_indicators.csv
│   ├── non_numerical_indicators.csv
│   └── metadata.csv
├── assets/
    └── images/


```

## 📦 Dependencies

### Core Requirements (requirements.txt)
```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.15.0
altair>=5.0.0
pillow>=9.5.0
openpyxl>=3.1.0
```


## ⚡ Using uv for Package Management

### Install packages
```bash
# Install a single package
uv pip install package-name

# Install from requirements file
uv pip install -r requirements.txt

# Install development dependencies
uv pip install -r requirements-dev.txt
```

### Update packages
```bash
# Update all packages
uv pip install --upgrade -r requirements.txt

# Update a specific package
uv pip install --upgrade package-name
```

### Generate requirements file
```bash
# Generate requirements.txt from current environment
uv pip freeze > requirements.txt
```


**Happy coding! 🚀**