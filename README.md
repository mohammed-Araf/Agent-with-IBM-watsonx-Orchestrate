# IBM watsonx Orchestrate Python Project

This project is a starting point for developing with IBM watsonx Orchestrate using the Python SDK.

## Prerequisites

*   Python 3.11+
*   IBM Cloud Account with watsonx Orchestrate service

## Setup Instructions

1.  **Clone the repository** (if you haven't already).

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: If `requirements.txt` is missing, install manually:*
    ```bash
    pip install ibm-watsonx-orchestrate python-dotenv
    ```

4.  **Configure Environment Variables:**
    *   Rename `.env` (if created) or create a new `.env` file based on the example.
    *   Add your IBM Cloud API Key and watsonx Orchestrate Endpoint.
    ```
    IBM_CLOUD_API_KEY=your_actual_api_key
    IBM_WATSONX_ORCHESTRATE_ENDPOINT=https://your-instance-url
    ```

## Running the Verification Script

To check if everything is set up correctly, run:

```bash
python verify_setup.py
```

## Next Steps

*   Explore the `ibm-watsonx-orchestrate` SDK documentation.
*   Build your agent logic in `main.py` or new files.
*   Use the `orchestrate` CLI for advanced management (if installed via the SDK).

## Useful Links
*   [IBM watsonx Orchestrate Documentation](https://cloud.ibm.com/docs/watsonx-orchestrate)
*   [PyPI Package](https://pypi.org/project/ibm-watsonx-orchestrate/)
