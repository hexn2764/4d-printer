import random
import csv
import os

OUTPUT_FILENAME = os.path.join(os.path.dirname(__file__), "4d_printer_test_data.csv")

NUM_LINES = 10000

REQUIREMENT_PREFIXES = [
    "Motor", "Heating", "Sensor", "Control", "Navigation", "Power", "Safety", "Fan", "Display",
    "Battery", "Button", "Software", "Firmware", "Voltage", "Temperature", "Alignment", "Rotation",
    "Signal", "Material", "Nozzle", "Extruder", "Platform", "Cooling", "Layer", "Calibration", "Axis",
    "Timing", "Feed", "Transformation", "Frame", "Support", "Mechanism", "Logic", "Synchronization", "Profile",
    "Encoder", "Drive", "Tracking", "Actuator", "Diagnostics", "Flow", "Processing", "Transport", "Detection"
]

REQUIREMENT_NOUNS = [
    "Unit", "Module", "System", "Array", "Controller", "Processor", "Sensor", "Motor", "Heater", "Fan",
    "Battery", "Display", "Button", "Housing", "Frame", "Algorithm", "Protocol", "Response", "Calibration",
    "PrintHead", "MotionPlatform", "LayerFormation", "FlowControl", "TimingMechanism", "TransformSequence",
    "SupportStructure", "TemperatureProfile", "MaterialFeed", "StressResponse", "FlexibilityControl",
    "MotionAxis", "PositionEncoder", "SafetyCircuit", "ErrorHandler", "TimingController", "DriveSystem",
    "FeedbackLoop", "SynchronizationUnit", "CoolingModule", "FirmwareModule"
]

TEST_CASE_NOUNS = [
    "Check", "Test", "Verification", "Analysis", "Simulation", "Alignment", "Responsiveness", "Sequence",
    "EfficiencyTest", "SelfTest", "Function", "Mitigation", "Detection", "FlowRate", "Prevention", "Delivery",
    "CleanlinessCheck", "ConversionEfficiency", "Alarm", "Resolution", "Retrieval", "Interaction", "Integration",
    "Lock", "Containment", "TimeoutTest", "StartupTest", "ShutdownTest", "StressTest", "RecoveryTest", "LoadTest",
    "MaterialTransformationTest", "LayerTimingCheck", "PlatformLevelingCheck", "TemperatureRampTest",
    "AxisMotionTest", "VibrationTest", "ThermalExpansionTest", "SignalStabilityCheck", "FirmwareUpdateTest",
    "DataLoggingVerification", "DiagnosticsTest", "EmergencyStopTest", "OverloadTest", "VoltageDropTest",
    "ResponseTimeCheck", "PositionAccuracyTest", "PrintQualityAnalysis"
]

TIME_UNITS_SUFFIXES = [
    'hr', 'hour', 'min', 'sec', 's', 'ms', 'millisecond', 'ns', 'nanosecond'
]

STATUS_OPTIONS = ["Passed", "Failed", "Unknown"]

def generate_requirement():
    parts = []

    if random.random() < 0.5:
        parts.append(f"{random.randint(1, 100)}_")

    main_part = random.choice(REQUIREMENT_PREFIXES) + random.choice(REQUIREMENT_NOUNS)
    parts.append(main_part)

    if random.random() < 0.5:
        parts.append(f"_{random.randint(1, 10)}")

    return ''.join(parts)

def generate_test_case_name():
    return random.choice(TEST_CASE_NOUNS)

def generate_duration():
    num_components = random.choice([1, 2])
    used_units = set()
    components = []

    while len(components) < num_components:
        unit = random.choice(TIME_UNITS_SUFFIXES)
        if unit in used_units:
            continue
        used_units.add(unit)

        value = random.randint(1, 100)
        components.append(f"{value} {unit}")

    return ' '.join(components)

def generate_status():
    return random.choice(STATUS_OPTIONS)

def main():
    with open(OUTPUT_FILENAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["Test case", "Duration", "Status"])

        for _ in range(NUM_LINES):
            requirement = generate_requirement()
            test_case_name = generate_test_case_name()
            test_case_field = f"{requirement}\\{test_case_name}"
            duration = generate_duration()
            status = generate_status()
            writer.writerow([test_case_field, duration, status])

    print(f"Generated {NUM_LINES} rows of test data in '{OUTPUT_FILENAME}'")

if __name__ == "__main__":
    main()
