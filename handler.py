import json

def handler(event):
    try:
        # Extract the function code and inputs
        function_code = event.get("code", "")
        inputs = event.get("inputs", {})

        # Dynamically execute the function code
        exec(function_code, globals())
        # Call the function with the provided inputs
        result = globals()["function"](**inputs)

        # Return the result
        return {
            "statusCode": 200,
            "body": json.dumps({"result": result}),
        }
    except Exception as e:
        # Return an error message
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }