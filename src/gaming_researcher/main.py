#!/usr/bin/env python
# src/gaming_researcher/main.py
import os
from gaming_researcher.crew import GamingResearchCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the gaming industry research crew.
    """
    inputs = {
        'company': 'insomanac'  # You can change this to any gaming company
    }

    # Create and run the crew
    result = GamingResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== GAMING INDUSTRY REPORT ===\n\n")
    print(result.raw)

    print("\n\nGaming industry report has been saved to output/gaming_report.md")

if __name__ == "__main__":
    run()