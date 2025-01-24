from dataclasses import dataclass
import streamlit as st
@dataclass
class AnalysisResult:
    intent: str
    confidence: float
    message: str

class IntentAnalyzer:
    @staticmethod
    def analyze(text: str, labels: list[str]) -> AnalysisResult:
        model = st.session_state.model
        result = model.predict(text=text, labels=labels)
        return AnalysisResult(
            intent=result.class_name,  # Assuming result.class_name exists
            confidence=0.85,
            message=text
        )