"""
B.Tech / B.E Engineering - Complete Detailed Guide PDF Generator
All branches with: Duration, Fees, Subjects, Jobs, Salary, Scope
Pure Python - No external libraries needed.
"""

import re
import zlib
from pathlib import Path

# ===== PDF SETTINGS =====
PAGE_W, PAGE_H = 595, 842  # A4
ML, MR, MT, MB = 45, 45, 55, 50
BODY_SIZE = 9.5
HEAD_SIZE = 13
TITLE_SIZE = 18
SUB_SIZE = 11
LINE_H = 12.5
HEAD_LINE_H = 17
SUB_LINE_H = 14



# ===== CONTENT =====
CONTENT = """
================================================================================
B.TECH / B.E (ENGINEERING) - COMPLETE DETAILED GUIDE
================================================================================
India ke sabse popular career options me se ek hai Engineering.
Is guide me har ek branch ki FULL DETAIL di gayi hai:
  -> Duration, Fees, Subjects, Jobs, Salary, Future Scope

================================================================================
[*] GENERAL INFORMATION
================================================================================

  Duration         : 4 Years (8 Semesters)
  Eligibility      : 12th PCM (Physics, Chemistry, Maths) - min 60%
  Top Exams        : JEE Main, JEE Advanced, BITSAT, VITEEE, SRMJEE,
                     MHT-CET, KCET, WBJEE, AP EAMCET, State CETs
  Top Colleges     : IITs, NITs, IIITs, BITS, VIT, SRM, DTU, NSUT,
                     Jadavpur, BIT Mesra, COEP, PSG Tech

  Fees Range:
    - Govt (IIT/NIT)   : Rs 2-8 Lakh (total 4 years)
    - Govt (State)     : Rs 1-4 Lakh (total 4 years)
    - Private (Top)    : Rs 8-25 Lakh (total 4 years)
    - Private (Avg)    : Rs 4-12 Lakh (total 4 years)

================================================================================
[1] COMPUTER SCIENCE & ENGINEERING (CSE)
================================================================================

  >> What is CSE?
     Computer Science me aap software development, algorithms,
     data structures, OS, databases, networking, AI/ML sab seekhte ho.
     Ye sabse HIGH DEMAND branch hai aaj ke time me.

  >> Duration: 4 Years (8 Semesters)

  >> Fees:
     - IIT/NIT        : Rs 2-8 Lakh total
     - Private (Top)  : Rs 10-20 Lakh total
     - Private (Avg)  : Rs 4-10 Lakh total

  >> Key Subjects (Semester-wise):
     Sem 1-2: Maths, Physics, Chemistry, Basic Programming (C/C++),
              Engineering Drawing, Communication Skills
     Sem 3-4: Data Structures, Algorithms, DBMS, Computer Organization,
              Discrete Maths, OOP (Java/Python), Digital Logic
     Sem 5-6: Operating Systems, Computer Networks, Software Engineering,
              Compiler Design, Theory of Computation, Web Development
     Sem 7-8: Machine Learning, Cloud Computing, Cyber Security,
              Project/Internship, Electives (AI, Blockchain, IoT)

  >> Specializations:
     - Artificial Intelligence & Machine Learning (AI/ML)
     - Data Science & Big Data Analytics
     - Cyber Security & Ethical Hacking
     - Cloud Computing & DevOps
     - Full Stack Web Development
     - Mobile App Development (Android/iOS)
     - Blockchain Technology
     - Internet of Things (IoT)
     - Game Development
     - Quantum Computing

  >> Job Roles:
     - Software Developer/Engineer
     - Data Scientist / ML Engineer
     - Full Stack Developer
     - DevOps Engineer
     - Cloud Architect
     - Cybersecurity Analyst
     - System Designer / Architect
     - Product Manager (Tech)
     - AI Research Scientist
     - Blockchain Developer

  >> Salary (Per Annum - India):
     - Fresher        : Rs 4-12 LPA (IIT/NIT: 12-50+ LPA)
     - 2-5 Years Exp  : Rs 8-25 LPA
     - 5-10 Years Exp : Rs 20-50 LPA
     - 10+ Years/Lead : Rs 40-1 Cr+ LPA
     - Abroad (USA)   : $80,000 - $200,000+ per year

  >> Top Recruiters:
     Google, Microsoft, Amazon, Meta (Facebook), Apple, Flipkart,
     Infosys, TCS, Wipro, Adobe, Uber, Paytm, Razorpay, CRED

  >> Future Scope: EXCELLENT - Sabse zyada demand, remote work possible,
     freelancing, startup opportunities unlimited.



================================================================================
[2] ARTIFICIAL INTELLIGENCE & MACHINE LEARNING (AI/ML)
================================================================================

  >> What is AI/ML?
     AI/ML me machines ko intelligent banana seekhte ho - jaise
     image recognition, chatbots, self-driving cars, recommendation
     systems (Netflix/YouTube jaisa). CSE ka advanced version.

  >> Duration: 4 Years

  >> Fees:
     - IIT/NIT        : Rs 2-8 Lakh total
     - Private (Top)  : Rs 12-22 Lakh total
     - Private (Avg)  : Rs 5-12 Lakh total

  >> Key Subjects:
     - Programming (Python, R, C++)
     - Linear Algebra & Probability/Statistics
     - Data Structures & Algorithms
     - Machine Learning (Supervised/Unsupervised)
     - Deep Learning (Neural Networks, CNN, RNN, Transformers)
     - Natural Language Processing (NLP)
     - Computer Vision
     - Reinforcement Learning
     - Big Data Analytics (Hadoop, Spark)
     - MLOps & Model Deployment
     - Ethics in AI

  >> Job Roles:
     - Machine Learning Engineer
     - Data Scientist
     - AI Research Scientist
     - NLP Engineer
     - Computer Vision Engineer
     - MLOps Engineer
     - AI Product Manager
     - Robotics AI Engineer

  >> Salary (Per Annum - India):
     - Fresher        : Rs 6-15 LPA (IIT: 20-60+ LPA)
     - 2-5 Years      : Rs 12-35 LPA
     - 5-10 Years     : Rs 30-60 LPA
     - Senior/Lead    : Rs 50 LPA - 1.5 Cr+
     - Abroad (USA)   : $100,000 - $300,000+ per year

  >> Top Recruiters:
     Google DeepMind, OpenAI, Microsoft Research, Meta AI, NVIDIA,
     Amazon AWS, IBM Watson, Tesla, Apple, Indian startups

  >> Future Scope: OUTSTANDING - AI is the future. Har industry me
     AI lag raha hai. Next 10-20 saal me demand exponentially badhegi.


================================================================================
[3] DATA SCIENCE & BIG DATA
================================================================================

  >> What is Data Science?
     Data se insights nikalna, patterns dhundhna, predictions karna.
     Companies data use karti hain business decisions ke liye.

  >> Duration: 4 Years

  >> Fees:
     - IIT/NIT        : Rs 2-8 Lakh total
     - Private (Top)  : Rs 10-20 Lakh total

  >> Key Subjects:
     - Statistics & Probability
     - Python / R Programming
     - SQL & Database Management
     - Machine Learning
     - Data Visualization (Tableau, Power BI)
     - Big Data Tools (Hadoop, Spark, Kafka)
     - Data Mining & Warehousing
     - Cloud Platforms (AWS, GCP, Azure)
     - A/B Testing & Experimentation
     - Business Analytics

  >> Job Roles:
     - Data Scientist
     - Data Analyst
     - Business Intelligence Analyst
     - Data Engineer
     - Analytics Manager
     - Quantitative Analyst (Finance)

  >> Salary:
     - Fresher        : Rs 5-12 LPA
     - 3-5 Years      : Rs 12-30 LPA
     - Senior         : Rs 30-60+ LPA
     - Abroad         : $90,000 - $180,000+

  >> Future Scope: EXCELLENT - Data is the new oil. Har company ko
     data scientists chahiye. Healthcare, Finance, E-commerce sab me demand.


================================================================================
[4] INFORMATION TECHNOLOGY (IT)
================================================================================

  >> What is IT?
     IT me software + networking + database + web technologies
     sab milke padhte ho. CSE se thoda broad hai, business
     applications pe focus zyada hota hai.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-6 Lakh total
     - Private        : Rs 4-15 Lakh total

  >> Key Subjects:
     - Programming (Java, Python, C++)
     - Web Technologies (HTML, CSS, JS, React, Node)
     - Database Systems (SQL, MongoDB)
     - Computer Networks & Security
     - Cloud Computing
     - Software Engineering & Testing
     - ERP Systems
     - IT Project Management
     - Mobile Computing

  >> Job Roles:
     - Software Developer
     - Web Developer
     - System Administrator
     - Network Engineer
     - IT Consultant
     - Database Administrator
     - Quality Assurance Engineer

  >> Salary:
     - Fresher        : Rs 3.5-10 LPA
     - 3-5 Years      : Rs 8-20 LPA
     - Senior         : Rs 20-45 LPA

  >> Future Scope: VERY GOOD - IT sector me jobs kabhi khatam nahi hogi.
     Digital India initiative se government sector me bhi demand hai.



================================================================================
[5] ELECTRONICS & COMMUNICATION ENGINEERING (ECE)
================================================================================

  >> What is ECE?
     Electronic devices, circuits, communication systems (mobile,
     satellite, Wi-Fi), embedded systems, VLSI chip design - sab ECE me.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-6 Lakh total
     - Private        : Rs 4-15 Lakh total

  >> Key Subjects:
     - Analog & Digital Electronics
     - Signals & Systems
     - Communication Systems (Analog + Digital)
     - Microprocessors & Microcontrollers
     - VLSI Design (Chip Design)
     - Embedded Systems
     - Antenna & Wave Propagation
     - Control Systems
     - Digital Signal Processing (DSP)
     - Wireless & Mobile Communication
     - Optical Fiber Communication
     - IoT (Internet of Things)

  >> Job Roles:
     - VLSI Design Engineer
     - Embedded Systems Engineer
     - Telecom Engineer
     - RF Engineer
     - Network Engineer
     - IoT Developer
     - Signal Processing Engineer
     - Chip Design Engineer (Semiconductor)

  >> Salary:
     - Fresher        : Rs 3-8 LPA (core), Rs 6-15 LPA (IT switch)
     - 3-5 Years      : Rs 8-20 LPA
     - Senior (VLSI)  : Rs 25-50+ LPA
     - Abroad (Chip)  : $100,000 - $200,000+

  >> Top Recruiters:
     Qualcomm, Intel, Samsung, Texas Instruments, Broadcom, MediaTek,
     ISRO, DRDO, BSNL, Jio, Airtel, Nokia, Ericsson

  >> Future Scope: VERY GOOD - 5G, semiconductor industry booming in
     India (Tata Semiconductors, Vedanta-Foxconn). VLSI engineers ki
     bahut demand hai. IoT & embedded systems bhi grow ho rahe.


================================================================================
[6] ELECTRICAL ENGINEERING (EE / EEE)
================================================================================

  >> What is EE/EEE?
     Power generation, transmission, motors, transformers, renewable
     energy (solar, wind), power electronics - sab yahan aata hai.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-5 Lakh total
     - Private        : Rs 4-12 Lakh total

  >> Key Subjects:
     - Circuit Theory & Network Analysis
     - Electrical Machines (Motors, Generators, Transformers)
     - Power Systems (Generation, Transmission, Distribution)
     - Power Electronics (Converters, Inverters)
     - Control Systems
     - Renewable Energy Systems (Solar, Wind)
     - Electrical Measurements & Instrumentation
     - High Voltage Engineering
     - Switchgear & Protection
     - PLC & SCADA (Automation)

  >> Job Roles:
     - Power Systems Engineer
     - Electrical Design Engineer
     - Control Systems Engineer
     - Solar/Wind Energy Engineer
     - Maintenance Engineer (Power Plants)
     - Substation Engineer
     - Automation Engineer (PLC/SCADA)
     - PSU Jobs (NTPC, BHEL, Power Grid, ONGC)

  >> Salary:
     - Fresher        : Rs 3-7 LPA (Private), Rs 5-9 LPA (PSU)
     - 3-5 Years      : Rs 7-15 LPA
     - PSU Senior     : Rs 15-30 LPA + perks (house, car, medical)
     - Private Senior : Rs 20-40 LPA

  >> Top Recruiters:
     NTPC, BHEL, Power Grid, ONGC, IOCL, L&T, Siemens, ABB,
     Schneider Electric, Tata Power, Adani Power, BPCL, HPCL

  >> Future Scope: STABLE & GROWING - Renewable energy India me boom
     kar raha hai. EV (Electric Vehicles) industry bhi grow ho rahi.
     PSU jobs me stability + perks excellent hain.


================================================================================
[7] MECHANICAL ENGINEERING (ME)
================================================================================

  >> What is ME?
     Machines design karna, manufacture karna, automobiles, robotics,
     thermodynamics, fluid mechanics - sabse purani aur versatile branch.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-5 Lakh total
     - Private        : Rs 4-14 Lakh total

  >> Key Subjects:
     - Engineering Mechanics & Strength of Materials
     - Thermodynamics & Heat Transfer
     - Fluid Mechanics & Hydraulics
     - Manufacturing Processes (Casting, Welding, Machining)
     - Machine Design & Kinematics
     - Automobile Engineering
     - Robotics & Mechatronics
     - CAD/CAM/CAE (AutoCAD, SolidWorks, CATIA, ANSYS)
     - Industrial Engineering & Production Management
     - Refrigeration & Air Conditioning
     - Power Plant Engineering
     - Finite Element Analysis (FEA)

  >> Job Roles:
     - Design Engineer (CAD/CAM)
     - Production/Manufacturing Engineer
     - Automobile Engineer
     - Quality Control Engineer
     - R&D Engineer
     - Maintenance Engineer
     - Robotics Engineer
     - HVAC Engineer
     - PSU Jobs (BHEL, ONGC, NTPC, Indian Railways)

  >> Salary:
     - Fresher        : Rs 3-6 LPA (Core), Rs 5-10 LPA (Non-core/IT)
     - 3-5 Years      : Rs 6-15 LPA
     - Senior (Core)  : Rs 15-35 LPA
     - PSU            : Rs 8-25 LPA + government perks
     - Abroad         : $60,000 - $120,000+

  >> Top Recruiters:
     Tata Motors, Mahindra, Maruti Suzuki, Hyundai, L&T, BHEL,
     Bosch, Caterpillar, Cummins, General Electric, Siemens

  >> Future Scope: GOOD - Core jobs less in India par EV, Robotics,
     3D Printing, Defence manufacturing (Make in India) se demand badh rahi.



================================================================================
[8] CIVIL ENGINEERING (CE)
================================================================================

  >> What is CE?
     Roads, bridges, buildings, dams, airports, tunnels, water supply
     systems - infrastructure banane ka kaam Civil Engineers ka hai.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-4 Lakh total
     - Private        : Rs 3-12 Lakh total

  >> Key Subjects:
     - Surveying & Geomatics
     - Strength of Materials / Structural Analysis
     - Concrete Technology & Design of Structures (RCC/Steel)
     - Geotechnical Engineering (Soil Mechanics)
     - Fluid Mechanics & Hydraulic Engineering
     - Transportation Engineering (Roads, Railways)
     - Environmental Engineering (Water, Waste Treatment)
     - Construction Planning & Management
     - Earthquake Engineering
     - Estimation & Costing
     - AutoCAD, STAAD Pro, ETABS, Revit (BIM)

  >> Job Roles:
     - Structural Engineer
     - Site Engineer / Construction Manager
     - Transportation Engineer
     - Geotechnical Engineer
     - Environmental Engineer
     - Urban Planner
     - Quantity Surveyor / Estimator
     - Government Engineer (PWD, CPWD, NHAI)
     - PSU (NHPC, NTPC Civil, Railways)

  >> Salary:
     - Fresher        : Rs 2.5-5 LPA
     - 3-5 Years      : Rs 5-12 LPA
     - Senior/Manager : Rs 12-30 LPA
     - Own firm       : Rs 20-50+ LPA (depends on projects)
     - Govt/PSU       : Rs 6-20 LPA + perks

  >> Top Recruiters:
     L&T Construction, DLF, Shapoorji Pallonji, Tata Projects,
     NHAI, CPWD, Railways, Godrej Properties, Prestige, Lodha

  >> Future Scope: MODERATE-GOOD - Smart Cities Mission, Highways,
     Metro expansion, Airports - sab civil engineers chahiye.
     Government jobs me always demand. Real estate boom helps.


================================================================================
[9] CHEMICAL ENGINEERING
================================================================================

  >> What is Chemical Engineering?
     Chemical reactions ko industrial scale pe use karna - petroleum
     refining, pharmaceuticals, food processing, fertilizers, paints.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-5 Lakh total
     - Private        : Rs 4-12 Lakh total

  >> Key Subjects:
     - Chemical Process Calculations
     - Thermodynamics (Chemical)
     - Fluid Mechanics & Heat Transfer
     - Mass Transfer Operations
     - Chemical Reaction Engineering
     - Process Control & Instrumentation
     - Petroleum Refining
     - Polymer Science & Technology
     - Environmental Engineering
     - Plant Design & Economics
     - Process Simulation (Aspen, HYSYS)

  >> Job Roles:
     - Process Engineer
     - Chemical Plant Engineer
     - Petroleum Engineer
     - Quality Control Chemist
     - R&D Engineer (Pharma/FMCG)
     - Environmental Consultant
     - PSU Jobs (IOCL, BPCL, HPCL, ONGC, GAIL)
     - Food Processing Engineer

  >> Salary:
     - Fresher        : Rs 3-7 LPA
     - PSU Fresher    : Rs 7-12 LPA
     - 5+ Years       : Rs 10-25 LPA
     - PSU Senior     : Rs 20-35 LPA + perks
     - Abroad         : $70,000 - $130,000+

  >> Top Recruiters:
     Reliance, IOCL, BPCL, HPCL, ONGC, GAIL, UPL, Tata Chemicals,
     Asian Paints, Hindustan Unilever, Dr. Reddy's, Sun Pharma

  >> Future Scope: GOOD - Petroleum, Pharma, Green Energy (hydrogen),
     food industry always need chemical engineers. PSU jobs are goldmine.


================================================================================
[10] AEROSPACE / AERONAUTICAL ENGINEERING
================================================================================

  >> What is Aerospace?
     Aircraft, rockets, satellites, drones design karna.
     Aeronautical = planes, Astronautical = spacecraft.

  >> Duration: 4 Years

  >> Fees:
     - Govt (IITs)    : Rs 2-8 Lakh total
     - Private        : Rs 6-18 Lakh total

  >> Key Subjects:
     - Aerodynamics
     - Aircraft Structures & Materials
     - Flight Mechanics & Control
     - Propulsion Systems (Jet Engines, Rockets)
     - Space Mechanics & Orbital Dynamics
     - Avionics (Aircraft Electronics)
     - Computational Fluid Dynamics (CFD)
     - Aircraft Design & Performance
     - Composite Materials
     - Missile Technology
     - UAV/Drone Technology

  >> Job Roles:
     - Aircraft Design Engineer
     - Propulsion Engineer
     - Avionics Engineer
     - Flight Test Engineer
     - Satellite Systems Engineer
     - ISRO/DRDO Scientist
     - Drone/UAV Engineer
     - Airline Maintenance Engineer (AME)
     - Defence R&D

  >> Salary:
     - Fresher        : Rs 4-8 LPA
     - ISRO/DRDO      : Rs 7-12 LPA (starting) + Govt perks
     - 5+ Years       : Rs 12-30 LPA
     - Abroad (Boeing/Airbus): $80,000 - $150,000+
     - HAL/BEL        : Rs 8-20 LPA + perks

  >> Top Recruiters:
     ISRO, DRDO, HAL, BEL, NAL, Boeing India, Airbus, GE Aviation,
     Rolls-Royce, Lockheed Martin, Dassault, SpaceX (abroad)

  >> Future Scope: GROWING - India space program expanding (Gaganyaan,
     private space - Agnikul, Skyroot). Drone industry booming.
     Defence manufacturing (Make in India) creating more jobs.



================================================================================
[11] BIOTECHNOLOGY ENGINEERING
================================================================================

  >> What is Biotechnology?
     Biology + Technology = medicines, vaccines, genetic engineering,
     agriculture biotech, bioinformatics. COVID vaccine bhi biotech se bani!

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-6 Lakh total
     - Private        : Rs 5-15 Lakh total

  >> Key Subjects:
     - Biochemistry & Molecular Biology
     - Microbiology & Cell Biology
     - Genetic Engineering & Genomics
     - Bioprocess Engineering (Fermentation)
     - Immunology & Virology
     - Bioinformatics & Computational Biology
     - Pharmaceutical Biotechnology
     - Plant & Animal Biotechnology
     - Environmental Biotechnology
     - Food Biotechnology
     - Bioethics & IPR (Intellectual Property)

  >> Job Roles:
     - Research Scientist (Pharma/Biotech)
     - Genetic Engineer
     - Bioprocess Engineer
     - Quality Analyst (Pharma)
     - Bioinformatics Analyst
     - Clinical Research Associate
     - Regulatory Affairs Specialist
     - Patent Analyst (Biotech)

  >> Salary:
     - Fresher        : Rs 3-6 LPA
     - 3-5 Years      : Rs 6-15 LPA
     - Senior/R&D     : Rs 15-35 LPA
     - Abroad         : $60,000 - $120,000+
     - PhD holders    : Rs 12-30 LPA (India)

  >> Top Recruiters:
     Biocon, Serum Institute, Dr. Reddy's, Cipla, Sun Pharma,
     Novartis, Pfizer, GSK, Monsanto/Bayer, CSIR Labs, ICMR

  >> Future Scope: GROWING - Personalized medicine, gene therapy, mRNA
     vaccines, agri-biotech - future bright hai. PhD karoge to aur bhi achha.


================================================================================
[12] ROBOTICS & MECHATRONICS ENGINEERING
================================================================================

  >> What is Robotics/Mechatronics?
     Mechanical + Electronics + Computer Science = Robots banaana!
     Industrial robots, surgical robots, drones, humanoids.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 2-6 Lakh total
     - Private        : Rs 6-16 Lakh total

  >> Key Subjects:
     - Mechanics & Kinematics of Robots
     - Sensors & Actuators
     - Microcontrollers (Arduino, Raspberry Pi, ARM)
     - Control Systems & Automation
     - Computer Vision & Image Processing
     - Machine Learning for Robotics
     - Industrial Automation (PLC, SCADA)
     - Robot Operating System (ROS)
     - 3D Printing & Rapid Prototyping
     - Artificial Intelligence
     - Human-Robot Interaction

  >> Job Roles:
     - Robotics Engineer
     - Automation Engineer
     - Control Systems Engineer
     - Drone Engineer
     - Industrial Robot Programmer
     - Research Scientist (Robotics)
     - Mechatronics Design Engineer

  >> Salary:
     - Fresher        : Rs 4-8 LPA
     - 3-5 Years      : Rs 8-20 LPA
     - Senior         : Rs 20-40 LPA
     - Abroad         : $80,000 - $160,000+

  >> Top Recruiters:
     ABB Robotics, KUKA, Fanuc, Bosch, Siemens, Tesla, Boston
     Dynamics, ISRO, DRDO, Amazon Robotics, Addverb (Indian)

  >> Future Scope: EXCELLENT - Industry 4.0, warehouse automation
     (Amazon), surgical robots, self-driving cars - sab robotics hai.


================================================================================
[13] PETROLEUM ENGINEERING
================================================================================

  >> What is Petroleum Engineering?
     Oil & Gas nikalna (drilling), refining, transportation.
     High salary wali niche branch.

  >> Duration: 4 Years

  >> Fees:
     - Govt (ISM Dhanbad/RGIPT): Rs 2-6 Lakh total
     - Private        : Rs 5-12 Lakh total

  >> Key Subjects:
     - Drilling Engineering
     - Reservoir Engineering
     - Production Engineering
     - Petroleum Geology
     - Well Logging & Formation Evaluation
     - Enhanced Oil Recovery (EOR)
     - Natural Gas Engineering
     - Pipeline Engineering
     - Health, Safety & Environment (HSE)

  >> Job Roles:
     - Drilling Engineer
     - Reservoir Engineer
     - Production Engineer
     - Mud Engineer
     - Well Completion Engineer
     - Pipeline Engineer
     - HSE Officer (Oil & Gas)
     - PSU (ONGC, IOCL, GAIL, OIL)

  >> Salary:
     - Fresher (PSU)  : Rs 8-14 LPA
     - Private MNC    : Rs 10-20 LPA
     - 5+ Years       : Rs 20-40 LPA
     - Abroad (Gulf)  : $80,000 - $200,000+ (tax free!)

  >> Top Recruiters:
     ONGC, Oil India, IOCL, GAIL, Reliance, Schlumberger,
     Halliburton, Baker Hughes, Shell, BP, Saudi Aramco

  >> Future Scope: MODERATE - Oil demand slowly declining but gas &
     transition fuels still needed for 20-30 years. Gulf jobs pay very well.


================================================================================
[14] MINING ENGINEERING
================================================================================

  >> What is Mining Engineering?
     Minerals (coal, iron, gold, diamonds) safely extract karna.
     India mineral-rich hai - coal, iron ore, bauxite, manganese.

  >> Duration: 4 Years

  >> Fees:
     - Govt (ISM/IITs) : Rs 2-6 Lakh total
     - Private          : Rs 4-10 Lakh total

  >> Key Subjects:
     - Mining Methods (Surface & Underground)
     - Rock Mechanics & Ground Control
     - Mine Ventilation & Safety
     - Drilling & Blasting
     - Mineral Processing & Beneficiation
     - Mine Planning & Design
     - Environmental Impact of Mining
     - Mine Surveying

  >> Job Roles:
     - Mining Engineer
     - Mine Manager
     - Blasting Engineer
     - Safety Officer (Mines)
     - Environmental Engineer (Mining)
     - PSU (Coal India, NMDC, MOIL)
     - Government Mining Inspector

  >> Salary:
     - Fresher (PSU)  : Rs 7-12 LPA
     - Coal India      : Rs 10-15 LPA (starting) + perks
     - Senior Manager  : Rs 20-40 LPA
     - Private (Vedanta/Tata Steel): Rs 6-20 LPA

  >> Future Scope: STABLE - Coal India is world's largest coal miner.
     India needs minerals for steel, EVs (lithium mining). Niche but stable.



================================================================================
[15] MARINE / NAVAL ARCHITECTURE ENGINEERING
================================================================================

  >> What is Marine Engineering?
     Ships design karna, ship engines, offshore platforms, ports.
     Merchant Navy officers bhi is se bante hain.

  >> Duration: 4 Years (B.Tech) / 4 Years (Marine Engineering - sailing)

  >> Fees:
     - Govt (IIT Madras/Kharagpur): Rs 2-6 Lakh
     - IMU/MERI/AMET : Rs 8-20 Lakh total
     - Private       : Rs 10-25 Lakh total

  >> Key Subjects:
     - Naval Architecture & Ship Design
     - Marine Propulsion Systems
     - Ship Structures & Stability
     - Marine Safety & Regulations
     - Ocean Engineering
     - Port & Harbor Engineering
     - Offshore Platform Design
     - Marine Electrical Systems

  >> Job Roles:
     - Marine Engineer (Merchant Navy)
     - Naval Architect (Ship Designer)
     - Port Engineer
     - Offshore Engineer
     - Shipyard Engineer
     - Indian Navy (Engineering branch)
     - Underwater Robotics Engineer

  >> Salary:
     - Merchant Navy  : Rs 15-60 LPA (on ship, tax-free mostly)
     - Shore jobs     : Rs 5-15 LPA
     - Senior Captain : Rs 1-2 Cr per year (on ship)
     - Naval Officer  : Rs 8-15 LPA + military perks

  >> Future Scope: GOOD - India building ports (Sagarmala project).
     International shipping always needs engineers. High salary but
     6 months ship, 6 months home - lifestyle challenging.


================================================================================
[16] AUTOMOBILE / AUTOMOTIVE ENGINEERING
================================================================================

  >> What is Automobile Engineering?
     Cars, bikes, trucks, buses design aur manufacture karna.
     EV (Electric Vehicles) ab naya hot area hai.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-5 Lakh total
     - Private        : Rs 5-14 Lakh total

  >> Key Subjects:
     - Automotive Engines (IC Engines)
     - Vehicle Dynamics & Chassis Design
     - Automotive Electrical & Electronics
     - Transmission Systems
     - Vehicle Body Engineering
     - Electric Vehicle Technology (EV)
     - Battery Management Systems
     - Autonomous Vehicle Technology
     - Emission Control & Green Fuels
     - CAD (SolidWorks, CATIA, AutoCAD)
     - Vehicle Safety & Crash Testing

  >> Job Roles:
     - Automotive Design Engineer
     - EV Battery Engineer
     - Powertrain Engineer
     - Vehicle Testing Engineer
     - Production Engineer (Auto plant)
     - Quality Engineer
     - R&D Engineer (OEM)
     - Motorsport Engineer (Formula 1, etc.)

  >> Salary:
     - Fresher        : Rs 3-7 LPA
     - 3-5 Years      : Rs 7-15 LPA
     - Senior (OEM)   : Rs 15-35 LPA
     - EV Startups    : Rs 8-25 LPA
     - Abroad (BMW/Mercedes): $70,000 - $130,000+

  >> Top Recruiters:
     Tata Motors, Mahindra, Maruti, Hyundai, BMW, Mercedes,
     Ather Energy, Ola Electric, Tesla, Bosch, Continental

  >> Future Scope: VERY GOOD - EV revolution happening now!
     India target: 30% EVs by 2030. EV engineers ki massive demand.


================================================================================
[17] INSTRUMENTATION & CONTROL ENGINEERING
================================================================================

  >> What is Instrumentation?
     Sensors, measurement devices, control systems jo factories,
     power plants, refineries me use hote hain - automation ka backbone.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-5 Lakh total
     - Private        : Rs 4-12 Lakh total

  >> Key Subjects:
     - Sensors & Transducers
     - Process Control Systems
     - PLC & SCADA Programming
     - Industrial Automation
     - Biomedical Instrumentation
     - Analytical Instrumentation
     - Control System Design
     - Digital Signal Processing
     - Microprocessors & Embedded Systems
     - DCS (Distributed Control Systems)

  >> Job Roles:
     - Instrumentation Engineer
     - Control Systems Engineer
     - Automation Engineer
     - DCS/PLC Programmer
     - Biomedical Engineer
     - PSU (ONGC, NTPC, Power Grid, Refineries)
     - Quality & Calibration Engineer

  >> Salary:
     - Fresher        : Rs 3-6 LPA
     - PSU            : Rs 7-12 LPA starting
     - 5+ Years       : Rs 10-25 LPA
     - Senior (Oil/Gas): Rs 20-40 LPA

  >> Future Scope: GOOD - Industry 4.0 & IoT need instrumentation
     engineers. PSU jobs always available. Niche but stable career.


================================================================================
[18] TEXTILE ENGINEERING
================================================================================

  >> What is Textile Engineering?
     Kapda (fabric) banane ki technology - fiber se fashion tak.
     India world's 2nd largest textile producer hai.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-4 Lakh total
     - Private        : Rs 3-10 Lakh total

  >> Key Subjects:
     - Fiber Science & Technology
     - Yarn Manufacturing (Spinning)
     - Fabric Manufacturing (Weaving, Knitting)
     - Textile Chemistry (Dyeing, Printing, Finishing)
     - Garment Technology
     - Technical Textiles (Medical, Geo, Agro textiles)
     - Quality Control & Testing
     - Fashion Technology
     - Textile Machine Design

  >> Job Roles:
     - Textile Engineer
     - Production Manager (Textile Mill)
     - Quality Control Manager
     - Fashion Technologist
     - Technical Textile Specialist
     - Merchandiser (Export)
     - R&D (Fabric innovation)

  >> Salary:
     - Fresher        : Rs 2.5-5 LPA
     - 3-5 Years      : Rs 5-12 LPA
     - Senior/Manager : Rs 12-25 LPA
     - Export business : Rs 20 LPA - unlimited (own business)

  >> Future Scope: MODERATE - India ka textile export $50B+ hai.
     Technical textiles (bulletproof, medical masks) growing fast.



================================================================================
[19] FOOD TECHNOLOGY / FOOD ENGINEERING
================================================================================

  >> What is Food Technology?
     Food processing, preservation, packaging, quality testing.
     Maggi, Amul, Haldiram - sab food engineers banate hain!

  >> Duration: 4 Years

  >> Fees:
     - Govt (NIFTEM/CFTRI): Rs 2-5 Lakh total
     - Private        : Rs 4-12 Lakh total

  >> Key Subjects:
     - Food Chemistry & Biochemistry
     - Food Microbiology & Safety
     - Food Processing Technology
     - Dairy Technology
     - Bakery & Confectionery Technology
     - Food Packaging Technology
     - Food Quality & Standards (FSSAI, ISO)
     - Nutrition & Dietetics
     - Food Plant Design & Layout
     - Fermentation Technology (Beer, Wine, Probiotics)
     - Fruit & Vegetable Processing

  >> Job Roles:
     - Food Technologist
     - Quality Assurance Manager
     - R&D Scientist (FMCG)
     - Food Safety Officer
     - Production Manager (Food Factory)
     - Nutrition Consultant
     - FSSAI Inspector (Govt)
     - Own Food Business / Startup

  >> Salary:
     - Fresher        : Rs 3-6 LPA
     - 3-5 Years      : Rs 6-12 LPA
     - Senior (FMCG)  : Rs 12-30 LPA
     - Food Business  : Unlimited potential

  >> Top Recruiters:
     Nestle, Amul, ITC, Britannia, Parle, Haldiram's, MTR,
     PepsiCo, Coca-Cola, Dabur, Mother Dairy, Hindustan Unilever

  >> Future Scope: GOOD - India's food processing industry growing 10%+
     yearly. Organic food, health supplements, plant-based foods trending.


================================================================================
[20] BIOMEDICAL ENGINEERING
================================================================================

  >> What is Biomedical Engineering?
     Medical devices banane ka kaam - MRI machines, pacemakers,
     artificial organs, prosthetics, surgical robots.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 2-6 Lakh total
     - Private        : Rs 5-15 Lakh total

  >> Key Subjects:
     - Human Anatomy & Physiology
     - Biomechanics
     - Medical Imaging (X-ray, MRI, CT, Ultrasound)
     - Biomaterials & Artificial Organs
     - Biomedical Instrumentation
     - Clinical Engineering
     - Rehabilitation Engineering
     - Bioinformatics
     - Medical Signal Processing (ECG, EEG)
     - Hospital Management Systems

  >> Job Roles:
     - Biomedical Engineer
     - Medical Device Designer
     - Clinical Engineer (Hospital)
     - Prosthetics & Orthotics Engineer
     - R&D (Medical Devices)
     - Regulatory Affairs (Medical)
     - Healthcare IT Specialist

  >> Salary:
     - Fresher        : Rs 3-6 LPA
     - 3-5 Years      : Rs 6-15 LPA
     - Senior (MNC)   : Rs 15-35 LPA
     - Abroad         : $70,000 - $130,000+

  >> Top Recruiters:
     GE Healthcare, Siemens Healthineers, Philips, Medtronic,
     Johnson & Johnson, Abbott, Wipro GE, Trivitron, SkanRay

  >> Future Scope: GROWING - Wearable health tech, telemedicine, AI in
     healthcare, 3D printed organs - biomedical engineers ki demand badhegi.


================================================================================
[21] ENVIRONMENTAL ENGINEERING
================================================================================

  >> What is Environmental Engineering?
     Pollution control, water treatment, waste management, sustainability.
     Climate change ke time me bahut important field.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-5 Lakh total
     - Private        : Rs 4-12 Lakh total

  >> Key Subjects:
     - Water Supply & Treatment
     - Wastewater Engineering
     - Air Pollution Control
     - Solid Waste Management
     - Environmental Impact Assessment (EIA)
     - Climate Change & Sustainability
     - Noise Pollution Control
     - Green Building & LEED Certification
     - Renewable Energy Systems
     - Environmental Laws & Policy

  >> Job Roles:
     - Environmental Engineer
     - Water/Wastewater Treatment Plant Designer
     - EIA Consultant
     - Pollution Control Board Officer
     - Sustainability Consultant
     - Green Building Consultant
     - Climate Change Analyst
     - NGO / International Organizations (UN, WHO)

  >> Salary:
     - Fresher        : Rs 3-6 LPA
     - Govt/PSU       : Rs 5-12 LPA
     - Consultant 5yr : Rs 10-25 LPA
     - International  : Rs 20-50+ LPA
     - Abroad         : $60,000 - $110,000+

  >> Future Scope: GROWING FAST - Climate change is the biggest challenge.
     ESG (Environmental, Social, Governance) norms forcing every company
     to hire environmental engineers. Green jobs will boom.


================================================================================
[22] COMPUTER SCIENCE - CYBER SECURITY SPECIALIZATION
================================================================================

  >> What is Cyber Security?
     Systems, networks, data ko hackers se protect karna.
     Digital India = more cyber threats = more demand.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 2-6 Lakh total
     - Private        : Rs 6-18 Lakh total

  >> Key Subjects:
     - Network Security & Firewalls
     - Ethical Hacking & Penetration Testing
     - Cryptography & Encryption
     - Malware Analysis
     - Digital Forensics
     - Secure Coding Practices
     - Cloud Security (AWS/Azure Security)
     - Security Operations Center (SOC)
     - Risk Assessment & Compliance (ISO 27001)
     - Blockchain Security
     - Mobile & IoT Security

  >> Job Roles:
     - Cyber Security Analyst
     - Ethical Hacker / Penetration Tester
     - Security Architect
     - SOC Analyst
     - Incident Response Specialist
     - Forensic Investigator
     - CISO (Chief Information Security Officer)
     - Bug Bounty Hunter (Freelance)

  >> Salary:
     - Fresher        : Rs 5-12 LPA
     - 3-5 Years      : Rs 12-30 LPA
     - Senior/CISO    : Rs 40-1 Cr+ LPA
     - Bug Bounty     : Rs 5-50 LPA (top hunters)
     - Abroad         : $90,000 - $200,000+

  >> Future Scope: OUTSTANDING - Every company needs security.
     Shortage of 3 million+ security professionals globally.
     One of the highest paying CS specializations.



================================================================================
[23] COMPUTER SCIENCE - CLOUD COMPUTING & DEVOPS
================================================================================

  >> What is Cloud/DevOps?
     Software ko cloud pe deploy karna (AWS, Azure, GCP), servers
     manage karna, CI/CD pipelines banana, infrastructure automate karna.

  >> Duration: 4 Years

  >> Key Subjects:
     - Linux System Administration
     - Cloud Platforms (AWS, Azure, Google Cloud)
     - Containerization (Docker, Kubernetes)
     - CI/CD (Jenkins, GitHub Actions)
     - Infrastructure as Code (Terraform, Ansible)
     - Monitoring (Prometheus, Grafana)
     - Microservices Architecture
     - Networking & Load Balancing
     - Site Reliability Engineering (SRE)

  >> Job Roles:
     - Cloud Engineer
     - DevOps Engineer
     - Site Reliability Engineer (SRE)
     - Platform Engineer
     - Cloud Architect
     - Kubernetes Administrator

  >> Salary:
     - Fresher        : Rs 5-12 LPA
     - 3-5 Years      : Rs 15-35 LPA
     - Senior/Arch    : Rs 35-70 LPA
     - Abroad         : $100,000 - $200,000+

  >> Future Scope: EXCELLENT - Every company moving to cloud.
     DevOps engineers are among most in-demand roles globally.


================================================================================
[24] COMPUTER SCIENCE - FULL STACK WEB DEVELOPMENT
================================================================================

  >> What is Full Stack?
     Frontend (jo user dekhta hai) + Backend (server/database) dono
     develop karna. Most common developer role in industry.

  >> Duration: 4 Years (degree) + self-learning

  >> Key Technologies:
     Frontend: HTML, CSS, JavaScript, React/Angular/Vue, TypeScript
     Backend: Node.js, Python (Django/Flask), Java (Spring Boot)
     Database: PostgreSQL, MongoDB, Redis
     Tools: Git, Docker, AWS, Linux
     Mobile: React Native, Flutter (cross-platform)

  >> Job Roles:
     - Full Stack Developer
     - Frontend Developer
     - Backend Developer
     - MERN/MEAN Stack Developer
     - Web Application Architect
     - Freelance Developer

  >> Salary:
     - Fresher        : Rs 4-10 LPA
     - 2-4 Years      : Rs 10-25 LPA
     - Senior         : Rs 25-50 LPA
     - Freelance      : Rs 50K-5L per month (depends on clients)
     - Abroad (Remote): $60,000 - $150,000+

  >> Future Scope: EXCELLENT - Websites & apps kabhi khatam nahi honge.
     Remote work globally possible. Freelancing se unlimited earning.


================================================================================
[25] COMPUTER SCIENCE - BLOCKCHAIN & WEB3
================================================================================

  >> What is Blockchain?
     Decentralized ledger technology - cryptocurrency, smart contracts,
     DeFi, NFTs. Future of internet (Web3).

  >> Duration: 4 Years + specialization

  >> Key Subjects:
     - Distributed Systems
     - Cryptography
     - Smart Contract Development (Solidity, Rust)
     - Ethereum & Other Blockchains
     - DeFi (Decentralized Finance)
     - Consensus Mechanisms
     - Token Economics
     - Web3 Development

  >> Job Roles:
     - Blockchain Developer
     - Smart Contract Auditor
     - DeFi Protocol Engineer
     - Web3 Frontend Developer
     - Blockchain Security Researcher
     - Crypto Analyst

  >> Salary:
     - Fresher        : Rs 8-15 LPA
     - 2-4 Years      : Rs 15-40 LPA
     - Senior         : Rs 40-80 LPA
     - Abroad         : $120,000 - $300,000+ (very high!)

  >> Future Scope: HIGH POTENTIAL but volatile market. Technology
     is here to stay even if crypto prices fluctuate.


================================================================================
[26] COMPUTER SCIENCE - GAME DEVELOPMENT
================================================================================

  >> What is Game Dev?
     Video games banana - mobile, PC, console, VR games.
     India ka gaming market Rs 15,000 Cr+ hai.

  >> Duration: 4 Years + game engines learning

  >> Key Technologies:
     - Game Engines: Unity (C#), Unreal Engine (C++)
     - Game Physics & Mathematics
     - 3D Graphics & Rendering
     - Game AI & Pathfinding
     - Multiplayer Networking
     - VR/AR Development
     - Game Design & Level Design
     - Shader Programming

  >> Job Roles:
     - Game Developer/Programmer
     - Game Designer
     - Unity/Unreal Developer
     - VR/AR Developer
     - QA Tester (Gaming)
     - Indie Game Developer (own games)

  >> Salary:
     - Fresher        : Rs 4-8 LPA
     - 3-5 Years      : Rs 10-25 LPA
     - Senior (abroad): Rs 30-60 LPA
     - Indie success  : Unlimited (if game goes viral!)
     - Abroad         : $60,000 - $150,000+

  >> Future Scope: GROWING - Indian gaming industry exploding.
     Mobile gaming, esports, metaverse, VR - all growing fast.



================================================================================
[27] AGRICULTURAL ENGINEERING
================================================================================

  >> What is Agricultural Engineering?
     Modern farming technology - tractors, irrigation systems, food
     processing, soil science, precision agriculture (drone farming).

  >> Duration: 4 Years

  >> Fees:
     - Govt (IIT Kharagpur/Agri Univ): Rs 1-5 Lakh total
     - Private        : Rs 3-10 Lakh total

  >> Key Subjects:
     - Farm Machinery & Power
     - Irrigation & Drainage Engineering
     - Soil & Water Conservation
     - Food Processing Engineering
     - Renewable Energy in Agriculture
     - Precision Agriculture & GIS
     - Dairy & Food Engineering
     - Post-Harvest Technology
     - Agricultural Structures
     - Watershed Management

  >> Job Roles:
     - Agricultural Engineer
     - Farm Machinery Designer
     - Irrigation Engineer
     - Food Processing Plant Manager
     - Agriculture Officer (Govt)
     - Precision Farming Consultant
     - Agri-Tech Startup Founder

  >> Salary:
     - Fresher        : Rs 3-6 LPA
     - Govt Officer   : Rs 5-10 LPA + perks
     - Senior         : Rs 10-20 LPA
     - Agri Business  : Unlimited potential
     - Abroad         : $50,000 - $100,000+

  >> Future Scope: GROWING - AgriTech startups booming (Ninjacart,
     DeHaat, CropIn). Drone farming, smart irrigation - tech in farming.


================================================================================
[28] METALLURGICAL & MATERIALS ENGINEERING
================================================================================

  >> What is Metallurgy?
     Metals & materials - steel making, alloys, composites, nanomaterials.
     Without metallurgists, no cars, no buildings, no phones!

  >> Duration: 4 Years

  >> Fees:
     - Govt (IITs/NITs): Rs 2-6 Lakh total
     - Private         : Rs 3-10 Lakh total

  >> Key Subjects:
     - Physical Metallurgy & Phase Diagrams
     - Iron & Steel Making
     - Foundry & Casting Technology
     - Mechanical Metallurgy (Fracture, Fatigue)
     - Corrosion Engineering
     - Heat Treatment
     - Powder Metallurgy
     - Non-Ferrous Extractive Metallurgy
     - Ceramics & Polymers
     - Nanomaterials & Composites
     - Failure Analysis

  >> Job Roles:
     - Metallurgical Engineer
     - Materials Scientist
     - Quality Control (Steel/Auto)
     - Corrosion Engineer
     - Failure Analysis Engineer
     - R&D (Alloy development)
     - PSU (SAIL, NMDC, Hindalco)
     - Foundry Manager

  >> Salary:
     - Fresher        : Rs 3-7 LPA
     - PSU (SAIL)     : Rs 7-12 LPA starting
     - Tata Steel/JSW : Rs 6-15 LPA
     - Senior         : Rs 15-35 LPA
     - Abroad         : $60,000 - $120,000+

  >> Top Recruiters:
     Tata Steel, JSW, SAIL, Hindalco, Vedanta, ISRO, DRDO,
     ArcelorMittal, POSCO, Bharat Forge, Mahindra, auto OEMs

  >> Future Scope: GOOD - EV batteries need new materials, aerospace
     composites, 3D printing metals, nuclear materials - all need metallurgists.


================================================================================
[29] INDUSTRIAL & PRODUCTION ENGINEERING
================================================================================

  >> What is Industrial Engineering?
     Factory optimization - how to produce more, faster, cheaper,
     with less waste. Supply chain, lean manufacturing, Six Sigma.

  >> Duration: 4 Years

  >> Fees:
     - Govt           : Rs 1-5 Lakh total
     - Private        : Rs 4-12 Lakh total

  >> Key Subjects:
     - Operations Research & Optimization
     - Production Planning & Control
     - Quality Engineering (Six Sigma, TQM)
     - Supply Chain Management
     - Lean Manufacturing
     - Ergonomics & Work Study
     - CNC Programming & CAM
     - Industrial Safety
     - Project Management (PMP)
     - Cost Engineering
     - Automation & Robotics

  >> Job Roles:
     - Industrial Engineer
     - Production Engineer
     - Quality Engineer (Six Sigma Black Belt)
     - Supply Chain Manager
     - Operations Manager
     - Manufacturing Consultant
     - Project Manager
     - Management roles (MBA not needed!)

  >> Salary:
     - Fresher        : Rs 3-7 LPA
     - 3-5 Years      : Rs 7-15 LPA
     - Manager level  : Rs 15-35 LPA
     - Supply Chain Sr: Rs 25-50 LPA
     - Abroad         : $70,000 - $140,000+

  >> Future Scope: VERY GOOD - Every manufacturing company needs IE.
     Combines engineering + management. Easy switch to MBA/consulting roles.


================================================================================
[30] NUCLEAR ENGINEERING
================================================================================

  >> What is Nuclear Engineering?
     Nuclear power plants, radiation technology, nuclear medicine.
     India has 22+ nuclear reactors - clean energy source.

  >> Duration: 4 Years (offered at few colleges: IIT Kanpur has minor)

  >> Where to Study: BARC Training School (after B.Tech/M.Sc),
     IIT Kanpur, HBNI, AMU, Punjab Engineering College

  >> Key Subjects:
     - Nuclear Physics & Reactor Physics
     - Nuclear Reactor Engineering
     - Radiation Protection & Health Physics
     - Nuclear Materials
     - Thermal Hydraulics
     - Nuclear Fuel Cycle
     - Nuclear Safety & Regulations
     - Reactor Design

  >> Job Roles:
     - Nuclear Engineer (BARC, NPCIL)
     - Radiation Safety Officer
     - Nuclear Reactor Operator
     - Health Physicist
     - Research Scientist (DAE, IGCAR)
     - Nuclear Medicine Physicist

  >> Salary:
     - BARC Scientist  : Rs 7-12 LPA starting + Govt perks
     - Senior Scientist: Rs 15-30 LPA + house, medical, pension
     - NPCIL Engineer  : Rs 7-10 LPA starting
     - International   : $80,000 - $150,000+

  >> Future Scope: STABLE - India plans to triple nuclear power by 2032.
     Small Modular Reactors (SMR) is new technology. Very niche but secure.



================================================================================
SALARY COMPARISON TABLE (AVERAGE - ALL BRANCHES)
================================================================================

  Branch                    | Fresher    | 5 Yrs Exp  | 10+ Yrs
  ========================= | ========== | ========== | ===========
  CSE                       | 4-12 LPA   | 20-50 LPA  | 40-1 Cr+
  AI/ML                     | 6-15 LPA   | 30-60 LPA  | 50 LPA-1.5Cr
  Data Science              | 5-12 LPA   | 12-30 LPA  | 30-60 LPA
  Cyber Security            | 5-12 LPA   | 12-30 LPA  | 40-1 Cr
  Cloud/DevOps              | 5-12 LPA   | 15-35 LPA  | 35-70 LPA
  Full Stack                | 4-10 LPA   | 10-25 LPA  | 25-50 LPA
  Blockchain                | 8-15 LPA   | 15-40 LPA  | 40-80 LPA
  Game Dev                  | 4-8 LPA    | 10-25 LPA  | 30-60 LPA
  IT                        | 3.5-10 LPA | 8-20 LPA   | 20-45 LPA
  ECE                       | 3-8 LPA    | 8-20 LPA   | 25-50 LPA
  EE/EEE                    | 3-7 LPA    | 7-15 LPA   | 15-30 LPA
  Mechanical                | 3-6 LPA    | 6-15 LPA   | 15-35 LPA
  Civil                     | 2.5-5 LPA  | 5-12 LPA   | 12-30 LPA
  Chemical                  | 3-7 LPA    | 10-25 LPA  | 20-35 LPA
  Aerospace                 | 4-8 LPA    | 12-30 LPA  | 25-50 LPA
  Biotechnology             | 3-6 LPA    | 6-15 LPA   | 15-35 LPA
  Robotics                  | 4-8 LPA    | 8-20 LPA   | 20-40 LPA
  Petroleum                 | 8-14 LPA   | 20-40 LPA  | 30-60 LPA
  Mining                    | 7-12 LPA   | 15-30 LPA  | 20-40 LPA
  Marine                    | 15-60 LPA  | 30-80 LPA  | 1-2 Cr
  Automobile                | 3-7 LPA    | 7-15 LPA   | 15-35 LPA
  Instrumentation           | 3-6 LPA    | 10-25 LPA  | 20-40 LPA
  Textile                   | 2.5-5 LPA  | 5-12 LPA   | 12-25 LPA
  Food Technology           | 3-6 LPA    | 6-12 LPA   | 12-30 LPA
  Biomedical                | 3-6 LPA    | 6-15 LPA   | 15-35 LPA
  Environmental             | 3-6 LPA    | 10-25 LPA  | 20-50 LPA
  Agricultural              | 3-6 LPA    | 6-15 LPA   | 10-20 LPA
  Metallurgy                | 3-7 LPA    | 8-20 LPA   | 15-35 LPA
  Industrial/Production     | 3-7 LPA    | 7-15 LPA   | 15-35 LPA
  Nuclear                   | 7-12 LPA   | 15-30 LPA  | 20-40 LPA

  NOTE: LPA = Lakhs Per Annum. Salaries vary by college reputation,
  skills, city, and company. IIT/NIT grads get higher packages.


================================================================================
TOP ENTRANCE EXAMS FOR B.TECH
================================================================================

  Exam Name      | Conducted By  | For Colleges         | Level
  ============== | ============= | ==================== | ========
  JEE Main       | NTA           | NITs, IIITs, GFTIs   | National
  JEE Advanced   | IITs          | IITs (23 total)      | National
  BITSAT         | BITS Pilani   | BITS campuses        | National
  VITEEE         | VIT           | VIT campuses         | National
  SRMJEE         | SRM           | SRM campuses         | National
  COMEDK         | Consortium    | Karnataka colleges   | State
  MHT-CET        | Govt of MH    | Maharashtra colleges | State
  KCET           | KEA           | Karnataka colleges   | State
  WBJEE          | WBJEE Board   | West Bengal colleges | State
  AP EAMCET      | JNTU          | AP/Telangana colleges| State
  UPSEE/AKTU     | AKTU          | UP colleges          | State

  JEE Main: Jan & April (twice a year)
  JEE Advanced: May/June (only top 2.5 lakh JEE Main rankers eligible)


================================================================================
HOW TO CHOOSE YOUR BRANCH - TIPS
================================================================================

  1. INTEREST FIRST - Koi bhi branch me success tabhi milega jab
     aapko genuinely interest ho. Forced branch = dropout/backlog risk.

  2. MARKET DEMAND - Abhi CS/AI/Data Science ki demand sabse zyada hai,
     but 4 saal baad kya hoga koi nahi bata sakta. Jo aaj hot hai,
     4 saal baad saturated ho sakta hai.

  3. COLLEGE > BRANCH - Agar IIT/NIT mil raha hai kisi bhi branch me,
     to lelo. IIT ka tag + coding skills = placement pakka.

  4. CORE vs IT - Bahut mechanical/civil/electrical wale IT jobs
     me chale jaate hain. Coding seekhna ab har branch me zaroori hai.

  5. HIGHER STUDIES - Agar research ya abroad jaana hai (MS/PhD),
     to core branch better hai. Publications matter more than branch.

  6. GOVERNMENT JOBS - EE, ME, CE, ECE ke liye PSU me bahut posts
     hain (GATE exam through). PSU = high salary + job security.

  7. STARTUP IDEAS - Agar startup banana hai, CSE/IT best hai.
     But Biotech, Food Tech, AgriTech startups bhi booming hain.

  8. FINANCIAL SITUATION - Agar jaldi paisa kamana hai, IT/CS best.
     Core branches me growth slow but steady hoti hai.

  9. CODING SEEKHO CHAHE KOI BHI BRANCH HO - Aaj ke time me coding
     ek basic skill hai, jaise English language.

  10. CERTIFICATIONS MATTER - Google Cloud, AWS, Six Sigma, PMP,
      Cisco (CCNA) - ye certificates salary 30-50% badha sakte hain.


================================================================================
IMPORTANT LINKS & RESOURCES
================================================================================

  JEE Main     : jeemain.nta.nic.in
  JEE Advanced : jeeadv.ac.in
  GATE         : gate2025.iitr.ac.in (for M.Tech / PSU jobs)
  NIRF Ranking : nirfrankings.org (college rankings)
  Shiksha      : shiksha.com (college comparison)
  CollegeDunia : collegedunia.com
  Placement    : LinkedIn, Glassdoor (salary verification)


================================================================================
GENERATED BY KIRO FOR KRISHNA1K
================================================================================
  This PDF was auto-generated using pure Python.
  No external libraries used.
  Contact: github.com/Krishna1k
================================================================================
"""



# ===== PDF GENERATION ENGINE (Pure Python) =====

def escape_pdf(s):
    s = s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return re.sub(r"[^\x20-\x7E]", "", s)


def wrap(line, mx=100):
    if len(line) <= mx:
        return [line]
    ind = re.match(r"^(\s*)", line).group(1)
    words, out, cur = line.split(" "), [], ind
    for w in words:
        if len(cur) + len(w) + 1 > mx:
            out.append(cur.rstrip())
            cur = ind + w
        else:
            cur = (cur + " " + w) if cur.strip() else (ind + w)
    if cur.strip():
        out.append(cur.rstrip())
    return out


def paginate(content):
    raw = content.splitlines()
    lines = []
    for ln in raw:
        s = ln.strip()
        if s.startswith("====="):
            lines.append(("rule", ""))
        elif s.startswith("[") and s.endswith("]") and len(s) < 80:
            lines.append(("head", s))
        elif s and s == s.upper() and len(s) > 5 and not s.startswith("-") \
                and not s.startswith("*") and re.match(r"^[A-Z0-9 &/().,\'\-\[\]|:=+!?]+$", s):
            lines.append(("head", s))
        elif s.startswith(">>"):
            lines.append(("sub", s))
        else:
            for w in wrap(ln):
                lines.append(("body", w))

    pages, cur, y = [], [], PAGE_H - MT
    for kind, text in lines:
        lh = HEAD_LINE_H if kind == "head" else (SUB_LINE_H if kind == "sub" else LINE_H)
        if y - lh < MB:
            pages.append(cur)
            cur, y = [], PAGE_H - MT
        cur.append((kind, text, y))
        y -= lh
    if cur:
        pages.append(cur)
    return pages


def stream(page_lines):
    parts = []
    for kind, text, y in page_lines:
        if kind == "rule":
            parts.append(f"0.3 0.3 0.7 RG {ML} {y+4} m {PAGE_W-MR} {y+4} l S 0 0 0 RG")
            continue
        if not text.strip():
            continue
        if kind == "head":
            font, size = "/F2", HEAD_SIZE
            parts.append(f"0.1 0.1 0.5 rg")
        elif kind == "sub":
            font, size = "/F2", SUB_SIZE
            parts.append(f"0.0 0.3 0.0 rg")
        else:
            font, size = "/F1", BODY_SIZE
            parts.append(f"0 0 0 rg")
        parts.append(f"BT {font} {size} Tf {ML} {y} Td ({escape_pdf(text)}) Tj ET")
    # page number
    parts.append(f"BT /F1 8 Tf {PAGE_W-MR-30} {MB-20} Td (Page) Tj ET")
    return "\n".join(parts).encode("latin-1")


def make_pdf(out_path):
    pages = paginate(CONTENT)
    objs = []

    cat_n, pages_n, f1_n, f2_n = 1, 2, 3, 4
    pg_nums, ct_nums = [], []
    n = 5
    for _ in pages:
        pg_nums.append(n); n += 1
        ct_nums.append(n); n += 1

    objs = [None] * (n - 1)

    objs[0] = f"<< /Type /Catalog /Pages {pages_n} 0 R >>".encode()
    kids = " ".join(f"{x} 0 R" for x in pg_nums)
    objs[1] = f"<< /Type /Pages /Count {len(pages)} /Kids [ {kids} ] >>".encode()
    objs[2] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
    objs[3] = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"

    for i, pl in enumerate(pages):
        s = stream(pl)
        c = zlib.compress(s)
        objs[ct_nums[i]-1] = (
            f"<< /Length {len(c)} /Filter /FlateDecode >>\nstream\n"
        ).encode() + c + b"\nendstream"
        objs[pg_nums[i]-1] = (
            f"<< /Type /Page /Parent {pages_n} 0 R "
            f"/MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Resources << /Font << /F1 {f1_n} 0 R /F2 {f2_n} 0 R >> >> "
            f"/Contents {ct_nums[i]} 0 R >>"
        ).encode()

    buf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offs = [0]
    for i, body in enumerate(objs, 1):
        offs.append(len(buf))
        buf += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"

    xref = len(buf)
    buf += f"xref\n0 {len(objs)+1}\n".encode()
    buf += b"0000000000 65535 f \n"
    for o in offs[1:]:
        buf += f"{o:010d} 00000 n \n".encode()
    buf += f"trailer\n<< /Size {len(objs)+1} /Root {cat_n} 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()

    out_path.write_bytes(buf)
    print(f"PDF Generated: {out_path.name}")
    print(f"  Size: {len(buf):,} bytes")
    print(f"  Pages: {len(pages)}")


if __name__ == "__main__":
    out = Path(__file__).parent / "BTech_Engineering_Complete_Guide.pdf"
    make_pdf(out)
    print("Done! File ready for download.")
