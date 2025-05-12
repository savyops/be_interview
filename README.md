# BE Interview

1. Billing
- Given that ChargeUser function has 20% failure rate. What would you do to improve the payment system reliability? Implement.
- Assume a user switched mid cycle to a new plan. For example: from yearly plan to monthly plan. Assuming the system charges users prepaid, how will you prorate the user? Write a function to determine the new end date for user's billing period
- What extra measure(s) would you implement in the ChargeUser logic

2. Dangerous Python Code Execution Sandbox
- Your AI product generates Python code from LLM prompts and executes it in a backend service. How would you design a secure and reliable system to run untrusted code?
- How would you scale this to 1000+ concurrent executions?
- How would you allow some imports (e.g., numpy) but not others (os)?
- How would you cache repeated code executions?

3. LLM Repititive Response
- Your application can calls an LLM for repititive questions
- How would you optimize this for cost without trading off accuracy.

4. Log Analysis
A service that collects log data, analyzes it and returns a report
- Can you point out the issues with the code?
- What would you do differently?
- To setup, 
    - cd to log_analysis folder
    - install dependencies as in requirements.txt 
    - run `uvicorn log_server:app`

