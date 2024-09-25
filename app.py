from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "sb.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sorav Bhatia"
PAGE_ICON = "👨‍💻"
NAME = "Sorav Bhatia"
DESCRIPTION = """
Senior Technical Analyst | Business Intelligence & Analytics Leader
"""
EMAIL = "soravbhatia384@gmail.com"

PROJECTS = {
    "🏆 EREX Authorization Dashboard - Developed a sophisticated real-time authorization dashboard using Python, SQL, and ML, integrating data across multiple healthcare systems (EREX, TruCare, CLAIMS). Leveraged predictive analytics (RNN models) and neural networks to improve resource planning by 25%.": "https://youtu.be/Sb0A9i6d320",
    "🏆 Provider Call Center Dashboard - Created a dynamic dashboard for call center operations, leveraging Power BI and SQL to provide real-time performance insights. Used advanced data transformation techniques and machine learning algorithms to improve operational metrics by 20%.": "https://youtu.be/Sb0A9i6d320",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Over 12 years of experience architecting, developing, and optimizing complex, enterprise-level BI solutions. 
- ✔️ Deep expertise in predictive modeling, advanced ML techniques, and neural network architectures, including multi-layer neural networks with backpropagation, optimization methods, and advanced activation functions like RELU.
- ✔️ Proficient in real-time data integration and transformation, driving strategic decision-making and operational efficiency.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 👩‍💻 BI & Visualization Tools: Power BI, Tableau, QlikView, MicroStrategy, Cognos, Business Objects, Looker
- 📊 Data Engineering & Integration: SQL Server, Hadoop, Netezza, Talend, DataStage, Apache Spark, Kafka, ETL
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 📚 Advanced Analytics & Machine Learning: Neural Networks (RNN, CNN, LSTM), Stacking, Backpropagation, Sigmoid, RELU, Optimization (Gradient Descent, Adam), Cross-Entropy Loss, Clustering, Regression, Decision Trees, Random Forests, Reinforcement Learning, Deep Learning (TensorFlow, PyTorch)
- 🗄️ Automation Expertise: Workflow Automation, Process Automation, SQL Stored Procedures, Task Scheduling (Windows Task Scheduler, Cron), Python Scripting, Automated Reporting Systems
- 🗄️ Programming & Scripting: Python (Pandas, NumPy, Scikit-learn, TensorFlow), SQL (T-SQL, PL/SQL), R, Java, Scala, Bash/Shell Scripting
- 🗄️ Cloud Platforms & Big Data: AWS (Redshift, S3, Lambda, EMR), Azure, GCP, Snowflake, Google BigQuery, Databricks
- 🗄️ Data Management & Governance: Master Data Management (MDM), Data Warehousing, Data Lake Architecture, Data Mining, Data Governance, GDPR, HIPAA
- 🗄️ Neural Networks & Mathematical Concepts: Multi-layer Neural Networks, Perceptron, Chain Rule, Gradient Descent, Partial Derivatives, Convergence Theorem, ML Data Transformation (One to Multidimensional Space)
- 🗄️ Project Management & Leadership: Agile, Scrum, Lean, PMP, Kanban, Team Development, Mentoring, Cross-Functional Collaboration, Stakeholder Management
- 🗄️ Methodologies & Tools: Data-Driven Decision-Making, A/B Testing, Predictive Analytics, Automation, DevOps, CI/CD, Git, Jenkins, Docker, Kubernetes
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Technical Analyst | AAH — Alameda, CA**")
st.write("Nov2021 - Present")
st.write(
    """
- ►  Advanced Machine Learning & Predictive Modeling: Developed machine learning models using RNN and LSTM architectures to predict trends in authorization data, improving forecast accuracy by 35%. Implemented complex neural networks using backpropagation, cross-entropy loss, and optimization techniques to drive better business decision-making.
- ► Automation of Manual Processes: Spearheaded the automation of manual data workflows, reducing processing time by 50%. Developed automated reporting systems and workflow automation using Python, SQL, and task scheduling, leading to a significant reduction in manual effort by business teams.
- ► Strategic BI Leadership: Led the design and implementation of enterprise-level BI dashboards (EREX Authorization, Provider Analytics) using Python and SQL, enabling real-time, data-driven insights across departments, directly improving resource allocation and operational efficiency.
- ► Data Integration & Security: Built highly scalable data pipelines in SQL Server and integrated data from EREX, TruCare, HealthSuite, and CLAIMS systems, ensuring real-time data consistency and compliance with HIPAA regulations.
- ► Cross-Functional Collaboration: Collaborated with data analysts, business analysts, Quality Analysts, IT dev, and senior leadership to develop tailored BI solutions that improved operational performance by 30% and facilitated better cross-departmental communication.
- ► Data Governance: Implemented automated data validation processes, ensuring the accuracy and security of sensitive healthcare data while adhering to strict regulatory guidelines.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Lead Business Analyst | CenCal — Santa Barbara, CA**")
st.write("Nov 2016 - Nov 2021")
st.write(
    """
- ► Enterprise Data Solutions & Neural Network Implementation: Spearheaded the implementation of machine learning algorithms, including multi-layer perceptron neural networks, for provider data analysis. Optimized complex data workflows, automating manual processes and reducing data processing time by 40%.
- ► Data Quality Assurance & Testing: Led rigorous testing protocols, including UAT and regression testing, to ensure high data quality and accuracy across various environments, including claims and provider services.
- ► Cross-Functional Leadership: Managed collaboration between multiple departments, including IT, finance, and operations, to design custom data models and automated reporting solutions that improved decision-making and reduced reporting times by 60%.
- ► Member/Provider Data Import & Reporting
- ► PCP incentives Redesign
- ► PDR (provider data repository)
- ► Case tracking module in HIS (health Information system)
- ► Enhanced claims queue project
- ► Sb137 (provider directory) project (for on-line and printed directory)
- ► Provider portal phase 1 and Phase 2 Project.
- ► Caradigm screen enhancement project to include the data that were required as a part of 274 Provider network reporting to the State as well as SB137 Provider Directory
- ► Created the Selection Criteria using T-SQL to extract the data from legacy data base to build the logic for Online Provider Directory residing on SQL server database (CCHDB).
- ► Designed the prototype for front End interface with the inheritance of 274 data structure (Group, Site, Practitioners).
- ► House of Bricks Project that involved analyzing the current shell scripts data in UNIX.
- ► Performed data analysis using VBA in Excel for Production Reports Project.
- ► Created use cases and wrote user stories from Business owners in Claims, Health services, Quality, Provider services, Members services department on the modules like Member eligibility, Authorization, Claims ,PCP reassignment, reports and distribution, Breathe Smart as a part of Provider Portal Phase 1 and Phase 2 project, also worked in Designing of COC (coordination of Care) report.
- ► Configured the different user accounts in HIS with different role (like Demo user, biller, office staff, and provider) with login information during UAT testing for different test scenarios.
- ► Worked in the design and creation of application called EDICentral (in SQL) by Centecore that inputs the data from different entities, process it and create the Outbound data file for vendors, State and other entities as part of Data interface project. Wrote the Data extraction criteria (in SQL) from the processes described in the existing shell scripts(in UNIX)
- ► Managed the Inbounds, Outbound and pass-through interfaces for Laboratory data from the following entities-PDL, UDL, Quest, LabCorp, Sb County Lab, French, Arroyo Grande, Marian Hospitals, Immunization Data from CAIR(California Immunization Registry), Member Eligibility data for Care to Care and CCS, Census Data - Admissions & Discharges . ER data files from the following hospitals – Lompoc, Cottage, Dignity, French, Arroyo Grande, and Marian Medical Center. Claims Check data, Claims EFT data and No Check data for Check processing
- ► Created technical documentation for Member fulfillment process.
- ► Worked with developers and third party(IMS) in creation of Claim Status Inquiry/Response (276/277) files, and Eligibility Inquiry/Response (270/271) files
- ► Managed the Authorization data Load-(Care to Care and Holman Authorization Data) and Med-Impact PBM Claims data load (type 54).
- ► Worked with Developers for the creation of MedImpact PBM Eligibility- the type 23 file, MedImpact Type 110 Claims file, MedImpact Type 18 Provider Panel report, MedImpact Type 24 340B data, MedImpact Weekly Reports
- ► Designed the as-Is model and the to-be model for EOP (explanation of payment) process.
- ► Generated reports for SPR (specialized Program Reporting) project.
- ► Created technical specifications for Coordination of benefit and HISDB file.
- ► Identified the technical problems and recommended the modifications to the NMT/NEMT(Non-Medical transportation) claims file
- ► Determined requirements and designed the technical specification for State Capitation 820 data file
- ► Performed unit testing to test Inbound Claim Process and Inbound Claim Reject process in SQL server
- ► Designed the As-Is and To-Be model for all the Televox data interfaces
- ► Wrote the technical specification document for payment Advice 835 process.
- ► Created the requirements document and technical specification document with Data mapping of 837(Institutional &Professional) data elements from legacy system to new claims adjudication system by using the companion guide and the implementation guide for 837 encounter reporting to state
- ► Gathered the requirements, documented the technical specifications for the Diabetes SMART process.
- ► Analyzed the existing Claims logic for LTC claims and the existing BILL type/Claim type logic and created the to-be model for COBA claims processing which was implemented as SCF(system change form)
- ► ML based tool called Risk Assessment tool that provided risk scoring based on user entry.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Business/Requirement Analyst | Molina Healthcare — Long Beach, CA**")
st.write("Mar 2013 - Nov 2016")
st.write(
    """
- ► Automation of Reporting Systems: Transformed manual member and provider reporting workflows by implementing automated solutions using SQL and SSRS, reducing reporting times by 30% and ensuring real-time data accuracy.
- ► Data Integration & Compliance: Developed robust data import/export pipelines using SQL and SSRS, ensuring compliance with HIPAA regulations and improving data consistency across member and provider data.
- ► Process Optimization: Managed UAT sessions to streamline member and provider data workflows, reducing data discrepancies by 30% and enhancing overall system accuracy.

"""
)
# --- JOB 4
st.write('\n')
st.write("🚧", "**Research Analyst | Dr. Elizabeth Abercrombie's LAB — Rutgers university, Newark NJ**")
st.write("Aug 2010 - Mar 2013")
st.write(
    """
- ► Worked as RA on the research of Neuronal Activity Patterns & Circuit Dysfunction in Multiple Rodent Models of Huntington's Disease
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")