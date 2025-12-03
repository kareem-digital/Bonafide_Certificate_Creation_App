# Bonafide Certificate Generator

A web application and Python script to automatically generate bonafide certificates for students by reading data from an Excel file and populating a Word document template.

## 🌟 Two Ways to Use

### 1. Web App (Streamlit) - Recommended for Easy Use
- Beautiful web interface
- No coding knowledge required
- Can be deployed online for school-wide access
- Download certificates directly from browser

### 2. Command Line Script
- For automation and batch processing
- Direct Python script execution

## Features

- 🎓 Reads student data from an Excel file
- 📝 Generates personalized bonafide certificates
- 👥 Automatically handles gender-specific pronouns and relations (S/O for male, D/O for female)
- 💾 Creates individual Word documents for each student
- 🌐 Web interface for easy certificate generation
- ☁️ Can be deployed online for anyone to use

## Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

## Dependencies

Install all required Python packages using:

```bash
pip install -r requirements.txt
```

### Package Details

- **pandas**: For reading and processing Excel files
- **python-docx**: For creating and modifying Word documents
- **openpyxl**: Required by pandas to read .xlsx files
- **streamlit**: For the web application interface

## Project Structure

```
bonafide/
├── app.py                             # Streamlit web application
├── generate_single_certificates.py    # Command line script
├── bonafide_certificate.docx          # Word template with placeholders
├── student records.xlsx               # Excel file with student data
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore file
├── README.md                          # This file
├── DEPLOYMENT.md                      # Deployment guide
└── venv/                              # Virtual environment (optional)
```

## Excel File Format

The `student records.xlsx` file should have the following columns:

- **Roll.No**: Student roll number
- **St. ID**: Student ID
- **Reg. No**: Registration number (used to search for students)
- **Name**: Student name
- **Father**: Father's name
- **Class**: Student's class
- **Session**: Academic session
- **DOB**: Date of birth
- **Gender**: Gender (M/F)
- Other columns as needed

**Note**: The Excel file should have the school name in the first row, with actual column headers in the second row.

## Word Template

The `bonafide_certificate.docx` template should contain the following placeholders:

- `{{REGNO}}`: Registration number
- `{{NAME}}`: Student name
- `{{RELATION}}`: Relation (S/O or D/O)
- `{{FATHER}}`: Father's name
- `{{CLASS}}`: Class
- `{{SESSION}}`: Academic session
- `{{DOB}}`: Date of birth
- `{{PRONOUN_SUBJECT}}`: Subject pronoun (He/She)
- `{{PRONOUN_POSSESSIVE}}`: Possessive pronoun (His/Her)

## Setup

1. Clone or download this repository

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Ensure you have:
   - `student records.xlsx` with student data
   - `bonafide_certificate.docx` template with placeholders

## Usage

### Option 1: Web App (Streamlit) - Recommended

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Your browser will automatically open to http://localhost:8501

3. In the web interface:
   - Enter the Registration Number in the text field
   - Click "Search & Generate"
   - View student details
   - Click "Download Certificate" to save the file

4. **To share with others on your network:**
   - Streamlit will display a Network URL (e.g., http://192.168.x.x:8501)
   - Share this URL with anyone on the same WiFi network
   - They can access the app from their devices

### Option 2: Command Line Script

1. Run the script:
   ```bash
   python generate_single_certificates.py
   ```

2. Enter the **Reg. No** (Registration Number) when prompted:
   ```
   Enter Reg. No: 2552
   ```

3. The script will:
   - Search for the student with the given registration number
   - Generate a certificate using the template
   - Save it as `certificate_{REGNO}.docx`

## Examples

### Web App
```bash
(venv) PS C:\Users\...\bonafide> streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.100:8501
```

### Command Line
```bash
(venv) PS C:\Users\...\bonafide> python generate_single_certificates.py
Enter Reg. No: 2552
Certificate generated: certificate_2552.docx
```

## Important Notes

- **Reg. No vs St. ID**: Make sure to enter the Registration Number (Reg. No), not the Student ID (St. ID)
- The script handles registration numbers stored as decimals in Excel (e.g., 2552.0)
- If a student is not found, the script will display an error message

## Troubleshooting

### "No student found with Reg. No: XXX"
- Verify the registration number exists in the Excel file
- Make sure you're entering the **Reg. No** column value, not the St. ID

### "KeyError: 'Reg. No'"
- Check that the Excel file has headers in the correct row
- The script expects headers in the second row (after the school name)

### Missing dependencies
- Make sure all required packages are installed: `pip install -r requirements.txt`

## 🚀 Deployment (Making it Available Online)

To deploy this app online so anyone can access it from anywhere:

1. **Quick Start**: See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed step-by-step instructions

2. **Recommended Platform**: Streamlit Community Cloud (Free!)
   - Push your code to GitHub
   - Deploy on https://share.streamlit.io/
   - Get a public URL like `https://your-app.streamlit.app`
   - Free for public repositories

3. **Alternative Options**:
   - Heroku (requires credit card for verification)
   - Local network deployment (for school WiFi only)

For complete deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

## License

This project is open source and available for educational purposes.
