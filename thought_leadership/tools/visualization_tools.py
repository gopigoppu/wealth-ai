from google.adk.tools import FunctionTool
from typing import Dict, List, Any


def breakdown_card(data: Dict[str, float]) -> str:
    """
    Render a 'portfolio breakdown card' summary, with visual bars and bullet points.
    Handles missing, malformed, or empty input gracefully.
    """
    try:
        if not isinstance(data, dict):
            return "**Unable to generate breakdown: Input is not a dictionary.**"
        if not data:
            return "**No allocation data available.**"
        cleaned = {k: float(v) for k, v in data.items() if v is not None and (isinstance(
            v, int) or isinstance(v, float) or (isinstance(v, str) and v.replace('.', '', 1).isdigit()))}
        if not cleaned or sum(cleaned.values()) == 0:
            return "**No valid nonzero allocation data to display.**"
        total = sum(cleaned.values())
        lines = []
        for label, value in cleaned.items():
            pct = round(100 * value / total)
            # Ensure minimum bar if value is nonzero, max 20 chars
            bar_len = max(1, int(round(20 * value / total))
                          ) if value > 0 else 0
            bar = "█" * bar_len + '-' * (20 - bar_len)
            lines.append(f"- **{label}**: ${value:,.0f}  ({pct}% | {bar})")
        return "### Portfolio Allocation\n" + "\n".join(lines)
    except Exception as e:
        return f"**Could not generate breakdown card due to unexpected error:** {str(e)}"


def table_tool(data: List[Dict[str, Any]]) -> str:
    """
    Render a list of dicts as a markdown table. Always shows a user-friendly message if input is bad or missing.
    """
    try:
        if not isinstance(data, list) or not data or not all(isinstance(row, dict) for row in data):
            return "**No valid table data to display.**"
        headers = list(data[0].keys())
        if not headers:
            return "**No table headers found.**"
        table_lines = [" | ".join(headers), " | ".join(["---"] * len(headers))]
        for row in data:
            # Ensure row has all headers; blank if missing
            table_lines.append(" | ".join(str(row.get(h, ""))
                               for h in headers))
        if len(table_lines) <= 2:
            return "**Table is empty. No data to show.**"
        return "\n".join(table_lines)
    except Exception as e:
        return f"**Could not generate table due to error:** {str(e)}"


breakdown_card = FunctionTool(breakdown_card)
table_tool = FunctionTool(table_tool)
