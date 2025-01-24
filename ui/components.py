import streamlit as st

from core.session_manager import SessionManager
from utils.constants import UIElements


class LabelManager:
    @staticmethod
    def render_label_input(placeholder: str):
        st.text_input(
            "Add new intent label",
            key="new_label",
            placeholder=placeholder,
            on_change=lambda: SessionManager.add_label(st.session_state.new_label)
        )

    @staticmethod
    def render_label_list(labels: list, no_labels_message: str):
        if not labels:
            st.info(no_labels_message)
            return

        for label in labels:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.text(label)
            with col2:
                if st.button(UIElements.DELETE_BUTTON.value, key=f"delete_{label}"):
                    SessionManager.remove_label(label)


class ResultsDisplay:
    @staticmethod
    def show_results(result, message: str):
        st.markdown("### 📊 Analysis Results")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Detected Intent:")
            st.markdown(f"**{result.class_name}**")

        st.markdown("#### Original Message:")
        st.info(message)

        st.markdown("#### Model Confidence:")
        st.progress(UIElements.CONFIDENCE_DEFAULT.value)