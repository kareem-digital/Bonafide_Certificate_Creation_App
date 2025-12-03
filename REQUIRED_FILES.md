# 📁 Required Files for Deployment

This app requires two files that are **NOT included in this repository** for security reasons:

## Files You Need to Upload:

### 1. student records.xlsx
- **Description**: Excel file with student data
- **Location**: Must be in the root directory
- **Format**: See SECURITY.md for required columns

### 2. bonafide_certificate.docx
- **Description**: Word template for certificates
- **Location**: Must be in the root directory
- **Format**: Must contain placeholders like {{NAME}}, {{REGNO}}, etc.

## How to Deploy:

### Option A: For Personal/School Use (Private Data)

**Don't deploy to Streamlit Cloud** - Instead, run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then share the Network URL (e.g., http://192.168.x.x:8501) with people on your WiFi.

### Option B: For Demo/Testing (Sample Data)

If you want to deploy online for demonstration:

1. Create sample/dummy student records (with fake data)
2. Create a sample certificate template
3. Add these files before deploying
4. Clearly mark the deployment as "DEMO" version

## ⚠️ Important Security Note

**Never upload real student data to a public Streamlit Cloud deployment!**

Real student records contain sensitive personal information and should only be:
- Stored locally on secure computers
- Accessed through private networks
- Protected by proper authentication

---

For full security guidelines, see [SECURITY.md](SECURITY.md)
