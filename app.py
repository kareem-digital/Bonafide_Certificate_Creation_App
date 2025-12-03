import streamlit as st
import pandas as pd
from docx import Document
import io
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Bonafide Certificate Generator",
    page_icon="📜",
    layout="centered"
)

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

# Load data function with caching
@st.cache_data
def load_student_data():
    try:
        df = pd.read_excel("student records.xlsx", header=1)
        return df, None
    except FileNotFoundError:
        return None, "Error: 'student records.xlsx' file not found. Please upload the file."
    except Exception as e:
        return None, f"Error loading data: {str(e)}"

# Generate certificate function
def generate_certificate(row, reg_no):
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

        # Load Word template
        doc = Document("bonafide_certificate.docx")

        # Replace placeholders
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

        # Save to BytesIO object
        doc_io = io.BytesIO()
        doc.save(doc_io)
        doc_io.seek(0)

        return doc_io, name, None
    except FileNotFoundError:
        return None, None, "Error: 'bonafide_certificate.docx' template not found."
    except Exception as e:
        return None, None, f"Error generating certificate: {str(e)}"

# Main app
def main():
    # Load student data
    df, error = load_student_data()

    if error:
        st.error(error)
        st.info("Please ensure 'student records.xlsx' is in the same directory as this app.")
        return

    # Show statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", len(df))
    with col2:
        st.metric("Total Classes", df["Class"].nunique())
    with col3:
        st.metric("Sessions", df["Session"].nunique())

    st.markdown("---")

    # Input section
    st.subheader("Generate Certificate")

    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])

    with col1:
        reg_input = st.text_input(
            "Enter Registration Number",
            placeholder="e.g., 2552",
            help="Enter the student's registration number (Reg. No)"
        )

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        search_button = st.button("🔍 Search & Generate", use_container_width=True)

    # Search and generate certificate
    if search_button:
        if not reg_input:
            st.warning("⚠️ Please enter a registration number.")
            return

        reg_input = reg_input.strip()

        with st.spinner("🔄 Searching for student..."):
            # Filter student record
            student = df[df["Reg. No"].fillna(0).astype(int).astype(str) == reg_input]

            if student.empty:
                st.error(f"❌ No student found with Registration Number: {reg_input}")
                st.info("💡 Tip: Make sure you're entering the Reg. No, not the St. ID")
                return

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
                doc_io, name, error = generate_certificate(row, reg_input)

                if error:
                    st.error(error)
                    return

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
            <small>Bonafide Certificate Generator v1.0<br>
            Made with ❤️ using Streamlit</small>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
