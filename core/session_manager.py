import streamlit as st
from open_intent_classifier.model import IntentClassifier
from utils.constants import SessionKeys



import streamlit as st
from open_intent_classifier.model import IntentClassifier
from utils.constants import SessionKeys

class SessionManager:
    @staticmethod
    def initialize() -> None:
        if SessionKeys.LABELS.value not in st.session_state:
            st.session_state[SessionKeys.LABELS.value] = []
        if SessionKeys.MODEL.value not in st.session_state:
            st.session_state[SessionKeys.MODEL.value] = IntentClassifier()

    @staticmethod
    def add_label(label: str) -> None:
        if label and label not in st.session_state[SessionKeys.LABELS.value]:
            st.session_state[SessionKeys.LABELS.value].append(label)
            st.session_state[SessionKeys.NEW_LABEL.value] = ""

    @staticmethod
    def remove_label(label: str) -> None:
        st.session_state[SessionKeys.LABELS.value].remove(label)