from agents import Agent, Runner, trace, function_tool
from connection import config
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Default poem (Allama Iqbal's verse on praising Pakistani youth)
default_poem = """
Iqbal is not hopeless from the barren land of his nation;  
A little care, and this soil is richly fertile, O cup-bearer!
"""

# Lyrics Poetry Agent (ghazal, emotional, musical form)
lyrics_agent = Agent(
    name='Lyrics Agent',
    instructions="""
    You are a poetry analyzer expert in identifying lyrical poetry.
    If the poem contains deep emotions, musical rhythm, or expressions of personal feelings (like love, pain, patriotism),
    classify it as lyrical. Give a brief explanation on why it's lyrical.
    """
)

# Narrative Poetry Agent (storytelling form)
narrative_agent = Agent(
    name="Narrative Agent",
    instructions="""
    You are a poetry analyzer expert in identifying narrative poetry.
    If the poem tells a story or has a plot with characters and events,
    classify it as narrative. Provide a short explanation of how the poem tells a story.
    """
)

# Dramatic Poetry Agent (dialogue-based, performance form)
dramatic_agent = Agent(
    name="Dramatic Agent",
    instructions="""
    You are a poetry analyzer expert in identifying dramatic poetry.
    If the poem involves dialogue, monologues, or is meant to be performed (like a scene or drama),
    classify it as dramatic. Explain why it fits the dramatic style.
    """
)

# Triage Agent (routes to the right agent)
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
    You are a triage poetry agent. Your task is to analyze the given poem
    and decide whether it is lyrical, narrative, or dramatic.
    Based on your judgment, pass the poem to the correct specialized agent.
    
    Use the following:
    - Lyrical: emotions, feelings, musicality
    - Narrative: story, plot, characters
    - Dramatic: dialogue, monologue, stage/performance style
    """,
    handoffs=[lyrics_agent, narrative_agent, dramatic_agent],
)

# Main function to run the Poetry Analyzer
async def main():
    with trace("Poetry Analyzer"):
        result = await Runner.run(
            triage_agent,
            default_poem,
            run_config=config
        )
        print("Final Analysis:\n", result.final_output)
        print("Last Agent Selected:", result.last_agent.name)

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
