import streamlit as st

from graph.workflow import run_workflow

st.set_page_config(
    page_title="AI Software Team Simulator",
    layout="wide"
)

st.title("🤖 AI Software Team Simulator")

project = st.text_input(
    "Enter Project Idea"
)

if st.button("Generate"):

    with st.spinner("AI Team Working..."):

        results = run_workflow(project)

    st.header("📋 Product Manager")
    st.write(results["pm_output"])

    st.header("🏗 Architect")
    st.write(results["architect_output"])

    st.header("🗄 Database Engineer")
    st.write(results["database_output"])

    st.header("⚙ Backend Engineer")
    st.write(results["backend_output"])

    st.header("🧪 QA Engineer")
    st.write(results["qa_output"])

    st.header("🚀 DevOps Engineer")
    st.write(results["devops_output"])

    st.header("⚠ Risk Analysis")
    st.write(results["risk_output"])

    st.header("💰 Cost Analysis")
    st.write(results["cost_output"])

    st.header("📚 Documentation")
    st.write(results["docs_output"])