"""
This module contains a cyber security assistant for analyzing microchip code.
"""
import re

def analyze_security(code: str) -> str:
    """
    Analyzes microchip code for security vulnerabilities (simulation).

    In a real implementation, this would use a static analysis tool.
    For this placeholder, it returns a hardcoded string based on keywords
    in the code.

    Args:
        code (str): The C++ code to analyze.

    Returns:
        str: A security analysis report.
    """
    report = "Security Analysis Report:\n"
    if re.search(r'\bstrcpy\b', code):
        report += "- High: Use of `strcpy` is deprecated and can lead to buffer overflows. Use `strncpy` instead.\n"
    if re.search(r'\bsprintf\b', code):
        report += "- High: Use of `sprintf` is deprecated and can lead to buffer overflows. Use `snprintf` instead.\n"
    if re.search(r'\bgets\b', code):
        report += "- Critical: Use of `gets` is extremely dangerous and can lead to buffer overflows. Use `fgets` instead.\n"
    if "delay(" in code:
        report += "- Low: Use of `delay` can make the device unresponsive. Consider using a non-blocking approach.\n"

    if report == "Security Analysis Report:\n":
        report += "No major security vulnerabilities found."

    return report
