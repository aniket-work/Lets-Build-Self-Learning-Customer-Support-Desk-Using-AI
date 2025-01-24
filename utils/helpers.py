from typing import List, Any
import streamlit as st

def validate_label(label: str, existing_labels: List[str]) -> bool:
    return bool(label and label not in existing_labels)

def format_error_message(error: Exception) -> str:
    return f"Error: {str(error)}"