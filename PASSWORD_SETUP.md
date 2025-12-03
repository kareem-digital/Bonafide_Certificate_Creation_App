# 🔐 Password Protection Setup

The app now has password protection! Only users with the password can access it.

## Default Password

For local testing, the default password is: **`school2024`**

⚠️ **IMPORTANT**: Change this password when deploying to Streamlit Cloud!

---

## Setting Custom Password on Streamlit Cloud

### Step 1: Deploy Your App

1. Go to https://share.streamlit.io/
2. Deploy your app as usual
3. Wait for deployment to complete

### Step 2: Configure Password in Secrets

1. **Go to your app's dashboard**
   - Visit https://share.streamlit.io/
   - Click on your app

2. **Open Settings**
   - Click the "⋮" (three dots) menu
   - Select "Settings"

3. **Add Secret**
   - Go to the "Secrets" tab
   - Add this content:
     ```toml
     password = "YourSecurePasswordHere"
     ```
   - Replace `YourSecurePasswordHere` with your actual password

4. **Save and Reboot**
   - Click "Save"
   - Click "Reboot app"

### Example Strong Passwords:

```toml
password = "MAMSchool@2024!"
password = "Bonafide#Cert$2024"
password = "SecurePass@MPS2024"
```

---

## How School Staff Will Use It

### Step 1: Visit the App URL

Share this URL with authorized school staff:
```
https://your-app-name.streamlit.app
```

### Step 2: Enter Password

When they visit the app, they'll see a password screen:
- Enter the password you configured
- Click Enter or press Enter key

### Step 3: Generate Certificates

Once authenticated:
- Enter student Registration Number
- Click "Search & Generate"
- Download the certificate

---

## For Local Development

### Using Default Password

Just run the app:
```bash
streamlit run app.py
```

Default password: `school2024`

### Using Custom Password Locally

1. Create `.streamlit/secrets.toml` file:
   ```bash
   mkdir .streamlit
   ```

2. Add your password:
   ```toml
   password = "your-local-password"
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

⚠️ **Note**: `.streamlit/secrets.toml` is in `.gitignore` and won't be committed to GitHub.

---

## Security Features

✅ Password is required to access the app
✅ Password is not stored in plain text in code
✅ Failed login attempts show error message
✅ Session management keeps you logged in
✅ Password is hashed before comparison

---

## Sharing with School Staff

When sharing the app with school staff, provide:

1. **App URL**: `https://your-app.streamlit.app`
2. **Password**: The password you configured
3. **Instructions**:
   - Visit the URL
   - Enter the password
   - Enter Registration Number
   - Download certificate

### Example Email to School Staff:

```
Subject: Bonafide Certificate Generator - Access Details

Dear Team,

The online bonafide certificate generator is now ready!

🔗 App URL: https://your-app-name.streamlit.app
🔐 Password: [Your Password Here]

How to use:
1. Visit the URL above
2. Enter the password
3. Enter student's Registration Number (Reg. No)
4. Click "Search & Generate"
5. Download the certificate

Please keep the password confidential and share only with authorized staff.

For support, contact: [Your Contact Info]

Best regards,
[Your Name]
```

---

## Troubleshooting

### "Incorrect password" message

- Double-check the password (case-sensitive)
- Make sure you saved the password in Streamlit Cloud secrets
- Try rebooting the app in Streamlit Cloud settings

### Password field not showing

- Clear your browser cache
- Try a different browser
- Check if the app deployed successfully

### Want to change password?

1. Go to Streamlit Cloud → Your App → Settings → Secrets
2. Update the password value
3. Save and reboot the app
4. Inform all users of the new password

---

## 🎓 Best Practices

1. **Use a strong password** - At least 12 characters with numbers and symbols
2. **Don't share publicly** - Only give password to authorized staff
3. **Change regularly** - Update password every 3-6 months
4. **Keep backup** - Store password in a secure password manager
5. **Monitor usage** - Check Streamlit Cloud analytics for unusual activity

---

**Remember**: This password protection adds a layer of security, but the data is still technically accessible on GitHub. For maximum security with highly sensitive data, consider running the app locally on school premises.
