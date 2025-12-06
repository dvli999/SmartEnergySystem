import subprocess
import pandas as pd
import joblib

# --- Step 1: Call CORBA client ---
classpath = r"C:\Users\medal\IdeaProjects\SmartEnergySystem\target\classes"
cmd = [
    "java", "-cp", classpath, "corba.TempsClient",
    "-ORBInitialPort", "1050", "-ORBInitialHost", "localhost"
]

result = subprocess.run(cmd, capture_output=True, text=True)
output = result.stdout.strip()

# --- Step 2: Parse CORBA output ---
time_data = {}
for line in output.splitlines():
    if ":" in line:
        key, value = line.split(":", 1)
        time_data[key.strip().lower()] = int(value.strip())

# Compute weekend flag
time_data['weekend'] = 1 if time_data['jour'] >= 5 else 0

# --- Step 3: Load ML model and scaler ---
rf_model = joblib.load('rf_modele_energie.pkl')
scaler = joblib.load('scaler_energie.pkl')
features = joblib.load('features_energie.pkl')

# --- Step 4: Prepare data for prediction ---
df_futur = pd.DataFrame([{
    'heure_jour': time_data['heure'],
    'jour_semaine': time_data['jour'],
    'weekend': time_data['weekend']
}])

X_futur = scaler.transform(df_futur[features])

# --- Step 5: Make prediction ---
prediction = rf_model.predict(X_futur)[0]
print(f"=== Prediction ===")
print(f"Heure: {time_data['heure']}, Jour: {time_data['jour']}, Semaine: {time_data['semaine']}")
print(f"Predicted energy consumption: {prediction:.1f} kWh")

# Optional: check if consumption is high
threshold = 70  # Example threshold
if prediction > threshold:
    print("⚠️ Consumption is high! Consider turning off some appliances.")
