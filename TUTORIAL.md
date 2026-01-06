# Tutorial: Building a Generative AI Agent with a Custom Tool
**IBM watsonx Orchestrate**

This tutorial guides you through building a simple Generative AI agent that can perform a specific task—calculation—using a custom tool. This demonstrates the core concept of "Agentic AI," where a language model uses defined functions to solve problems accurately.

## 1. Prerequisites

Before you begin, ensure you have:
*   **Python 3.11+** installed.
*   An **IBM Cloud Account** with the **watsonx Orchestrate** service enabled.
*   Your **API Key** and **Service Endpoint URL**.

## 2. Project Setup

1.  **Clone or Create the Project Directory**:
    Ensure your folder has the following structure:
    ```
    /project-root
      ├── .env
      ├── requirements.txt
      ├── tools.py
      ├── agent.py
      └── main.py
    ```

2.  **Install Dependencies**:
    Create a `requirements.txt` file (or use the one provided):
    ```txt
    ibm-watsonx-orchestrate
    python-dotenv
    ```
    Run the installation:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your credentials:
    ```ini
    IBM_CLOUD_API_KEY=your_actual_api_key_here
    IBM_WATSONX_ORCHESTRATE_ENDPOINT=https://your-instance-url.ibm.com
    ```
    
    ### 🔑 Where to find these credentials?
    For detailed instructions on setting up your environment and finding credentials, please visit the **[IBM watsonx Orchestrate Developer Portal](https://developer.watson-orchestrate.ibm.com/)**.
    
    1.  **IBM_CLOUD_API_KEY**:
        *   Log in to [IBM Cloud](https://cloud.ibm.com).
        *   Go to **Manage** > **Access (IAM)**.
        *   Select **API keys** from the sidebar.
        *   Click **Create an IBM Cloud API key**.
    
    2.  **IBM_WATSONX_ORCHESTRATE_ENDPOINT**:
        *   If you are using the Developer Edition, follow the setup guide on the [Developer Portal](https://developer.watson-orchestrate.ibm.com/) to configure your environment using the ADK.
        *   The CLI command `orchestrate env add` helps configure these connections automatically in many cases.

## 3. The Code Explained

### Step 1: Define the Tool (`tools.py`)
Tools are functions that the agent can "call." We use the `@tool` decorator to register them.

```python
from ibm_watsonx_orchestrate.tools import tool

@tool
def calculate(operation: str, a: float, b: float) -> float:
    """
    Performs basic arithmetic operations.
    Args:
        operation: 'add', 'subtract', 'multiply', 'divide'
        a: First number
        b: Second number
    """
    if operation == 'add': return a + b
    elif operation == 'multiply': return a * b
    # ... (other operations)
```

### Step 2: Configure the Agent (`agent.py`)
This script initializes the client and prepares the tools for the agent.

```python
import os
from dotenv import load_dotenv
from ibm_watsonx_orchestrate import OrchestrateClient
from tools import calculate

load_dotenv()

def create_agent():
    api_key = os.getenv("IBM_CLOUD_API_KEY")
    client = OrchestrateClient(api_key=api_key, ...)
    return client, [calculate]
```

### Step 3: Run the Agent (`main.py`)
This script runs a loop where you can chat with the agent. In a real scenario, the SDK handles the routing of your text -> LLM -> Tool -> Result -> LLM -> Final Answer.

## 4. Running the Agent

Execute the main script:
```bash
python main.py
```

**Example Interaction:**
```
You: Calculate 50 * 25
Agent: (Thinking...)
Agent: Using the calculator: 50 * 25 = 1250.
```

## 5. Next Steps
*   **Add more tools**: Create a `get_weather(city)` function.
*   **Refine the Prompt**: Give the agent a personality in `agent.py`.
*   **Deploy**: Use the `ibm-watsonx-orchestrate` CLI to deploy your agent to the cloud.
