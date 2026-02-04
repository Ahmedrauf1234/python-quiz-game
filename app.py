import streamlit as st


quiz_questions = [
    {
        "question": "Python me variable ka sahi tareeqa kaunsa hai?",
        "options": {
            "A": "1num = 10",
            "B": "num-1 = 10",
            "C": "num1 = 10",
            "D": "num 1 = 10"
        },
        "answer": "C"
    },
    {
        "question": "Python me list ka correct syntax kya hai?",
        "options": {
            "A": "(1, 2, 3)",
            "B": "{1, 2, 3}",
            "C": "[1, 2, 3]",
            "D": "<1, 2, 3>"
        },
        "answer": "C"
    },
    {
        "question": "Python me function ka keyword kya hai?",
        "options": {
            "A": "func",
            "B": "def",
            "C": "function",
            "D": "define"
        },
        "answer": "B"
    },
    {
        "question": "len() function kya karta hai?",
        "options": {
            "A": "Data add karta hai",
            "B": "Data delete karta hai",
            "C": "Length count karta hai",
            "D": "Data sort karta hai"
        },
        "answer": "C"
    }
]
#========================side bar work===================>>

name = st.sidebar.text_input("Enter your Name")
if name :
    st.success(f"Welcome {name}")
#=========================Title=================>>
st.title("Quiz Game")
#=======================================

user_Answers = []
score = 0
def quizgame():
    
    
    for index,Quiz in enumerate(quiz_questions , start=1):
         cols = st.columns(1)[0]
         with cols:
             st.markdown(f" ###### Q{index+1}) {Quiz['question']}")
             options_list = ["Select an option"] + list(Quiz['options'].keys())
             choice = st.radio("Select Option:" ,options_list, 
                               format_func=lambda x: f"{x}) {Quiz['options'][x]}" if x in Quiz['options'] else x,
            key=index)
             user_Answers.append(choice)
#================================Submit Button==================>>
    score = 0
    button = st.button("Submit Quiz")
    if(button) :
      for index, q in enumerate(quiz_questions):
        if user_Answers[index] == q['answer']:
            score += 1
      st.success(f"Your score is {score} / {len(quiz_questions)}")
      if score == len(quiz_questions):
        st.balloons()
      elif score >= 2:
        st.info("👍 Good effort! Practice aur karo")
      else:
        st.warning("😅 Thori aur mehnat chahiye")

#=========================Completed ======================>>
             
quizgame()