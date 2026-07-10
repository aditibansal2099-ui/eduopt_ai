import streamlit as st
import pandas as pd
import json
import os


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="EduOpt AI",
    page_icon="🤖",
    layout="wide"
)



# ---------------- DATABASE ----------------

DATABASE_FILE = "eduopt_database.json"



def load_database():

    if not os.path.exists(DATABASE_FILE):

        return {
            "schools": {}
        }

    with open(DATABASE_FILE,"r") as file:

        return json.load(file)



def save_database(data):

    with open(DATABASE_FILE,"w") as file:

        json.dump(
            data,
            file,
            indent=4
        )



database = load_database()



# ---------------- SESSION ----------------


if "logged_in" not in st.session_state:

    st.session_state.logged_in=False



if "school_id" not in st.session_state:

    st.session_state.school_id=""



if "page" not in st.session_state:

    st.session_state.page="Home"




# ---------------- DESIGN ----------------


st.markdown("""

<style>


body{

background:#f8fafc;

}


.hero{

font-size:60px;
font-weight:900;
background:linear-gradient(
90deg,
#2563eb,
#7c3aed
);

-webkit-background-clip:text;
color:transparent;

animation:slide 1.2s;

}



.subtitle{

font-size:28px;
color:#475569;

}



.quote{

font-size:22px;
font-style:italic;
color:#14b8a6;

}



.card{
background:white;
padding:25px;
border-radius:20px;

box-shadow:
0 10px 25px rgba(0,0,0,0.12);

transition:0.3s;

animation:fade 1s;

}



.card:hover{

transform:translateY(-8px);

}



@keyframes fade{

from{

opacity:0;
transform:translateY(20px);

}

to{

opacity:1;
transform:translateY(0);

}

}



@keyframes slide{

from{

opacity:0;

}

to{

opacity:1;

}

}



.stButton button{


background:
linear-gradient(
90deg,
#2563eb,
#7c3aed
);

color:white;

border-radius:12px;

font-weight:bold;

}


</style>

""",
unsafe_allow_html=True)





# ---------------- PUBLIC PAGES ----------------



def home():


    st.markdown(
        "<div class='hero'>🤖 EduOpt AI</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        "<div class='subtitle'>"
        "AI Powered Student Support & School Optimization Platform"
        "</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        "<div class='quote'>"
        "\"Every student deserves the right guidance at the right time.\""
        "</div>",
        unsafe_allow_html=True
    )


    st.write(
    """
EduOpt AI helps schools use Artificial Intelligence
to understand students better.

It identifies student requirements,
optimizes school resources and supports teachers
in making data-driven decisions.
"""
    )


    if st.button("🚀 Get Started"):

     st.session_state.page="🏫 School Management"

     st.rerun()


    st.divider()


    st.subheader(
        "✨ Why Choose EduOpt AI?"
    )


    c1,c2,c3=st.columns(3)


    with c1:

        st.markdown(
        """
        <div class="card">

        🤖

        <h3>AI Prediction</h3>

        Identify student needs automatically.

        </div>
        """,
        unsafe_allow_html=True
        )



    with c2:

        st.markdown(
        """
        <div class="card">

        ⚙️

        <h3>Smart Optimization</h3>

        Manage school resources efficiently.

        </div>
        """,
        unsafe_allow_html=True
        )



    with c3:

        st.markdown(
        """
        <div class="card">

        📚

        <h3>Student Growth</h3>

        Personalised development plans.

        </div>
        """,
        unsafe_allow_html=True
        )






def about():


    st.title(
        "📖 About EduOpt AI"
    )


    st.subheader(
        "Our Problem"
    )


    st.write(
    """
Schools face challenges like:

• Identifying students needing support

• Managing counselling and remedial requirements

• Limited resources

• Difficulty tracking progress
"""
    )


    st.subheader(
        "Our Solution"
    )


    st.write(
    """
EduOpt AI provides:

✓ AI based student analysis

✓ Personalised recommendations

✓ Resource optimisation

✓ Progress monitoring

✓ Better school management
"""
    )





def features():


    st.title(
        "✨ EduOpt AI Features"
    )


    features=[

    "🤖 AI Student Prediction",

    "📚 Remedial Support",

    "💙 Counselling Management",

    "🕒 Attendance Monitoring",

    "🏆 Sports Engagement",

    "🎨 Creative Activities",

    "⚙️ Resource Optimization",

    "📊 Dashboard",

    "📄 AI Reports",

    "📅 Weekly Progress"

    ]


    for item in features:

        st.success(item)





def contact():


    st.title(
        "📞 Contact Us"
    )


    st.write(
    """
EduOpt AI Team

Email:
support@eduoptai.com


AI Powered Education Management Platform
"""
    )





def help_page():


    st.title(
        "❓ Help"
    )


    st.write(
    """
How to use EduOpt AI:

1. Register your school

2. Login

3. Upload student data

4. Generate AI prediction

5. Optimize resources

6. Download reports

7. Track progress
"""
    )





# ---------------- SCHOOL LOGIN ----------------



def school_login():


    st.title(
        "🏫 School Portal"
    )


    choice=st.radio(
        "Select",
        [
            "Register School",
            "Login School"
        ]
    )



    if choice=="Register School":


        school_name=st.text_input(
            "School Name"
        )


        username=st.text_input(
            "Create School ID"
        )


        password=st.text_input(
            "Create Password",
            type="password"
        )



        if st.button(
            "Create Account"
        ):


            database["schools"][username]={

                "school_name":school_name,

                "password":password,

                "students":[],

                "reports":[]

            }


            save_database(database)


            st.success(
                "School Registered Successfully"
            )


            st.info(
                "Login now to continue"
            )




    else:


        username=st.text_input(
            "School ID"
        )


        password=st.text_input(
            "Password",
            type="password"
        )


        if st.button(
            "Login"
        ):


            if username in database["schools"] and database["schools"][username]["password"]==password:


                st.session_state.logged_in=True

                st.session_state.school_id=username

                st.session_state.page="🏫 School Management"

                st.rerun()


            else:

                st.error(
                    "Incorrect Login"
                )
# ---------------- SCHOOL MANAGEMENT ----------------


def school_management():


    st.title(
        "🏫 School Management"
    )


    school=database["schools"][st.session_state.school_id]


    st.info(
        f"""
School: {school['school_name']}

Saved Students:
{len(school['students'])}
"""
    )


    option=st.radio(

        "Choose Action",

        [
            "Use Existing Student Data",
            "Upload New CSV",
            "Enter Student Manually"
        ]

    )



    # ---------------- EXISTING DATA ----------------


    if option=="Use Existing Student Data":


        if len(school["students"])>0:


            data=pd.DataFrame(
                school["students"]
            )


            st.subheader(
                "📋 Existing Student Database"
            )


            st.dataframe(data)



            if st.button(
                "Continue to AI Prediction"
            ):


                st.session_state.current_data=data

                st.session_state.page="🤖 AI Prediction"

                st.rerun()



        else:


            st.warning(
                "No previous data available."
            )





    # ---------------- CSV ----------------


    elif option=="Upload New CSV":


        file=st.file_uploader(

            "Upload Student CSV",

            type="csv"

        )



        if file:


            data=pd.read_csv(file)



            st.subheader(
                "Preview"
            )


            st.dataframe(data)



            if st.button(
                "Save Data & Continue"
            ):


                school["students"]=data.to_dict(
                    orient="records"
                )


                save_database(database)



                st.session_state.current_data=data


                st.success(
                    "Student Data Saved"
                )



                st.session_state.page="🤖 AI Prediction"


                st.rerun()





    # ---------------- MANUAL ENTRY ----------------


    else:


        st.subheader(
            "👨‍🎓 Add Student"
        )


        name=st.text_input(
            "Student Name"
        )


        student_class=st.text_input(
            "Class"
        )


        attendance=st.number_input(
            "Attendance %",
            0,
            100
        )


        marks=st.number_input(
            "Average Marks",
            0,
            100
        )


        behaviour=st.number_input(
            "Behaviour Score",
            1,
            10
        )


        feedback=st.text_area(
            "Teacher Feedback"
        )


        counselling=st.selectbox(
            "Previous Counselling",
            [
                "Yes",
                "No"
            ]
        )


        mental=st.selectbox(
            "Mental Health Concern",
            [
                "Yes",
                "No"
            ]
        )


        difficulty=st.selectbox(
            "Learning Difficulty",
            [
                "Yes",
                "No"
            ]
        )



        if st.button(
            "Save Student"
        ):


            student={

            "Student_Name":name,

            "Class":student_class,

            "Attendance":attendance,

            "Average_Marks":marks,

            "Behaviour_Score":behaviour,

            "Teacher_Feedback":feedback,

            "Previous_Counselling":counselling,

            "Mental_Health_Concern":mental,

            "Learning_Difficulty":difficulty

            }



            school["students"].append(
                student
            )


            save_database(database)


            st.session_state.current_data=pd.DataFrame(
                school["students"]
            )


            st.success(
                "Student Added Successfully"
            )





# ---------------- AI PREDICTION ----------------



def ai_prediction():
    st.title("🤖 AI Student Prediction")


    if "current_data" not in st.session_state:

        st.warning("Please upload student data first.")
        return


    data = st.session_state.current_data.copy()


    predictions = []


    for index,row in data.iterrows():

        needs=[]


        marks = float(row["Average_Marks"])
        attendance = float(row["Attendance"])

        mental = str(row["Mental_Health_Concern"]).lower()
        difficulty = str(row["Learning_Difficulty"]).lower()
        behaviour = float(row["Behaviour_Score"])



        # REMEDIAL LOGIC

        if marks < 50 or difficulty=="yes":

            needs.append(
                "📚 Remedial Classes"
            )



        # COUNSELLING LOGIC

        if mental=="yes" or behaviour < 5:

            needs.append(
                "💙 Counselling"
            )



        # ATTENDANCE LOGIC

        if attendance < 75:

            needs.append(
                "🕒 Talk to Parents + Attendance Monitoring"
            )



        # SPORTS / ACTIVITY ONLY IF STUDENT IS STABLE

        if len(needs)==0:

            needs.append(
                "🏆 Sports / Art / Music Activities"
            )



        predictions.append(
            ", ".join(needs)
        )



    data["AI_Recommendation"]=predictions


    st.session_state.predicted_data=data


    st.subheader(
        "AI Student Support Recommendation"
    )


    st.dataframe(data)



    if st.button("Continue to Optimization"):

        st.session_state.page="⚙️ Optimization"

        st.rerun()
# ---------------- OPTIMIZATION ----------------def ai


def optimization():


    st.title(
        "⚙️ AI Resource Optimization"
    )


    if "predicted_data" not in st.session_state:


        st.warning(
            "Generate AI prediction first."
        )

        return



    data=st.session_state.predicted_data



    st.write(
        "Enter available school resources:"
    )


    counselling_slots=st.number_input(
        "💙 Counselling Slots",
        0
    )


    remedial_slots=st.number_input(
        "📚 Remedial Slots",
        0
    )


    sports_slots=st.number_input(
        "🏆 Sports Slots",
        0
    )


    art_slots=st.number_input(
        "🎨 Art Slots",
        0
    )


    music_slots=st.number_input(
        "🎵 Music Slots",
        0
    )



    if st.button(
        "Generate AI Allocation"
    ):


        counselling=[]

        remedial=[]

        activities=[]



        for index,row in data.iterrows():


            name=row["Student_Name"]

            recommendation=row["AI_Recommendation"]



            if "Counselling" in recommendation:

                counselling.append(name)



            if "Remedial Classes" in recommendation:

                remedial.append(name)



            if (
                "Sports" in recommendation
                or
                "Art" in recommendation
                or
                "Music" in recommendation
            ):

                activities.append(name)




        st.subheader(
            "🤖 AI Priority Result"
        )


        st.write(
            "### 💙 Counselling Priority"
        )

        st.write(
            counselling[:counselling_slots]
        )



        st.write(
            "### 📚 Remedial Priority"
        )

        st.write(
            remedial[:remedial_slots]
        )



        st.write(
            "### 🏆 Activity Engagement"
        )

        st.write(
            activities
        )


        st.success(
            "Optimization Completed"
        )



        st.session_state.optimized=True





# ---------------- DASHBOARD ----------------


def dashboard():


    st.title(
        "📊 EduOpt AI Dashboard"
    )


    if "predicted_data" not in st.session_state:


        st.warning(
            "No AI report available."
        )

        return



    data=st.session_state.predicted_data



    total=len(data)



    counselling=data["AI_Recommendation"].str.contains(
        "Counselling"
    ).sum()



    remedial=data["AI_Recommendation"].str.contains(
        "Remedial"
    ).sum()



    attendance=data["AI_Recommendation"].str.contains(
        "Attendance"
    ).sum()



    activities=data["AI_Recommendation"].str.contains(
        "Sports|Art|Music"
    ).sum()



    c1,c2,c3,c4=st.columns(4)



    c1.metric(
        "👨‍🎓 Total Students",
        total
    )


    c2.metric(
        "💙 Counselling",
        counselling
    )


    c3.metric(
        "📚 Remedial",
        remedial
    )


    c4.metric(
        "🏆 Activities",
        activities
    )



# ---------------- REPORTS ----------------



def reports():


    st.title(
        "📄 AI Reports"
    )


    if "predicted_data" not in st.session_state:


        st.warning(
            "No report generated."
        )

        return



    data=st.session_state.predicted_data



    st.dataframe(data)



    csv=data.to_csv(
        index=False
    ).encode()



    st.download_button(

        "⬇ Download AI Report",

        csv,

        "EduOpt_AI_Report.csv",

        "text/csv"

    )





# ---------------- WEEKLY PROGRESS ----------------



def weekly_progress():


    st.title(
        "📅 Weekly Progress Tracking"
    )


    if "current_data" not in st.session_state:


        st.warning(
            "No students available."
        )

        return



    data=st.session_state.current_data



    student=st.selectbox(

        "Select Student",

        data["Student_Name"].tolist()

    )



    progress=st.radio(

        "Is there improvement?",

        [
            "Yes",
            "No"
        ]

    )



    if progress=="Yes":


        improvement=st.text_area(
            "What improved?"
        )


        remark=st.text_area(
            "Teacher Remark"
        )


        if st.button(
            "Save Progress"
        ):

            st.success(
                "Progress Updated"
            )


            st.write(
                improvement
            )


            st.write(
                remark
            )



    else:


        st.warning(
        """
AI Suggestions:

• Provide counselling support

• Arrange remedial classes

• Increase teacher monitoring

• Encourage suitable activities
"""
        )





# ---------------- FINAL WEBSITE NAVIGATION ----------------



menu=[

"🏠 Home",

"📖 About Us",

"✨ Features",

"🏫 School Management",

"📞 Contact",

"❓ Help"

]



if st.session_state.logged_in:


    menu.insert(
        4,
        "🤖 AI Prediction"
    )

    menu.insert(
        5,
        "⚙️ Optimization"
    )

    menu.insert(
        6,
        "📊 Dashboard"
    )

    menu.insert(
        7,
        "📄 Reports"
    )

    menu.insert(
        8,
        "📅 Weekly Progress"
    )



current_page = st.session_state.get("page", "🏠 Home")

if current_page not in menu:
    current_page = "🏠 Home"


page = st.sidebar.selectbox(
    "Navigation",
    menu,
    index=menu.index(current_page)
)



if page=="🏠 Home":

    home()


elif page=="📖 About Us":

    about()


elif page=="✨ Features":

    features()


elif page=="🏫 School Management":

    if st.session_state.logged_in:

        school_management()

    else:

        school_login()



elif page=="🤖 AI Prediction":

    ai_prediction()


elif page=="⚙️ Optimization":

    optimization()


elif page=="📊 Dashboard":

    dashboard()


elif page=="📄 Reports":

    reports()


elif page=="📅 Weekly Progress":

    weekly_progress()


elif page=="📞 Contact":

    contact()


elif page=="❓ Help":

    help_page()