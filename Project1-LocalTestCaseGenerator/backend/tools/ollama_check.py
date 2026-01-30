import ollama
import sys

def check_ollama():
    try:
        print("Checking Ollama connection...")
        response = ollama.list()
        print("Connected successfully!")
        
        # Debug structure
        # print(f"DEBUG: {response}")
        
        models = response.get('models', [])
        found = False
        for m in models:
            # The model object might be an object or a dict depending on version
            name = getattr(m, 'model', None) or m.get('model', '')
            if 'llama3.2' in name:
                found = True
                print(f"Model found: {name}")
                break
        
        if found:
            print("Performing handshake test with llama3.2...")
            response = ollama.chat(model='llama3.2', messages=[
                {'role': 'user', 'content': 'Respond with only the word: SUCCESS'}
            ])
            content = response['message']['content'].strip()
            print(f"Handshake response: {content}")
            return True
        else:
            print("Model 'llama3.2' NOT found in the list.")
            return False
            
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if check_ollama():
        sys.exit(0)
    else:
        sys.exit(1)
