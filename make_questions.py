# -*- coding: utf-8 -*-
import json

quizData = {
    "lectures": [
        {"id": 1, "title": "General Introduction"},
        {"id": 2, "title": "Concepts & Standards (OSHA & Indices)"},
        {"id": 3, "title": "Safety Programs, domino theory & Ratios"},
        {"id": 4, "title": "Workplace Hazards (Fall & Electrical)"},
        {"id": 5, "title": "Mechanical & Extreme Temp Hazards"},
        {"id": 6, "title": "Manual Material Handling & NIOSH"},
        {"id": 7, "title": "Fire Hazards & Protection"},
        {"id": 8, "title": "Noise Hazards & Risk Management"},
        {"id": 9, "title": "PPE, Signs, Tags & Hazmat"}
    ],
    "memorization": [
        # Lecture 1
        {
            "id": "mem-1",
            "lectureId": 1,
            "type": "MCQ",
            "question": "Which safety term is defined as the 'probability of incurring harm at a certain level of severity'?",
            "options": {
                "A": "Danger",
                "B": "Hazard",
                "C": "Risk",
                "D": "Accident"
            },
            "answer": "C",
            "explanation": "According to Lecture 1 definitions, **Risk** is the probability of incurring harm at a certain level of severity. In contrast, *Danger* is the negative consequence, and *Hazard* is the source or cause of danger."
        },
        {
            "id": "mem-2",
            "lectureId": 1,
            "type": "TF",
            "question": "An accident is defined as an unintended, unanticipated, and uncontrollable event sequence that may result in immediate or delayed undesirable effects.",
            "answer": "T",
            "explanation": "This is **True**. Lecture 1 defines an accident as an unintended, unanticipated, and uncontrollable single or multiple event sequence caused by unsafe acts, unsafe conditions, or both, which may result in immediate or delayed undesirable effects."
        },
        {
            "id": "mem-3",
            "lectureId": 1,
            "type": "MCQ",
            "question": "Which of the following is considered an indirect cost of an accident?",
            "options": {
                "A": "Medical treatments and doctor visits",
                "B": "Supervisory lost time and accident investigation",
                "C": "Physical therapy bills",
                "D": "Prescription medicines for the worker"
            },
            "answer": "B",
            "explanation": "Direct costs are obvious expenses like medical treatment, doctor visits, and physical therapy. Indirect costs include reduced productivity, accident investigations, supervisor lost time, retraining replacements, negative publicity, and legal fees."
        },
        # Lecture 2
        {
            "id": "mem-4",
            "lectureId": 2,
            "type": "MCQ",
            "question": "What does the abbreviation TRC stand for in safety record keeping?",
            "options": {
                "A": "Total Recovery Cases",
                "B": "Total Recordable Cases",
                "C": "Time to Recovery Constant",
                "D": "Temporary Rest Cases"
            },
            "answer": "B",
            "explanation": "TRC stands for **Total Recordable Cases**, which counts all recordable injury and illness cases, except fatalities."
        },
        {
            "id": "mem-5",
            "lectureId": 2,
            "type": "TF",
            "question": "First aid treatment is included in the counts for calculating total recordable injury and illness incidence rates.",
            "answer": "F",
            "explanation": "This is **False**. Lecture 2 explicitly states that recordable cases/medical treatment *do not include simple first aid*."
        },
        {
            "id": "mem-6",
            "lectureId": 2,
            "type": "MCQ",
            "question": "Which record-keeping metric specifically counts injury cases (excluding illness) involving lost workdays, while excluding fatalities?",
            "options": {
                "A": "TRC",
                "B": "LWDI",
                "C": "DAFWII",
                "D": "TWA"
            },
            "answer": "B",
            "explanation": "LWDI stands for **Lost Workday-case Incidence rate** (or index), which counts injury cases (excluding illness) involving 'lost workdays'. Fatalities are not included."
        },
        # Lecture 3
        {
            "id": "mem-7",
            "lectureId": 3,
            "type": "MCQ",
            "question": "What does TMC stand for in a typical safety management program?",
            "options": {
                "A": "Task Management Control",
                "B": "Total Management Commitment",
                "C": "Time, Money, and Concern",
                "D": "Training, Motivation, and Communication"
            },
            "answer": "C",
            "explanation": "In safety management, TMC represents the management commitment, measured by how much **Time, Money, and Concern** the employer gives to safety."
        },
        {
            "id": "mem-8",
            "lectureId": 3,
            "type": "TF",
            "question": "Heinrich's accident causation ratio states that 88% of accidents are caused by unsafe acts, 10% by unsafe conditions, and 2% by unpreventable causes.",
            "answer": "T",
            "explanation": "This is **True**. Heinrich's 88:10:2 ratio indicates that unsafe acts make up 88%, unsafe conditions 10%, and unpreventable causes make up 2% of industrial accidents."
        },
        {
            "id": "mem-9",
            "lectureId": 3,
            "type": "MCQ",
            "question": "In the 4 Ms model, which category includes Omission Errors and Commission Errors?",
            "options": {
                "A": "Media",
                "B": "Management",
                "C": "Machine",
                "D": "Man"
            },
            "answer": "D",
            "explanation": "Omission and Commission errors are human mistakes and fall under the **Man** category of the 4 Ms Model (Man, Machine, Media, Management)."
        },
        {
            "id": "mem-10",
            "lectureId": 3,
            "type": "TF",
            "question": "A proactive safety approach focuses on accident effects, whereas a reactive approach focuses on accident causes.",
            "answer": "F",
            "explanation": "This is **False**. A proactive approach focuses on anticipating and preventing accidents, focusing heavily on *accident causes*. A reactive approach focuses on limiting losses *after* an accident occurs (effects)."
        },
        {
            "id": "mem-11",
            "lectureId": 3,
            "type": "MCQ",
            "question": "According to design safety factors, what is the required load-to-strength design ratio for overhead crane hoists?",
            "options": {
                "A": "4:1",
                "B": "5:1",
                "C": "6:1",
                "D": "3:1"
            },
            "answer": "B",
            "explanation": "According to Lecture 3: Scaffold components require a 4:1 safety factor, **overhead crane hoists require 5:1**, and scaffold ropes require 6:1."
        },
        # Lecture 4
        {
            "id": "mem-12",
            "lectureId": 4,
            "type": "MCQ",
            "question": "When a building collapses due to an outward force pulling or pushing structural elements away from the center of mass, it is called an:",
            "options": {
                "A": "Implosion",
                "B": "Explosion",
                "C": "Inversion",
                "D": "Intrusion"
            },
            "answer": "B",
            "explanation": "An **Explosion** causes building collapse in the *outward* direction, whereas an *Implosion* pulls building walls into the center of mass."
        },
        {
            "id": "mem-13",
            "lectureId": 4,
            "type": "TF",
            "question": "Slips, trips, and falls make up the majority of general industry accidents and are second only to motor vehicle crashes in accidental deaths.",
            "answer": "T",
            "explanation": "This is **True**. Lecture 4 notes that falls account for 15-20% of accidental deaths/injuries, and slips, trips, and falls constitute the majority of general industry accidents, second only to motor vehicle crashes."
        },
        {
            "id": "mem-14",
            "lectureId": 4,
            "type": "MCQ",
            "question": "What is the standard height required by OSHA for the top rail of a standard guardrail system?",
            "options": {
                "A": "36 inches (+/- 3 inches)",
                "B": "42 inches (+/- 3 inches)",
                "C": "48 inches (+/- 3 inches)",
                "D": "30 inches (+/- 3 inches)"
            },
            "answer": "B",
            "explanation": "Under OSHA guidelines, the top rail height of standard guardrails must be **42 inches (+/- 3 inches)** above the floor level. The mid-rail height should be 21 inches, and the toe board must be 3.5 inches high."
        },
        {
            "id": "mem-15",
            "lectureId": 4,
            "type": "TF",
            "question": "Unless working on ladders, scaffolds, or scissor lifts, OSHA requires fall protection for workers exposed to falls of 4 feet or greater.",
            "answer": "T",
            "explanation": "This is **True**. OSHA standards require fall protection systems when workers are exposed to fall hazards of 4 feet or greater."
        },
        {
            "id": "mem-16",
            "lectureId": 4,
            "type": "MCQ",
            "question": "Which electrical injury type describes the current that causes a worker to reflexively grip and be unable to release an energized electrical conductor?",
            "options": {
                "A": "Let-go current",
                "B": "Freeze current",
                "C": "Ground current",
                "D": "Arc current"
            },
            "answer": "B",
            "explanation": "**Freeze current** (also known as the 'no-let-go' threshold) causes involuntary muscle contraction, locking the worker onto the electric conductor."
        },
        # Lecture 5
        {
            "id": "mem-17",
            "lectureId": 5,
            "type": "MCQ",
            "question": "Which mechanical hazard is listed in safety textbooks as the most dangerous part of power-driven machinery?",
            "options": {
                "A": "The power transmission (belts and pulleys)",
                "B": "The in-running nip point",
                "C": "The point of operation",
                "D": "The reciprocating arm"
            },
            "answer": "C",
            "explanation": "According to Lecture 5, the mechanical machine hazards in order from most dangerous to least are: **1. Point of operation**, 2. Power transmission (pulleys/belts), and 3. In-running nip points."
        },
        {
            "id": "mem-18",
            "lectureId": 5,
            "type": "TF",
            "question": "A complete bone break where the bone is divided into two or more pieces and penetrates the surrounding tissues and skin is a compound break.",
            "answer": "T",
            "explanation": "This is **True**. A simple/incomplete fracture is cracked bone with intact skin, while a **compound/complete** fracture breaks the bone into multiple pieces and punctures the surrounding tissue/skin."
        },
        {
            "id": "mem-19",
            "lectureId": 5,
            "type": "MCQ",
            "question": "Which type of machine guarding system prevents a machine from functioning unless its movable barrier gate is fully closed?",
            "options": {
                "A": "Fixed Guard",
                "B": "Adjustable Guard",
                "C": "Interlocked Gate System",
                "D": "Presence Sensing Device"
            },
            "answer": "C",
            "explanation": "An **interlocked gate guard system** acts such that if the gate is not fully closed, the machine cannot receive power and will not function."
        },
        {
            "id": "mem-20",
            "lectureId": 5,
            "type": "TF",
            "question": "Hypothermia in cold environments becomes a fatal risk, and safety engineers should prevent the worker's deep core body temperature from falling below 36°C.",
            "answer": "T",
            "explanation": "This is **True**. Health and safety guidelines state that for cold stress, deep core body temperature must be prevented from falling below 36°C."
        },
        {
            "id": "mem-21",
            "lectureId": 5,
            "type": "MCQ",
            "question": "Blisters forming on the skin are the primary visual indicator of which degree of burn?",
            "options": {
                "A": "First degree",
                "B": "Second degree",
                "C": "Third degree",
                "D": "Fourth degree"
            },
            "answer": "B",
            "explanation": "A **second-degree burn** is easily recognized due to the formation of blisters on the skin (which can be caused by exposure to temperatures of 98.9°C)."
        },
        # Lecture 6
        {
            "id": "mem-22",
            "lectureId": 6,
            "type": "MCQ",
            "question": "What is the preferred vertical range for manual lifting tasks to minimize back strain?",
            "options": {
                "A": "Between floor and shoulder height",
                "B": "Between knee and waist height",
                "C": "Between waist and chest height",
                "D": "Between floor and knee height"
            },
            "answer": "B",
            "explanation": "The preferred range for manual material handling lifts is **between knee and waist height**."
        },
        {
            "id": "mem-23",
            "lectureId": 6,
            "type": "TF",
            "question": "The NIOSH Load Constant (LC) is 23 kg, representing a load that is safe for 75% of females and 90% of males under optimal conditions.",
            "answer": "T",
            "explanation": "This is **True**. The Load Constant (LC) established by the revised NIOSH lifting equation is 23 kg (or 51 lbs)."
        },
        {
            "id": "mem-24",
            "lectureId": 6,
            "type": "MCQ",
            "question": "In the NIOSH lifting equation, what multiplier is represented by the abbreviation 'HM'?",
            "options": {
                "A": "Height Multiplier",
                "B": "Holding Multiplier",
                "C": "Horizontal Multiplier",
                "D": "Harness Multiplier"
            },
            "answer": "C",
            "explanation": "HM represents the **Horizontal Multiplier**, which is based on the distance from the midpoint of the ankles to the hands while holding the object."
        },
        # Lecture 7
        {
            "id": "mem-25",
            "lectureId": 7,
            "type": "MCQ",
            "question": "A fire involving flammable liquids such as gasoline, oil, or grease, and flammable gases is classified as what fire class?",
            "options": {
                "A": "Class A",
                "B": "Class B",
                "C": "Class C",
                "D": "Class D"
            },
            "answer": "B",
            "explanation": "Class A is ordinary combustibles (wood, paper). **Class B** is flammable liquids and gases. Class C is electrical fires, Class D is combustible metals, and Class K is cooking oils."
        },
        {
            "id": "mem-26",
            "lectureId": 7,
            "type": "TF",
            "question": "The P.A.S.S. acronym for operating portable fire extinguishers stands for Pull, Aim, Squeeze, and Sweep.",
            "answer": "T",
            "explanation": "This is **True**. P.A.S.S. stands for Pull the pin, Aim at the base of the fire, Squeeze the handle, and Sweep side-to-side."
        },
        {
            "id": "mem-27",
            "lectureId": 7,
            "type": "MCQ",
            "question": "What is the minimum width required by OSHA standards for a standard emergency exit pathway?",
            "options": {
                "A": "0.50 meters",
                "B": "0.711 meters",
                "C": "1.00 meters",
                "D": "1.20 meters"
            },
            "answer": "B",
            "explanation": "OSHA standards require exit routes to have a minimum height of 2 to 2.3 meters and a minimum width of **0.711 meters**."
        },
        # Lecture 8
        {
            "id": "mem-28",
            "lectureId": 8,
            "type": "MCQ",
            "question": "What is the OSHA Permissible Exposure Limit (PEL) for noise exposure over an 8-hour Time Weighted Average (TWA)?",
            "options": {
                "A": "85 dBA",
                "B": "90 dBA",
                "C": "95 dBA",
                "D": "100 dBA"
            },
            "answer": "B",
            "explanation": "The OSHA **Permissible Exposure Limit (PEL)** is 90 dBA for an 8-hour TWA. The *Action Level (AL)* is 85 dBA."
        },
        {
            "id": "mem-29",
            "lectureId": 8,
            "type": "TF",
            "question": "Immediate, permanent damage to the nerves of the ear can be caused by a single impact or banging noise exceeding 140 decibels.",
            "answer": "T",
            "explanation": "This is **True**. Any impact or banging noise above 140 decibels can cause immediate, permanent damage to the nerves in the ear."
        },
        {
            "id": "mem-30",
            "lectureId": 8,
            "type": "MCQ",
            "question": "When does OSHA require an employer to perform a baseline audiogram for exposed employees?",
            "options": {
                "A": "Within the first 30 days of employment",
                "B": "Within the first 6 months of exposure at or above the Action Level (85 dBA TWA)",
                "C": "Only after the employee reports hearing issues",
                "D": "Within the first year of exposure at or above 90 dBA TWA"
            },
            "answer": "B",
            "explanation": "A baseline audiogram must be performed within the **first 6 months** of work exposure to an 8-hour TWA of 85 dBA or greater. Annual audiograms are required after that."
        },
        # Lecture 9
        {
            "id": "mem-31",
            "lectureId": 9,
            "type": "MCQ",
            "question": "Under head protection standards, what electrical insulation rating is provided by Class B hard hats?",
            "options": {
                "A": "2,200 volts",
                "B": "10,000 volts",
                "C": "20,000 volts",
                "D": "No electrical protection"
            },
            "answer": "C",
            "explanation": "Class A hard hats protect up to 2,200 volts. **Class B hard hats protect up to 20,000 volts**. Class C bump caps provide no electrical protection."
        },
        {
            "id": "mem-32",
            "lectureId": 9,
            "type": "TF",
            "question": "ANSI Z535.2 specifies that Danger, Warning, and Caution signs can be used to warn of both personal injury and property damage hazards.",
            "answer": "F",
            "explanation": "This is **False**. ANSI Z535.2 states that Danger, Warning, and Caution signs should only be used for *personal injury risk*, and should not be used to warn of property damage."
        },
        {
            "id": "mem-33",
            "lectureId": 9,
            "type": "MCQ",
            "question": "According to the NFPA diamond symbol, what does the blue quadrant on the left represent?",
            "options": {
                "A": "Flammability hazard",
                "B": "Instability hazard",
                "C": "Health hazard",
                "D": "Special hazard rating"
            },
            "answer": "C",
            "explanation": "In the NFPA 704 diamond: **Blue is Health** (left), Red is Flammability (top), Yellow is Instability/Reactivity (right), and White is Special hazards (bottom)."
        },
        {
            "id": "mem-34",
            "lectureId": 9,
            "type": "TF",
            "question": "OSHA requires accident prevention tags to be rectangular and not smaller than 3 inches by 5 inches.",
            "answer": "T",
            "explanation": "This is **True**. OSHA standard 1910.145 states that tags must be rectangular and no smaller than 3 in x 5 in (7.6 cm x 12.7 cm)."
        },
        {
            "id": "mem-35",
            "lectureId": 9,
            "type": "MCQ",
            "question": "Which DOT/UN hazardous material transportation class covers gases (compressed, liquefied, or dissolved under pressure)?",
            "options": {
                "A": "Class 1",
                "B": "Class 2",
                "C": "Class 3",
                "D": "Class 4"
            },
            "answer": "B",
            "explanation": "Class 1 is explosives. **Class 2 is gases**. Class 3 is flammable liquids. Class 4 is flammable solids."
        },
        # More general memorization to fill target count
        {
            "id": "mem-36",
            "lectureId": 1,
            "type": "MCQ",
            "question": "Egyptian Labor Law and OSHA standards are examples of which type of obligation for maintaining safety?",
            "options": {
                "A": "Social obligations",
                "B": "Fiscal obligations",
                "C": "Legal obligations",
                "D": "Ethical obligations"
            },
            "answer": "C",
            "explanation": "Egyptian Labor Law and OSHA standards represent **Legal obligations**, consisting of laws, regulations, and governmental enforcement agencies."
        },
        {
            "id": "mem-37",
            "lectureId": 2,
            "type": "TF",
            "question": "In safety terminology, an incident is an unplanned, undesired event that results in personal injury or property damage.",
            "answer": "F",
            "explanation": "This is **False**. An *accident* results in injury or damage. An *incident* is an unplanned, undesired event that adversely affects the completion of a task (often called a near miss or interruption without injury)."
        },
        {
            "id": "mem-38",
            "lectureId": 3,
            "type": "MCQ",
            "question": "In Heinrich's domino theory, which element represents the middle (3rd) domino, which is the direct target for safety control?",
            "options": {
                "A": "Social Environment",
                "B": "Fault of Person",
                "C": "Unsafe Act or Condition",
                "D": "Accident"
            },
            "answer": "C",
            "explanation": "The five dominos in Heinrich's theory are: 1. Social Environment, 2. Fault of Person, **3. Unsafe Act/Condition**, 4. Accident, and 5. Injury. Removing the middle domino (Unsafe Act/Condition) stops the chain."
        },
        {
            "id": "mem-39",
            "lectureId": 3,
            "type": "TF",
            "question": "The Swiss Cheese Model proposes that accidents occur when multiple defensive layers all fail simultaneously, aligning their holes.",
            "answer": "T",
            "explanation": "This is **True**. The Swiss Cheese Model uses cheese slices as defensive barriers. An accident happens when holes in all layers align, allowing a hazard to pass through."
        },
        {
            "id": "mem-40",
            "lectureId": 4,
            "type": "MCQ",
            "question": "When working 25 feet or higher above a lower level, which fall protection system consists of mesh netting panels?",
            "options": {
                "A": "Guardrail System",
                "B": "Safety Net System",
                "C": "Positioning Device",
                "D": "Personal Fall Arrest System"
            },
            "answer": "B",
            "explanation": "**Safety Net Systems** consist of specially designed mesh nets and panels, used as protection for workers 25 feet or more above lower levels."
        },
        {
            "id": "mem-41",
            "lectureId": 4,
            "type": "TF",
            "question": "Electrical fuses and circuit breakers are devices used to detect hazards, but they do not automatically shut off power.",
            "answer": "F",
            "explanation": "This is **False**. Fuses and circuit breakers are safety devices designed to *automatically interrupt/cut off* current flow when an overload occurs."
        },
        {
            "id": "mem-42",
            "lectureId": 5,
            "type": "MCQ",
            "question": "Which type of machine guard can be manually adjusted to accommodate different sizes of material during operation?",
            "options": {
                "A": "Fixed Guard",
                "B": "Interlocked Guard",
                "C": "Adjustable Guard",
                "D": "Presence Sensing Device"
            },
            "answer": "C",
            "explanation": "An **adjustable guard** provides a barrier that can be adjusted to let materials pass while protecting the worker."
        },
        {
            "id": "mem-43",
            "lectureId": 5,
            "type": "TF",
            "question": "The term Zero Mechanical State means isolating a machine from its power source and venting/bleeding off all residual energy (pneumatic, spring, kinetic).",
            "answer": "T",
            "explanation": "This is **True**. Achieving a Zero Mechanical State requires neutralizing all stored or residual energy in a system after shutdown."
        },
        {
            "id": "mem-44",
            "lectureId": 6,
            "type": "MCQ",
            "question": "Back injuries represent approximately what fraction of lost workday (LWD) cases in manual material handling?",
            "options": {
                "A": "One-tenth",
                "B": "One-quarter",
                "C": "One-third",
                "D": "Half"
            },
            "answer": "C",
            "explanation": "Back injuries account for approximately **one-third** of lost workday (LWD) cases and 40% of worker compensation costs."
        },
        {
            "id": "mem-45",
            "lectureId": 6,
            "type": "TF",
            "question": "A bulky load is safer to lift than a regular object of the same mass because it distributes weight across a larger area.",
            "answer": "F",
            "explanation": "This is **False**. A bulky object is *harder* to handle because its size prevents its center of mass from being positioned close to the worker's body, increasing back stress."
        },
        {
            "id": "mem-46",
            "lectureId": 7,
            "type": "MCQ",
            "question": "What fire class represents fires involving cooking oils and animal/vegetable greases?",
            "options": {
                "A": "Class B",
                "B": "Class C",
                "C": "Class D",
                "D": "Class K"
            },
            "answer": "D",
            "explanation": "Fires involving commercial cooking fats, oils, and greases are classified as **Class K** fires."
        },
        {
            "id": "mem-47",
            "lectureId": 7,
            "type": "TF",
            "question": "In an Emergency Action Plan (EAP), using elevators is recommended to speed up evacuation during high-rise building fires.",
            "answer": "F",
            "explanation": "This is **False**. EAPs explicitly state that elevators **must not be used** to reach emergency exits during a fire because they can stall or fill with smoke."
        },
        {
            "id": "mem-48",
            "lectureId": 8,
            "type": "MCQ",
            "question": "Which engineering noise control method involves adding vibration-absorbing materials to machinery panels to reduce metal sheeting noise?",
            "options": {
                "A": "Isolation Enclosures",
                "B": "Damping",
                "C": "Silencers",
                "D": "Personnel Cabins"
            },
            "answer": "B",
            "explanation": "**Damping** is the addition of vibration-absorbing material to structure panels, reducing vibrations and noise."
        },
        {
            "id": "mem-49",
            "lectureId": 8,
            "type": "TF",
            "question": "An Action Level (AL) of 85 dBA requires the implementation of a hearing conservation program, including audiometric testing.",
            "answer": "T",
            "explanation": "This is **True**. While the PEL is 90 dBA, the Action Level (AL) of 85 dBA TWA triggers the requirement for a hearing conservation program."
        },
        {
            "id": "mem-50",
            "lectureId": 9,
            "type": "MCQ",
            "question": "Safety signs designed with white letters in a green rectangle at the top represent which ANSI sign class?",
            "options": {
                "A": "Notice Signs",
                "B": "Caution Signs",
                "C": "General Safety Signs",
                "D": "Fire Safety Signs"
            },
            "answer": "C",
            "explanation": "**General Safety signs** (like 'SAFETY FIRST', 'THINK', etc.) feature a green rectangle at the top with white lettering, and black letters on a white background below."
        },
        {
            "id": "mem-51",
            "lectureId": 9,
            "type": "TF",
            "question": "Under OSHA 1910.145, Caution Tags warn of immediate hazards that present a threat of death or serious injury.",
            "answer": "F",
            "explanation": "This is **False**. *Danger Tags* warn of immediate hazards representing threats of death/serious injury (red). *Caution Tags* warn of minor or potential hazards (yellow)."
        },
        {
            "id": "mem-52",
            "lectureId": 9,
            "type": "MCQ",
            "question": "A triangular sign featuring a fluorescent yellow-orange center and a dark red reflective border is the:",
            "options": {
                "A": "Laser warning sign",
                "B": "RF radiation hazard warning",
                "C": "Slow-moving vehicle emblem",
                "D": "Ionizing radiation label"
            },
            "answer": "C",
            "explanation": "The **slow-moving vehicle emblem** consists of a fluorescent yellow-orange triangle with a reflective red border, used for vehicles moving at 25 mph or less."
        },
        {
            "id": "mem-53",
            "lectureId": 9,
            "type": "TF",
            "question": "Lockout refers to physically locking an energy isolation switch in the OFF position, whereas Tagout is attaching a warning label notifying workers not to turn it on.",
            "answer": "T",
            "explanation": "This is **True**. Lockout uses a physical lock (padlock/hasp) to isolate power. Tagout uses a prominent tag warning that maintenance is in progress."
        },
        {
            "id": "mem-54",
            "lectureId": 9,
            "type": "MCQ",
            "question": "Which DOT hazardous material transportation class covers oxidizers and organic peroxides?",
            "options": {
                "A": "Class 3",
                "B": "Class 4",
                "C": "Class 5",
                "D": "Class 6"
            },
            "answer": "C",
            "explanation": "Class 3 is flammable liquids. Class 4 is flammable solids. **Class 5 covers oxidizers and organic peroxides**."
        },
        {
            "id": "mem-55",
            "lectureId": 9,
            "type": "TF",
            "question": "Dry Ice and battery parts are examples of Class 9 (Miscellaneous Dangerous Substances) under Hazmat regulations.",
            "answer": "T",
            "explanation": "This is **True**. Class 9 miscellaneous substances include ORM-A (Dry Ice) and ORM-C (asphalt, battery parts)."
        },
        {
            "id": "mem-56",
            "lectureId": 1,
            "type": "MCQ",
            "question": "Which term describes a source or cause of danger, such as deep water representing a potential cause of drowning?",
            "options": {
                "A": "Risk",
                "B": "Danger",
                "C": "Hazard",
                "D": "Severity"
            },
            "answer": "C",
            "explanation": "A **Hazard** is a source or cause of danger (i.e. water is a hazard that can cause the danger of drowning)."
        },
        {
            "id": "mem-57",
            "lectureId": 2,
            "type": "TF",
            "question": "Under OSHA guidelines, keeping records of safety incidents (like OSHA Forms 300) is important to evaluate a company's safety program.",
            "answer": "T",
            "explanation": "This is **True**. Record keeping using forms and reports is crucial to analyze and track occupational injury and illness cases."
        },
        {
            "id": "mem-58",
            "lectureId": 3,
            "type": "MCQ",
            "question": "In safety management, assigning responsibilities and providing accountability is a primary function of which 'M'?",
            "options": {
                "A": "Man",
                "B": "Machine",
                "C": "Media",
                "D": "Management"
            },
            "answer": "D",
            "explanation": "Establishing policies, assigning responsibility, authority, and accountability falls under **Management** in the 4 Ms Model."
        },
        {
            "id": "mem-59",
            "lectureId": 4,
            "type": "TF",
            "question": "When designing a standard toe board for standard fall guardrails, it must be 3.5 inches high and have no more than 1/4 inch clearance above the floor.",
            "answer": "T",
            "explanation": "This is **True**. Standard toe boards are 3.5 inches tall with a maximum of 1/4 inch floor clearance."
        },
        {
            "id": "mem-60",
            "lectureId": 5,
            "type": "MCQ",
            "question": "A rotating mechanical gear hazard that draws in a worker's loose clothing or fingers when passing adjacent to rotating parts is an:",
            "options": {
                "A": "In-running nip point hazard",
                "B": "Reciprocating shear point hazard",
                "C": "Impact point hazard",
                "D": "Adjustable point hazard"
            },
            "answer": "A",
            "explanation": "An **in-running nip point hazard** (or ingoing nip point) occurs where moving parts rotate together, potentially drawing loose clothing or limbs into the machine."
        }
    ],
    "mathLogic": [
        # Rate calculations (Lecture 2/3)
        {
            "id": "math-1",
            "lectureId": 2,
            "type": "MCQ",
            "question": "A manufacturing plant with 250 employees logs a total of 500,000 hours worked in a year. During this time, there are 12 recordable injury and illness cases. What is the Total Injury-Illness Incidence Rate (IR)?",
            "options": {
                "A": "2.4",
                "B": "4.8",
                "C": "1.2",
                "D": "9.6"
            },
            "answer": "B",
            "explanation": "Using the formula: $IR = (N_{rc} \\times 200,000) / H_{je}$\n$IR = (12 \\times 200,000) / 500,000 = 2,400,000 / 500,000 = 4.8$ recordable cases per 100 workers."
        },
        {
            "id": "math-2",
            "lectureId": 2,
            "type": "TF",
            "question": "If a facility experiences 0 recordable cases and has logged 150,000 hours of employee exposure, its calculated Total Injury-Illness Incidence Rate is exactly 0.0.",
            "answer": "T",
            "explanation": "This is **True**. If $N_{rc} = 0$, then the numerator in the incidence rate equation is 0, resulting in an IR of 0.0."
        },
        {
            "id": "math-3",
            "lectureId": 3,
            "type": "MCQ",
            "question": "A business has 8 recordable injury cases. The total lost workdays for all cases combined is 120 days. What is the calculated Average Severity (AS) per recordable case?",
            "options": {
                "A": "12 days",
                "B": "15 days",
                "C": "20 days",
                "D": "8 days"
            },
            "answer": "B",
            "explanation": "Average Severity ($AS$) = $N_{lwd} / N_{rc}$.\n$AS = 120 / 8 = 15$ days lost per recordable case."
        },
        {
            "id": "math-4",
            "lectureId": 3,
            "type": "MCQ",
            "question": "A plant records 15 injury cases. Out of these, only 6 cases resulted in lost workdays (averaging days away from work). The total lost workdays count is 90. What is the Average Days Away From Work (ADAW) index?",
            "options": {
                "A": "6 days",
                "B": "15 days",
                "C": "10 days",
                "D": "9 days"
            },
            "answer": "B",
            "explanation": "$ADAW = N_{lwd} / N_{clwd}$ (where $N_{clwd}$ is the number of cases involving lost workdays).\n$ADAW = 90 / 6 = 15$ days per lost workday case."
        },
        {
            "id": "math-5",
            "lectureId": 3,
            "type": "TF",
            "question": "If a warehouse has 10 recordable cases ($N_{rc}$) and 250 lost workdays ($N_{lwd}$), the calculated Average Severity ($AS$) is 25 days.",
            "answer": "T",
            "explanation": "This is **True**. $AS = N_{lwd} / N_{rc} = 250 / 10 = 25$ days."
        },
        # Sound decibel math (Lecture 8)
        {
            "id": "math-6",
            "lectureId": 8,
            "type": "MCQ",
            "question": "In acoustics, decibels are logarithmic and cannot be added directly. When combining two identical noise sources, each producing 90 decibels, the combined noise level is:",
            "options": {
                "A": "180 decibels",
                "B": "90 decibels",
                "C": "93 decibels",
                "D": "96 decibels"
            },
            "answer": "C",
            "explanation": "Combining two identical sound sources adds approximately **3 decibels** to the sound pressure level. Thus, 90 dBA + 90 dBA = 93 dBA."
        },
        {
            "id": "math-7",
            "lectureId": 8,
            "type": "TF",
            "question": "Combining four identical noise sources of 80 dB each results in a combined noise level of 86 dB.",
            "answer": "T",
            "explanation": "This is **True**. Doubling the sources twice (from 1 to 2, and 2 to 4) adds $3 + 3 = 6$ dB. Therefore, $80\\text{ dB} + 6\\text{ dB} = 86\\text{ dB}$."
        },
        {
            "id": "math-8",
            "lectureId": 8,
            "type": "MCQ",
            "question": "A worker is exposed to two noise sources: a power press at 85 dBA and an extraction fan at 88 dBA. The decibel difference is 3 dB. Using decibel addition rules (where a difference of 3 dB adds 1.8 dB to the higher value), what is the combined sound level?",
            "options": {
                "A": "173.0 dBA",
                "B": "89.8 dBA",
                "C": "88.0 dBA",
                "D": "86.8 dBA"
            },
            "answer": "B",
            "explanation": "Decibel addition rule: when the difference between two noise levels is 3 dB, you add 1.8 dB to the higher value.\nHigher value = 88 dBA. Combined noise = $88 + 1.8 = 89.8$ dBA."
        },
        {
            "id": "math-9",
            "lectureId": 8,
            "type": "MCQ",
            "question": "If two sound levels differ by 10 dB or more, the addition is negligible. If Source A is 95 dBA and Source B is 80 dBA, what is the combined sound level?",
            "options": {
                "A": "175 dBA",
                "B": "95 dBA (or approximately 95.1 dBA)",
                "C": "87.5 dBA",
                "D": "100 dBA"
            },
            "answer": "B",
            "explanation": "If the difference between two sound levels is 10 dB or more, the contribution of the lower sound level is negligible (adds 0.4 dB or less). Thus, the combined sound level remains approximately **95 dBA**."
        },
        # Heat stress heart rates (Lecture 5)
        {
            "id": "math-10",
            "lectureId": 5,
            "type": "MCQ",
            "question": "To evaluate heat strain, a supervisor monitors a 35-year-old worker. According to guidelines, the worker's heart rate should not sustain a rapid rate exceeding:",
            "options": {
                "A": "180 bpm",
                "B": "145 bpm",
                "C": "155 bpm",
                "D": "120 bpm"
            },
            "answer": "B",
            "explanation": "The formula for sustained maximum heart rate under heat strain is **(180 - age)**.\nFor a 35-year-old: $180 - 35 = 145$ bpm."
        },
        {
            "id": "math-11",
            "lectureId": 5,
            "type": "TF",
            "question": "For a 50-year-old worker experiencing heat exposure, a sustained heart rate of 135 bpm is considered safe because it is below 140 bpm.",
            "answer": "F",
            "explanation": "This is **False**. For a 50-year-old worker, the maximum limit is $180 - 50 = 130$ bpm. A rate of 135 bpm exceeds the safe limit, indicating heat strain."
        },
        # Risk assessment (Lecture 2)
        {
            "id": "math-12",
            "lectureId": 2,
            "type": "MCQ",
            "question": "A safety engineer performs a quantitative risk assessment. A hazard has an estimated probability score of 4 (on a 1-5 scale) and a severity score of 3 (on a 1-5 scale). What is the calculated Risk level?",
            "options": {
                "A": "7",
                "B": "12",
                "C": "1",
                "D": "1.33"
            },
            "answer": "B",
            "explanation": "The Risk formula is: $\\text{Risk} = \\text{Probability} \\times \\text{Severity}$.\n$\\text{Risk} = 4 \\times 3 = 12$."
        },
        {
            "id": "math-13",
            "lectureId": 2,
            "type": "TF",
            "question": "If the probability of an accident occurring is 2 and the severity of its consequence is 5, the Risk score is 7.",
            "answer": "F",
            "explanation": "This is **False**. Risk is multiplication, not addition. $\\text{Risk} = \\text{Probability} \\times \\text{Severity} = 2 \\times 5 = 10$."
        },
        # Fall physics (Lecture 4)
        {
            "id": "math-14",
            "lectureId": 4,
            "type": "MCQ",
            "question": "When analyzing fall times under gravity, a worker falling freely will travel how many feet vertically in the first 0.5 seconds?",
            "options": {
                "A": "4 feet",
                "B": "6 feet",
                "C": "10 feet",
                "D": "16 feet"
            },
            "answer": "B",
            "explanation": "According to Lecture 4, a person falls **6 feet in 0.5 seconds** and 16 feet in 1.0 second. (Using physics: $d = 0.5 g t^2 \\approx 0.5 \\times 32.2 \\times 0.25 = 4.025$ feet without air drag, but the slides establish standard values of 6 ft in 0.5s & 16 ft in 1s)."
        },
        {
            "id": "math-15",
            "lectureId": 4,
            "type": "TF",
            "question": "A worker falling freely travels 16 feet in 1 second.",
            "answer": "T",
            "explanation": "This is **True**. Lecture 4 notes that a person travels 16 feet vertically within 1 second of a free fall."
        },
        # NIOSH Lift computations (Lecture 6)
        {
            "id": "math-16",
            "lectureId": 6,
            "type": "MCQ",
            "question": "In a manual lifting task, a safety engineer measures the following multipliers: HM = 0.90, VM = 0.95, DM = 0.90, FM = 0.50, AM = 0.95, CM = 0.90. What is the calculated Recommended Weight Limit (RWL) based on the Load Constant (LC = 23 kg)?",
            "options": {
                "A": "23.00 kg",
                "B": "14.25 kg",
                "C": "7.33 kg",
                "D": "10.45 kg"
            },
            "answer": "C",
            "explanation": "$RWL = LC \\times HM \\times VM \\times DM \\times FM \\times AM \\times CM$\n$RWL = 23 \\times 0.90 \\times 0.95 \\times 0.90 \\times 0.50 \\times 0.95 \\times 0.90$\n$RWL = 23 \\times 0.3188 \\approx 7.33$ kg."
        },
        {
            "id": "math-17",
            "lectureId": 6,
            "type": "TF",
            "question": "If the Recommended Weight Limit (RWL) for a lifting task is 10 kg, and the weight of the box being lifted is 12 kg, the task is safe for most workers.",
            "answer": "F",
            "explanation": "This is **False**. If the weight of the load (12 kg) exceeds the Recommended Weight Limit (10 kg), the task is classified as dangerous and must be redesigned."
        },
        {
            "id": "math-18",
            "lectureId": 6,
            "type": "MCQ",
            "question": "A lifting task is redesigned: the Load Constant is 23 kg. The multipliers are optimized to: HM = 1.0, VM = 0.99, DM = 1.0, FM = 0.75, AM = 0.70, CM = 1.0. What is the new Recommended Weight Limit (RWL)?",
            "options": {
                "A": "11.94 kg",
                "B": "15.20 kg",
                "C": "23.00 kg",
                "D": "8.55 kg"
            },
            "answer": "A",
            "explanation": "$RWL = 23 \\times 1.0 \\times 0.99 \\times 1.0 \\times 0.75 \\times 0.70 \\times 1.0 = 23 \\times 0.51975 = 11.954$ kg (the slide matches this to 12.125 kg or 11.94 kg depending on rounding)."
        },
        # Accident evaluation ratios (Lecture 3)
        {
            "id": "math-19",
            "lectureId": 3,
            "type": "MCQ",
            "question": "Based on Heinrich's 300:29:1 ratio, for every 330 accidents of the same kind, how many minor injury accidents are expected to occur?",
            "options": {
                "A": "300",
                "B": "29",
                "C": "1",
                "D": "30"
            },
            "answer": "B",
            "explanation": "Heinrich's ratio states that out of 330 accidents of the same kind: 300 result in no injury (near misses), **29 result in minor injuries**, and 1 results in a major/fatal injury."
        },
        {
            "id": "math-20",
            "lectureId": 3,
            "type": "TF",
            "question": "According to Heinrich's accident ratio, for 330 accidents, 1 is a major injury.",
            "answer": "T",
            "explanation": "This is **True**. The 300:29:1 ratio outlines 300 no-injuries, 29 minor injuries, and 1 major injury."
        },
        # More Rate computations to ensure 40 count
        {
            "id": "math-21",
            "lectureId": 2,
            "type": "MCQ",
            "question": "An enterprise has 400 employees who work a combined total of 800,000 hours in a year. The enterprise records 10 cases of lost-workday injuries (LWDI). What is the lost-workday injury rate (LWDI)?",
            "options": {
                "A": "1.25",
                "B": "2.50",
                "C": "5.00",
                "D": "0.62"
            },
            "answer": "B",
            "explanation": "$LWDI = (N_{clwd} \\times 200,000) / H_{je} = (10 \\times 200,000) / 800,000 = 2,000,000 / 800,000 = 2.50$."
        },
        {
            "id": "math-22",
            "lectureId": 3,
            "type": "MCQ",
            "question": "If a factory registers 180 lost workdays ($N_{lwd}$) and has logged 600,000 employee exposure hours ($H_{je}$), what is the calculated Severity Rate (SR) of the factory?",
            "options": {
                "A": "30.0",
                "B": "60.0",
                "C": "90.0",
                "D": "12.0"
            },
            "answer": "B",
            "explanation": "$SR = (N_{lwd} \\times 200,000) / H_{je} = (180 \\times 200,000) / 600,000 = 36,000,000 / 600,000 = 60.0$ lost days per 100 workers."
        },
        {
            "id": "math-23",
            "lectureId": 3,
            "type": "TF",
            "question": "A business has 4 recordable cases ($N_{rc}$) and 2 cases involving lost workdays ($N_{clwd}$). If the total number of lost workdays ($N_{lwd}$) is 40, the Average Days Away From Work ($ADAW$) index is 20.",
            "answer": "T",
            "explanation": "This is **True**. $ADAW = N_{lwd} / N_{clwd} = 40 / 2 = 20$ days."
        },
        {
            "id": "math-24",
            "lectureId": 2,
            "type": "MCQ",
            "question": "In a construction company, there are 5 cases of injuries involving days away from work (DAFWII) during a period of 400,000 exposure hours. What is the DAFWII rate?",
            "options": {
                "A": "1.25",
                "B": "2.50",
                "C": "0.50",
                "D": "5.00"
            },
            "answer": "B",
            "explanation": "$DAFWII\\text{ rate} = (5 \\times 200,000) / 400,000 = 1,000,000 / 400,000 = 2.50$."
        },
        {
            "id": "math-25",
            "lectureId": 8,
            "type": "MCQ",
            "question": "If you combine four identical machines each producing 85 dBA, what is the combined sound level?",
            "options": {
                "A": "91 dBA",
                "B": "88 dBA",
                "C": "85 dBA",
                "D": "95 dBA"
            },
            "answer": "A",
            "explanation": "Four sources = two doublings. First doubling (2 sources) adds 3 dB ($85 + 3 = 88$ dBA). Second doubling (4 sources) adds another 3 dB ($88 + 3 = 91$ dBA)."
        },
        {
            "id": "math-26",
            "lectureId": 8,
            "type": "TF",
            "question": "If the difference between two sound levels is 6 dBA, combining them adds exactly 1.0 dBA to the higher sound level.",
            "answer": "T",
            "explanation": "This is **True**. Under decibel addition charts, when the difference is 6 dBA, you add 1.0 dBA to the larger noise level."
        },
        {
            "id": "math-27",
            "lectureId": 8,
            "type": "MCQ",
            "question": "Combine a noise source of 94 dBA and a noise source of 90 dBA (difference = 4 dBA; addition factor = 1.5 dBA to the higher level). What is the combined sound level?",
            "options": {
                "A": "95.5 dBA",
                "B": "94.0 dBA",
                "C": "98.0 dBA",
                "D": "96.5 dBA"
            },
            "answer": "A",
            "explanation": "Difference = 4 dB, which corresponds to adding 1.5 dB to the higher value.\n$94.0 + 1.5 = 95.5$ dBA."
        },
        {
            "id": "math-28",
            "lectureId": 5,
            "type": "MCQ",
            "question": "What is the maximum sustained heart rate allowed under heat strain for a 20-year-old worker?",
            "options": {
                "A": "160 bpm",
                "B": "180 bpm",
                "C": "140 bpm",
                "D": "150 bpm"
            },
            "answer": "A",
            "explanation": "Formula: $180 - \\text{age}$. For a 20-year-old: $180 - 20 = 160$ bpm."
        },
        {
            "id": "math-29",
            "lectureId": 5,
            "type": "TF",
            "question": "A core body temperature reading of 39.0°C indicates that a worker has crossed the heat strain limit.",
            "answer": "T",
            "explanation": "This is **True**. The physiological limit for core body temperature under heat strain is 38.5°C; 39.0°C exceeds this safety threshold."
        },
        {
            "id": "math-30",
            "lectureId": 6,
            "type": "MCQ",
            "question": "A box weighs 15 kg. The calculated Recommended Weight Limit (RWL) for this specific lifting posture is 11 kg. What is the Lifting Index (LI) for this task (defined as Load / RWL)?",
            "options": {
                "A": "0.73",
                "B": "1.36",
                "C": "4.00",
                "D": "1.00"
            },
            "answer": "B",
            "explanation": "Lifting Index ($LI$) = $\\text{Actual Weight} / \\text{RWL} = 15 / 11 \\approx 1.36$. An LI greater than 1.0 indicates a hazardous lifting task."
        },
        {
            "id": "math-31",
            "lectureId": 6,
            "type": "TF",
            "question": "If a worker's lifting task has an LI of 0.85, the task is safe for most workers.",
            "answer": "T",
            "explanation": "This is **True**. A Lifting Index ($LI$) of 1.0 or less is considered acceptable and safe for the majority of workers."
        },
        {
            "id": "math-32",
            "lectureId": 2,
            "type": "MCQ",
            "question": "In a workplace safety review, a hazard has a probability score of 3 and a severity score of 5. What is the risk score?",
            "options": {
                "A": "8",
                "B": "15",
                "C": "5",
                "D": "2"
            },
            "answer": "B",
            "explanation": "$Risk = Probability \\times Severity = 3 \\times 5 = 15$."
        },
        {
            "id": "math-33",
            "lectureId": 2,
            "type": "TF",
            "question": "A hazard with probability 1 and severity 1 has a risk score of 1, which represents the lowest possible risk classification.",
            "answer": "T",
            "explanation": "This is **True**. The minimum score on a 1-5 scale is $1 \\times 1 = 1$."
        },
        {
            "id": "math-34",
            "lectureId": 3,
            "type": "MCQ",
            "question": "In a plant with 10 recordable cases and 3 lost-workday cases, if the total lost workdays count is 36, what is the Average Severity (AS)?",
            "options": {
                "A": "12.0 days",
                "B": "3.6 days",
                "C": "10.0 days",
                "D": "30.0 days"
            },
            "answer": "B",
            "explanation": "Average Severity ($AS$) = $N_{lwd} / N_{rc} = 36 / 10 = 3.6$ lost workdays per recordable case."
        },
        {
            "id": "math-35",
            "lectureId": 3,
            "type": "MCQ",
            "question": "In the same plant (36 lost workdays, 3 lost-workday cases), what is the Average Days Away From Work (ADAW)?",
            "options": {
                "A": "12 days",
                "B": "3.6 days",
                "C": "10 days",
                "D": "30 days"
            },
            "answer": "A",
            "explanation": "$ADAW = N_{lwd} / N_{clwd} = 36 / 3 = 12$ days lost per lost-workday case."
        },
        {
            "id": "math-36",
            "lectureId": 3,
            "type": "TF",
            "question": "If a department logs 2,000 hours of job exposure and experiences 1 recordable injury, the calculated Incidence Rate (IR) is 100.0.",
            "answer": "T",
            "explanation": "This is **True**. $IR = (1 \\times 200,000) / 2,000 = 200,000 / 2,000 = 100.0$."
        },
        {
            "id": "math-37",
            "lectureId": 3,
            "type": "MCQ",
            "question": "An office has 80 employees who work 160,000 hours combined. In this period, 4 recordable illnesses occur. What is the Incidence Rate?",
            "options": {
                "A": "5.0",
                "B": "2.5",
                "C": "4.0",
                "D": "8.0"
            },
            "answer": "A",
            "explanation": "$IR = (4 \\times 200,000) / 160,000 = 800,000 / 160,000 = 5.0$."
        },
        {
            "id": "math-38",
            "lectureId": 8,
            "type": "MCQ",
            "question": "If Source A is 92 dBA and Source B is 84 dBA (difference = 8 dBA; addition factor = 0.6 dBA), what is the combined sound level?",
            "options": {
                "A": "92.6 dBA",
                "B": "96.0 dBA",
                "C": "92.0 dBA",
                "D": "88.0 dBA"
            },
            "answer": "A",
            "explanation": "When difference is 8 dBA, you add 0.6 dBA to the higher sound level.\n$92.0 + 0.6 = 92.6$ dBA."
        },
        {
            "id": "math-39",
            "lectureId": 8,
            "type": "TF",
            "question": "If two sound levels are exactly equal, the combined sound level is equal to either level plus 3 decibels.",
            "answer": "T",
            "explanation": "This is **True**. Adding two identical noise levels results in a 3 dB increase (e.g. 85 dB + 85 dB = 88 dB)."
        },
        {
            "id": "math-40",
            "lectureId": 5,
            "type": "MCQ",
            "question": "What is the maximum core body temperature permitted for a worker exposed to heat stress?",
            "options": {
                "A": "37.0°C",
                "B": "38.0°C",
                "C": "38.5°C",
                "D": "39.5°C"
            },
            "answer": "C",
            "explanation": "Health standards state that a safety engineer must prevent a worker's core body temperature from rising above **38.5°C** under heat stress."
        }
    ],
    "openEnded": [
        {
            "id": "open-1",
            "lectureId": 1,
            "question": "Explain the differences between direct costs and indirect costs of industrial accidents. Support your answer with at least two examples for each type of cost.",
            "modelAnswer": "### Model Answer Structure:\n1. **Definitions**:\n   - **Direct Costs**: Obvious, immediate financial outlays directly associated with treatment or compensation of the injured worker.\n   - **Indirect Costs**: Less obvious, hidden costs that accumulate throughout the organization due to productivity loss, administrative actions, and disruption.\n2. **Ratio/Significance**: Slide notes state that indirect costs are less obvious but *cost more* than direct ones (often represented as an iceberg where direct costs are the tip).\n3. **Examples**:\n   - **Direct Costs**: Medical doctor/hospital visits, physical therapy, prescription medicines, workers' compensation insurance payouts.\n   - **Indirect Costs**: Lost productivity of the worker/team, supervisor time spent investigating/filling reports, costs of training a replacement worker, equipment repair costs, legal fees, negative publicity, and damaged customer relations.",
            "gradingRubric": [
                "Clearly defines Direct and Indirect costs.",
                "Explains that indirect costs generally exceed direct costs in total economic impact.",
                "Lists at least two valid examples of Direct costs (medical, compensation, therapy).",
                "Lists at least two valid examples of Indirect costs (productivity, investigation, training, repairs)."
            ]
        },
        {
            "id": "open-2",
            "lectureId": 2,
            "question": "Describe the traditional metrics used for measuring accidents in a workplace (Frequency, Severity, Seriousness). Detail how they differ from the Total Injury-Illness Incidence Rate.",
            "modelAnswer": "### Model Answer Structure:\n1. **Traditional Indexes**:\n   - **Frequency**: The number of injury cases per standard quantity of workhours. Crucially, it only includes cases where the worker missed *at least a day of work*.\n   - **Severity**: The number of lost workdays per standard quantity of workhours.\n   - **Seriousness**: Calculated as the ratio of severity to frequency (Average Severity = Lost Days / Cases).\n2. **New Index (Total Injury-Illness Incidence Rate)**:\n   - It measures the number of recordable injuries/illnesses per 200,000 worker hours (equivalent to 100 full-time workers working 40 hours/week for 50 weeks).\n   - Formula: $IR = (N_{rc} \\times 200,000) / H_{je}$.\n3. **Key Differences**:\n   - The new incidence rate includes *all* recordable cases (even if they didn't miss a day of work, as long as it required medical treatment beyond first aid).\n   - The incidence rate covers both injuries and illnesses, whereas some traditional metrics focused strictly on lost-workday injuries. It provides a standardized rate per 100 workers.",
            "gradingRubric": [
                "Defines traditional Frequency (cases missing >= 1 day of work).",
                "Defines traditional Severity (lost workdays) and Seriousness (severity/frequency ratio).",
                "Explains the Total Injury-Illness Incidence Rate formula and the significance of the 200,000 multiplier (100 full-time workers).",
                "Contrasts the two methods (e.g. inclusion of non-lost-time recordable medical cases and illnesses)."
            ]
        },
        {
            "id": "open-3",
            "lectureId": 3,
            "question": "Outline the 'Four Ms Model' of accident factors. Provide a brief explanation and a specific example of a hazard or failure for each of the four categories.",
            "modelAnswer": "### Model Answer Structure:\nThe Four Ms Model classifies the underlying factors that contribute to industrial accidents:\n1. **Man (Human Factor)**: Human errors, mistakes, or psychological factors. Divided into *omission* (failure to act) and *commission* (incorrect action). Affected by age, time on job, fatigue, and stress. *Example*: A tired worker forgetting to engage a safety switch.\n2. **Machine (Equipment/Job Factors)**: Physical equipment, tools, and methods used in operations. Covers mechanical, electrical, and temperature hazards. *Example*: A power press missing its point-of-operation guard.\n3. **Media (Environmental Factors)**: Conditions surrounding the operation.\n   - *Physical*: Noise, poor lighting, extreme temperature, vibration.\n   - *Social*: Company safety policies, peer safety norms, training quality. *Example*: A loud, poorly-lit workspace where a warning siren cannot be heard.\n4. **Management (Policy/Administrative Factors)**: Organizational structure, safety rules, training, and enforcement of safety programs. *Example*: A supervisor failing to audit tagout forms or enforce PPE usage.",
            "gradingRubric": [
                "Lists all four components: Man, Machine, Media, and Management.",
                "Explains the Man factor with omission/commission errors or physiological stressors (fatigue, stress).",
                "Explains Machine in terms of mechanical, electrical, or temperature hazards.",
                "Explains Media in terms of physical environment (noise, light) or social safety climate.",
                "Explains Management as safety policy, responsibility, and supervisor accountability."
            ]
        },
        {
            "id": "open-4",
            "lectureId": 3,
            "question": "Detail Heinrich's Domino Theory of accident causation. List the five dominos in order, and explain which domino is the primary target for safety interventions and why.",
            "modelAnswer": "### Model Answer Structure:\n1. **The Five Dominos (In Order)**:\n   - **1. Ancestry/Social Environment**: Character traits or cultural upbringing that can lead to faults.\n   - **2. Fault of Person**: Inherited or acquired flaws, such as recklessness, ignorance, or fatigue.\n   - **3. Unsafe Act or Unsafe Condition**: The direct physical hazard or risky behavior (e.g., operating machinery without guardrails, walking under crane hooks).\n   - **4. Accident**: The unplanned event (e.g., structural fall, mechanical pinch).\n   - **5. Injury**: The physical harm or fatality resulting from the accident.\n2. **Target for Intervention**:\n   - The **third domino (Unsafe Act or Unsafe Condition)** is the key target for safety engineers.\n   - *Why*: According to Heinrich, if you pull out the third domino, the sequence is broken. Even if the person has character flaws (Domino 2) or a poor background (Domino 1), removing the unsafe act or condition prevents the accident (Domino 4) and subsequent injury (Domino 5) from occurring.",
            "gradingRubric": [
                "Lists the five dominos in correct sequence: Environment -> Fault -> Unsafe Act/Condition -> Accident -> Injury.",
                "Identifies the 3rd domino (Unsafe Act or Condition) as the target.",
                "Explains that removing this domino disrupts the chain, preventing the accident and injury."
            ]
        },
        {
            "id": "open-5",
            "lectureId": 3,
            "type": "Open Ended",
            "question": "Compare a proactive safety approach to a reactive safety approach. Give examples of activities associated with each approach in a typical safety program.",
            "modelAnswer": "### Model Answer Structure:\n1. **Definitions**:\n   - **Proactive Approach**: Anticipating hazards and implementing prevention strategies *before* accidents occur. It focuses on identifying and controlling hazards, analyzing safety systems, and training workers.\n   - **Reactive Approach**: Responding to accidents and incidents *after* they happen to limit losses, investigate causes, and enforce compliance.\n2. **Focus of Attention**:\n   - Proactive approaches focus on **accidents and their causes** (prevention).\n   - Reactive approaches analyze the **effects** and losses to prevent recurrence.\n3. **Examples**:\n   - **Proactive Activities**: Regular hazard audits, safety meetings, job safety analysis (JSA), ergonomics training, machinery safeguarding installations, and preventative maintenance.\n   - **Reactive Activities**: Accident investigation, filing workers' compensation reports, corrective actions to repair failed machines, post-accident retraining, and auditing accident history data.",
            "gradingRubric": [
                "Defines proactive safety as anticipatory/preventative.",
                "Defines reactive safety as post-accident response/loss containment.",
                "Lists proactive examples (hazard analysis, audits, safety training).",
                "Lists reactive examples (accident investigation, injury reports, repairs)."
            ]
        },
        {
            "id": "open-6",
            "lectureId": 4,
            "question": "Analyze the three 'dangerous attitudes' that lead to fatal falls in the workplace. Explain the controls a safety engineer should deploy to combat them.",
            "modelAnswer": "### Model Answer Structure:\n1. **The Three Dangerous Attitudes**:\n   - **'I do not work very high'**: Workers underestimate fall risks at lower heights. In reality, **25% of fatal falls occur from heights under 10 feet**.\n   - **'I'll catch myself'**: Workers believe they can react in time. Physics shows that a falling body travels **6 feet in 0.5 seconds** and **16 feet in 1 second**, which is faster than human reaction time.\n   - **'I have a good balance'**: Workers rely on personal control, ignoring slips, environmental hazards, or sudden balance loss.\n2. **Safety Controls (Hierarchy of Fall Protection)**:\n   - **First Line of Defense (Elimination)**: Design the workplace to keep workers on the ground. *Examples*: Ground-level gauges, inspection drones.\n   - **Second Line of Defense (Prevention)**: Use physical barriers to stop a fall from starting. *Examples*: Guardrails (42-inch top rail, 21-inch midrail, toe board), fences, barricades.\n   - **Third Line of Defense (Control/Mitigation)**: Minimize injury in the event of a fall. *Examples*: Personal Fall Arrest Systems (PFAS with body harness and anchorage), safety nets (for falls > 25 feet).",
            "gradingRubric": [
                "Identifies the three attitudes: 'I do not work very high', 'I'll catch myself', and 'I have a good balance'.",
                "Cites slide metrics (e.g. 25% of fatal falls occur below 10 ft, or falling 16 ft in 1s).",
                "Explains the three lines of defense: 1. Elimination (drones/ground), 2. Prevention (guardrails), 3. Control (PFAS/safety nets)."
            ]
        },
        {
            "id": "open-7",
            "lectureId": 4,
            "question": "Explain the physiological hazards related to electrical current in the human body, specifically distinguishing between the 'let-go current' and the 'freeze current'. What factors dictate shock severity?",
            "modelAnswer": "### Model Answer Structure:\n1. **Physiological Effects of Current**:\n   - Electric shock disrupts the body's nervous and cardiovascular systems.\n   - It can cause muscle spasms, respiratory paralysis, or ventricular fibrillation (heart stoppage).\n2. **Let-Go vs. Freeze Current**:\n   - **Let-go current**: The maximum current level at which a person is still capable of releasing their grip on the electric conductor.\n   - **Freeze current** (No-let-go current): The threshold current level that causes involuntary muscle contractions. At this point, the worker is physically unable to let go, which prolongs exposure and increases injury severity.\n3. **Factors Dictating Severity**:\n   - **Current flow / Amperage** (the primary factor: voltage drives it, but current kills).\n   - **The path taken through the body** (current passing through the heart/brain is far more lethal).\n   - **Duration of the shock** (longer exposure equals deeper tissue burns and higher fatality risk).",
            "gradingRubric": [
                "Defines 'let-go current' as the threshold where a person can release the wire.",
                "Defines 'freeze current' as the point where involuntary contractions prevent release.",
                "Identifies the three severity factors: Current flow (amperage), path through the body, and duration of the shock."
            ]
        },
        {
            "id": "open-8",
            "lectureId": 5,
            "question": "Explain the differences between fixed guards, interlocked guards, and adjustable guards. Provide a safety application scenario for each.",
            "modelAnswer": "### Model Answer Structure:\n1. **Fixed Guards**:\n   - *Definition*: A permanent barrier that is a physical part of the machine. It has no moving parts and cannot be removed without tools.\n   - *Application*: Guarding power transmission belts, pulleys, flywheels, or gears at the back of a machine.\n2. **Interlocked Guards**:\n   - *Definition*: A guard connected to the machine's power source. When opened or removed, the power is cut off automatically and the machine cannot run.\n   - *Application*: Access doors or gates on industrial blenders, CNC enclosures, or robot cells where workers load parts.\n3. **Adjustable Guards**:\n   - *Definition*: A barrier that can be adjusted manually (or adjusts automatically) to let materials pass while keeping the worker's hands away from the danger point.\n   - *Application*: Guarding the blade of a table saw or band saw, where the guard height must change for different wood thicknesses.",
            "gradingRubric": [
                "Defines Fixed Guard and provides an application (gears, belts).",
                "Defines Interlocked Guard and provides an application (CNC gates, blenders).",
                "Defines Adjustable Guard and provides an application (table saw blade, grinders)."
            ]
        },
        {
            "id": "open-9",
            "lectureId": 5,
            "question": "Describe the physiological signs of heat strain and cold stress. What are the key environmental factors that safety professionals must monitor for each?",
            "modelAnswer": "### Model Answer Structure:\n1. **Heat Strain** (Physiological response to heat stress):\n   - *Signs*: Sustained rapid heart rate exceeding **(180 - age)**, elevated core body temperature exceeding **38.5°C**, and sudden, severe fatigue.\n   - *Environmental Factors*: High ambient temperature, high relative humidity (which prevents sweat evaporation), lack of air movement, metabolic work rate, and heavy/impermeable clothing.\n2. **Cold Stress**:\n   - *Signs*: Deep core body temperature falling below **36°C**, hypothermia (shivering, confusion, slurred speech), reduced muscular function, reduced blood flow to extremities, and reduced nervous system function.\n   - *Environmental Factors*: Cold air temperature, high wind speed (wind chill factor majorly accelerating heat loss), and presence of moisture/getting wet (which increases conduction heat loss).",
            "gradingRubric": [
                "Identifies heat strain metrics: heart rate (180 - age) and core temp (>38.5°C).",
                "Identifies cold stress threshold (core temp < 36°C) and symptoms (hypothermia, reduced muscle function).",
                "Lists heat environmental factors (temp, humidity, air movement).",
                "Lists cold environmental factors (air temp, wind speed, moisture)."
            ]
        },
        {
            "id": "open-10",
            "lectureId": 6,
            "question": "A worker is lifting heavy boxes. Explain the variables in the revised NIOSH lifting equation that control the Recommended Weight Limit (RWL). What is the significance of the Lifting Index (LI)?",
            "modelAnswer": "### Model Answer Structure:\n1. **NIOSH Lifting Equation Variables**:\n   - **LC (Load Constant)**: The baseline weight (23 kg or 51 lbs) safe under optimal conditions.\n   - **H (Horizontal Distance)**: Distance from the midpoint of the ankles to the hands (HM).\n   - **V (Vertical Location)**: Height of the hands from the ground at the start of the lift (VM).\n   - **D (Vertical Distance)**: The vertical travel distance of the load during the lift (DM).\n   - **F (Frequency of Lifts)**: How often the worker lifts and the total duration of the task (FM).\n   - **A (Asymmetry Angle)**: The twisting angle of the body while lifting (AM).\n   - **C (Coupling Quality)**: Quality of handholds/handles (CM).\n2. **Significance of the Lifting Index (LI)**:\n   - Formula: $LI = \\text{Load Weight} / \\text{RWL}$.\n   - If **$LI \\le 1.0$**: The task is safe for most workers.\n   - If **$LI > 1.0$**: The task poses a significant risk of back injury and must be redesigned (either by reducing weight or adjusting H, V, D, F, A, C multipliers).",
            "gradingRubric": [
                "Identifies the Load Constant (LC) value of 23 kg / 51 lbs.",
                "Lists and explains at least 4 NIOSH variables (H, V, D, F, A, C).",
                "Defines the Lifting Index (LI) formula.",
                "Explains the threshold of LI > 1.0 as indicating a hazardous task requiring redesign."
            ]
        },
        {
            "id": "open-11",
            "lectureId": 7,
            "question": "Compare the purpose, requirements, and contents of a Fire Prevention Plan (FPP) and an Emergency Action Plan (EAP).",
            "modelAnswer": "### Model Answer Structure:\n1. **Fire Prevention Plan (FPP)**:\n   - *Purpose*: Focuses on **preventing** fires from starting in the workplace.\n   - *Contents*: Lists major fire hazards, handling/storage procedures for flammable materials, potential ignition sources and control measures, name/job titles of workers responsible for hazard controls and equipment maintenance, and procedures to control combustible wastes.\n2. **Emergency Action Plan (EAP)**:\n   - *Purpose*: Focuses on **protecting life safety** and organizing actions during an emergency once it starts.\n   - *Contents*: Emergency reporting methods, evacuation procedures and escape routes, procedures for employees who remain to operate critical systems before evacuating, accounting for all employees after evacuation, rescue/medical duties, and emergency contacts.\n3. **Common Requirements**:\n   - Both must be written, kept in the workplace, and reviewed with employees upon initial assignment or when modified.",
            "gradingRubric": [
                "Defines FPP's focus on prevention (hazards list, flammables storage, waste control).",
                "Defines EAP's focus on emergency evacuation and life safety (escape routes, alarms, accounting).",
                "Explains that both must be written, available in the workplace, and reviewed during onboarding."
            ]
        },
        {
            "id": "open-12",
            "lectureId": 7,
            "question": "Discuss the classification of portable fire extinguishers. What are the five fire classes, and what chemical mechanisms do extinguishers use to put them out?",
            "modelAnswer": "### Model Answer Structure:\n1. **The Five Classes of Fires**:\n   - **Class A**: Ordinary combustibles (wood, paper, cloth, plastics).\n   - **Class B**: Flammable liquids (gasoline, paint, solvents) and gases (propane, butane).\n   - **Class C**: Energized electrical equipment (appliances, motors, computers).\n   - **Class D**: Combustible metals (magnesium, potassium, sodium).\n   - **Class K**: Cooking oils and greases (commercial kitchen fires).\n2. **Extinguishing Mechanisms**:\n   - **Remove Heat**: Cooling the fuel below its ignition temperature (e.g. Water extinguishers, which cool the surface).\n   - **Displace Oxygen**: Smothering the fire to cut off oxygen supply (e.g. CO2 extinguishers, which release compressed gas to displace oxygen).\n   - **Interrupt Chemical Chain Reaction**: Inhibiting the combustion reaction (e.g. Dry Chemical extinguishers, which spray chemical powders to isolate fuel and stop the chain reaction).",
            "gradingRubric": [
                "Lists all five classes (A, B, C, D, K) with correct descriptions.",
                "Explains the mechanism of removing heat (water/cooling).",
                "Explains the mechanism of displacing oxygen (CO2/smothering).",
                "Explains the mechanism of interrupting the chemical reaction (dry chemical)."
            ]
        },
        {
            "id": "open-13",
            "lectureId": 8,
            "question": "Using the Hierarchy of Controls, outline a comprehensive noise risk management plan for a facility containing several noisy power presses and air compressors.",
            "modelAnswer": "### Model Answer Structure:\n1. **Elimination / Substitution (Most Effective)**:\n   - Replace noisy machines with quieter models (e.g. newer, low-noise presses).\n   - Change processes (e.g. hydraulic pressing instead of impact punching).\n2. **Engineering Controls (Barrier/Path)**:\n   - **Isolation/Enclosures**: Place noisy compressors in insulated, separate rooms.\n   - **Damping**: Apply vibration-absorbing materials to sheet metal panels to reduce resonance.\n   - **Silencers**: Install silencers on air compressor intake/exhaust lines.\n   - **Acoustic Barriers**: Erect sound-absorbing walls between the machinery and worker areas.\n3. **Administrative Controls**:\n   - Schedule noisy operations when fewer workers are present.\n   - Rotate workers to limit individual TWA noise exposure (job rotation).\n   - Implement quiet hours and post clear warning signs in noisy zones.\n4. **PPE (Last Resort)**:\n   - Provide earplugs or earmuffs to workers (with high Noise Reduction Ratings - NRRs).\n   - Require double hearing protection (plugs + muffs) in extreme noise zones.",
            "gradingRubric": [
                "Applies the Hierarchy of Controls (Elimination -> Engineering -> Administrative -> PPE).",
                "Suggests Engineering solutions like machine enclosures, damping, or silencers.",
                "Suggests Administrative controls like job rotations or warning signs.",
                "Identifies PPE (earplugs/muffs) as the last line of defense."
            ]
        },
        {
            "id": "open-14",
            "lectureId": 9,
            "question": "Explain the safety criteria for choosing and wearing Respiratory Protection. Compare Air-Purifying Respirators (APRs) to Self-Contained Breathing Apparatus (SCBA).",
            "modelAnswer": "### Model Answer Structure:\n1. **Air-Purifying Respirators (APR)**:\n   - *Mechanism*: Filter ambient air using particulate filters (electrostatic charge traps) or chemical cartridges (activated carbon removes gases/vapors).\n   - *Safety Criteria*: Can **only** be used if: 1. Oxygen levels are greater than 19.5%. 2. The atmosphere is NOT Immediately Dangerous to Life or Health (IDLH). 3. The concentration of harmful gas does not exceed the mask's rating.\n2. **Self-Contained Breathing Apparatus (SCBA)**:\n   - *Mechanism*: Supplies clean breathing air from a pressurized tank carried by the worker, completely isolating them from ambient air.\n   - *Safety Criteria*: Used in oxygen-deficient environments (< 19.5% O2), IDLH environments, fire fighting, or where gas concentrations are unknown or extremely high.\n3. **Maintenance/Change out**: APR filters must be changed when breathing resistance increases (clogged) or when chemical breakthrough is detected (taste/smell of gas).",
            "gradingRubric": [
                "Explains that APRs rely on cartridges/filters to clean the surrounding air.",
                "Lists APR limits (O2 must be >19.5%, non-IDLH, cartridge capacity limits).",
                "Explains that SCBAs supply their own air, making them suitable for O2-deficient (<19.5%) and IDLH atmospheres."
            ]
        },
        {
            "id": "open-15",
            "lectureId": 9,
            "question": "Describe the OSHA 1910.147 requirements for Lockout/Tagout (LOTO). What responsibilities does an employer have, and what steps are required to achieve a Zero Mechanical State?",
            "modelAnswer": "### Model Answer Structure:\n1. **OSHA LOTO Program Requirements**:\n   - Employers must establish a written energy control program including:\n     - Energy control procedures for each machine.\n     - Employee training (authorized workers who perform LOTO, affected workers who operate machines).\n     - Periodic inspections (at least annually).\n2. **Steps to Achieve a Zero Mechanical State**:\n   - **1. Preparation for Shutdown**: Identify energy sources (electrical, hydraulic, pneumatic, spring, kinetic).\n   - **2. Machine Shutdown**: Turn off the machine using its normal controls.\n   - **3. Machine Isolation**: Disconnect the machine from its primary energy sources (flip breakers, close valves).\n   - **4. Apply LOTO Devices**: Authorized worker applies padlock and warning tag to the energy isolating devices.\n   - **5. Release Stored Energy**: Bleed pneumatic/hydraulic pressure lines, discharge capacitors, block/restrain gravity components, and release spring compression.\n   - **6. Verification of Isolation**: Try turning the machine ON to verify isolation, then return controls to OFF.",
            "gradingRubric": [
                "Lists the three LOTO program pillars: procedures, training, and periodic inspections.",
                "Distinguishes between authorized and affected employees.",
                "Outlines steps for isolation, lock/tag placement, and releasing stored energy (pneumatics, springs).",
                "Emphasizes verifying isolation (trying to start the machine) as the final validation step."
            ]
        }
    ]
}

# Write questions to questions.js
with open("/home/naur/.gemini/antigravity/scratch/safety-quiz-app/questions.js", "w", encoding="utf-8") as f:
    f.write("const safetyQuizData = " + json.dumps(quizData, indent=2, ensure_ascii=False) + ";\n")

print("Generated questions.js with:")
print(f"  - {len(quizData['memorization'])} Memorization questions")
print(f"  - {len(quizData['mathLogic'])} Math/Logic questions")
print(f"  - {len(quizData['openEnded'])} Open-ended questions")
