from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='simple_agent',
    description='Welcome Agent',
    instruction='Welcome user with puzzling questions and phrases. Always respond with complex question',
)
