import streamlit as st

from graph.workflow import run_workflow
from utils.pdf_generator import create_pdf

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="AI Software Team Simulator",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

.main-title {
    background: linear-gradient(135deg,#0F172A,#1E293B);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(0,229,255,0.3);
    margin-bottom: 25px;
}

.main-title h1 {
    color: white;
    font-size: 55px;
}

.main-title p {
    color: #00E5FF;
    font-size: 22px;
}

.metric-card {
    background-color: #1A1D24;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #00E5FF;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------

st.markdown("""
<div class="main-title">
<h1>🤖 AI Software Team Simulator</h1>
<p>Build Complete Software Projects using AI Agents</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# STATS
# ----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🤖 Agents", "9")

with col2:
    st.metric("⚙ Workflow", "LangGraph")

with col3:
    st.metric("🧠 Model", "Ollama")

with col4:
    st.metric("📄 Export", "PDF")

st.divider()

# ----------------------------
# INPUT
# ----------------------------

project = st.text_input(
    "Enter Project Idea",
    placeholder="Example: Hospital Management System"
)

# ----------------------------
# GENERATE
# ----------------------------

if st.button("🚀 Generate"):

    if project.strip() == "":
        st.warning("Please enter a project idea.")
        st.stop()

    with st.spinner("🤖 AI Team Working..."):

        results = run_workflow(project)

    st.success("✅ Project Generated Successfully")

    # ----------------------------
    # TABS
    # ----------------------------

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "📋 PM",
        "🏗 Architect",
        "🗄 Database",
        "⚙ Backend",
        "🧪 QA",
        "🚀 DevOps",
        "⚠ Risk",
        "💰 Cost",
        "📚 Docs"
    ])

    with tab1:
        st.markdown(results["pm_output"])

    with tab2:
        st.markdown(results["architect_output"])

    with tab3:
        st.markdown(results["database_output"])

    with tab4:
        st.markdown(results["backend_output"])

    with tab5:
        st.markdown(results["qa_output"])

    with tab6:
        st.markdown(results["devops_output"])

    with tab7:
        st.markdown(results["risk_output"])

    with tab8:
        st.markdown(results["cost_output"])

    with tab9:
        st.markdown(results["docs_output"])

    # ----------------------------
    # PDF CONTENT
    # ----------------------------

    pdf_content = f"""

PRODUCT MANAGER

{results["pm_output"]}


ARCHITECT

{results["architect_output"]}


DATABASE

{results["database_output"]}


BACKEND

{results["backend_output"]}


QA

{results["qa_output"]}


DEVOPS

{results["devops_output"]}


RISK

{results["risk_output"]}


COST

{results["cost_output"]}


DOCUMENTATION

{results["docs_output"]}

"""

    create_pdf("project_report.pdf", pdf_content)

    st.divider()

    st.subheader("📥 Export Reports")

    with open("project_report.pdf", "rb") as pdf_file:

        st.download_button(
            label="📄 Download Full Report PDF",
            data=pdf_file,
            file_name="project_report.pdf",
            mime="application/pdf"
        )