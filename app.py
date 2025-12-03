import streamlit as st
import pandas as pd
from docx import Document
import io
from datetime import datetime
import hashlib

# Page configuration
st.set_page_config(
    page_title="Bonafide Certificate Generator",
    page_icon="📜",
    layout="centered"
)

# Password authentication
def check_password():
    """Returns True if the user has entered the correct password."""

    # Get password from Streamlit secrets, or use default for local testing
    try:
        correct_password = st.secrets.get("password", "school2024")
    except:
        correct_password = "school2024"  # Default password for local testing

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hashlib.sha256(st.session_state["password"].encode()).hexdigest() == hashlib.sha256(correct_password.encode()).hexdigest():
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state["password_correct"] = False

    # First run or password not yet entered
    if "password_correct" not in st.session_state:
        st.markdown("### 🔐 Authentication Required")
        st.markdown("Please enter the password to access the certificate generator.")
        st.text_input(
            "Password",
            type="password",
            on_change=password_entered,
            key="password",
            help="Contact school administration for the password"
        )
        st.info("💡 Default password for testing: `school2024`")
        return False

    # Password incorrect
    elif not st.session_state["password_correct"]:
        st.markdown("### 🔐 Authentication Required")
        st.markdown("Please enter the password to access the certificate generator.")
        st.text_input(
            "Password",
            type="password",
            on_change=password_entered,
            key="password",
            help="Contact school administration for the password"
        )
        st.error("❌ Incorrect password. Please try again.")
        return False

    # Password correct
    else:
        return True

# Check authentication before showing the app
if not check_password():
    st.stop()

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem;
        font-size: 1.1rem;
    }
    .upload-section {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 2rem;
    }
    .success-message {
        padding: 1rem;
        background-color: #d4edda;
        border-radius: 0.5rem;
        color: #155724;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("📜 Bonafide Certificate Generator")
st.markdown("### M.A.M. I CUM MILLAT PUBLIC SCHOOL")
st.markdown("---")

# Initialize session state for files
if 'excel_file' not in st.session_state:
    st.session_state.excel_file = None
if 'word_file' not in st.session_state:
    st.session_state.word_file = None
if 'df' not in st.session_state:
    st.session_state.df = None

# File Upload Section
st.markdown("## 📁 Step 1: Upload Required Files")
st.markdown('<div class="upload-section">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📊 Student Records (Excel)")
    uploaded_excel = st.file_uploader(
        "Upload Excel File",
        type=['xlsx', 'xls'],
        help="Upload the student records Excel file",
        key="excel_uploader"
    )

    if uploaded_excel:
        st.session_state.excel_file = uploaded_excel
        try:
            # Load Excel file
            st.session_state.df = pd.read_excel(uploaded_excel, header=1)
            st.success(f"✅ Loaded {len(st.session_state.df)} student records")
        except Exception as e:
            st.error(f"❌ Error reading Excel file: {str(e)}")
            st.session_state.df = None

with col2:
    st.markdown("#### 📄 Certificate Template (Word)")
    uploaded_word = st.file_uploader(
        "Upload Word Template",
        type=['docx'],
        help="Upload the bonafide certificate template",
        key="word_uploader"
    )

    if uploaded_word:
        st.session_state.word_file = uploaded_word
        st.success("✅ Template loaded successfully")

st.markdown('</div>', unsafe_allow_html=True)

# Check if files are uploaded
if st.session_state.excel_file is None or st.session_state.word_file is None:
    st.warning("⚠️ Please upload both files to continue")

    # Show instructions
    with st.expander("📖 How to use this app"):
        st.markdown("""
        ### Instructions:

        1. **Upload Student Records** (Excel file)
           - Must contain columns: Reg. No, Name, Father, Class, Session, DOB, Gender
           - First row should be school name, second row should be column headers

        2. **Upload Certificate Template** (Word file)
           - Must contain placeholders: {{REGNO}}, {{NAME}}, {{FATHER}}, {{CLASS}}, etc.

        3. **Enter Registration Number** and generate certificate

        4. **Download** the generated certificate

        ### Note:
        - Files are stored only during your session
        - When you close the browser, files are deleted
        - You'll need to upload again next time you use the app
        """)

    st.stop()

# Show statistics if data is loaded
if st.session_state.df is not None:
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", len(st.session_state.df))
    with col2:
        st.metric("Total Classes", st.session_state.df["Class"].nunique())
    with col3:
        st.metric("Sessions", st.session_state.df["Session"].nunique())

# Generate Certificate Section
st.markdown("---")
st.markdown("## 🔍 Step 2: Generate Certificate")

# Input section
col1, col2 = st.columns([2, 1])

with col1:
    reg_input = st.text_input(
        "Enter Registration Number",
        placeholder="e.g., 2552",
        help="Enter the student's registration number (Reg. No)",
        key="reg_input"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    search_button = st.button("🔍 Search & Generate", use_container_width=True)

# Generate certificate function
def generate_certificate(row, reg_no, word_template):
    try:
        # Extract student information
        name = row["Name"]
        father = row["Father"]
        class_ = row["Class"]
        session = row["Session"]
        dob = row["DOB"]
        gender = str(row["Gender"]).strip().upper()

        # Gender logic
        if gender == "M":
            relation = "S/O"
            pronoun_subject = "He"
            pronoun_possessive = "His"
        else:
            relation = "D/O"
            pronoun_subject = "She"
            pronoun_possessive = "Her"

        # Load Word template from uploaded file
        doc = Document(word_template)

        # Replace placeholders in paragraphs
        for para in doc.paragraphs:
            text = para.text
            text = text.replace("{{REGNO}}", str(reg_no))
            text = text.replace("{{NAME}}", name)
            text = text.replace("{{RELATION}}", relation)
            text = text.replace("{{FATHER}}", father)
            text = text.replace("{{CLASS}}", str(class_))
            text = text.replace("{{SESSION}}", session)
            text = text.replace("{{DOB}}", str(dob))
            text = text.replace("{{PRONOUN_SUBJECT}}", pronoun_subject)
            text = text.replace("{{PRONOUN_POSSESSIVE}}", pronoun_possessive)
            para.text = text

        # Replace placeholders in tables (if any)
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        text = para.text
                        text = text.replace("{{REGNO}}", str(reg_no))
                        text = text.replace("{{NAME}}", name)
                        text = text.replace("{{RELATION}}", relation)
                        text = text.replace("{{FATHER}}", father)
                        text = text.replace("{{CLASS}}", str(class_))
                        text = text.replace("{{SESSION}}", session)
                        text = text.replace("{{DOB}}", str(dob))
                        text = text.replace("{{PRONOUN_SUBJECT}}", pronoun_subject)
                        text = text.replace("{{PRONOUN_POSSESSIVE}}", pronoun_possessive)
                        para.text = text

        # Save to BytesIO object
        doc_io = io.BytesIO()
        doc.save(doc_io)
        doc_io.seek(0)

        return doc_io, name, None
    except Exception as e:
        return None, None, f"Error generating certificate: {str(e)}"

# Search and generate certificate
if search_button:
    if not reg_input:
        st.warning("⚠️ Please enter a registration number.")
    else:
        reg_input = reg_input.strip()

        with st.spinner("🔄 Searching for student..."):
            # Filter student record
            df = st.session_state.df
            student = df[df["Reg. No"].fillna(0).astype(int).astype(str) == reg_input]

            if student.empty:
                st.error(f"❌ No student found with Registration Number: {reg_input}")
                st.info("💡 Tip: Make sure you're entering the Reg. No, not the St. ID")
            else:
                # Get first (and only) row
                row = student.iloc[0]

                # Display student information
                st.success(f"✅ Student Found!")

                # Student details card
                st.markdown("### Student Details")
                info_col1, info_col2 = st.columns(2)

                with info_col1:
                    st.write(f"**Name:** {row['Name']}")
                    st.write(f"**Father's Name:** {row['Father']}")
                    st.write(f"**Class:** {row['Class']}")

                with info_col2:
                    st.write(f"**Reg. No:** {reg_input}")
                    st.write(f"**Session:** {row['Session']}")
                    st.write(f"**DOB:** {row['DOB']}")

                st.markdown("---")

                # Generate certificate
                with st.spinner("📝 Generating certificate..."):
                    doc_io, name, error = generate_certificate(row, reg_input, st.session_state.word_file)

                    if error:
                        st.error(error)
                    else:
                        st.success("🎉 Certificate generated successfully!")

                        # Download button
                        st.download_button(
                            label="📥 Download Certificate",
                            data=doc_io,
                            file_name=f"certificate_{reg_input}_{name.replace(' ', '_')}.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <small>Bonafide Certificate Generator v2.0<br>
        🔒 Secure • Files stored in session only<br>
        Made with ❤️ using Streamlit</small>
    </div>
""", unsafe_allow_html=True)
