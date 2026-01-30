import ollama
import json
import sys
import argparse

SYSTEM_PROMPT = """
You are an Expert QA Engineer. Your task is to generate detailed software test cases based on the provided requirements.
You MUST respond ONLY with a valid JSON array of objects. Do not include any conversational text, markdown formatting (like ```json), or explanations outside the JSON.

Each test case object must have exactly these keys:
- id: A string (e.g., "TC-001")
- title: A descriptive string
- scenario: A brief explanation of the test scenario or objective
- pre_conditions: A string
- steps: A list of strings
- expected_result: A string
- priority: One of "High", "Medium", "Low"

Generate a mix of happy path, negative, and edge case scenarios.
"""

def generate_test_cases(prompt, model='llama3.2'):
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': f"Requirements: {prompt}"}
            ]
        )
        
        content = response['message']['content'].strip()
        
        # Robust JSON Extraction: Find the first '[' and last ']'
        try:
            start_index = content.find('[')
            end_index = content.rfind(']')
            
            if start_index != -1 and end_index != -1:
                json_str = content[start_index:end_index + 1]
                return json.loads(json_str)
            else:
                # Fallback to direct load
                return json.loads(content)
        except json.JSONDecodeError:
            # Final attempt: strip common markdown artifacts
            content = content.replace("```json", "").replace("```", "").strip()
            try:
                # Re-try extraction from cleaned content
                start_index = content.find('[')
                end_index = content.rfind(']')
                if start_index != -1 and end_index != -1:
                    return json.loads(content[start_index:end_index + 1])
                return json.loads(content)
            except json.JSONDecodeError as je:
                return {"error": "Invalid JSON returned from model", "raw": content}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="User requirements for test case generation")
    parser.add_argument("--model", default="llama3.2", help="Ollama model to use")
    args = parser.parse_args()

    result = generate_test_cases(args.prompt, args.model)
    print(json.dumps(result))
