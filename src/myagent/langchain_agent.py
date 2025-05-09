from langchain_community.llms import Ollama
import textwrap
from langchain_community.tools import DuckDuckGoSearchResults

model = Ollama(model="llama3.2:latest")

search = DuckDuckGoSearchResults(k=5)
# Initialize DuckDuckGo with TOP 5 results only
search = DuckDuckGoSearchResults(k=5)  # Limits to 5 results

def generate_markdown_report(query: str) -> str:
    # Fetch search results
    results = search.run(query)
    
    # Generate structured summary
    prompt = f"""
    **Task:** Create a detailed, engaging Markdown report about: "{query}".
    
    **Search Results:**
    {results}
    
    **Format Requirements:**
    1. Start with "## [Emoji] Engaging Title" (make it catchy)
    2. Include sections: "### Overview", "### Key Breakthroughs", "### Implications", "### Synopsis"
    3. Write in concise, lively language with bullet points for readability
    4. Include 5 reference links at the end
    5. Use emojis sparingly for emphasis
    """
    
    report = model.invoke(prompt)
    
    # Format with consistent spacing
    return textwrap.dedent(f"""
    <!-- AUTO-GENERATED AI REPORT -->
    {report}
    """).strip()

# Example usage
if __name__ == "__main__":
    query = "Give me a detailed summary of Pushpa2 movie"
    markdown_report = generate_markdown_report(query)
    print(markdown_report)