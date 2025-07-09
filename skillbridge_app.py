import streamlit as st
from snowflake.snowpark.context import get_active_session

# Title of the app
st.title("SkillBridge: Empowering Fresh Graduates 🚀")
st.write("Welcome to **SkillBridge**! This app connects you to learning resources, mentorship, and career opportunities. 🚀")

# Sign-up Form for Name and Email
st.subheader("Sign up to Get Started! 📝")
name = st.text_input("Enter your full name:")
email = st.text_input("Enter your email:")

if st.button("Sign Up"):
    if name and email:
        st.write(f"Thanks for signing up, {name}! 🎉 We’ll help you connect with the right resources.")
    else:
        st.warning("Please enter both your name and email to sign up.")

# Step 2: Select Career Interest (for mentor and resource suggestions)
career_interest = st.selectbox(
    "Select your career interest to get personalized recommendations 💼",
    ["Data Science", "Software Development", "Digital Marketing", "Corporate Finance", "Investment Banking", 
     "Risk Management", "SEO/SEM", "Content Strategy", "Full-Stack Development", "Front-End Development", 
     "Backend Development", "Machine Learning", "Artificial Intelligence", "Financial Modeling", 
     "Social Media", "Mobile Development", "Data Visualization"]
)

# Query Snowflake for mentors based on user choice
query = f"""
    SELECT name, email, expertise, years_of_experience, available_for_mentoring
    FROM skillbridge_schema.mentors
    WHERE UPPER(expertise) = UPPER('{career_interest}')
"""

# Fetch mentor data from Snowflake
session = get_active_session()
mentors_data = session.sql(query).to_pandas()

# Display mentor data
st.subheader(f"👩‍🏫 Mentor Suggestions for {career_interest}")
if mentors_data.empty:
    st.write(f"No mentors found for **{career_interest}**. Please try another career interest. 🤔")
else:
    st.dataframe(mentors_data)

# Step 3: Display a Catalog of Resources (Courses, Blogs, and Videos) based on Career Interest
st.subheader(f"📚 Recommended Resources for {career_interest}")

if career_interest == "Data Science":
    st.write("""
        - **Courses**: 
            1. [Introduction to Data Science with Python](https://www.coursera.org/learn/python-for-data-science)
            2. [Machine Learning Algorithms](https://www.coursera.org/learn/machine-learning)
            3. [Data Science and Machine Learning Bootcamp with R](https://www.udemy.com/course/data-science-and-machine-learning-bootcamp-with-r/)
        - **Blogs**:
            1. [Towards Data Science - Blog](https://towardsdatascience.com/)
            2. [Analytics Vidhya - Blog](https://www.analyticsvidhya.com/)
        - **Videos**:
            1. [Data Science Crash Course](https://www.youtube.com/watch?v=ua-CiDNNj30)
            2. [StatQuest: Data Science](https://www.youtube.com/watch?v=XXfJXp4xWGA)
    """)
elif career_interest == "Software Development":
    st.write("""
        - **Courses**: 
            1. [Full-Stack Web Development with React](https://www.udemy.com/course/full-stack-web-development-with-react/)
            2. [JavaScript: The Advanced Concepts](https://www.udemy.com/course/advanced-javascript-concepts/)
            3. [The Complete Node.js Developer Course](https://www.udemy.com/course/the-complete-nodejs-developer-course-2/)
        - **Blogs**:
            1. [freeCodeCamp - Blog](https://www.freecodecamp.org/news/)
            2. [CSS-Tricks - Blog](https://css-tricks.com/)
        - **Videos**:
            1. [JavaScript Full Course](https://www.youtube.com/watch?v=PkZNo7MFNFg)
            2. [React Crash Course](https://www.youtube.com/watch?v=sBws8MSXN7A)
    """)
elif career_interest == "Digital Marketing":
    st.write("""
        - **Courses**: 
            1. [Digital Marketing Specialization](https://www.coursera.org/specializations/digital-marketing)
            2. [Google Ads Certification](https://skillshop.withgoogle.com/)
            3. [SEO Training Course](https://www.udemy.com/course/seo-2020-learn-search-engine-optimization/)
        - **Blogs**:
            1. [Neil Patel - Blog](https://neilpatel.com/blog/)
            2. [Moz - Blog](https://moz.com/blog)
        - **Videos**:
            1. [Digital Marketing 101](https://www.youtube.com/watch?v=hzpXP_ZusJ8)
            2. [SEO Tutorial for Beginners](https://www.youtube.com/watch?v=kM4ESDh2-Ts)
    """)

# Step 4: Feedback Section with Emojis
st.subheader("💬 Your Feedback Matters!")
feedback = st.text_area("How do you feel about this app? Any suggestions for improvement? 😃")

if feedback:
    st.write(f"Thanks for your feedback: {feedback} 🙏")

# Step 5: Chatbox for Doubts/Questions (Simulated)
st.subheader("💬 Ask Questions or Chat with Peers")
question = st.text_area("Have any doubts? Ask here! 🤔")

if question:
    st.write(f"Your Question: {question} 🤖")
    st.write("We'll try to answer it shortly, or your peers can help you out! 💡")

# Optional: Add more sections based on user's preferences

