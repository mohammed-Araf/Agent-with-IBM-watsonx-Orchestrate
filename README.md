# Agent with IBM watsonx Orchestrate

This project demonstrates how to build a simple Generative AI agent using the IBM watsonx Orchestrate Python SDK. The agent is designed to perform a specific task—basic arithmetic calculations—by utilizing a custom "calculator" tool. This serves as a foundational example of "Agentic AI," where LLMs leverage external tools to solve problems accurately.

## ⚠️ Note on Agent Development Kit (ADK)
This repository demonstrates a **Python SDK** implementation. For the official IBM recommendation using the new **Agent Development Kit (ADK)** with YAML configuration and CLI tools, please refer to the [IBM watsonx Orchestrate Developer Portal](https://developer.watson-orchestrate.ibm.com/).

## 🚀 Features

*   **Generative AI Agent**: Uses IBM watsonx Orchestrate to power a conversational agent.
*   **Custom Tool Integration**: Includes a Python-based "Calculator" tool that the agent can invoke.
*   **Simple CLI Interface**: Interact with the agent through a user-friendly command-line interface.
*   **Step-by-Step Tutorial**: Includes a detailed [TUTORIAL.md](TUTORIAL.md) guide for learning and reproduction.

## 📂 Project Structure

*   `main.py`: The entry point for running the agent in the CLI.
*   `tools.py`: Defines the `calculate` tool function using the `@tool` decorator.
*   `agent.py`: Handles the initialization and configuration of the Orchestrate agent.
*   `TUTORIAL.md`: A comprehensive guide explaining the code and setup process.

## 🛠️ Quick Start

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/mohammed-Araf/Agent-with-IBM-watsonx-Orchestrate.git
    cd Agent-with-IBM-watsonx-Orchestrate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    Create a `.env` file and add your IBM Cloud credentials:
    ```ini
    IBM_CLOUD_API_KEY=your_api_key
    IBM_WATSONX_ORCHESTRATE_ENDPOINT=https://your-instance-url
    ```
    *(See [TUTORIAL.md](TUTORIAL.md#where-to-find-these-credentials) for instructions on finding your API Key and Endpoint)*

4.  **Run the Agent**:
    ```bash
    python main.py
    ```

## 📖 Learn More

For a deep dive into how this agent was built and how the code works, check out the **[TUTORIAL.md](TUTORIAL.md)** file included in this repository.

## 🔗 Resources
*   **[IBM watsonx Orchestrate Developer Portal](https://developer.watson-orchestrate.ibm.com/)** (Recommended for new developers)
*   [IBM watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base)
*   [IBM watsonx Orchestrate Python SDK](https://pypi.org/project/ibm-watsonx-orchestrate/)
