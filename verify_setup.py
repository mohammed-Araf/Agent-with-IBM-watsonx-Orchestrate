import os
from dotenv import load_dotenv
# Note: The import below is based on the package name we installed. 
# Since we don't have the exact API reference, we'll verify the import path.
# Based on PyPI, the package is ibm-watsonx-orchestrate.
# Common convention is underscores.

# Load environment variables
load_dotenv()

def main():
    # Initialize the client
    # Note: In a real scenario, you would need valid credentials
    print("Initializing IBM watsonx Orchestrate Setup Verification...")
    
    api_key = os.getenv("IBM_CLOUD_API_KEY")
    service_url = os.getenv("IBM_WATSONX_ORCHESTRATE_ENDPOINT")
    
    if not api_key or api_key == "your_api_key_here":
        print("Warning: IBM_CLOUD_API_KEY is not set to a valid key in .env file.")
        print("Please update .env with your actual IBM Cloud API Key.")
    else:
        print("API Key found (masked): " + "*" * (len(api_key) - 4) + api_key[-4:])

    if not service_url:
        print("Warning: IBM_WATSONX_ORCHESTRATE_ENDPOINT not set in .env file.")
    else:
        print(f"Service URL: {service_url}")

    try:
        # Attempt to import the library to verify installation
        import ibm_watsonx_orchestrate
        print(f"Successfully imported ibm_watsonx_orchestrate version: {ibm_watsonx_orchestrate.__version__}")
        
        print("\nSetup verification complete. You are ready to start building!")
        
    except ImportError:
        print("Error: Could not import ibm_watsonx_orchestrate. Please ensure the package is installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
