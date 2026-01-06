# Plan: Build a Simple "Calculator" Agent with IBM watsonx Orchestrate

This plan outlines the steps to create a generative AI agent that uses a custom tool (a simple calculator) to perform math operations. This demonstrates the core concept of "Agentic AI" where the LLM uses tools to solve problems it can't (or shouldn't) solve with pure text prediction.

## 1. Setup & Configuration
- [ ] **Verify Environment**: Ensure `ibm-watsonx-orchestrate` and `python-dotenv` are installed (already in `requirements.txt`).
- [ ] **Configure Credentials**: (User needs to do this manually in `.env`)
    - `IBM_CLOUD_API_KEY`
    - `IBM_WATSONX_ORCHESTRATE_ENDPOINT`

## 2. Implement the Tool (The "Calculator")
- [ ] **Create `tools.py`**: Define a Python function `calculate(operation, a, b)` that performs basic arithmetic.
- [ ] **Define Tool Schema**: Create the Pydantic model or JSON schema that describes this tool to the agent (so the AI knows *how* to use it).

## 3. Implement the Agent
- [ ] **Create `agent.py`**:
    - Initialize the `OrchestrateClient` using credentials.
    - Register the `calculate` tool with the client.
    - Initialize the Agent with a base LLM (e.g., `granite-chat` or similar available model).
    - Give the agent instructions (system prompt): "You are a helpful assistant that can perform calculations."

## 4. Run & Test
- [ ] **Create `main.py`** (or update existing):
    - Run a loop that accepts user input.
    - Pass input to the agent.
    - Print the agent's response (which should include the tool usage result).
- [ ] **Test Queries**:
    - "What is 25 * 4?"
    - "Add 123 and 456."

## 5. Documentation
- [ ] **Create `TUTORIAL.md`**: A comprehensive guide for others to reproduce this.
    - Prerequisites.
    - Explanation of the code (Tools, Agent, Execution).
    - How to run it.
    - Example output.

## Technical Details (Mental Draft)
*   **Library**: `ibm_watsonx_orchestrate`
*   **Tool Definition**: The SDK likely supports `@tool` decorators or explicit schema registration. I will assume a standard function-calling pattern common in modern SDKs. *Self-correction: Since I can't see the full SDK docs, I will use a standard generic structure for the tool definition and adjust if linter/runtime errors occur.*
