import streamlit as st
import pandas as pd
from prediction import load_model
import re

data = load_model()
regressor_loaded = data["model"]


def show_predict_page():
    st.title("Predict Next Month")
    st.write("""Client Financial management: Help clients organise their budget by predicting their spending for the next month. This will help improve financial stability and overall pleasure.""")
    st.subheader("We need some information to predict your next month")

    job_dict = {'Accounting technician', 'Seismic interpreter',
       'Programme researcher, broadcasting/film/video',
       'Insurance risk surveyor', 'Solicitor',
       'Therapist, speech and language', 'Pathologist', 'Energy engineer',
       'Call centre manager', 'Associate Professor', 'Buyer, retail',
       'Early years teacher', 'Petroleum engineer',
       'IT sales professional', 'Engineer, mining', 'Surveyor, quantity',
       'Psychologist, counselling', 'Research scientist (maths)',
       'IT consultant', 'Senior tax professional/tax inspector',
       'Engineer, civil (contracting)', 'Sports development officer',
       'Acupuncturist', 'Horticultural therapist', 'Sports coach',
       'Designer, exhibition/display', 'Paediatric nurse',
       'Research officer, government', 'Interior and spatial designer',
       'Social research officer, government',
       'Architectural technologist', 'Programmer, systems',
       'Statistician', 'Chief Financial Officer',
       'Local government officer', 'Forensic psychologist',
       'Diplomatic Services operational officer', 'Quarry manager',
       'Optician, dispensing', 'Health and safety inspector',
       'Recycling officer', 'Museum/gallery curator', 'Counsellor',
       'Historic buildings inspector/conservation officer',
       'Product manager', 'Special effects artist', 'Designer, textile',
       'Volunteer coordinator', 'Therapist, music', 'Systems analyst',
       'Firefighter', 'Teacher, adult education', 'Architect',
       'Immigration officer', 'Learning disability nurse',
       'Analytical chemist', 'General practice doctor', 'Bonds trader',
       'Surveyor, insurance', 'Dentist',
       'Emergency planning/management officer',
       'Civil engineer, contracting', 'Materials engineer',
       'Medical secretary', 'Surveyor, building control', 'Best boy',
       'Designer, multimedia', 'Occupational psychologist',
       'Fisheries officer', 'Dancer', 'Adult nurse',
       'Technical sales engineer', 'Producer, television/film/video',
       'Administrator, arts', 'English as a foreign language teacher',
       'Wellsite geologist', 'Location manager',
       'Insurance account manager', 'Teacher, early years/pre',
       'Engineer, aeronautical', 'International aid/development worker',
       'Community arts worker', 'Commercial art gallery manager',
       'Engineer, broadcasting (operations)', 'Accountant, chartered',
       'Magazine features editor', 'Occupational therapist',
       'Agricultural engineer', 'Biochemist, clinical',
       'Clothing/textile technologist', 'Teacher, secondary school',
       'Scientist, biomedical', 'Hydrographic surveyor',
       'Games developer', 'Secretary, company', 'Electronics engineer',
       'Phytotherapist', 'Software engineer', 'Chartered accountant',
       'Field seismologist', 'Radiation protection practitioner',
       'Warehouse manager', 'Scientist, product/process development',
       'Barista', 'Scientific laboratory technician',
       'Surveyor, hydrographic', 'Designer, furniture', 'Press sub',
       'Technical author', 'Copywriter, advertising',
       'Teaching laboratory technician',
       'Medical laboratory scientific officer', 'Management consultant',
       'Consulting civil engineer', 'Regulatory affairs officer',
       'Legal executive', 'Tour manager', 'Farm manager', 'Ranger/warden',
       'Occupational hygienist', 'Primary school teacher',
       'Psychotherapist', 'Manufacturing systems engineer',
       'Licensed conveyancer', 'Tourist information centre manager',
       'Scientist, research (physical sciences)', 'Retail manager',
       'Broadcast presenter', 'Operational researcher',
       'Conservation officer, nature', 'Psychotherapist, dance movement',
       'Counselling psychologist', 'Editor, commissioning',
       'Health promotion specialist', 'Hydrologist',
       'Television/film/video producer', 'Copy', 'Lexicographer',
       'Data processing manager',
       'Armed forces logistics/support/administrative officer',
       'Sales promotion account executive', 'Geologist, engineering',
       'Chief Executive Officer', 'Production assistant, television',
       'Lobbyist', 'Radio broadcast assistant',
       'Teacher, English as a foreign language', 'Drilling engineer',
       'Chief Strategy Officer', 'Editor, film/video', 'Patent attorney',
       'Fine artist', 'Clinical embryologist',
       'Surveyor, planning and development',
       'Designer, television/film set', 'Artist',
       'Physiological scientist', 'Trade union research officer', 'Sub',
       'Nurse, mental health',
       'Clinical scientist, histocompatibility and immunogenetics',
       'Engineer, water', 'Oceanographer', 'Public relations officer',
       'Designer, jewellery', 'Site engineer', 'Horticulturist, amenity',
       'Broadcast journalist', 'Sales professional, IT',
       'Sports therapist', 'Actor', 'Fitness centre manager',
       'Meteorologist', 'Retail merchandiser',
       'Trading standards officer', 'Intelligence analyst',
       'Accountant, chartered public finance', 'Radio producer',
       'Broadcast engineer', 'Dietitian',
       'Engineer, manufacturing systems', 'Administrator, Civil Service',
       'Research officer, political party', 'Television floor manager',
       'Retail buyer', 'Astronomer', 'Archaeologist',
       'Brewing technologist', 'Secretary/administrator',
       'Accountant, chartered certified',
       'Public relations account executive', 'Advertising copywriter',
       'Publishing rights manager', 'Therapist, drama',
       'Scientist, water quality', 'Chartered management accountant',
       'Youth worker', 'Multimedia programmer', "Barrister's clerk",
       'Camera operator', 'Careers information officer',
       'Psychologist, educational', 'Teacher, primary school',
       'Engineer, structural', 'Jewellery designer',
       'Insurance claims handler', 'Pensions consultant',
       'Colour technologist', 'Chief Technology Officer',
       'Cytogeneticist', 'Aeronautical engineer',
       'Clinical cytogeneticist', 'Cabin crew', 'Chiropodist',
       'Financial adviser', 'English as a second language teacher',
       'Engineer, technical sales', 'Embryologist, clinical',
       'Chief Marketing Officer', 'Translator', 'Product designer',
       'Chief of Staff', 'Commercial/residential surveyor',
       'Advertising art director', 'Printmaker', 'Hotel manager',
       'Risk analyst', 'Trade mark attorney', 'Publishing copy',
       'Surveyor, mining', 'Careers adviser', 'Make',
       'Computer games developer', 'Investment banker, operational',
       'Engineer, automotive', 'Arts development officer',
       'Engineer, drilling', 'Contracting civil engineer',
       'Facilities manager', 'Passenger transport manager',
       'Conservation officer, historic buildings', 'Automotive engineer',
       'Engineer, building services', 'Arts administrator', 'Optometrist',
       'Psychiatric nurse', 'Radiographer, therapeutic',
       'Armed forces technical officer',
       'Accountant, chartered management', 'Forensic scientist',
       'Water engineer', 'Adult guidance worker', 'Land',
       'Research scientist (medical)', 'Restaurant manager',
       'Estate agent', 'Neurosurgeon', 'Quality manager', 'Retail banker',
       'Psychotherapist, child', 'Chemist, analytical', 'Contractor',
       'Archivist', 'Financial risk analyst', 'Engineer, maintenance',
       'Metallurgist', 'Curator', 'Legal secretary',
       'Designer, interior/spatial', 'Surveyor, minerals',
       'Designer, ceramics/pottery', 'Comptroller',
       'Psychologist, forensic', 'Food technologist', 'Health physicist',
       'Psychologist, sport and exercise', 'Economist',
       'Environmental manager', 'Medical technical officer',
       'Therapist, sports', 'Secondary school teacher',
       'Armed forces operational officer', 'Doctor, hospital',
       'Mining engineer', 'Research scientist (life sciences)',
       'Radiographer, diagnostic', "Politician's assistant",
       'Buyer, industrial', 'Risk manager', 'Producer, radio',
       'Air cabin crew', 'Marine scientist', 'Nutritional therapist',
       'Production engineer', 'Geologist, wellsite',
       'Accommodation manager', 'Further education lecturer',
       'Teacher, music', 'Industrial buyer', 'Agricultural consultant',
       'Banker', 'Lawyer', 'Scientist, physiological',
       'Exhibitions officer, museum/gallery', 'Tourism officer',
       'Immunologist', 'IT trainer', 'Programmer, multimedia',
       'Ceramics designer', 'Research scientist (physical sciences)',
       'Civil Service administrator', 'Social researcher',
       'Visual merchandiser', 'Scientist, research (medical)',
       'Catering manager', 'TEFL teacher', 'Physiotherapist',
       'Oncologist', 'Control and instrumentation engineer', 'Writer',
       'Engineer, maintenance (IT)', 'Midwife', 'Financial trader',
       'Building control surveyor', 'Customer service manager',
       'Hydrogeologist', 'Chiropractor', 'Housing manager/officer',
       'Commissioning editor', 'Travel agency manager',
       'Network engineer', 'Print production planner',
       'Administrator, charities/voluntary organisations',
       'Chemical engineer', 'Quantity surveyor',
       'Commercial horticulturist', 'Building surveyor',
       'Sales executive', 'Engineering geologist',
       'Designer, industrial/product', 'Theatre stage manager',
       'Theatre director', 'Special educational needs teacher',
       'Information systems manager', 'Applications developer',
       'Market researcher', 'Information officer', 'Homeopath',
       'Educational psychologist', 'Veterinary surgeon', 'Data scientist',
       'Structural engineer', 'Leisure centre manager',
       'Hospital pharmacist', 'Civil Service fast streamer', 'Musician',
       'Community pharmacist', 'Graphic designer',
       'Therapist, nutritional', 'Environmental health practitioner',
       'Production designer, theatre/television/film',
       'Geophysical data processor', 'Ophthalmologist',
       "Nurse, children's", 'Merchandiser, retail',
       'Clinical psychologist', 'Maintenance engineer',
       'Restaurant manager, fast food', 'Rural practice surveyor',
       'Actuary', 'Private music teacher', 'Horticultural consultant',
       'Administrator, education',
       'Scientist, clinical (histocompatibility and immunogenetics)',
       'Editorial assistant', 'Cartographer', 'Prison officer',
       'Music therapist', 'Environmental education officer',
       'Designer, fashion/clothing', 'Purchasing manager',
       'Audiological scientist', 'Holiday representative',
       'Diagnostic radiographer', 'Clinical molecular geneticist',
       'Communications engineer', 'Garment/textile technologist',
       'Advertising account executive', 'Chartered loss adjuster',
       'Surveyor, commercial/residential',
       'Furniture conservator/restorer', 'Warden/ranger', 'Gaffer',
       'Podiatrist', 'Psychologist, clinical', 'Arboriculturist',
       'Lecturer, further education', 'Health service manager',
       'Conservator, furniture', 'Pharmacist, hospital',
       'Librarian, public', 'Engineer, chemical',
       'Government social research officer', 'Energy manager',
       'Furniture designer', 'Clinical biochemist', 'Scientist, marine',
       'Therapist, art', 'Geneticist, molecular', 'Police officer',
       'Engineer, manufacturing', 'Presenter, broadcasting',
       'Designer, graphic', 'Surveyor, rural practice',
       'Teacher, special educational needs', 'Equities trader',
       'Museum/gallery exhibitions officer', 'Airline pilot',
       'Engineer, energy', 'Video editor', 'Herbalist',
       'Health and safety adviser', 'Art gallery manager',
       'Psychologist, prison and probation services', 'Surgeon',
       'Scientist, research (life sciences)',
       'Armed forces training and education officer',
       'Education administrator', 'Charity officer',
       'Electrical engineer', 'Professor Emeritus',
       'Plant breeder/geneticist', 'Water quality scientist',
       'Health visitor', 'Museum/gallery conservator', 'Aid worker',
       'Paramedic', 'Mental health nurse', 'Biomedical engineer',
       'Toxicologist', 'Engineer, agricultural',
       'Therapist, horticultural', 'Art therapist',
       'Community development worker', 'Engineer, communications',
       'Stage manager', 'Company secretary',
       'Sport and exercise psychologist', 'Claims inspector/assessor',
       'Scientist, audiological', 'Lecturer, higher education',
       'Charity fundraiser', 'Ambulance person',
       'Operational investment banker', 'Therapist, occupational',
       'Tax adviser', 'Engineer, land', 'Education officer, museum',
       'Financial planner', 'Geographical information systems officer',
       'Interpreter', 'Clinical research associate', 'Financial manager',
       'Office manager', 'Systems developer', 'Engineer, electronics',
       'Patent examiner', 'Land/geomatics surveyor', 'Animator',
       'Town planner', 'Building services engineer', 'Soil scientist',
       'Ship broker', 'Insurance broker', 'Psychiatrist',
       'Heritage manager', 'Environmental consultant', 'Administrator',
       'Public house manager', 'Records manager',
       'Education officer, community', 'Advertising account planner',
       'Estate manager/land agent', 'Conservator, museum/gallery',
       'Physicist, medical', 'Fish farm manager', 'Marketing executive',
       'Engineer, materials', 'Loss adjuster, chartered', 'Nurse, adult',
       'Advice worker', 'Community education officer', 'Proofreader',
       'Medical illustrator', 'Orthoptist', 'Engineer, petroleum',
       'Nurse, learning disability', 'Set designer',
       'Waste management officer', 'Mechanical engineer',
       'Equality and diversity officer', 'Animal nutritionist',
       'Haematologist', 'Pension scheme manager', 'Transport planner'}
    
    isRightToWorkRequired_dict = {
        'No': 0,
        'Yes': 1,
    }
    Python_dict = {
        'No': 0,
        'Yes': 1,
    }    
    SQL_dict = {
        'No': 0,
        'Yes': 1,
    }    
    R_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    Tableau_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    SAS_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    Matlab_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    Hadoop_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    Spark_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    Java_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    Scala_dict = {
        'No': 0,
        'Yes': 1,
    }
    
    recruiter_dict = {
        'No': 0,
        'Yes': 1,
    }
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(" **Job Classification and options**")
        job_classification_options = list(job_classification_dict.keys())
        job_classification = st.selectbox("jobClassification", job_classification_options)
        jobClassification = job_classification_dict[job_classification]
        state_options = list(state_dict.keys())
        state = st.selectbox("state", state_options)
        state = state_dict[state]
        isRightToWorkRequired_options = list(isRightToWorkRequired_dict.keys())
        isRightToWorkRequired = st.selectbox("isRightToWorkRequired", isRightToWorkRequired_options)
        isRightToWorkRequired = isRightToWorkRequired_dict[isRightToWorkRequired]
        recruiter_options = list(recruiter_dict.keys())
        recruiter = st.selectbox("recruiter", recruiter_options)
        recruiter = recruiter_dict[recruiter] 
        st.write(""" Australia map Photo by Jon Tyson on Unsplash
   """)
        st.image("https://images.unsplash.com/photo-1530230624258-4055a187ef65?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1341&q=80")

    with col2:
        st.subheader(" **Programming Language Required** ")
        Python_options = list(Python_dict.keys())
        Python = st.selectbox("Python", Python_options)
        Python = Python_dict[Python]
   
        SQL_options = list(SQL_dict.keys())
        SQL = st.selectbox("SQL", SQL_options)
        SQL = SQL_dict[SQL]
    
        R_options = list(R_dict.keys())
        R = st.selectbox("R", R_options)
        R = R_dict[R]
    
        Tableau_options = list(Tableau_dict.keys())
        Tableau = st.selectbox("Tableau", Tableau_options)
        Tableau = Tableau_dict[Tableau]
    
        SAS_options = list(SAS_dict.keys())
        SAS = st.selectbox("SAS", SAS_options)
        SAS = SAS_dict[SAS]
    
        Matlab_options = list(Matlab_dict.keys())
        Matlab = st.selectbox("Matlab", Matlab_options)
        Matlab = Matlab_dict[Matlab] 
    
        Hadoop_options = list(Hadoop_dict.keys())
        Hadoop = st.selectbox("Hadoop", Hadoop_options)
        Hadoop = Hadoop_dict[Hadoop] 
    
        Spark_options = list(Spark_dict.keys())
        Spark = st.selectbox("Spark", Spark_options)
        Spark = Spark_dict[Spark] 
    
        Java_options = list(Java_dict.keys())
        Java = st.selectbox("Java", Java_options)
        Java = Java_dict[Java] 
    
        Scala_options = list(Scala_dict.keys())
        Scala = st.selectbox("Scala", Scala_options)
        Scala = Scala_dict[Scala] 
    

    ok = st.button("Calculate Salary")
    if ok:
        X = pd.DataFrame({
        'jobClassification': [jobClassification],
        'state': [state],
        'isRightToWorkRequired': [isRightToWorkRequired],
        'Python': [Python],
        'SQL': [SQL],
        'R': [R],
        'Tableau': [Tableau],
        'SAS': [SAS],
        'Matlab': [Matlab],
        'Hadoop': [Hadoop],
        'Spark': [Spark],
        'Java': [Java],
        'Scala': [Scala],
        'recruiter': [recruiter],
        })
        
        salary = regressor_loaded.predict(X)
        salary_range_str = salary[0].strip('[]()')  # remove the brackets and parentheses
        salary_range_list = salary_range_str.split(',')  # split the string by comma
        min_salary = int(float(salary_range_list[0]))  # convert the first value to float and then to int
        max_salary = int(float(salary_range_list[1]))  # convert the second value to float and then to int
        st.subheader(f"The estimate salary from the given information is in the range of {min_salary:,.0f} to {max_salary:,.0f}$")
        
    st.write(""" ANLP_Baymax group 55 - Data Scientist salary prediction using a machine learning model """)
    st.write("""36118 Applied Natural Language Processing University of Technology Sydney """)
        
