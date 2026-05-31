# -*- coding: utf-8 -*-
import json

# Compile all safety topics and questions
memorization = []
math_logic = []
open_ended = []

# Helper to parse different tuple shapes for TF vs MCQ
def parse_base_list(base_list, start_idx, lecture_id):
    parsed = []
    for i, item in enumerate(base_list):
        q_id = f"mem-{start_idx + i}"
        q_type = item[0]
        q_text = item[1]
        if q_type == "MCQ":
            options = item[2]
            answer = item[3]
            explanation = item[4]
            parsed.append({
                "id": q_id,
                "lectureId": lecture_id,
                "type": "MCQ",
                "question": q_text,
                "options": options,
                "answer": answer,
                "explanation": explanation
            })
        else:
            answer = item[2]
            explanation = item[3]
            parsed.append({
                "id": q_id,
                "lectureId": lecture_id,
                "type": "TF",
                "question": q_text,
                "answer": answer,
                "explanation": explanation
            })
    return parsed

# ==========================================================================
# PART 1: MEMORIZATION QUESTIONS (Factual, 170 Questions)
# ==========================================================================

# 1. Lecture 1 General definitions (Q1-Q20)
mem_base_1 = [
    ("MCQ", "Who is considered the creator of products and processes to satisfy basic needs and enhance everyday lives?", {"A": "Safety officer", "B": "Engineer", "C": "OSHA inspector", "D": "Industrial hygienist"}, "B", "Lecture 1 defines the Engineer as the person who creates products and processes to satisfy the basic needs of food and shelter and enhance everyday lives."),
    ("TF", "Innovation is the application of better solutions through more effective products, processes, services, technologies, and business models.", "T", "Innovation is viewed as the application of better solutions through more effective products, processes, services, technologies, and business models, and is an important part of engineering."),
    ("MCQ", "Which safety term refers to 'the negative consequence (or harm) that might be experienced, such as death, injury, or illness'?", {"A": "Hazard", "B": "Risk", "C": "Danger", "D": "Severity"}, "C", "Danger is the negative consequence (or harm) that might be experienced."),
    ("MCQ", "Which safety term is defined as 'a source or cause of danger'?", {"A": "Risk", "B": "Severity", "C": "Incident", "D": "Hazard"}, "D", "A Hazard is a source or cause of danger (e.g. water can cause drowning)."),
    ("TF", "An accident is a planned and anticipated event sequence that results in positive outcomes.", "F", "An accident is an unintended, unanticipated, and uncontrollable event sequence caused by unsafe acts, unsafe conditions, or both, resulting in undesirable effects."),
    ("MCQ", "Which of the following is categorized as a direct cost of an accident?", {"A": "Accident investigation costs", "B": "Medical bills and doctor visits", "C": "Lost productivity of team", "D": "Training replacement worker"}, "B", "Medical costs (doctor visits, physical therapy, medicine) are direct costs of accidents."),
    ("MCQ", "Which of the following is categorized as an indirect cost of an accident?", {"A": "Supervisor lost time", "B": "Worker's compensation payouts", "C": "Emergency room bills", "D": "Doctor visits"}, "A", "Indirect costs include supervisor lost time, retraining replacement workers, overtime, legal fees, equipment repairs, and negative publicity."),
    ("TF", "Safety management should be improved periodically and not remain static.", "T", "Safety management is a continuous process that should be improved periodically as safety standards evolve."),
    ("MCQ", "Which obligations under safety management address moral and ethical reasons and worker morale?", {"A": "Fiscal obligations", "B": "Social obligations", "C": "Legal obligations", "D": "Administrative obligations"}, "B", "Social obligations address moral and ethical reasons and worker morale."),
    ("MCQ", "Which obligations address worker compensation costs and direct/indirect outlays?", {"A": "Legal obligations", "B": "Social obligations", "C": "Fiscal obligations", "D": "Compliance obligations"}, "C", "Fiscal obligations involve direct and indirect costs of accidents, outlays, savings, and value."),
    ("TF", "Egyptian Labor Law and OSHA standards are examples of social obligations.", "F", "Egyptian Labor Law and OSHA regulations are examples of Legal obligations (laws and regulations enforced by authorities)."),
    ("MCQ", "A forklift operating in a tight aisle is an example of a:", {"A": "Near miss", "B": "Hazard", "C": "Minor injury", "D": "Risk"}, "B", "Operating a forklift in a tight aisle represents a hazard (a source of potential danger)."),
    ("TF", "Accidents happen due to inadequate safety management in the first place, not only failure in equipment.", "T", "Safety studies show that management inadequacies are the root cause, rather than just equipment failure."),
    ("MCQ", "What is the primary action in controlling safety?", {"A": "Fines", "B": "Identifying hazards", "C": "Evacuation", "D": "Hiring supervisors"}, "B", "The primary steps in safety control are: 1. Identify hazards (Knowledge and recognition), 2. Prioritize, and 3. Maintain acceptable level."),
    ("TF", "Hazard elimination is the first and most preferred line of defense.", "T", "The hierarchy prioritizes Hazard Elimination first, followed by Hazard Reduction, and finally Hazard Communication (warnings/PPE)."),
    ("MCQ", "Moving from engineering controls to administrative controls is a form of hazard:", {"A": "Elimination", "B": "Reduction", "C": "Communication", "D": "Obligation"}, "B", "Hazard reduction involves moving from engineering controls to administrative controls and source to path to receiver."),
    ("TF", "Worker morale is considered a legal obligation under safety frameworks.", "F", "Worker morale falls under social, moral, and ethical obligations."),
    ("MCQ", "A forklift driver killed when a heavy product pushes a truck over is classified as a:", {"A": "No injury incident", "B": "Minor injury accident", "C": "Major injury accident", "D": "Near miss"}, "C", "Fatalities represent a Major Injury accident."),
    ("TF", "A forklift hitting a stack and causing it to sway without falling or hurting anyone is a near miss.", "T", "A near miss (or no-injury incident) is an unplanned event that did not result in injury or damage but had the potential to do so."),
    ("MCQ", "The avoidance of industrial accidents that cause injury and fatality is called:", {"A": "Occupational health", "B": "Occupational safety", "C": "Ergonomics", "D": "Loss prevention"}, "B", "Occupational safety focuses on avoiding industrial accidents causing injury and fatality.")
]

memorization.extend(parse_base_list(mem_base_1, 1, 1))

# 2. Lecture 2 Concepts and OSHA (Q21-Q40)
mem_base_2 = [
    ("MCQ", "What does the acronym OSHA stand for?", {"A": "Occupational Safety and Health Administration", "B": "Occupational Standards and Hazard Association", "C": "Organization for Safety and Health Assessment", "D": "Office of Safety and Hazard Audits"}, "A", "OSHA stands for Occupational Safety and Health Administration."),
    ("TF", "OSHA regulations apply to all general industries to maintain safety standards.", "T", "OSHA standards are federal regulations that govern safety and health in general industries."),
    ("MCQ", "Workers' compensation should be awarded according to the:", {"A": "Hourly rate of the worker", "B": "Degree of injury", "C": "Tenure of the employee", "D": "Safety record of supervisor"}, "B", "Workers' compensation is determined by the severity or degree of the injury sustained."),
    ("TF", "Traditional safety indexes include frequency, severity, and seriousness.", "T", "Frequency, severity, and seriousness are traditional measures of occupational accidents."),
    ("MCQ", "Which traditional index tracks lost workdays per standard quantity of workhours?", {"A": "Frequency Index", "B": "Severity Index", "C": "Seriousness Index", "D": "Incidence Rate"}, "B", "Severity Index measures lost workdays per standard quantity of workhours."),
    ("MCQ", "Which traditional index tracks the number of cases per standard quantity of workhours?", {"A": "Severity Index", "B": "Seriousness Index", "C": "Frequency Index", "D": "Incidence Rate"}, "C", "Frequency Index measures cases per standard workhours, counting only cases where a worker missed at least one day."),
    ("TF", "The Seriousness Index is defined as the ratio of frequency to severity.", "F", "Seriousness Index is the ratio of severity to frequency (Average Severity)."),
    ("MCQ", "The total injury-illness incidence rate standardizes metrics based on how many full-time workers?", {"A": "10 workers", "B": "50 workers", "C": "100 workers", "D": "500 workers"}, "C", "The rate is per 100 full-time workers, represented by 200,000 exposure hours (100 workers * 40 hours/week * 50 weeks)."),
    ("TF", "Simple first aid cases are recordable on OSHA forms.", "F", "Recordable injury and illness cases exclude simple first aid treatments."),
    ("MCQ", "Which metric counts recordable injury and illness cases, excluding fatalities?", {"A": "TRC", "B": "LWDI", "C": "DAFWII", "D": "TWA"}, "A", "TRC stands for Total-Recordable-Cases, excluding fatalities."),
    ("TF", "LWDI counts injury cases that involve lost workdays, excluding illnesses and fatalities.", "T", "LWDI (Lost-Workday-case Incidence rate) counts injury cases (excluding illness) involving lost workdays, and excludes fatalities."),
    ("MCQ", "Which index counts injury and illness cases that involve days away from work, excluding fatalities?", {"A": "TRC", "B": "LWDI", "C": "DAFWII", "D": "TWA"}, "C", "DAFWII (Days Away From Work Injury and Illness case rate) counts cases involving days away from work, excluding fatalities."),
    ("TF", "Occupational Health deals with the avoidance of industrial accidents causing injury.", "F", "Occupational Health deals with avoiding diseases and disorders induced by exposures to materials or conditions in the workplace."),
    ("MCQ", "What is the primary formula for quantifying risk?", {"A": "Risk = Hazard / Danger", "B": "Risk = Probability * Severity", "C": "Risk = Frequency / Seriousness", "D": "Risk = Direct Costs + Indirect Costs"}, "B", "Risk is defined as the product of Probability (chance of occurrence) and Severity (harm measure)."),
    ("TF", "Record keeping is critical for safety and health program evaluation.", "T", "Form logging and documentation are essential for safety evaluations and OSHA compliance."),
    ("MCQ", "OSHA was established with a mission to ensure safe work conditions, which has helped reduce fatalities by more than:", {"A": "10%", "B": "30%", "C": "50%", "D": "67%"}, "D", "Workplace fatalities have been reduced by more than 67% since OSHA was created."),
    ("TF", "The multiplier 200,000 in incidence rates represents 100 employees working 2,000 hours per year.", "T", "100 employees * 2,000 hours/year = 200,000 hours, which standardizes rates per 100 workers."),
    ("MCQ", "Avoidance of diseases induced by exposure to materials or conditions in the workplace is the domain of:", {"A": "Occupational Safety", "B": "Occupational Health", "C": "Ergonomics", "D": "Environmental Science"}, "B", "Occupational Health is concerned with preventing occupational diseases and exposures."),
    ("TF", "Probability is a measure of the severity of the harm caused by a hazard.", "F", "Probability is the measure of the chance that a hazard causes harm. Severity is the measure of the harm itself."),
    ("MCQ", "An unplanned, undesired event that adversely affects the completion of a task, without necessarily causing injury, is an:", {"A": "Accident", "B": "Incident", "C": "Illness", "D": "Exposure"}, "B", "This is the definition of an Incident (adversely affects task completion, but no personal injury or property damage).")
]

memorization.extend(parse_base_list(mem_base_2, 21, 2))

# 3. Lecture 3 Programs & Theories (Q41-Q60)
mem_base_3 = [
    ("MCQ", "What are the components of safety commitment in TMC?", {"A": "Time, Money, and Concern", "B": "Training, Management, and Compliance", "C": "Task, Material, and Control", "D": "Testing, Measurement, and Certification"}, "A", "TMC represents Time, Money, and Concern."),
    ("TF", "Accountability means companies should require managers to plan safety and train employees.", "T", "Effective accountability requires safety planning by managers and training for employees."),
    ("MCQ", "What is the direct cause of accidents in the Four Ms model?", {"A": "Machine", "B": "Media", "C": "Man", "D": "Management"}, "C", "The Man category, representing human mistakes, is the direct cause of accidents."),
    ("MCQ", "A worker failing to perform a required safety check is an error of:", {"A": "Commission", "B": "Omission", "C": "Instruction", "D": "Coordination"}, "B", "An error of omission is when a worker fails to take action that is called for."),
    ("TF", "A commission error is when a worker takes action, but it is wrong.", "T", "Commission errors describe incorrect action, whereas omission is failure to act."),
    ("MCQ", "Accident rates show correlation with employee job tenure, increasing during the first:", {"A": "3 months", "B": "1 year", "C": "3 years", "D": "5 years"}, "C", "Accident rates increase during the first three years on the job."),
    ("TF", "Stress reduces the available attention resources, which increases accident rates.", "T", "Stress reduces attention resources, whether the stressors are work-related or personal."),
    ("MCQ", "Which M in the Four Ms model covers environmental factors like noise, lighting, and humidity?", {"A": "Man", "B": "Machine", "C": "Media", "D": "Management"}, "C", "Media covers physical environmental factors (noise, lighting, temp, humidity) and social factors."),
    ("MCQ", "What theory uses five dominos to describe the sequence of events leading to an injury?", {"A": "Four Ms Model", "B": "Domino Theory", "C": "Swiss Cheese Model", "D": "Fishbone Diagram"}, "B", "Heinrich's Domino Theory (1932) postulates that accident events are like five standing dominos."),
    ("TF", "The 6Ms (Man, Machine, Method, Media, Materials, Measurement) are used in Fishbone Diagrams.", "T", "The Fishbone Diagram utilizes these categories to trace root causes."),
    ("MCQ", "Which approach focuses on anticipating and preventing accidents?", {"A": "Reactive", "B": "Proactive", "C": "Compliance", "D": "Enforcement"}, "B", "The Proactive approach focuses on prevention, whereas Reactive limits losses post-accident."),
    ("TF", "The first and preferable line of defense against noise is personal protective equipment.", "F", "PPE is the last resort. The first line of defense is noise source elimination or process changes."),
    ("MCQ", "What is the design safety factor required for scaffold components?", {"A": "3:1", "B": "4:1", "C": "5:1", "D": "6:1"}, "B", "Scaffold components require a 4:1 safety factor. Crane hoists require 5:1, and ropes require 6:1."),
    ("MCQ", "What safety design principle requires that if a component fails, the system must enter a safe mode?", {"A": "Redundancy Principle", "B": "Worst Case Principle", "C": "Fail-Safe Principle", "D": "Interlocking Principle"}, "C", "The general fail-safe principle states that component failure must leave the system in a safe mode."),
    ("TF", "For overhead crane hoists, the design safety factor is 5:1.", "T", "Lecture 3 lists 5:1 for overhead crane hoists."),
    ("MCQ", "For scaffold ropes, what is the design safety factor?", {"A": "4:1", "B": "5:1", "C": "6:1", "D": "10:1"}, "C", "Scaffold ropes require a safety factor of 6:1."),
    ("TF", "Accident analysis should focus less on effects and more on accidents and their causes.", "T", "Preventive actions must target the causes of accidents rather than just their effects."),
    ("MCQ", "Which model describes defensive layers with holes representing failures that align to cause accidents?", {"A": "Four Ms", "B": "Swiss Cheese Model", "C": "Domino Theory", "D": "Heinrich Ratio"}, "B", "The Swiss Cheese Model uses slices of cheese to represent barriers, with holes as flaws."),
    ("TF", "Omission errors occur when a worker takes action, but it is the wrong action.", "F", "Omission is failure to take action. Commission is taking the wrong action."),
    ("MCQ", "What is the middle (3rd) domino in Heinrich's Domino Theory, which represents the point of safety control?", {"A": "Ancestry and Social Environment", "B": "Fault of Person", "C": "Unsafe Act or Condition", "D": "Accident"}, "C", "The 3rd domino is the Unsafe Act or Unsafe Condition. Removing it stops the chain.")
]

memorization.extend(parse_base_list(mem_base_3, 41, 3))

# 4. Lecture 4 Fall & Electrical (Q61-Q80)
mem_base_4 = [
    ("MCQ", "When building walls are pulled into the center of mass during structural collapse, it is called:", {"A": "Explosion", "B": "Implosion", "C": "Deflagration", "D": "Subsidence"}, "B", "Implosion pulls building walls into the center of mass."),
    ("TF", "Falls result in 15-20% of all accidental deaths and injuries in the workplace.", "T", "Lecture 4 lists falls as accounting for 15-20% of accidental deaths/injuries."),
    ("MCQ", "Which dangerous attitude causes workers to believe they can react and catch themselves during a fall?", {"A": "'I do not work very high'", "B": "'I'll catch myself'", "C": "'I have a good balance'", "D": "'I don't need PPE'"}, "B", "The 'I'll catch myself' attitude ignores the physics of free fall speed (falling 16 ft in 1s)."),
    ("MCQ", "Which dangerous attitude is disproven by the fact that 25% of fatal falls occur from heights under 10 feet?", {"A": "'I'll catch myself'", "B": "'I have a good balance'", "C": "'I do not work very high'", "D": "'I can jump down'"}, "C", "The 'I do not work very high' attitude is countered by the metric that 25% of fatal falls occur below 10 ft."),
    ("TF", "Standard guardrail heights must be 42 inches (+/- 3 inches) above the floor level.", "T", "This is the standard height specified by OSHA for top rails."),
    ("MCQ", "What is the standard height for mid-rails in guardrails?", {"A": "18 inches", "B": "21 inches", "C": "24 inches", "D": "30 inches"}, "B", "Mid-rails must be set at 21 inches height."),
    ("MCQ", "What is the height requirement for standard toe boards?", {"A": "2 inches", "B": "3.5 inches", "C": "4 inches", "D": "6 inches"}, "B", "Standard toe boards must be 3.5 inches high."),
    ("TF", "Hole covers must be designed to withstand the intended load and be secured.", "T", "Hole covers must be secured (bolted/latched) and designed to withstand the load."),
    ("MCQ", "Which line of defense against fall hazards includes guardrails and barriers?", {"A": "First line (Eliminate)", "B": "Second line (Prevent)", "C": "Third line (Control)", "D": "Last resort (PPE)"}, "B", "Second line of defense focuses on preventing the fall (guardrails, fences)."),
    ("MCQ", "Personal Fall Arrest Systems (PFAS) are classified under which fall hazard control category?", {"A": "First line of defense", "B": "Second line of defense", "C": "Third line of defense (Control)", "D": "Elimination"}, "C", "PFAS is a third line of defense control mechanism (mitigating the fall after it starts)."),
    ("TF", "Safety net systems are used for protection for workers 25 feet or more above lower levels.", "T", "Safety nets are required for workers exposed to falls of 25 ft or greater."),
    ("MCQ", "Under personal fall arrest systems, which component connects the body harness to the anchorage?", {"A": "Hole cover", "B": "Toe board", "C": "Lanyard", "D": "Positioning device"}, "C", "The lanyard (shock absorbing) connects the harness to the anchorage connector."),
    ("TF", "Electrical insulation hard hats are required to prevent electrical hazards.", "T", "Electrical workers require specially rated insulating hard hats (Class B or Class A)."),
    ("MCQ", "The current at which a person is still capable of releasing their grip on an electric wire is called the:", {"A": "Let-go current", "B": "Freeze current", "C": "Ground current", "D": "Arc current"}, "A", "Let-go current is the threshold at which a person can release the electric source."),
    ("TF", "Current flow (amperage) represents the greatest physical danger to the human body in electricity.", "T", "Amperage (current flow) is the primary factor that causes injury and fatality in electrocution."),
    ("MCQ", "What is the first line of defense in fall hazard controls?", {"A": "Standard guardrails", "B": "Safety nets", "C": "Eliminate the fall hazard", "D": "Body harnesses"}, "C", "First line of defense is always hazard elimination (e.g., ground gauges, drones)."),
    ("TF", "Positioning devices consist of a body belt and connection to allow hands-free work.", "T", "Positioning devices hold the worker in place, allowing hands-free operations."),
    ("MCQ", "Standard toe boards must have how much clearance above the floor?", {"A": "Not more than 1/4 inch", "B": "Not more than 1/2 inch", "C": "Exactly 1 inch", "D": "No clearance"}, "A", "Toe boards must have not more than 1/4 inch clearance above the floor."),
    ("TF", "Fuses and circuit breakers are designed to isolate electrical current automatically during overloads.", "T", "Fuses and breakers interrupt the circuit automatically during overloads or shorts."),
    ("MCQ", "In the US, electrocution accounts for approximately what percentage of all workplace deaths?", {"A": "2%", "B": "6%", "C": "12%", "D": "20%"}, "B", "Electrocution accounts for almost 6% of all workplace deaths in the United States.")
]

memorization.extend(parse_base_list(mem_base_4, 61, 4))

# 5. Lecture 5 Mechanical & Temperature (Q81-Q100)
mem_base_5 = [
    ("MCQ", "Which type of machine guarding includes photoelectrical (optical) and radio frequency safeguards?", {"A": "Guards", "B": "Devices", "C": "Fences", "D": "Gates"}, "B", "Photoelectrical, radio frequency, and electromechanical guards are classified as safeguarding Devices."),
    ("TF", "Fixed guards are permanent machine parts that do not have moving components.", "T", "Fixed guards are static barriers that cannot be removed without tools."),
    ("MCQ", "A mechanical crushing hazard that happens when the body gets caught between two moving parts (where one is rotating) is an:", {"A": "In-running nip point hazard", "B": "Squeeze-point type hazard", "C": "Adjustable point hazard", "D": "Cutting point hazard"}, "A", "In-running nip points occur between two parts, where one is rotating."),
    ("MCQ", "A crushing hazard between two moving parts where one is in linear motion is a:", {"A": "In-running nip point hazard", "B": "Squeeze-point type hazard", "C": "Adjustable point hazard", "D": "Cutting point hazard"}, "B", "Squeeze-point hazards happen between two parts, where one is in linear motion."),
    ("TF", "Shearing hazards often cause amputations of fingers and hands.", "T", "Power-driven shears used with paper, metal, and plastics present high risks of finger/hand amputation."),
    ("MCQ", "Which device requires the operator to constantly press two separate buttons at a safe distance from the danger zone?", {"A": "Presence Sensing Device", "B": "Two-Hand Control", "C": "Gate Safeguard", "D": "Photoelectrical cell"}, "B", "Two-hand controls force the worker to keep hands on buttons away from the point of operation."),
    ("TF", "Conduction is the transfer of heat from one location to another by way of a moving gas or liquid.", "F", "Conduction is heat transfer between touching bodies. Convection is heat transfer via a moving medium (gas/liquid)."),
    ("MCQ", "What is heat stress?", {"A": "The physiological response to hot temperatures", "B": "The net heat load from metabolic work, environmental factors, and clothing", "C": "Core body temperature rising above 38.5°C", "D": "Dehydration from sweating"}, "B", "Heat stress is the net heat load from metabolic work, environment, and clothing contributions."),
    ("MCQ", "What is heat strain?", {"A": "The net environmental heat load", "B": "The overall physiological response resulting from heat stress", "C": "Metabolic activity levels", "D": "Sustained rapid breathing"}, "B", "Heat strain is the physiological response (such as elevated heart rate or core temp) resulting from heat stress."),
    ("TF", "Hypothermia occurs when the deep body temperature falls below 36°C.", "T", "Cold stress hazards must be monitored to keep core body temperature from falling below 36°C."),
    ("MCQ", "Which degree of burn is minor and results in mild inflammation of the skin (e.g. sunburn)?", {"A": "First degree", "B": "Second degree", "C": "Third degree", "D": "Fourth degree"}, "A", "First-degree burns cause mild skin inflammation like sunburn."),
    ("TF", "Third-degree burns are easily recognizable due to the blisters that form on the skin.", "F", "Blisters characterize second-degree burns. Third-degree burns are deep, severe, and can be fatal."),
    ("MCQ", "Metabolic heat is heat produced in the body because of:", {"A": "Touching hot surfaces", "B": "Activity that burns energy", "C": "Radiation from steam pipes", "D": "Ambient humidity"}, "B", "Metabolic heat is generated internally by physical work and energy consumption."),
    ("TF", "Adjustable guards provide a barrier that can adjust to let materials pass.", "T", "Adjustable guards can be manually or self-adjusted to handle varying materials."),
    ("MCQ", "What is the last resort in heat stress management controls?", {"A": "Engineering ventilation", "B": "Set work-rest schedules (WTT)", "C": "Personal protective equipment (PPE)", "D": "Providing verbal instructions"}, "C", "Under temperature controls, PPE is the last resort."),
    ("TF", "Convection is the transfer of heat between two bodies that are touching.", "F", "Conduction is touching transfer. Convection uses moving air or liquids."),
    ("MCQ", "Under cold stress conditions, wind speed has what effect?", {"A": "No impact on cold stress", "B": "Reduces the effective temperature majorly", "C": "Increases core temperature", "D": "Improves muscular function"}, "B", "Wind speed increases convective heat loss, reducing the effective temperature (wind chill)."),
    ("TF", "Simple or incomplete bone breaks leave the bone cracked but in one piece, with intact skin.", "T", "Simple fractures are cracked bones without skin penetration."),
    ("MCQ", "Which burn degree is caused by steam or hot liquids, destroys skin layers, and can be fatal?", {"A": "First degree", "B": "Second degree", "C": "Third degree", "D": "Fourth degree"}, "C", "Third-degree burns destroy skin thickness, are caused by steam/hot liquids, and can be fatal."),
    ("TF", "Machine guarding responsibility lies only with supervisors, not employees.", "F", "Safety is a shared commitment. Management must provide guards, supervisors must maintain them, and employees must follow rules.")
]

memorization.extend(parse_base_list(mem_base_5, 81, 5))

# 6. Lecture 6 MMH & NIOSH (Q101-Q120)
mem_base_6 = [
    ("MCQ", "Which ergonomics term describes the act of rotating the upper body while the lower body is relatively fixed?", {"A": "Holding", "B": "Carrying", "C": "Twisting", "D": "Lifting"}, "C", "Twisting is the rotation of the upper body with the lower body fixed."),
    ("TF", "About 75% of workers whose jobs involve manual material handling suffer from low back pain.", "T", "Lecture 6 notes that 75% of MMH workers experience low back pain."),
    ("MCQ", "Back injuries account for what percentage of worker compensation costs?", {"A": "10%", "B": "20%", "C": "40%", "D": "60%"}, "C", "Back injuries represent 40% of worker compensation costs and one-third of LWD cases."),
    ("MCQ", "What is the safety weight threshold above which manual lifting frequently causes back injury for most workers?", {"A": "5 kg", "B": "10 kg", "C": "20 kg", "D": "40 kg"}, "C", "Lifting weights over 20 kg is a primary cause of back injury for most workers."),
    ("TF", "The vertical distance multiplier in the NIOSH equation represents the starting height of hands from the floor.", "F", "V (Vertical location) is the starting height. D (Vertical distance) is the travel distance of the load."),
    ("MCQ", "Which NIOSH multiplier is based on the twisting angle of the body while lifting?", {"A": "FM", "B": "VM", "C": "AM", "D": "CM"}, "C", "AM is the Angle Multiplier, based on the asymmetry twisting angle of the lift."),
    ("TF", "If the Recommended Weight Limit (RWL) is below the actual weight handled, the task must be redesigned.", "T", "An actual load weight greater than the RWL indicates a dangerous task."),
    ("MCQ", "Which NIOSH variable measures the frequency and duration of lifting over a work shift?", {"A": "H", "B": "V", "C": "F", "D": "C"}, "C", "F represents the frequency of lifts (multiplier FM)."),
    ("TF", "The Load Constant (LC) in the NIOSH lifting equation is 23 kg (or 51 lbs).", "T", "The baseline load constant is 23 kg."),
    ("MCQ", "In NIOSH equations, handhold quality (handles, grasp) is represented by which multiplier?", {"A": "HM", "B": "AM", "C": "CM", "D": "DM"}, "C", "CM is the Coupling Multiplier, representing handhold quality (good, fair, poor)."),
    ("TF", "Shelves that are too deep or too high contribute to workplace layout back injury risks.", "T", "Poor layouts (deep, high, or low shelves) cause stretching and bending, raising back injury risk."),
    ("MCQ", "What does the abbreviation NIOSH stand for?", {"A": "National Institute for Occupational Safety and Health", "B": "National Industrial Operations Safety and Hazards", "C": "National Insurance for Occupational Safety and Health", "D": "National Investigation of Safety Hazards"}, "A", "NIOSH stands for National Institute for Occupational Safety and Health."),
    ("TF", "The Horizontal Distance (H) is measured from the midpoint between the ankles to the hands.", "T", "Horizontal distance is measured from the ankle midpoint to the hand grasp point."),
    ("MCQ", "In NIOSH calculations, if a task is determined to be dangerous, the first recommendation is to assess which multiplier factor:", {"A": "Contributes most to the risk", "B": "Is the easiest to adjust", "C": "Has the highest value", "D": "Represents the load constant"}, "A", "Safety engineers must identify which factor contributes most to the risk (e.g. frequency, horizontal distance) to target redesigns."),
    ("TF", "Assigning additional workers to a lifting task is an administrative control to reduce lifting frequency.", "T", "Assigning additional workers, reducing frequency, or shortening task times represent administrative interventions."),
    ("MCQ", "What does the abbreviation MSD stand for in occupational health?", {"A": "Manual Safety Devices", "B": "Musculoskeletal Disorders", "C": "Management Safety Directives", "D": "Mechanical Safeguard Defects"}, "B", "MSD stands for Musculoskeletal Disorders, which are addressed in ergonomic standards."),
    ("TF", "Under ANSI standards, job analysis and job design are management responsibilities.", "T", "ANSI ergonomic standards specify job analysis and job design interventions as key responsibilities."),
    ("MCQ", "Static postures describe:", {"A": "Moving loads over distances", "B": "Maintaining a given posture for an extended time", "C": "Body parts being out of neutral position", "D": "Vibrating contact stress"}, "B", "Static postures occur when a single posture is maintained for an extended period of time."),
    ("TF", "Repetition refers to the amount of effort needed to accomplish a safety task.", "F", "Force is the effort needed. Repetition is the number of times a task is performed."),
    ("MCQ", "What term describes contact between sensitive body tissues and hard objects (like tools)?", {"A": "Vibration", "B": "Static posture", "C": "Contact stress", "D": "Awkward posture"}, "C", "Contact stress is the contact between sensitive body tissues and hard objects.")
]

memorization.extend(parse_base_list(mem_base_6, 101, 6))

# 7. Lecture 7 Fire Hazards (Q121-Q140)
mem_base_7 = [
    ("MCQ", "Fire is a chemical reaction that requires fuel, an ignition source, and what other element?", {"A": "Carbon dioxide", "B": "Oxygen", "C": "Nitrogen", "D": "Water"}, "B", "Fire requires the 'fire triangle' components: Fuel, Oxygen, and Ignition Source."),
    ("TF", "The Fire Prevention Plan (FPP) must be written and available for all employees.", "T", "Employers must maintain a written FPP in the workplace for employee review."),
    ("MCQ", "Which plan outlines escape routes and accounting for employees during emergencies?", {"A": "FPP", "B": "EAP", "C": "MSDS", "D": "LOTO"}, "B", "The Emergency Action Plan (EAP) contains escape routes, evacuation procedures, and accounting methods."),
    ("TF", "Class A fires involve flammable liquids and gases.", "F", "Class A is ordinary combustibles (wood, paper). Class B is flammable liquids/gases."),
    ("MCQ", "A fire involving ordinary combustibles like paper, wood, and cloth is classified as:", {"A": "Class A", "B": "Class B", "C": "Class C", "D": "Class D"}, "A", "Ordinary combustibles represent Class A fires."),
    ("MCQ", "Which class of fires involves energized electrical equipment?", {"A": "Class A", "B": "Class B", "C": "Class C", "D": "Class D"}, "C", "Energized electrical fires are Class C."),
    ("TF", "Class D fires involve combustible metals like potassium and magnesium.", "T", "Combustible metals fall under Class D fires."),
    ("MCQ", "An EAP review must be conducted with each employee in all the following times EXCEPT:", {"A": "When the plan is first created", "B": "When new employees are assigned to the job", "C": "Weekly during normal shifts", "D": "When any changes are made to the plan"}, "C", "EAP review is required: 1. Creation, 2. Onboarding, and 3. When changes are made. Weekly reviews are not mandatory."),
    ("TF", "FPP lists major fire hazards and the names/job titles of workers responsible for maintenance.", "T", "FPP contains hazards, controls, maintenance names, and waste control procedures."),
    ("MCQ", "Under EAP evacuation options, if extinguishers are provided but not intended for employee use, the policy is:", {"A": "All employees fight fire", "B": "Designated employees fight fire", "C": "Total evacuation", "D": "Shelter in place"}, "C", "Providing extinguishers without employee training implies a total evacuation policy."),
    ("TF", "Emergency exit routes must be permanent and separated by fire-resistant materials.", "T", "Exit routes must be permanent, fire-resistant structures with limited openings."),
    ("MCQ", "What is the minimum height required for emergency exit routes?", {"A": "1.5 to 1.8 meters", "B": "2.0 to 2.3 meters", "C": "2.5 to 2.8 meters", "D": "3.0 meters"}, "B", "OSHA requires exit routes to have a minimum height of 2 to 2.3 meters."),
    ("TF", "Exit doors must be locked from the inside to prevent unauthorized entry during fires.", "F", "Exit doors must be *unlocked* from the inside and side-hinged."),
    ("MCQ", "A portable water fire extinguisher is most suitable for which class of fires?", {"A": "Class A", "B": "Class B", "C": "Class C", "D": "Class D"}, "A", "Water extinguishers cool Class A (ordinary) fires. They cannot be used on Class B or C due to spreading/shock risks."),
    ("TF", "CO2 fire extinguishers contain gas under extreme pressure, displacing oxygen to extinguish fires.", "T", "CO2 smothering action displaces oxygen and cools the fuel."),
    ("MCQ", "Which dry chemical potassium bicarbonate extinguisher is designed for kitchen grease fires?", {"A": "Water type", "B": "Class K wet chemical type", "C": "Class D metal type", "D": "Halon type"}, "B", "Class K wet chemical extinguishers spray a fine mist for cooking oils and fats."),
    ("TF", "The P.A.S.S. technique stands for Pull, Align, Squeeze, and Sweep.", "F", "P.A.S.S. stands for Pull, Aim (at base), Squeeze, and Sweep."),
    ("MCQ", "What is the frequency required for visual inspections of portable fire extinguishers?", {"A": "Daily", "B": "Weekly", "C": "Monthly", "D": "Annually"}, "C", "Extinguishers require a monthly visual inspection, verified on the inspection tag."),
    ("TF", "Dust explosions represent a serious hazard in industries handling combustible dusts.", "T", "Lessons from the Imperial Sugar case study highlight dust explosions as major safety risks."),
    ("MCQ", "When checking an extinguisher during monthly visual inspection, the product inside should be checked for free flow by:", {"A": "Discharging a small amount", "B": "Turning the bottle upside down and shaking", "C": "Weighing the bottle", "D": "Checking the pressure gauge"}, "B", "To verify product free flow without discharging, turn the bottle upside down and shake.")
]

memorization.extend(parse_base_list(mem_base_7, 121, 7))

# 8. Lecture 8 Noise (Q141-Q155)
mem_base_8 = [
    ("MCQ", "Noise is defined as sound that:", {"A": "Is pleasing to the ear", "B": "Varies randomly in intensity and frequency and is unwanted", "C": "Has a constant frequency", "D": "Cannot travel through air"}, "B", "Noise is unwanted sound varying randomly in intensity and frequency, and can interfere with other sound reception (masking)."),
    ("TF", "Noise Induced Hearing Loss (NIHL) is the only negative effect of industrial noise.", "F", "Noise also increases blood pressure, causes mental fatigue, and interferes with communication, leading to accidents."),
    ("MCQ", "Exposure to noise levels above 115 decibels is risky for durations as short as:", {"A": "5 minutes", "B": "30 minutes", "C": "1 hour", "D": "8 hours"}, "A", "Exposure above 115 decibels for even five minutes is highly hazardous to hearing."),
    ("MCQ", "According to slides, what is the noise level generated by a circular saw?", {"A": "80 dBA", "B": "90-100 dBA", "C": "110 dBA", "D": "120 dBA"}, "B", "Circular saws produce noise levels of 90-100 decibels."),
    ("TF", "Decibels (dB) are linear units and can be added mathematically (e.g., 80 dB + 80 dB = 160 dB).", "F", "Decibels are logarithmic and cannot be added linearly."),
    ("MCQ", "What is the noise level generated by a chainsaw?", {"A": "90 dBA", "B": "100 dBA", "C": "110 dBA", "D": "140 dBA"}, "C", "Chainsaws generate high noise levels of 110 decibels."),
    ("TF", "OSHA's Action Level (AL) for noise is 85 dBA for an 8-hour TWA.", "T", "The Action Level (AL) is 85 dBA TWA, which triggers safety program requirements."),
    ("MCQ", "Which administrative control can be used to manage workplace noise risk?", {"A": "Installing silencers", "B": "Worker job rotation to limit TWA exposure", "C": "Erecting acoustic barriers", "D": "Earmuffs"}, "B", "Job rotation is an administrative control. Silencers and barriers are engineering controls; earmuffs are PPE."),
    ("TF", "Damping involves adding vibration-absorbing materials to reduce noise generated by sheet metal vibrations.", "T", "Damping reduces structure-borne sound by absorbing vibrations."),
    ("MCQ", "Devices designed to remove air-borne sound waves in pumps and compressors are:", {"A": "Acoustic barriers", "B": "Silencers", "C": "Personnel cabins", "D": "Damping pads"}, "B", "Silencers remove sound waves from moving air/gas in pumps and compressors."),
    ("TF", "Annual audiograms are required for employees exposed to TWAs of 85 dBA or higher.", "T", "Once a baseline is established, annual audiometric testing is required to monitor hearing status."),
    ("MCQ", "Which noise source is listed as producing 90-95 decibels?", {"A": "Circular saw", "B": "Jackhammer", "C": "Front-end Loader", "D": "Chainsaw"}, "C", "Front-end loaders generate 90-95 decibels."),
    ("TF", "The OSHA Action Level (AL) is higher than the Permissible Exposure Limit (PEL).", "F", "PEL is 90 dBA. AL is 85 dBA (lower threshold triggering conservation programs)."),
    ("MCQ", "If the source of noise cannot be isolated, what engineering control isolates the worker?", {"A": "Silencer", "B": "Damping pad", "C": "Personnel cabin", "D": "Earmuff"}, "C", "A personnel cabin isolates the worker in a quiet enclosure when the noise source cannot be muffled."),
    ("TF", "Earplugs and earmuffs can be combined for double protection in very noisy environments.", "T", "Dual hearing protection (plugs and muffs together) is used in extreme noise environments.")
]

memorization.extend(parse_base_list(mem_base_8, 141, 8))

# 9. Lecture 9 PPE & Hazmat (Q156-Q170)
mem_base_9 = [
    ("MCQ", "Under Hazmat regulations, which class of hazardous materials is designated for explosives?", {"A": "Class 1", "B": "Class 2", "C": "Class 3", "D": "Class 4"}, "A", "Class 1 covers explosives, subdivided into six sections."),
    ("TF", "Class 3 hazardous materials represent flammable liquids.", "T", "Class 3 is designated for flammable and combustible liquids."),
    ("MCQ", "Which Hazmat class covers radioactive substances?", {"A": "Class 5", "B": "Class 6", "C": "Class 7", "D": "Class 8"}, "C", "Class 7 is designated for radioactive substances."),
    ("MCQ", "Which Hazmat class covers corrosive substances that react with metals and skin?", {"A": "Class 5", "B": "Class 6", "C": "Class 7", "D": "Class 8"}, "D", "Class 8 is designated for corrosives."),
    ("TF", "Class A hard hats provide electrical insulation up to 20,000 volts.", "F", "Class A protects up to 2,200 volts. Class B protects up to 20,000 volts."),
    ("MCQ", "What type of hard hat is designed only for bump protection and provides no electrical protection?", {"A": "Class A", "B": "Class B", "C": "Class C", "D": "Class D"}, "C", "Class C hard hats protect against bumps/impacts but offer no electrical insulation."),
    ("TF", "Foot protection chevron outsoles are recommended specifically for slippery wet indoor surfaces.", "F", "Safety-Lok outsoles are recommended for wet indoor surfaces. Chevron is for hard surfaces indoor/outdoor."),
    ("MCQ", "Which safety tag is color-coded red with contrasting letters?", {"A": "Danger Tag", "B": "Caution Tag", "C": "Warning Tag", "D": "Notice Tag"}, "A", "Danger tags are red and warn of immediate threats of death or serious injury."),
    ("TF", "Warning tags are color-coded orange.", "T", "Warning tags are orange (between yellow caution and red danger)."),
    ("MCQ", "What is the color code for Caution Tags?", {"A": "Red", "B": "Orange", "C": "Yellow", "D": "Green"}, "C", "Caution tags are color-coded yellow."),
    ("TF", "Air Purifying Respirators (APRs) can be safely used in oxygen-deficient environments.", "F", "APRs do not supply oxygen; they only filter ambient air. They cannot be used if oxygen is less than 19.5%."),
    ("MCQ", "Which respirator type supplies breathing air from a pressurized tank carried by the worker?", {"A": "APR", "B": "PAPR", "C": "SCBA", "D": "HEPA filter"}, "C", "SCBA (Self-Contained Breathing Apparatus) supplies air from a pressurized cylinder."),
    ("TF", "General purpose gloves are suitable for chemical handling without liners.", "F", "General purpose gloves do not resist chemicals and should not be used for them without liners."),
    ("MCQ", "Which safety sign class is color-coded with blue/black headers on a white background?", {"A": "Danger", "B": "Caution", "C": "Notice", "D": "General Safety"}, "C", "Notice signs utilize blue or black text/headers on white backgrounds."),
    ("TF", "The NFPA diamond flammability hazard is represented in the red section at the top.", "T", "The red quadrant at the top of the NFPA diamond indicates flammability rating (0-4).")
]

memorization.extend(parse_base_list(mem_base_9, 156, 9))


# ==========================================================================
# PART 2: MATH, LOGIC & EQUATIONS (160 Questions)
# ==========================================================================

# 1. Total Injury-Illness Incidence Rate (IR) (20 Questions)
for r in range(1, 21):
    cases = r + 2
    hours = 100000 + (r * 25000)
    expected_ir = round((cases * 200000) / hours, 2)
    q_text = f"An industrial facility reports **{cases} recordable cases** of injuries and illnesses in a year. The total worker-hours of job exposure during this period is **{hours:,} hours**. What is the Total Injury-Illness Incidence Rate (IR)?"
    math_logic.append({
        "id": f"math-ir-{r}",
        "lectureId": 2,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": f"{round(expected_ir * 0.5, 2)}",
            "B": f"{expected_ir}",
            "C": f"{round(expected_ir * 1.5, 2)}",
            "D": f"{round(expected_ir + 1.2, 2)}"
        },
        "answer": "B",
        "explanation": f"Using the formula: $IR = (N_{{rc}} \\times 200,000) / H_{{je}}$\n$IR = ({cases} \\times 200,000) / {hours:,} = {cases * 200000:,} / {hours:,} = {expected_ir}$ cases per 100 full-time workers."
    })

# 2. Lost Workday Case Incidence Rate (LWDI) (20 Questions)
for r in range(1, 21):
    lost_cases = r + 1
    hours = 120000 + (r * 30000)
    expected_lwdi = round((lost_cases * 200000) / hours, 2)
    q_text = f"A warehouse records **{lost_cases} injury cases involving lost workdays** (excluding illnesses and fatalities). The total hours worked by all employees during the period is **{hours:,} hours**. What is the Lost-Workday-case Incidence rate (LWDI)?"
    math_logic.append({
        "id": f"math-lwdi-{r}",
        "lectureId": 2,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": f"{expected_lwdi}",
            "B": f"{round(expected_lwdi * 0.8, 2)}",
            "C": f"{round(expected_lwdi + 2.0, 2)}",
            "D": f"{round(expected_lwdi * 1.3, 2)}"
        },
        "answer": "A",
        "explanation": f"Using the formula: $LWDI = (N_{{clwd}} \\times 200,000) / H_{{je}}$\n$LWDI = ({lost_cases} \\times 200,000) / {hours:,} = {lost_cases * 200000:,} / {hours:,} = {expected_lwdi}$ cases per 100 workers."
    })

# 3. Severity Rate (SR) (20 Questions)
for r in range(1, 21):
    lost_days = r * 15
    hours = 150000 + (r * 20000)
    expected_sr = round((lost_days * 200000) / hours, 2)
    q_text = f"A plant tracks **{lost_days} lost workdays** due to occupational injuries. The worker-hours of exposure during the year is **{hours:,} hours**. What is the Severity Rate (SR)?"
    math_logic.append({
        "id": f"math-sr-{r}",
        "lectureId": 3,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": f"{round(expected_sr * 0.6, 2)}",
            "B": f"{round(expected_sr * 1.4, 2)}",
            "C": f"{expected_sr}",
            "D": f"{round(expected_sr + 5.5, 2)}"
        },
        "answer": "C",
        "explanation": f"Using the formula: $SR = (N_{{lwd}} \\times 200,000) / H_{{je}}$\n$SR = ({lost_days} \\times 200,000) / {hours:,} = {lost_days * 200000:,} / {hours:,} = {expected_sr}$ lost days per 100 workers."
    })

# 4. Average Severity (AS) & ADAW (20 Questions)
for r in range(1, 21):
    lost_days = r * 20
    cases = r + 2
    expected_as = round(lost_days / cases, 2)
    q_text = f"A department logs **{lost_days} total lost workdays** across **{cases} recordable cases** of injuries. What is the Average Severity (AS) per case?"
    math_logic.append({
        "id": f"math-as-{r}",
        "lectureId": 3,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": f"{expected_as}",
            "B": f"{round(expected_as * 0.7, 2)}",
            "C": f"{round(expected_as + 3.0, 2)}",
            "D": f"{round(expected_as * 1.5, 2)}"
        },
        "answer": "A",
        "explanation": f"Using the formula: $AS = N_{{lwd}} / N_{{rc}}$\n$AS = {lost_days} / {cases} = {expected_as}$ days lost per recordable case."
    })

# 5. Combined Noise Levels (25 Questions)
noise_diff_chart = {
    0: 3.0, 1: 2.5, 2: 2.1, 3: 1.8, 4: 1.5, 5: 1.2, 6: 1.0, 7: 0.8, 8: 0.6, 9: 0.5
}
for r in range(1, 26):
    n1 = 80 + (r % 15)
    n2 = n1 + (r % 10)
    diff = abs(n1 - n2)
    higher = max(n1, n2)
    if diff >= 10:
        expected_db = higher
        added = 0.0
    else:
        added = noise_diff_chart[diff]
        expected_db = round(higher + added, 1)
        
    q_text = f"An operator works near two machines. Machine 1 produces a noise level of **{n1} dBA** and Machine 2 produces **{n2} dBA**. Based on standard decibel addition rules, what is the combined noise level?"
    math_logic.append({
        "id": f"math-noise-{r}",
        "lectureId": 8,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": f"{n1 + n2} dBA",
            "B": f"{expected_db} dBA",
            "C": f"{expected_db - 3} dBA",
            "D": f"{higher} dBA"
        },
        "answer": "B",
        "explanation": f"Logarithmic decibel addition: The difference is $|{n1} - {n2}| = {diff}$ dBA. Under standard decibel addition charts, a difference of {diff} dB adds {added} dB to the higher sound level ({higher} dBA). Combined noise = {higher} + {added} = {expected_db} dBA."
    })

# 6. Heat Strain sustained maximum heart rate (25 Questions)
for r in range(1, 26):
    age = 20 + r
    expected_hr = 180 - age
    q_text = f"Under extreme temperature exposures, a safety engineer monitors a **{age}-year-old worker** to prevent heat strain. According to guidelines, the worker's sustained heart rate should not exceed how many beats per minute (bpm)?"
    math_logic.append({
        "id": f"math-hr-{r}",
        "lectureId": 5,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": "180 bpm",
            "B": f"{expected_hr} bpm",
            "C": f"{expected_hr + 20} bpm",
            "D": "120 bpm"
        },
        "answer": "B",
        "explanation": f"To recognize the presence of heat strain, the physiological heart rate limit is calculated using the formula: $HR_{{limit}} = 180 - \\text{{age}}$. For a {age}-year-old worker: $180 - {age} = {expected_hr}$ bpm."
    })

# 7. Quantitative Risk Level (20 Questions)
for r in range(1, 21):
    prob = (r % 5) + 1
    sev = ((r + 2) % 5) + 1
    expected_risk = prob * sev
    q_text = f"During a hazard assessment, a safety officer rates the probability of a mechanical pinch occurring as **{prob}** (on a 1-5 scale) and the severity of potential injury as **{sev}** (on a 1-5 scale). What is the calculated Risk score?"
    math_logic.append({
        "id": f"math-risk-{r}",
        "lectureId": 2,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": f"{prob + sev}",
            "B": f"{expected_risk}",
            "C": f"{prob}",
            "D": f"{round(prob / sev, 2)}"
        },
        "answer": "B",
        "explanation": f"Using the risk formula: $Risk = Probability \\times Severity$.\nRisk = {prob} \\times {sev} = {expected_risk}."
    })

# 8. NIOSH lifting equation Recommended Weight Limit (10 Questions)
for r in range(1, 11):
    hm = round(1.0 - (r * 0.04), 2)
    vm = round(0.99 - (r * 0.02), 2)
    dm = round(1.0 - (r * 0.03), 2)
    fm = 0.80 if r % 2 == 0 else 0.50
    am = round(0.95 - (r * 0.01), 2)
    cm = 1.0
    
    expected_rwl = round(23 * hm * vm * dm * fm * am * cm, 2)
    
    q_text = f"Evaluate a manual lifting task using the revised NIOSH lifting equation (LC = 23 kg). The task multipliers are measured as: HM = **{hm}**, VM = **{vm}**, DM = **{dm}**, FM = **{fm}**, AM = **{am}**, CM = **{cm}**. What is the Recommended Weight Limit (RWL) for this task?"
    
    math_logic.append({
        "id": f"math-rwl-{r}",
        "lectureId": 6,
        "type": "MCQ",
        "question": q_text,
        "options": {
            "A": f"{expected_rwl} kg",
            "B": f"{round(expected_rwl * 0.5, 2)} kg",
            "C": "23.00 kg",
            "D": f"{round(expected_rwl * 1.5, 2)} kg"
        },
        "answer": "A",
        "explanation": f"Using the NIOSH lifting equation: $RWL = LC \\times HM \\times VM \\times DM \\times FM \\times AM \\times CM$.\n$RWL = 23 \\times {hm} \\times {vm} \\times {dm} \\times {fm} \\times {am} \\times {cm} = {expected_rwl}$ kg."
    })


# ==========================================================================
# PART 3: OPEN BOOK SCENARIOS (150 Questions)
# ==========================================================================

# 15 Main Topics
essay_topics = [
    ("Safety Definitions", "Danger, Hazard, Risk, Severity, and accident sequence causes."),
    ("Direct vs Indirect Costs", "Tips of the iceberg costs, financial vs productivity outlays."),
    ("Accident Indexes", "Traditional Frequency/Severity vs modern TWA incidence rates."),
    ("Safety Programs (TMC)", "Management commitment, Accountability, and employee motivation."),
    ("Human Errors in 4Ms", "Omission vs commission errors, and age/fatigue stressors."),
    ("Accident Causation Theories", "Domino Theory (Heinrich 1932) and Swiss Cheese models."),
    ("Noise Risk Management", "Hierarchy of controls applied to compressor and power press rooms."),
    ("LOTO (Zero Mechanical State)", "Steps to isolate energy and verify zero mechanical states."),
    ("Workplace Falls Protection", "Three lines of defense, guardrails, and rescue strategies."),
    ("Electrical Hazards", "Freeze currents, voltages, and hard hat insulation ratings."),
    ("Mechanical Hazards", "Point of operation, nip points, guards vs safety devices."),
    ("Ergonomics & NIOSH", "Manual material handling weight limits and posturing variables."),
    ("Fire Prevention Plans", "Combustible wastes, maintenance safeguards, and exit routes."),
    ("Hazard Communication", "ANSI sign specifications and OSHA tags categories."),
    ("PPE Selection & Hazmat", "Respirator types (APR vs SCBA) and DOT/UN classes.")
]

for topic_idx, (topic_name, topic_desc) in enumerate(essay_topics):
    lecture_id = min(9, (topic_idx // 2) + 1)
    
    # 10 Questions per topic = 150 Questions total
    for q_num in range(1, 11):
        q_id = f"open-{topic_idx * 10 + q_num}"
        
        # Variations of questions based on topic
        if q_num == 1:
            question_text = f"Explain the core concept of **{topic_name}** as presented in the safety curriculum. Cite specific definitions, models, or guidelines."
            model_answer = f"### Model Answer:\n1. **Core Concept** of {topic_name}: Discusses the primary principles governing {topic_desc}.\n2. **Curriculum References**: Directly references Slide/Lecture guidelines regarding safety parameters.\n3. **Practical Application**: Implementing this helps safety professionals identify risks, manage compliance, and mitigate workplace injury hazards."
            rubrics = ["Defines the core concept correctly", "Cites relevant slide guidelines", "Explains practical applications"]
        elif q_num == 2:
            question_text = f"Provide a detailed step-by-step breakdown of how a safety officer should evaluate and audit **{topic_name}** in a manufacturing facility."
            model_answer = f"### Model Answer:\n1. **Audit Phase**: Review historical records (OSHA 300 logs), inspect workplace conditions, and observe behaviors.\n2. **Risk Assessment**: Map probabilities and severity ratings associated with the hazard.\n3. **Control Implementation**: Apply hierarchy of controls, starting with engineering barriers and moving to administrative schedules and PPE."
            rubrics = ["Outlines the audit phase", "Mentions checking OSHA logs/history", "Applies the hierarchy of controls"]
        elif q_num == 3:
            question_text = f"Discuss how the principles of **{topic_name}** integrate with the 'Four Ms Model' (Man, Machine, Media, Management)."
            model_answer = f"### Model Answer:\n1. **Man**: Focuses on human behaviors, stress, and errors (omission/commission) relating to {topic_name}.\n2. **Machine**: Evaluates mechanical, electrical, and temperature tools.\n3. **Media**: Covers physical environment (noise, light) and social safety culture.\n4. **Management**: Administers safety policies, training, and accountability metrics."
            rubrics = ["Links topic to Man (errors/fatigue)", "Links topic to Machine (guards/tools)", "Links topic to Media (environment)", "Links topic to Management (policy/enforcement)"]
        elif q_num == 4:
            question_text = f"Draft an administrative policy proposal for employees that outlines training and safety rules for **{topic_name}**."
            model_answer = f"### Model Answer:\n1. **Training Requirements**: Weekly toolbox talks, mandatory onboarding reviews, and annual refreshers.\n2. **Standard Operating Procedures (SOPs)**: Outlines steps for hazard reporting and daily inspections.\n3. **Compliance & Enforcement**: Detail supervisor accountability, audit checklists, and tags application."
            rubrics = ["Outlines training frequencies", "Details standard operating procedures", "Mentions supervisor accountability"]
        elif q_num == 5:
            question_text = f"Contrast engineering controls vs. administrative controls for managing risks associated with **{topic_name}**."
            model_answer = f"### Model Answer:\n1. **Engineering Controls**: Physical changes to the workplace that isolate or eliminate the hazard (e.g. guardrails, enclosures, silencers). Highly preferred as they do not depend on human behavior.\n2. **Administrative Controls**: Workplace practices and schedules that limit exposure duration (e.g. job rotations, quiet periods, training, LOTO tags). Less reliable as they depend on workers following rules."
            rubrics = ["Defines Engineering controls with examples", "Defines Administrative controls with examples", "Explains why engineering controls are preferred (not human-behavior dependent)"]
        elif q_num == 6:
            question_text = f"How should a safety manager address employee motivation and behavioral compliance regarding safety regulations for **{topic_name}**?"
            model_answer = f"### Model Answer:\n1. **Motivation**: Individual motivation and abilities are key pillars. Encourage participation via safety meetings and positive feedback.\n2. **Enforcement**: Clear rules, accountability structures, and transparent accident analysis histories to show workers the 'why' behind rules.\n3. **Participation**: Involve employees in hazard analysis audits and risk assessment ratings."
            rubrics = ["Discusses employee motivation pillars", "Proposes positive feedback and participation", "Addresses accountability and hazard analysis involvement"]
        elif q_num == 7:
            question_text = f"Create a mock case study analysis: An accident occurred due to failures in **{topic_name}**. Conduct a root-cause investigation."
            model_answer = f"### Model Answer:\n1. **Investigation**: Inspect physical site (unsafe conditions) and interview witnesses (unsafe acts).\n2. **Root Cause**: Trace back from injury to accident to unsafe act/condition, identifying gaps in safety management policies.\n3. **Corrective Action**: Redesign tasks, install physical safeguarding, and implement lockout/tagout audits to prevent recurrence."
            rubrics = ["Analyzes unsafe acts and unsafe conditions", "Traces causes back to safety management gaps", "Proposes concrete corrective actions (safeguards, audits)"]
        elif q_num == 8:
            question_text = f"Discuss the legal and social consequences a company faces if it fails to maintain proper compliance for **{topic_name}**."
            model_answer = f"### Model Answer:\n1. **Legal Consequences**: OSHA citations, penalties, lawsuit fees, and non-compliance fines under Egyptian Labor Law.\n2. **Social Consequences**: Severely reduced worker morale, negative publicity, damaged customer relations, and moral/ethical failure of employee welfare care."
            rubrics = ["Identifies legal consequences (OSHA fines, lawsuits)", "Identifies social consequences (morale, public image)", "Cites moral/ethical obligations to employee welfare"]
        elif q_num == 9:
            question_text = f"Explain how the Worst Case safety design principle applies when managing hazards in **{topic_name}**."
            model_answer = f"### Model Answer:\n1. **Worst Case Principle**: Design systems to remain safe even under the most extreme, worst-case combinations of component failures or environmental conditions.\n2. **Application**: Assume maximum loads (e.g., structural failure limits), highest voltages, or extreme temperature drafts when designing protective boundaries."
            rubrics = ["Defines the Worst Case Principle", "Applies the principle to extreme load, voltage, or heat conditions", "Explains the impact on safety design margins"]
        else:
            question_text = f"Propose a comprehensive safety checklist that supervisors can use during daily walk-through inspections to audit **{topic_name}**."
            model_answer = f"### Model Answer:\n1. **Inspection Items**: Check physical guard completeness, tag dates and placements, housekeeping of egress routes, and proper wear of required PPE.\n2. **Review Logs**: Verify training logs, incident visual tags, and machine maintenance records.\n3. **Sign-off**: Ensure supervisor signature, date, and documented corrective actions for any identified deficiencies."
            rubrics = ["Includes check of physical barriers and guards", "Includes verify LOTO tags/LOTO records", "Requires documented corrective actions for failures"]
            
        open_ended.append({
            "id": q_id,
            "lectureId": lecture_id,
            "question": question_text,
            "modelAnswer": model_answer,
            "gradingRubric": rubrics
        })

# Export
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
    "memorization": memorization,
    "mathLogic": math_logic,
    "openEnded": open_ended
}

with open("/home/naur/.gemini/antigravity/scratch/safety-quiz-app/questions.js", "w", encoding="utf-8") as f:
    f.write("const safetyQuizData = " + json.dumps(quizData, indent=2, ensure_ascii=False) + ";\n")

print(f"Successfully generated database in questions.js:")
print(f"  - {len(memorization)} Memorization questions")
print(f"  - {len(math_logic)} Math/Logic questions")
print(f"  - {len(open_ended)} Open Book scenarios")
