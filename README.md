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