# 🔒 Security & File Upload Instructions

## Why Are Files Missing from GitHub?

For **security and privacy reasons**, the following sensitive files are NOT stored in this public GitHub repository:

- ❌ `student records.xlsx` - Contains private student information
- ❌ `bonafide_certificate.docx` - School's official certificate template

These files must be uploaded directly to Streamlit Cloud to keep student data private.

---

## 📤 How to Upload Files to Streamlit Cloud

### Method 1: Using Streamlit Cloud File Manager (Recommended)

After deploying your app on Streamlit Cloud:

1. **Go to your app's settings**
   - Visit: https://share.streamlit.io/
   - Click on your app
   - Click the "⋮" (three dots) menu
   - Select "Settings"

2. **Upload files using the file manager**
   - Go to the "Secrets" or "Files" section
   - Upload both files:
     - `student records.xlsx`
     - `bonafide_certificate.docx`

3. **Restart your app**
   - Click "Reboot app" for changes to take effect

### Method 2: Using GitHub Private Repository (Requires Streamlit Pro)

If you have Streamlit Pro:

1. Make your repository private
2. Add the sensitive files back
3. Streamlit will still be able to access them

### Method 3: Fork and Add Files Locally

For developers who fork this project:

1. Clone the repository
2. Add your own files:
   - `student records.xlsx` - Your school's student records
   - `bonafide_certificate.docx` - Your certificate template
3. Run locally using: `streamlit run app.py`
4. Do NOT push these files to a public repository

---

## 📋 File Format Requirements

### student records.xlsx

The Excel file must have these columns in the **second row** (first row should be school name):

| Roll.No | St. ID | Reg. No | Name | Father | Mother | DOB | Class | Section | Session | Gender | Mobile | ... |
|---------|--------|---------|------|--------|--------|-----|-------|---------|---------|--------|--------|-----|

**Important columns:**
- `Reg. No` - Registration number (used for search)
- `Name` - Student name
- `Father` - Father's name
- `Class` - Student's class
- `Session` - Academic session
- `DOB` - Date of birth
- `Gender` - M for Male, F for Female

### bonafide_certificate.docx

The Word template must contain these placeholders:

- `{{REGNO}}` - Registration number
- `{{NAME}}` - Student name
- `{{RELATION}}` - S/O or D/O
- `{{FATHER}}` - Father's name
- `{{CLASS}}` - Class
- `{{SESSION}}` - Academic session
- `{{DOB}}` - Date of birth
- `{{PRONOUN_SUBJECT}}` - He/She
- `{{PRONOUN_POSSESSIVE}}` - His/Her

---

## 🔐 Security Best Practices

### ✅ DO:
- Keep student data files private and secure
- Use Streamlit Cloud's file upload feature
- Regularly update your dependencies
- Use strong passwords for your GitHub account
- Enable 2FA (Two-Factor Authentication) on GitHub

### ❌ DON'T:
- Never commit student data to public repositories
- Don't share student records in screenshots or documentation
- Don't hardcode sensitive information in code
- Don't ignore security warnings

---

## 🚨 What to Do If Files Were Accidentally Committed

If you accidentally pushed sensitive files to GitHub:

1. **Remove files from Git history**
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch 'student records.xlsx'" \
     --prune-empty --tag-name-filter cat -- --all
   ```

2. **Force push to GitHub**
   ```bash
   git push origin --force --all
   ```

3. **Change any exposed passwords or sensitive data**

4. **Consider the data as compromised** and take appropriate action

---

## 📞 Support

If you need help with file uploads or security concerns:
- Check Streamlit Cloud documentation: https://docs.streamlit.io/
- Contact your school's IT department
- Review this project's GitHub issues

---

**Remember**: Student data privacy is critical. Always handle it with care! 🔒
