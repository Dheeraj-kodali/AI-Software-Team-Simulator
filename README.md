# 🤖 AI Software Team Simulator

A multi-agent software project simulator built with **LangGraph**, **LangChain**, and **Streamlit** to generate comprehensive Software Design Documents (SDD) using specialized AI agents.

This project implements an autonomous collaborative pipeline where virtual agents work together step-by-step to design complete software systems based on user ideas.

---

## 🚀 Key Features

* **Multi-Agent Collaboration**: Orchestrates 9 specialized agents:
  1. **Product Manager (PM)**: Gathers requirements & defines project scope.
  2. **System Architect**: Designs system architecture & data flow.
  3. **Database Engineer**: Models relational and NoSQL schemas.
  4. **Backend Developer**: Specifies RESTful endpoints and core logic.
  5. **QA Engineer**: Plans functional, negative, and load testing.
  6. **DevOps Engineer**: Outlines cloud infrastructure, CI/CD, and Kubernetes plans.
  7. **Risk Analyst**: Conducts security, scalability, and compliance risk assessments.
  8. **Cost Estimator**: Projects cloud cost, maintenance, and resource budgets.
  9. **Documentation Agent**: Compiles all outputs into a single cohesive report.
* **Streamlit UI**: A clean, interactive web dashboard to generate projects and view agent readouts side-by-side.
* **Stateful API Key Rotator**: Includes a token-based rotator (`RotatingChatGroq`) that cycles between 3 API keys. It tracks cumulative tokens utilized and rotates them dynamically using customizable strategies:
  * `each_call`: Rotates the API key after every successful call utilizing tokens.
  * `token_limit`: Rotates only after a key's total token consumption exceeds a defined threshold (e.g. 5,000 tokens).
* **Strict Security Separation**: Keeps API keys completely out of the git workspace by storing them locally in the home directory (`~/.groq_keys`).
* **PDF Report Generation**: Exports complete design reports as formatted PDFs.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Dheeraj-kodali/AI-Software-Team-Simulator.git
cd AI-Software-Team-Simulator
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure API Keys
To protect your keys from accidental leaks, this project loads secrets from your home directory. 

1. Create a configuration file in your user home directory named `.groq_keys`:
   * **Windows**: `C:\Users\<YourUsername>\.groq_keys`
   * **macOS/Linux**: `~/.groq_keys`

2. Populate the file with your keys and settings (refer to `.env.example` in the project root for format):
   ```ini
   GROQ_API_KEY_1=gsk_your_first_groq_api_key
   GROQ_API_KEY_2=gsk_your_second_groq_api_key
   GROQ_API_KEY_3=gsk_your_third_groq_api_key

   # Rotation Settings
   ROTATION_STRATEGY=each_call  # Option: 'each_call' or 'token_limit'
   TOKEN_LIMIT_PER_KEY=5000     # Threshold for token_limit strategy
   ```

---

## 🎮 How to Run

### Run the Web Interface (Streamlit)
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

### Run Integration Tests
```bash
# Test the key rotation system logic
python test_rotation.py

# Test agent pipelines
python test_agents.py

# Test the complete workflow
python test_workflow.py
```
