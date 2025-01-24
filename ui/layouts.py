import streamlit as st

from config.config import Config
from core.intent_analyzer import IntentAnalyzer
from ui.components import LabelManager, ResultsDisplay


class AppLayout:
    def __init__(self):
        self.config = Config()

    def setup_page(self):
        page_config = {
            "page_title": self.config.app_config["page_title"],
            "page_icon": self.config.app_config["page_icon"],
            "layout": self.config.app_config["layout"]
        }
        st.set_page_config(**page_config)
        st.title("🤖 Self-Learning Customer Support Desk")
        st.subheader("AI-Driven Intent Detection Engine for Precision Insights")

    def render_sidebar(self):
        with st.sidebar:
            st.header("Intent Label Management")
            LabelManager.render_label_input(
                self.config.ui_config["labels"]["add_placeholder"]
            )
            st.subheader("Current Labels")
            LabelManager.render_label_list(
                st.session_state.labels,
                self.config.ui_config["labels"]["no_labels_message"]
            )

    def render_main_content(self):
        st.markdown("---")
        st.subheader("📝 Customer Message Analysis")

        text = st.text_area(
            "Enter customer message",
            placeholder=self.config.ui_config["messages"]["input_placeholder"],
            height=150
        )

        if st.button("Analyze Intent", type="primary",
                    disabled=len(st.session_state.labels) == 0):
            self._handle_analysis(text)

    def _handle_analysis(self, text: str):
        if not text:
            st.warning(self.config.ui_config["messages"]["empty_input"])
            return

        with st.spinner(self.config.ui_config["messages"]["analyzing"]):
            try:
                result = IntentAnalyzer.analyze(text, st.session_state.labels)
                st.markdown("### 📊 Analysis Results")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### Detected Intent:")
                    st.markdown(f"**{result.intent}**")  # Changed from result.class_name to result.intent

                st.markdown("#### Original Message:")
                st.info(result.message)

                st.markdown("#### Model Confidence:")
                st.progress(result.confidence)
            except Exception as e:
                st.error(self.config.ui_config["messages"]["error"].format(str(e)))