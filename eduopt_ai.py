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

/* =========================
   BACKGROUND
========================= */

.stApp{

background:
linear-gradient(
90deg,
#4F46E5,
#7C3AED,
#06B6D4
);

}


/* =========================
   NAVBAR / TOP AREA
========================= */

header{

background:transparent;

}


/* =========================
   HERO TITLE
========================= */

.hero{

font-size:64px;

font-weight:900;

line-height:1.05;

background:
linear-gradient(
90deg,
#60A5FA,
#8B5CF6
);

-webkit-background-clip:text;

color:transparent;

animation:slide 1s;

}


/* =========================
   SUBTITLE
========================= */

.subtitle{

font-size:24px;

color:#D7E3F8;

margin-top:15px;

line-height:1.6;

}


/* =========================
   QUOTE
========================= */

.quote{

font-size:20px;

color:#8BC4FF;

font-style:italic;

margin-top:20px;

}


/* =========================
   GLASS CARDS
========================= */

.card{

background:rgba(255,255,255,0.08);

backdrop-filter:blur(18px);

padding:30px;

border-radius:22px;

border:1px solid rgba(255,255,255,0.15);

box-shadow:
0 15px 40px rgba(0,0,0,.30);

transition:.35s;

animation:fade .8s;

}


.card:hover{

transform:translateY(-10px);

box-shadow:
0 20px 45px rgba(59,130,246,.35);

}


/* =========================
   BUTTONS
========================= */

.stButton button{

background:
radial-gradient(circle at top right,#3B82F655 0%,transparent 30%),
radial-gradient(circle at bottom left,#8B5CF644 0%,transparent 35%),
linear-gradient(
135deg,
#050816 0%,
#0A1028 35%,
#111C44 100%
);
            
color:white;

border:none;

padding:14px 34px;

border-radius:14px;

font-size:17px;

font-weight:700;

transition:.35s;

}


.stButton button:hover{

transform:translateY(-3px);

box-shadow:
0 10px 25px rgba(59,130,246,.45);

}


/* =========================
   METRICS
========================= */

[data-testid="metric-container"]{

background:rgba(18,28,58,.65);

border-radius:18px;

padding:18px;

border:1px solid rgba(255,255,255,.12);
backdrop-filter:blur(20px);

}


/* =========================
   TABLES
========================= */

[data-testid="stDataFrame"]{

border-radius:18px;

overflow:hidden;

}


/* =========================
   HEADINGS
========================= */

h1,h2,h3{

color:white;

}


/* =========================
   NORMAL TEXT
========================= */

p, label, li{

color:#E6EEF9;

}


/* =========================
   ANIMATIONS
========================= */

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

transform:translateX(-40px);

}

to{

opacity:1;

transform:translateX(0);

}

}

</style>
""", unsafe_allow_html=True)





# ---------------- PUBLIC PAGES ----------------



def home():

    col1, col2 = st.columns([1.15, 1], vertical_alignment="center")

    with col1:

        st.markdown(
            """
            <div class="subtitle">
                AI Powered School Management Platform
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero">
                Transforming Schools<br>
                with Artificial Intelligence
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="
                color:#DCE7FF;
                font-size:20px;
                line-height:1.8;
                margin-top:18px;
                margin-bottom:28px;
            ">
            EduOpt AI helps schools identify students who require
            counselling, remedial classes, attendance intervention,
            and extracurricular engagement while intelligently
            optimizing limited school resources.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="quote">
            "Every student deserves the right guidance at the right time."
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚀 Get Started", key="hero_btn"):
            st.session_state.page = "🏫 School Management"
            st.rerun()

    with col2:

        st.image(
            "assets/home.png",
            use_container_width=True,
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2 style="
            text-align:center;
            color:white;
            margin-bottom:30px;
            font-weight:700;
        ">
        Why Choose EduOpt AI?
        </h2>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="card">
            <h3>🤖 AI Prediction</h3>
            <p>Identify students requiring counselling, remedial support and academic guidance.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="card">
            <h3>⚙️ Resource Optimization</h3>
            <p>Allocate counselling, remedial and activity slots based on priority.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="card">
            <h3>📊 Dashboard</h3>
            <p>Monitor total students, recommendations and school-wide insights.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            """
            <div class="card">
            <h3>📄 Reports</h3>
            <p>Generate AI-powered reports and track weekly student progress.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )






def about():

    col1, col2 = st.columns([1.15,1], vertical_alignment="center")

    with col1:

        st.markdown("""
        <div class="subtitle">
        ABOUT EDUOPT AI
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero">
        Smart Schools.<br>
        Better Student Support.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">

        <h3>🚨 Problem</h3>

        <p style="font-size:18px;">
        Schools often struggle to identify students who require
        counselling, remedial classes, attendance monitoring or
        extracurricular engagement. Due to limited staff and resources,
        deserving students may not receive timely support.
        </p>

        <br>

        <h3>💡 Our Solution</h3>

        <p style="font-size:18px;">
        EduOpt AI uses Artificial Intelligence to analyse student data,
        predict required interventions, and optimize the allocation of
        counselling, remedial, sports and activity resources—helping every
        student receive the right support at the right time.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.image(
            "assets/about.png",
            use_container_width=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <h2 style="text-align:center;color:white;">
    Our Vision
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <p style="font-size:18px;text-align:center;">

    To build intelligent schools where Artificial Intelligence assists
    educators in making faster, fairer and data-driven decisions,
    ensuring every student receives personalized academic and emotional
    support.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <h2 style="text-align:center;color:white;">
    Our Mission
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <p style="font-size:18px;text-align:center;">

    Empower schools with AI-powered prediction,
    resource optimization and progress monitoring
    to improve student well-being and academic success.

    </p>

    </div>
    """, unsafe_allow_html=True)




def features():

    st.markdown("""
    <div class="subtitle">
    OUR FEATURES
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
    AI Features That Transform Schools
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- AI Prediction ---------------- #

    col1, col2 = st.columns([1.2,1])

    with col1:

        st.markdown("""
        <div class="card">

        <h2>🤖 AI Prediction</h2>

        <p style="font-size:18px;line-height:1.8;">

        EduOpt AI intelligently analyses attendance,
        academic performance, behaviour,
        teacher feedback, counselling history and
        learning difficulties to predict which students
        require support.

        The AI recommends:

        ✅ Counselling

        ✅ Remedial Classes

        ✅ Academic Guidance

        ✅ Attendance Intervention

        ✅ Sports / Activity Engagement

        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.image(
            "assets/prediction.png",
            use_container_width=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ---------------- Resource Optimization ---------------- #

    col3, col4 = st.columns([1.2,1])

    with col3:

        st.markdown("""
        <div class="card">

        <h2>⚙ Resource Optimization</h2>

        <p style="font-size:18px;line-height:1.8;">

        Schools often have fewer counselling,
        remedial and activity slots than students.

        EduOpt AI automatically prioritizes students
        based on urgency and available resources.

        It optimizes:

        ✅ Counselling Slots

        ✅ Remedial Slots

        ✅ Sports Activities

        ✅ Art Classes

        ✅ Music Classes

        ✅ Other School Resources

        </p>

        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.image(
            "assets/optimization.png",
            use_container_width=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <h2 style="text-align:center;">
    🌟 Why EduOpt AI?
    </h2>

    <p style="text-align:center;font-size:18px;">

    ✔ AI Powered Predictions

    ✔ Resource Optimization

    ✔ Dashboard Analytics

    ✔ Downloadable Reports

    ✔ Weekly Student Progress

    ✔ Secure School Login

    </p>

    </div>
    """, unsafe_allow_html=True)




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
