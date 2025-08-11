# ASEAN DIWA - Digital Innovation for Women Advancement

A Streamlit application built with stlite for analyzing and visualizing women's advancement metrics across ASEAN countries.

## 📊 Dataset Overview
- **Numerical Indicators**: 14 metrics
- **Non-numerical Indicators**: 9 metrics  
- **Metadata**: 37 rows
- **Focus**: Digital innovation and women's advancement in ASEAN region

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
git clone https://github.com/yourusername/asean-diwa.git
cd asean-diwa
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

#### Option B: Stlite Development Server (if using stlite-desktop)
```bash
# Install stlite-desktop if not already installed
uv pip install stlite-desktop

# Run with stlite
uv run stlite desktop streamlit_app.py
```

#### Option C: Local HTTP Server (for testing stlite in browser)
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
├── streamlit_app.py        # Main Streamlit application
├── index.html             # Stlite configuration for deployment
├── data/
│   ├── numerical_indicators.csv
│   ├── non_numerical_indicators.csv
│   └── metadata.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py     # Data loading utilities
│   ├── visualizations.py # Chart and visualization functions
│   └── utils.py          # Helper functions
├── assets/
│   ├── images/
│   └── styles.css
└── tests/
    ├── __init__.py
    ├── test_data_loader.py
    └── test_visualizations.py
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

### Development Requirements (requirements-dev.txt)
```
pytest>=7.4.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.5.0
jupyter>=1.0.0
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

## 🔧 Development Workflow

### 1. Setup Development Environment
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install all dependencies including dev tools
uv pip install -r requirements.txt -r requirements-dev.txt
```

### 2. Code Formatting and Linting
```bash
# Format code with black
uv run black .

# Lint with flake8
uv run flake8 src/ streamlit_app.py

# Type checking with mypy
uv run mypy src/ streamlit_app.py
```

### 3. Running Tests
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src/

# Run specific test file
uv run pytest tests/test_data_loader.py
```

### 4. Jupyter Development
```bash
# Start Jupyter lab
uv run jupyter lab

# Start Jupyter notebook
uv run jupyter notebook
```

## 🌐 Deployment

### GitHub Pages Deployment
1. Push your code to GitHub
2. Enable GitHub Pages in repository settings
3. The `index.html` file will serve your stlite application

### Vercel Deployment
1. Connect your GitHub repository to Vercel
2. Deploy automatically on commits
3. Access your live application

## 🐛 Troubleshooting

### Common Issues

**1. uv not found:**
```bash
# Make sure uv is in your PATH, or reinstall
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # or restart terminal
```

**2. Virtual environment issues:**
```bash
# Remove and recreate virtual environment
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

**3. Package conflicts:**
```bash
# Clear pip cache and reinstall
uv cache clean
uv pip install --force-reinstall -r requirements.txt
```

**4. Streamlit not starting:**
```bash
# Check if streamlit is installed
uv pip show streamlit

# Try running with full path
uv run python -m streamlit run streamlit_app.py
```

**5. Data loading issues:**
- Ensure CSV files are in the `data/` directory
- Check file permissions
- Verify CSV format and encoding

## 📝 Environment Variables

Create a `.env` file in the root directory (optional):
```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test them
4. Run code formatting: `uv run black .`
5. Run tests: `uv run pytest`
6. Commit your changes: `git commit -m 'Add some feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/asean-diwa/issues) page
2. Create a new issue with detailed description
3. Include error messages and system information

## 🙏 Acknowledgments

- ASEAN Secretariat for data and insights
- Streamlit team for the amazing framework
- Stlite developers for browser-based Python execution
- Contributors and supporters of women's digital advancement initiatives

---

**Happy coding! 🚀**