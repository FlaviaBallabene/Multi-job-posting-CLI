import streamlit as st
import json
from adapters.linkedin import LinkedInAdapter
from adapters.workday import WorkdayAdapter
from adapters.bamboohr import BambooHRAdapter
from cli.utils.helpers import load_job_file

st.set_page_config(page_title="Multi Job Posting GUI", page_icon=":briefcase:")

st.title("Multi Job Posting GUI")
st.write("Upload a job description and post it to multiple boards.")

# Upload job JSON file
uploaded_file = st.file_uploader("Upload Job JSON", type=["json"])

# Board selection
boards_selected = st.multiselect(
    "Select Boards",
    options=["LinkedIn", "Workday", "BambooHR"],
    default=["LinkedIn", "Workday", "BambooHR"]
)

if uploaded_file and boards_selected:
    job_data = json.load(uploaded_file)
    st.subheader("Job Details")
    st.json(job_data)

    if st.button("Post Job"):
        st.info("Posting job to selected boards...")
        results = {}

        for board in boards_selected:
            board_lower = board.lower()
            try:
                if board_lower == "linkedin":
                    adapter = LinkedInAdapter()
                elif board_lower == "workday":
                    adapter = WorkdayAdapter()
                elif board_lower == "bamboohr":
                    adapter = BambooHRAdapter()
                else:
                    st.warning(f"Unknown board: {board}")
                    continue

                response = adapter.post_job(job_data)
                results[board] = response
                st.success(f"Posted to {board}: {response.get('job_url')}")

            except Exception as e:
                results[board] = {"error": str(e)}
                st.error(f"Failed to post to {board}: {e}")

        st.subheader("Summary")
        st.json(results)