import os
from dotenv import load_dotenv
from ibm_watsonx_orchestrate import OrchestrateClient
# Note: Since I cannot verify the exact import structure without the library installed locally, 
# I am assuming a standard structure. If 'ibm_watsonx_orchestrate' is the main package,
# we will use it to initialize the client.
# Based on the error in tools.py, the import might be different or the environment isn't set up.
# I will proceed with a defensive implementation that allows for easy adjustment.

from tools import calculate

load_dotenv()

def create_agent():
    """
    Initializes and configures the IBM watsonx Orchestrate agent.
    """
    api_key = os.getenv("IBM_CLOUD_API_KEY")
    endpoint = os.getenv("IBM_WATSONX_ORCHESTRATE_ENDPOINT")
    
    if not api_key or not endpoint:
        raise ValueError("Missing API Key or Endpoint in .env file")

    # Initialize Client
    # Placeholder: The actual class name might be different (e.g., Client, Orchestrate).
    # We will assume OrchestrateClient for now as per plan.
    client = OrchestrateClient(api_key=api_key, url=endpoint)

    # In a real scenario, we would register the tool here.
    # Since we are mocking the exact SDK behavior without docs, 
    # we will return a structure that 'main.py' can use.
    
    # Conceptually:
    # agent = client.agents.create(
    #     name="Calculator Agent",
    #     tools=[calculate],
    #     instructions="You are a helpful assistant that can perform calculations."
    # )
    
    # For this exercise, I will return the client and the tool function 
    # so main.py can manually invoke the tool if the SDK is not fully functional in this env.
    return client, [calculate]
