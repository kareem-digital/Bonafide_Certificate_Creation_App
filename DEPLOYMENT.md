# Deployment Guide for Bonafide Certificate Generator

This guide will help you deploy your Streamlit app so anyone can access it online.

## Method 1: Streamlit Community Cloud (Recommended - Free!)

Streamlit Community Cloud is free and the easiest way to deploy your app.

### Prerequisites
- A GitHub account
- Your project pushed to a GitHub repository

### Step-by-Step Instructions

#### 1. Prepare Your Repository

1. Create a GitHub account at https://github.com if you don't have one

2. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name it something like `bonafide-certificate-generator`
   - Choose "Public" (required for free Streamlit Cloud)
   - Click "Create repository"

#### 2. Push Your Code to GitHub

Open your terminal in the project directory and run:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - Bonafide Certificate Generator"

# Add your GitHub repository as remote (replace with your username)
git remote add origin https://github.com/YOUR_USERNAME/bonafide-certificate-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

#### 3. Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io/

2. Click "Sign in with GitHub" and authorize Streamlit

3. Click "New app" button

4. Fill in the details:
   - **Repository**: Select your repository (e.g., `YOUR_USERNAME/bonafide-certificate-generator`)
   - **Branch**: `main`
   - **Main file path**: `app.py`

5. Click "Deploy!"

6. Wait 2-3 minutes for deployment to complete

7. Your app will be live at: `https://YOUR_USERNAME-bonafide-certificate-generator.streamlit.app`

### Important Notes for Deployment

⚠️ **Required Files**: Make sure these files are in your repository:
- `app.py` - The Streamlit application
- `requirements.txt` - Python dependencies
- `student records.xlsx` - Student data
- `bonafide_certificate.docx` - Certificate template

⚠️ **Data Privacy**:
- If your student records contain sensitive information, consider using Streamlit's secrets management
- For production use with sensitive data, use private repositories (requires Streamlit Pro)

## Method 2: Heroku (Alternative - Requires Credit Card)

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

### Files Needed

1. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

2. Create `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

### Deploy to Heroku

```bash
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Push to Heroku
git push heroku main

# Open your app
heroku open
```

## Method 3: Local Network (For School Use Only)

If you want to run this only within your school network:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run app.py
```

3. Streamlit will show two URLs:
   - **Local URL**: http://localhost:8501 (only for you)
   - **Network URL**: http://192.168.x.x:8501 (accessible by anyone on same WiFi)

4. Share the Network URL with others in your school

## Testing Your Deployed App

1. Open the deployed URL
2. Enter a valid registration number (e.g., 2552)
3. Click "Search & Generate"
4. Verify the student details appear correctly
5. Download the certificate and check if all fields are filled properly

## Troubleshooting

### App won't deploy
- Check that all required files are in the repository
- Verify `requirements.txt` has all dependencies
- Check Streamlit Cloud logs for errors

### "File not found" errors
- Ensure `student records.xlsx` and `bonafide_certificate.docx` are in the repository
- Check file names match exactly (including spaces and case)

### App is slow
- Large Excel files can slow down the app
- Consider using CSV format for faster loading
- Use `@st.cache_data` for data loading (already implemented)

## Updating Your Deployed App

To update your deployed app:

1. Make changes to your code locally
2. Commit and push to GitHub:
```bash
git add .
git commit -m "Description of changes"
git push
```
3. Streamlit Cloud will automatically redeploy (takes 1-2 minutes)

## Security Best Practices

1. **Don't commit sensitive data** to public repositories
2. Use **environment variables** for sensitive configurations
3. Consider **authentication** for production use
4. Regularly **update dependencies** for security patches

## Custom Domain (Optional)

To use a custom domain like `certificates.yourschool.com`:

1. Upgrade to Streamlit Pro (paid)
2. Follow Streamlit's custom domain setup guide
3. Update your DNS settings

## Support

For issues with:
- **Streamlit deployment**: https://docs.streamlit.io/streamlit-community-cloud
- **GitHub**: https://docs.github.com
- **This app**: Create an issue in your GitHub repository

---

Happy Deploying! 🚀
