import streamlit as st
from openai import OpenAI

# Sidebar for API key input
with st.sidebar:
    key = st.text_input(label="Enter ChatGPT Key", type="password")
    if key:
        client = OpenAI(api_key=key)  # Directly set API key here
    else:
        client = None

st.title("💬 AI Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Show past messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if client:
        # Generate reply from OpenAI
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # or gpt-4
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

        # Save assistant reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.warning("Please enter your API key in the sidebar.")

if st.button("Next"):
    if Amount_of_Rooms_Number_Input is None or Amount_of_Rooms_Number_Input == 1:
        Type_of_Room = st.selectbox("**Type of Room**", ["Deluxe", "Standard"])
        st.subheader("• Amount of Pax", divider="blue")
        if Type_of_Room == "Deluxe":
            col1, col2, col3 = st.columns(3)
            with col1:
                Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,
                                                   key="x1")
            with col2:
                Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,
                                                         key="x2")
            with col3:
                Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=1,
                                                          key="x3")

        elif Type_of_Room == "Standard":
            col1, col2, col3 = st.columns(3)
            with col1:
                Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4,
                                                   key="x4")
            with col2:
                Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,
                                                         key="x5")
            with col3:
                Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2,
                                                          key="x6")
    elif Amount_of_Rooms_Number_Input == 2:
        Type_of_Room = st.selectbox("**Type of Room**", ["Double Deluxe", "Double Standard", "Deluxe+Standard"])
        with st.container(border=20):
            st.header("Room.1")
            if Type_of_Room == "Double Deluxe":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=4, max_value=6,
                                                       key="xg1")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,
                                                             key="xg2")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2,
                                                              key="xg3")
            elif Type_of_Room == "Double Standard":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=4, max_value=8,
                                                       key="xg4")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=4,
                                                             key="xg5")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=4,
                                                              key="xg6")
            elif Type_of_Room == "Deluxe+Standard":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=4, max_value=7,
                                                       key="xg7")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=3,
                                                             key="xg8")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=3,
                                                              key="xg9")
        with st.container(border=20):
            st.header("Room.2")
            if Type_of_Room == "Double Deluxe":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=4, max_value=6,
                                                       key="xc10")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,
                                                             key="xc11")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2,
                                                              key="xc12")
            elif Type_of_Room == "Double Standard":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=4, max_value=8,
                                                       key="xc13")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=4,
                                                             key="xc14")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=4,
                                                              key="xc15")
            elif Type_of_Room == "Deluxe+Standard":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=4, max_value=7,
                                                       key="xc16")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=3,
                                                             key="xc17")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=3,
                                                              key="xc18")
    BN = st.selectbox("**Extra Meal Options**", ["BBQ", "Normal"])
    # ---------------------------------------------------------------------------------------------------#
    if st.button("Submit-(Refresh)"):
        check = 0
        if Check_out_Date == Check_in_Date:
            check = 0
            st.info("Please Change the Check-out date")
        elif Check_in_Date > Check_out_Date:
            check = 0
            st.info("Please have the Check-out date be later after Check-in date")
        if Name_Text_Input == "":
            check = 0
            st.info("Please Enter Your Full Name")
        else:
            check = 1
            if check == 1:
                Full_Price_Meal_Plan = Meal_Plan_Select_Box
                Full_Price_Room_Number = (
                    1 if Amount_of_Rooms_Number_Input == 1 else 2 if Amount_of_Rooms_Number_Input == 2 else 3 if Amount_of_Rooms_Number_Input == 3 else 4)
                Full_Price_Type_Room = Type_of_Room
                if Amount_of_Rooms_Number_Input == 1:
                    Full_Price = ((
                                      22000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Full_Price_Type_Room == "Deluxe" else 28000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Full_Price_Type_Room == "Deluxe" else 18000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Full_Price_Type_Room == "Standard" else 23000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Full_Price_Type_Room == "Standard" else 27000) + (
                                      (Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (
                                                  Number_of_Children_6_11 * 1000)))
                if Amount_of_Rooms_Number_Input == 2:
                    Full_Price = (
                        44000 if Number_of_Adults == 4 and Full_Price_Room_Number == 2 and Full_Price_Type_Room == "Double Deluxe" else 2)
                with st.container(border=40):
                    st.header("**Booking Summary**", divider="grey")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Full Name: {Name_Text_Input}**")
                        st.write(f"**Check-in Date: {Check_in_Date}**")
                        st.write(f"**Check-out Date: {Check_out_Date}**")
                        st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                    with col2:
                        st.write(f"**Amount of Room: {Amount_of_Rooms_Number_Input}**")
                        st.write(f"**Type of Room: {Type_of_Room}**")
                        st.write(
                            f"**Amount of Pax: {Number_of_Adults + Number_of_Children_0_5 + Number_of_Children_6_11}**")
                        st.write(f"**Full Price: {Full_Price}**")

                        google_map_iframe = """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3162.8851888000005!2d80.3105!3d6.8741!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ae36574f4419451%3A0x1234567890abcdef!2sPowerhouse%20River%20Resort!5e0!3m2!1sen!2slk!4v1689176350000!5m2!1sen!2slk" width="400" height="400" style="border:0;" allowfullscreen="" loading="lazy" class="map-frame"  <!-- Add a class for CSS styling -->></iframe> """
                        custom_css = """<style>.map-frame {border-radius: 20px; /* Adjust this value for more or less rounding */overflow: hidden;  /* Ensures the content within the rounded border is also rounded */border: 5px solid #007BFF; /* Optional: Add a border color */}</style>"""
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        st.markdown(custom_css, unsafe_allow_html=True)
                        st.markdown(google_map_iframe, unsafe_allow_html=True)
