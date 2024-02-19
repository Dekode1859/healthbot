import streamlit as st
import openai

# Function to interact with GPT-3 model
def ask_gpt3_personalized_extra(prompt, height_cm, weight_kg, age, fitness_goal, Activity_Level, dietary_restrictions):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot that will answer queries related to fitness and nutrition. The chatbot should understand questions about workout routines, dietary advice, and general fitness tips. Chatbot will offer personalized workout and diet plans based on user inputs such as body type, fitness goals, and dietary restrictions.{messages}"},
            {"role": "user", "content": "my height is " + str(height_cm) + " cm, my weight is " + str(weight_kg) + " kg, and I am " + str(age) + " years old. I want to " + fitness_goal.lower() + " and I am " + Activity_Level.lower() + " and I have " + ", ".join(dietary_restrictions) + " dietary restrictions."+prompt},
        ]
    )
    return response['choices'][0]['message']['content']

def ask_gpt3_personalized(prompt, height_cm, weight_kg, age):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot that will answer queries related to fitness and nutrition. The chatbot should understand questions about workout routines, dietary advice, and general fitness tips. Chatbot will offer personalized workout and diet plans based on user inputs such as body type, fitness goals, and dietary restrictions.{messages}"},
            {"role": "user", "content": "my height is " + str(height_cm) + " cm, my weight is " + str(weight_kg) + " kg, and I am " + str(age) + " years old."+prompt},
        ]
    )
    return response['choices'][0]['message']['content']

def ask_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot that will answer queries related to fitness and nutrition. The chatbot should understand questions about workout routines, dietary advice, and general fitness tips. Chatbot will offer personalized workout and diet plans based on user inputs such as body type, fitness goals, and dietary restrictions.{messages}"},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

# Main function to run the Streamlit app
def main():
    st.title("Fitness Chatbot")
    st.sidebar.title("Personal Information")
    openai.api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    height_cm = st.sidebar.number_input("Height (cm)", 0, 250)
    weight_kg = st.sidebar.number_input("Weight (kg)", 0, 500)
    age = st.sidebar.number_input("Age", 0, 100)
    fitness_goal = st.sidebar.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight", "Improve Endurance"])
    Activity_Level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"])
    dietary_restrictions = st.sidebar.multiselect("Dietary Restrictions", ["Vegetarian", "Vegan", "Gluten Free", "Lactose Free", "Keto", "Paleo", "None"])
    
    # Initialize conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # User input
    user_input = st.chat_input("Ask something")

    # If user input is not empty
    if user_input:
        # Add user input to conversation history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get chatbot response
        if height_cm and weight_kg and age:
            chatbot_response = ask_gpt3_personalized(user_input, height_cm, weight_kg, age)
        elif height_cm and weight_kg and age and fitness_goal and Activity_Level and dietary_restrictions:
            chatbot_response = ask_gpt3_personalized_extra(user_input, height_cm, weight_kg, age, fitness_goal, Activity_Level, dietary_restrictions)
        else:
            chatbot_response = ask_gpt3(user_input)

        # Add chatbot response to conversation history
        st.session_state.messages.append({"role": "assistant", "content": chatbot_response})

        # Display conversation history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

if __name__ == "__main__":
    main()