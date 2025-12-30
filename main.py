import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt
from call_function import available_functions, call_function

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY is not set in environment variables.")

def main():
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    client = genai.Client(api_key=api_key)
    
    # Loop for multiple iterations
    for iteration in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            ),
        )
        
        if response.usage_metadata is None:
            raise RuntimeError("Failed API request: Response metadata is missing.")
        
        if args.verbose:
            prompt_token_count = response.usage_metadata.prompt_token_count
            candidate_token_count = response.usage_metadata.candidates_token_count
            if iteration == 0:
                print(f"User prompt: {args.user_prompt}")
            print(f"Iteration {iteration + 1}: Prompt tokens: {prompt_token_count}, Response tokens: {candidate_token_count}")
        
        # Add candidates to conversation history
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        
        # Check for function calls
        if response.candidates[0].content.parts[0].function_call:
            function_calls = [part.function_call for part in response.candidates[0].content.parts if part.function_call]
            function_results = []
            
            for function_call in function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)
                
                # Validate the result
                if not function_call_result.parts:
                    raise RuntimeError("Function call result has no parts")
                
                if function_call_result.parts[0].function_response is None:
                    raise RuntimeError("Function response is None")
                
                if function_call_result.parts[0].function_response.response is None:
                    raise RuntimeError("Function response.response is None")
                
                function_results.append(function_call_result.parts[0])
                
                # Print result only in verbose mode
                if args.verbose:
                    result_response = function_call_result.parts[0].function_response.response
                    # Extract the actual result from the dict wrapper
                    if isinstance(result_response, dict) and "result" in result_response:
                        actual_result = result_response["result"]
                    else:
                        actual_result = result_response
                    print(f"-> {actual_result}")
            
            # Add function results to messages
            messages.append(types.Content(role="user", parts=function_results))
        else:
            # No function calls - final response
            print("Final response:")
            print(response.text)
            return
    
    # If we reach here, we've hit the iteration limit
    print("Error: Maximum iterations reached without final response")
    exit(1)

if __name__ == "__main__":
    main()
