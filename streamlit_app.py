import streamlit as st
import os
import base64
from PIL import Image
from io import BytesIO


def main():
    st.set_page_config(page_title="Shawn Kam - Resume", layout="centered")

    st.markdown(
        f"""
        <style>
            /* Change the font */
            body {{
                font-family: 'Georgia', serif;
            }}
            h1 {{
                color: #4a47a3;
            }}
            h2 {{
                color: #2e9cca;
            }}
            h3 {{
                color: #a4161a;
            }}
            a {{
                color: #0e9aa7;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Add a decorative border to the page
    st.markdown(
        """
        <style>
        .stApp {
            border: 2px solid #4a47a3;
            border-radius: 10px;
            padding: 1em;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    
# Set the URL of the image
image_url = "https://github.com/shawnkam95/st-Resume/blob/main/Resume.jpg?raw=true"

st.title("Shawn Kam's Resume")
# Load the image from the URL using requests and PIL
try:
    response = requests.get(image_url)
    response.raise_for_status()
    profile_image = Image.open(BytesIO(response.content))
except requests.exceptions.HTTPError as err:
    st.error(f"HTTP Error: {err}")
    profile_image = None
except Exception as e:
    st.error(f"Error: {e}")
    profile_image = None

# Display the profile image if it was loaded successfully
if profile_image is not None:
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            width: 150px;
            height: 150px;
            border: 2px solid #4a47a3;
            border-radius: 50%;
            overflow: hidden;
            box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
            "
        >
            <img src="data:image/jpeg;base64,{image_to_base64(profile_image)}" style="width: 100%; height: 100%; object-fit: cover; object-position: center;" />
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.error("Failed to load profile image.")

    # Add a decorative border and shadow to the profile image
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            width: 150px;
            height: 150px;
            border: 2px solid #4a47a3;
            border-radius: 50%;
            overflow: hidden;
            box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
            "
        >
            <img src="data:image/jpeg;base64,{image_to_base64(profile_image)}" style="width: 100%; height: 100%; object-fit: cover; object-position: center;" />
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("Kuala Lumpur, Malaysia | yuenhoe95@gmail.com | Phone: +6016-6975731 | [LinkedIn](https://www.linkedin.com/in/shawn-kam-27b454129/)")

    st.markdown("---")

    st.header("About Me")
    st.write("As a recent master's graduate in data science and business analytics, I am a positive and collaborative team player with a passion for analytics. Actively seeking internship opportunities in New Zealand with possession of 6-month valid working holiday visa for year 2023. My technical expertise, enthusiasm, and collaborative mindset enable me to contribute effectively to any data-driven team. I'm excited to make meaningful contributions to an organization in New Zealand.")
    st.markdown("---")

    st.header("Education")
    st.subheader("MSc in Data Science and Business Analytics, Asia Pacific University")
    st.write("Kuala Lumpur, Malaysia")
    st.write("Dec 2021 - Jan 2023")
    st.write("Postgraduate Study")
    st.write("CGPA Grade : 3.77/4.00")
    st.write("Research Project - Sales Demand Forecast on E-Commerce Business using Predictive Analytics")

    st.subheader("MSc in Data Science and Business Analytics, De Montfort University")
    st.write("Leicester, UK")
    st.write("Dec 2021 - Jan 2023")
    st.write("Postgraduate Study")
    st.write("CGPA Grade : 3.77/4.00")
    st.write("Dual Degree Award Programme")
    st.write("Approved collaboration in accordance with the QAA UK Quality Code for Higher Education for the Assurance of Academic Quality and Standards in Higher Education as published by the United Kingdom Quality Assurance Agency (QAA).")

    st.subheader("Bachelor of International Business (Honours), Universiti Tunku Abdul Rahman (UTAR)")
    st.write("Kuala Lumpur, Malaysia")
    st.write("May 2014 - May 2017")
    st.write("Certification : Bachelor Degree (Honours)")
    st.write("Research Project - Perception of Private University Students Toward Application of Virtual Reality into Malaysia Tertiary Education System")
    st.markdown("---")

    st.header("Skills")
    st.write("SQL, Python, Microsoft Excel, Microsoft Powerpoint, Tableau, Microsoft Power BI, PHP, Microsoft Visio, Search Engine Optimization (SE0), Data Analytics, Data Preparation, Data Visualization, Machine Learning, Negotiation, Business Planning")
    st.markdown("---")

    st.header("Work Experience")
    st.subheader("Professional Service Engineer, Juris Technologies Sdn Bhd")
    st.write("Kuala Lumpur, Malaysia")
    st.write("Mar 2023 - Present")
    st.write("- Designed efficient system architecture and applet for loan origination and onboarding processes using SQL and PHP.")
    st.write("- Gathered and analyzed user requirements, translating them into functional specifications for development teams.")
    st.write("- Created flowcharts, diagrams, and graphic visualizations to aid in system design and user experience.")
    st.write("- Collaborated with cross-functional teams (e.g Software Engineer) to align projects with business objectives and ensure timely delivery.")
    st.write("- Continuously reviewed and refined processes, identifying and implementing improvement opportunities.")

    st.subheader("E-Commerce Executive, Midea Group (Malaysia Subsidiary)")
    st.write("Kuala Lumpur, Malaysia")
    st.write("Apr 2020 - Dec 2021")
    st.write("- Managed sales on Lazada and Shopee, liaising with key account managers for promotional campaigns.")
    st.write("- Engaged in digital marketing activities, including SEO, PPC, and Social Media campaigns to optimize performance.")
    st.write("- Conducted weekly and monthly analytics and visualized results to gain additional budget approval from key management.")
    st.write("- Collaborated with factories for cost management and sourced new electrical appliances with innovative features/designs.")
    st.write("- Inventory management and product lead time forecast to ensure efficient delivery and stock control.")

    st.subheader("Merchandiser, Wow Shop Sdn Bhd")
    st.write("Kuala Lumpur, Malaysia")
    st.write("Dec 2018 - Apr 2020")
    st.write("- Sourced new OEM electrical appliances for audiences, expanding product offerings for the TV shopping platform.")
    st.write("- Negotiated pricing and cost margins with suppliers to optimize profitability and competitiveness.")
    st.write("- Managed SKU inventory, ensuring optimal stock levels and efficient product turnover.")
    st.write("- Conducted in-depth sales reviews, analyzing customer demographics, conversion rates, and overall performance.")
    st.write("- Coordinated slot arrangements and provided visual suggestions to maximize product exposure and sales potential.")
    st.markdown("---")
    
    # Set the URL of the image
    image_url2 = "https://raw.githubusercontent.com/shawnkam95/st-Resume/main/SAS%20BADGE.jpg"

    st.header("Professional Certificate")
    st.subheader("SAS Analytics, SAS")
    st.markdown("---")

    st.header("References")
    st.write("Available upon request.")


def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()



if __name__ == "__main__":
    main()
