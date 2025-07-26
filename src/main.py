import sys
import json
from models import CircleInput
from calculator import calculate_properties

def main():
    """
    Main loop to read from stdin, process data, and write to stdout.
    This script acts as a sidecar process for the main Tauri application.
    """
    for line in sys.stdin:
        try:
            # parse the input line as JSON
            input_data = json.loads(line)
            
            # extract payload and metadata
            payload = input_data.get("payload", {})
            metadata = input_data.get("metadata", {})
            center_coords = metadata.get("center", {"x": 0, "y": 0})

            circle_input = CircleInput(**payload)

            # call the calculation function
            properties = calculate_properties(circle_input, center_coords)

            # convert the result to JSON
            output_json = json.dumps(properties.to_json())

            # write the output to stdout
            print(output_json)
            sys.stdout.flush()

        except json.JSONDecodeError as e:
            error_message = json.dumps({"error": f"Invalid JSON input: {e}"})
            print(error_message, file=sys.stderr)
            sys.stderr.flush()
        except Exception as e:
            error_message = json.dumps({"error": f"An unexpected error occurred: {e}"})
            print(error_message, file=sys.stderr)
            sys.stderr.flush()

if __name__ == "__main__":
    main()