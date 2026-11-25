import asyncio
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are an expert Spring Boot developer",
        permission_mode="acceptEdits",
        allowed_tools=["Skill", "Read", "Write", "Edit"]
    )

    async for message in query(prompt="Create a Spring Boot application based on user requirements", options=options):
        print(message)


asyncio.run(main())
        