from enum import Enum

class SessionKeys(Enum):
    LABELS = "labels"
    MODEL = "model"
    NEW_LABEL = "new_label"

class UIElements(Enum):
    DELETE_BUTTON = "🗑️"
    CONFIDENCE_DEFAULT = 0.85