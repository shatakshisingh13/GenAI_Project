import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Setup page
st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

fs = FewShotPosts()
tags = fs.get_tags()

# Inject custom styles (no JS)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #f4f6f8;
        }
        .main-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            color: #0077B5;
            margin-top: 1rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.05rem;
            color: #4b5563;
            margin-bottom: 2rem;
        }
        .post-box {
            background: white;
            border: 1px solid #d1d5db;
            border-radius: 10px;
            padding: 1.2rem;
            font-size: 1.3rem;
            white-space: pre-wrap;
            font-family: 'Calibri', monospace;
            color: #1f2937;
            min-height: 200px;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='main-title'>LinkedIn Post Generator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Write smarter. Post faster. Shine brighter ✨</div>", unsafe_allow_html=True)

# Selection Inputs
col1, col2, col3 = st.columns(3)
with col1:
    selected_tag = st.selectbox("📌 Topic", tags)
with col2:
    selected_length = st.selectbox("✏️ Length", ["Short", "Medium", "Long"])
with col3:
    selected_language = st.selectbox("🌐 Language", ["English", "Hinglish"])

# Generate Post
if st.button("Generate Post"):
    with st.spinner("Generating post..."):
        post = generate_post(selected_length, selected_language, selected_tag)

    st.markdown("Your Generated Post")
    st.markdown(f"""
        <div class="post-box">{post}</div>
    """, unsafe_allow_html=True)

    st.download_button("⬇ Download as Text", post, file_name="linkedin_post.txt", mime="text/plain")

# Footer
st.markdown("<hr><center style='color:gray; font-size: 0.9rem;'>Crafted with 💙 by Shatakshi</center>", unsafe_allow_html=True)
