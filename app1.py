import streamlit as st
import pandas as pd
import time

# 1. Page Config for a premium widescreen layout
st.set_page_config(
    page_title="Skill trace- to find real gems",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Advanced CSS to match the Dark & Glowing Gradient Theme from your image
st.markdown("""
    <style>
    /* Global dark background adjustment */
    .stApp {
        background-color: #0d0e15;
    }
    
    /* Main Glowing Title styling */
    .header-container {
        text-align: center;
        padding: 30px 0px 10px 0px;
    }
    .main-title {
        font-size: 50px;
        font-weight: 800;
        background: linear-gradient(135deg, #FF416C, #8A2387, #8e2de2, #4a00e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 18px;
        color: #9ca3af;
        font-weight: 400;
        margin-top: 5px;
        margin-bottom: 35px;
    }

    /* Central Card for Ingestion & Settings */
    .upload-box {
        background: linear-gradient(145deg, #151622, #1b1d2e);
        border: 1px solid #2d314d;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 35px;
    }
    
    /* Elegant Metric Cards with Soft Neon Glows */
    .metric-card {
        background: #161726;
        border-radius: 14px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-2px);
    }
    .glow-blue { border-left: 5px solid #00c6ff; border-top: 1px solid #203a43; }
    .glow-purple { border-left: 5px solid #9d4edd; border-top: 1px solid #3c1642; }
    .glow-red { border-left: 5px solid #ff416c; border-top: 1px solid #4a0010; }
    
    .m-title { font-size: 13px; text-transform: uppercase; color: #9ca3af; letter-spacing: 1.5px; font-weight: 600; }
    .m-value { font-size: 36px; font-weight: 700; color: #ffffff; margin-top: 8px; }
    .m-label { font-size: 12px; color: #6b7280; margin-top: 4px; }
    </style>
""", unsafe_allow_html=True)

# Header Setup
st.markdown("""
    <div class="header-container">
        <div class="main-title">INDIA.RUNS | SKILL TRACE </div>
        <div class="sub-title">Automated Skill Validation Platform • Team Tara Tactics</div>
    </div>
""", unsafe_allow_html=True)

# 3. Dynamic Center Layout Container for File Upload & Inputs
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
st.subheader("📥 Central Pipeline Ingestion Hub")

col_left, col_right = st.columns([2, 1])

with col_left:
    uploaded_file = st.file_uploader(
        "Drag and drop resume dataset batches here", 
        type=["csv", "pdf", "docx"],
        help="Supports raw text files, single or batch candidate PDF resumes."
    )

with col_right:
    jd_profile = st.selectbox(
        "Target Engineering Profile Type",
        ["Backend Python / Flask Engine Suite", "Data Integration Systems Engineer", "Full-Stack API Architect"]
    )
    process_btn = st.button("🚀 Run Super Model Framework", use_container_width=True, type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# 4. Super Model Processing Pipeline Logic
if uploaded_file is not None:
    if process_btn:
        st.markdown("### ⚙️ Multi-Stage AI Operational Pipeline Status")
        
        # Interactive live tracking sequence matching slide rules
        with st.status("Spawning Dual-Agent Verification Engine...", expanded=True) as status:
            st.write("🔹 **Stage 1: Raw Ingestion Matrix** — Reading text lines and normalizing document structures...")
            time.sleep(1.2)
            
            st.write("🔹 **Stage 2: Context Normalizer (Agent 1)** — Converting informal descriptions and Hinglish text shortcuts...")
            time.sleep(1.4)
            
            st.write("🔹 **Stage 3: Evidence Auditor (Agent 2)** — Checking engineering benchmarks, system constraints, and execution data...")
            time.sleep(1.4)
            
            st.write("🔹 **Stage 4: Mathematical Circuit Breaker Validation** — Auto-penalizing hollow profile templates...")
            time.sleep(1.0)
            
            status.update(label="Super Model Score Compilation Complete!", state="complete", expanded=False)
        
        st.balloons()
        
        # 5. Colorful & Elegant Glowing Status Performance Cards
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("""
                <div class="metric-card glow-blue">
                    <div class="m-title">Profiles Evaluated</div>
                    <div class="m-value">24 Candidates</div>
                    <div class="m-label">Ingested from Batch Upload</div>
                </div>
            """, unsafe_allow_html=True)
            
        with c2:
            st.markdown("""
                <div class="metric-card glow-purple">
                    <div class="m-title">Hidden Gems Detected</div>
                    <div class="m-value">3 Engineers</div>
                    <div class="m-label">Elevated by Agent Normalization</div>
                </div>
            """, unsafe_allow_html=True)
            
        with c3:
            st.markdown("""
                <div class="metric-card glow-red">
                    <div class="m-title">Paper Kings Filtered</div>
                    <div class="m-value">7 Profiles</div>
                    <div class="m-label">Dropped by 70% Penalty Rule</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><hr style='border-color: #2d314d;'><br>", unsafe_allow_html=True)
        
        # 6. Interactive Leaderboard Section
        st.markdown("### 🏆 Objective Talent Leaderboard")
        
        candidates_data = [
            {
                "Rank": 1,
                "Candidate Core Profile": "Hidden Gem Alpha (Tier-3 Institute)",
                "Technical Synergy Match": "95%",
                "Architectural Proof Log": "Verified: Managed high-throughput data sync pipelines.",
                "Circuit Breaker Status": "Passed Safety Threshold ✅",
                "Employability Index Score": 92.5
            },
            {
                "Rank": 2,
                "Candidate Core Profile": "Hidden Gem Beta (Conversational Layout)",
                "Technical Synergy Match": "88%",
                "Architectural Proof Log": "Verified: Built custom database concurrency locks.",
                "Circuit Breaker Status": "Passed Safety Threshold ✅",
                "Employability Index Score": 87.0
            },
            {
                "Rank": 3,
                "Candidate Core Profile": "Paper King Prime (Polished Western Layout)",
                "Technical Synergy Match": "96%",
                "Architectural Proof Log": "Failed: High buzzword density with zero execution data.",
                "Circuit Breaker Status": "TRIGGERED PENALTY 🚨 (-70% Applied)",
                "Employability Index Score": 28.8
            }
        ]
        
        df = pd.DataFrame(candidates_data)
        
        # Styling function for conditional coloring in the main table
        def highlight_breaker_col(val):
            if "TRIGGERED" in str(val):
                return "background-color: #3d141d; color: #fca5a5; font-weight: bold; border-radius: 4px;"
            return "background-color: #143224; color: #86efac; font-weight: bold; border-radius: 4px;"
            
        styled_df = df.style.applymap(highlight_breaker_col, subset=["Circuit Breaker Status"])
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
        
        # 7. Multi-Agent JSON System Logs Viewer
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🔍 Underlying LLM Agent Reason Trace Logs")
        selected_cand = st.selectbox("Select a profile to view deep system audit traces:", df["Candidate Core Profile"].tolist())
        
        system_traces = {
            "Hidden Gem Alpha (Tier-3 Institute)": {
                "agent_1_normalization_notes": "Unpolished format but code logic was verified. Irrelevant details discarded cleanly.",
                "agent_2_evidence_audit": "Clear proof points provided for multi-tier pipeline setups.",
                "circuit_breaker_flag": "FALSE"
            },
            "Hidden Gem Beta (Conversational Layout)": {
                "agent_1_normalization_notes": "Heavy use of conversational language/Hinglish idioms normalized successfully into technical backend milestones.",
                "agent_2_evidence_audit": "Confirmed solid understanding of asynchronous structural locks.",
                "circuit_breaker_flag": "FALSE"
            },
            "Paper King Prime (Polished Western Layout)": {
                "agent_1_normalization_notes": "Perfect design styling structure matching global target job templates.",
                "agent_2_evidence_audit": "Critical failure: Requisite tools are mentioned sequentially but profile contains zero quantitative metrics or scaling achievements.",
                "circuit_breaker_flag": "TRUE (Final score reduced to prevent ATS gaming)"
            }
        }
        st.json(system_traces[selected_cand])

else:
    # Warm welcome message matching the aesthetic
    st.info("💡 Complete the central upload block above and click the launch button to run your screening pipeline.")