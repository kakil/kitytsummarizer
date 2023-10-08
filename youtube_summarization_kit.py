import streamlit as st 
import helpers
import llm
from prompts import youtube_prompts

selected_model = "gpt-3.5-turbo"

youtube_url = "https://www.youtube.com/watch?v=s5h6miODIoE"

# video_transcript = helpers.get_video_transcript(youtube_url)

# prompt = youtube_prompts.youtube_to_points_summary.format(transcript=video_transcript)

# response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

# print(response)

def main():
    # Streamlit app title and description
    st.title("YouTube Video Summarizer")
    st.write("Enter a YouTube video url to summarize")

    # User input for keyword
    url = st.text_input("Enter URL:")

    if url:
        st.write(f"Retrieving YouTube URL: '{url}'...")

        # Get video transcript
        video_transcript = helpers.get_video_transcript(url)
        
        prompt = youtube_prompts.youtube_to_points_summary.format(transcript=video_transcript)
        
        response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

        # Summarize each video
        if response:
            st.write(response)
        else:
            st.warning("Summary not available for this video.")

if __name__ == "__main__":
    main()