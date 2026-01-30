# SOP: Automated Test Case Generation

## Goal
To transform raw user requirements into a structured, prioritized list of software test cases using the `llama3.2` model via Ollama.

## Inputs
- `user_requirement`: A string describing the feature or functionality to be tested.
- `output_format`: JSON (as defined in `gemini.md`).

## Tool Logic
1. **Sanitize Input**: Ensure the user requirement is not empty and is safely passed to the tool.
2. **Construct System Prompt**:
   - Define the persona: "Expert Software Quality Assurance Engineer".
   - Specify the output schema strictly: Array of objects with keys `id`, `title`, `pre_conditions`, `steps` (array), `expected_result`, `priority`.
   - Enforce JSON-only output.
3. **Invoke Ollama Tool**: Call `tools/ollama_generator.py` with the combined prompt.
4. **Validation**: Parse the output to ensure it matches the schema.

## Edge Cases
- **Vague Requirements**: If the requirement is too short, the model should attempt to extrapolate logical test cases but flag them as "assumptions".
- **Empty Requirements**: Return an error message to the user.
- **Model Timeout**: If Ollama takes too long, handle gracefully with a 503 error.

## Success Criteria
- Valid JSON returned.
- Minimum of 3 test cases generated per requirement.
- Covers at least one "happy path" and one "edge case".
