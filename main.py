import os
import sys
from agent import create_agent

def main():
    print("----------------------------------------------------------------")
    print("  IBM watsonx Orchestrate - Simple Calculator Agent Demo")
    print("----------------------------------------------------------------")
    
    try:
        # Initialize the agent logic
        # Note: In a real deployment, this would connect to the live service.
        # Since we are in a dev environment without live creds, this might raise errors
        # if the SDK tries to connect immediately.
        client, tools = create_agent()
        print("Agent initialized successfully.")
        
        # Simple REPL (Read-Eval-Print Loop)
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            print("Agent: (Thinking...)")
            
            # ------------------------------------------------------------------
            # SIMULATION LOGIC
            # Since we cannot call the actual LLM API without a valid key,
            # we will simulate the agent's decision-making process here.
            # ------------------------------------------------------------------
            
            response = ""
            
            # Simple keyword matching to simulate "Intent Recognition"
            if "add" in user_input or "+" in user_input:
                # Extract numbers (very naive implementation for demo purposes)
                import re
                nums = [float(n) for n in re.findall(r'-?\d+\.?\d*', user_input)]
                if len(nums) >= 2:
                    tool_func = tools[0] # calculate
                    result = tool_func("add", nums[0], nums[1])
                    response = f"I'll use my calculator tool. The result of adding {nums[0]} and {nums[1]} is {result}."
                else:
                    response = "I see you want to add, but I couldn't find two numbers."
            
            elif "multiply" in user_input or "*" in user_input:
                import re
                nums = [float(n) for n in re.findall(r'-?\d+\.?\d*', user_input)]
                if len(nums) >= 2:
                    tool_func = tools[0] # calculate
                    result = tool_func("multiply", nums[0], nums[1])
                    response = f"Using the calculator: {nums[0]} * {nums[1]} = {result}."
                else:
                    response = "Please provide two numbers to multiply."
            
            else:
                response = "I am a simple calculator agent. I can add or multiply numbers. Try asking 'What is 5 + 5?'"

            print(f"Agent: {response}")

    except ValueError as e:
        print(f"\nConfiguration Error: {e}")
        print("Please check your .env file.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        # For debugging purposes only
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
