📊 Heart Disease Dataset: Attribute Descriptions
This dataset contains clinical and diagnostic data used to predict the presence or absence of heart disease in a patient. Below is a detailed explanation of each attribute.
🔢 Variable Descriptions
S.No	Attribute	Code (Column Name)	Description
1	Age	age	Age of the patient (in years)
2	Sex	sex	Sex of the patient (1 = male, 0 = female)
3	Chest Pain Type	chest_pain_type	Type of chest pain (1–4; see below for details)
4	Resting Blood Pressure	resting_bp	Resting blood pressure (in mm Hg)
5	Serum Cholesterol	cholesterol	Serum cholesterol level (in mg/dl)
6	Fasting Blood Sugar	fasting_blood_sugar	Whether fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
7	Resting ECG Results	resting_ecg	Results from resting electrocardiogram (0–2; see below)
8	Max Heart Rate Achieved	max_heart_rate	Maximum heart rate achieved during exercise (71–202 bpm)
9	Exercise-Induced Angina	exercise_angina	1 = Yes; 0 = No
10	ST Depression (Oldpeak)	oldpeak	ST depression induced by exercise compared to rest
11	ST Slope	st_slope	Slope of the peak exercise ST segment (0–2; see below)
| 12 | Target (Diagnosis) | target | 1 = Heart disease; 0 = Normal (no disease) |
📘 Nominal & Binary Attribute Details
Sex
1 = Male
0 = Female
Chest Pain Type
1 = Typical angina
2 = Atypical angina
3 = Non-anginal pain
4 = Asymptomatic
Fasting Blood Sugar
1 = True (blood sugar > 120 mg/dl)
0 = False
Resting ECG Results
0 = Normal
1 = ST-T wave abnormality (e.g., T wave inversion, ST elevation/depression > 0.05 mV)
2 = Left ventricular hypertrophy (by Estes' criteria)
Exercise-Induced Angina
1 = Yes
0 = No
ST Slope
0 = Upsloping
1 = Flat
2 = Downsloping
Target (Class)
1 = Presence of heart disease
0 = Normal (no disease)