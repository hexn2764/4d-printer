import random
import csv
import os
import sys

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
    """
    Generates a random requirement identifier string composed of optional numeric prefix, a combined
    prefix+noun core, and an optional numeric suffix.

    The identifier simulates realistic engineering requirement names, with variability in format.
    For example: "42_MotorUnit_3", "HeatingModule", "SensorArray_7", etc.

    Returns:
        str: A formatted requirement identifier string.
    """
    parts = []

    if random.random() < 0.5:
        parts.append(f"{random.randint(1, 100)}_")

    main_part = random.choice(REQUIREMENT_PREFIXES) + random.choice(REQUIREMENT_NOUNS)
    parts.append(main_part)

    if random.random() < 0.5:
        parts.append(f"_{random.randint(1, 10)}")

    return ''.join(parts)

def generate_test_case_name():
    """
    Selects a random test case name from a predefined list of possible test case nouns.

    This simulates realistic test case names used in 4D printer testing scenarios.

    Returns:
        str: The name of the test case.
    """
    return random.choice(TEST_CASE_NOUNS)

def generate_duration():
    """
    Generates a random duration string composed of 1 or 2 time components.

    Each component consists of a randomly selected integer value and a randomly selected time unit suffix.
    The components are concatenated with a space separator. Units are guaranteed to be unique within one duration.

    Example outputs: "34 ms", "12 min 87 ms", "5 hr", etc.

    Returns:
        str: The formatted duration string.
    """
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
    """
    Randomly selects a test status from the predefined list of possible status values:
    "Passed", "Failed", or "Unknown".

    Returns:
        str: The test status string.
    """
    return random.choice(STATUS_OPTIONS)

def main():
    """
    Generates a CSV file containing simulated 4D printer test data.

    The CSV contains NUM_LINES rows, each with the following fields:
    - "Test case": Combination of requirement identifier and test case name.
    - "Duration": Simulated duration string.
    - "Status": Simulated test result status.

    The output is written to '4d_printer_test_data.csv' in the current script directory.

    No input arguments required.
    """
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
    if len(sys.argv) > 1:
        OUTPUT_FILENAME = sys.argv[1]
    else:
        OUTPUT_FILENAME = os.path.join(os.path.dirname(__file__), "4d_printer_test_data.csv")

    main()

