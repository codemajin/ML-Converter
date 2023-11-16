import pickle
from io import BytesIO
from typing import Dict

import joblib
import streamlit as st

from supports import CLASSIFICATION_SUPPORTS, REGRESSION_SUPPORTS, LANGUAGE_SUPPORTS


def select_model(model_type: str) -> str:
    """Select a trained machine learning model (class name in scikit-learn).

    Args:
        model_type (str): 'Classification' or 'Regression'

    Returns:
        str: Model class name in scikit-learn
    """
    if model_type == "Classification":
        return st.selectbox("**Model Selection**", [class_.__name__ for class_ in CLASSIFICATION_SUPPORTS])
    else:
        return st.selectbox("**Model Selection**", [class_.__name__ for class_ in REGRESSION_SUPPORTS])


def deserialize(uploaded_file: st.runtime.uploaded_file_manager.UploadedFile, serialization: str) -> object:
    """Deserialize uploaded files.

    Args:
        uploaded_file (st.runtime.uploaded_file_manager.UploadedFile): Uploaded files
        serialization (str): 'Pickle' or 'Joblib'

    Returns:
        object: Deserialized object (Trained machine learning model)
    """
    bytes_data = uploaded_file.getvalue()
    if serialization == "Pickle":
        return pickle.load(BytesIO(bytes_data))
    else:
        return joblib.load(BytesIO(bytes_data))


def inputs_column() -> Dict:
    """Setup inputs column.

    Returns:
        Dict: Inputs
    """
    model_type = st.radio("**Model Type**", ["Classification", "Regression"])
    model_choice = select_model(model_type)
    serialization = st.radio("**Serialization**", ["Pickle", "Joblib"])
    language_choice = st.selectbox("**Language Selection**", LANGUAGE_SUPPORTS.keys())
    uploaded_file = st.file_uploader("Choose a file")

    return {
        "model_type": model_type,
        "model_choice": model_choice,
        "serialization": serialization,
        "language_choice": language_choice,
        "uploaded_file": uploaded_file,
    }


def outputs_column(inputs: Dict) -> None:
    """Setup outputs column.

    Args:
        inputs (Dict): Inputs
    """
    if inputs["uploaded_file"] is not None:
        obj = deserialize(inputs["uploaded_file"], inputs["serialization"])
        if obj.__class__.__name__ == inputs["model_choice"]:
            code = LANGUAGE_SUPPORTS[inputs["language_choice"]](obj)
            st.code(code, language=inputs["language_choice"].lower().replace("#", "sharp"), line_numbers=True)
        else:
            st.error(f"""
                The uploaded model and the selected model do not match.\n
                Your Choice: {inputs['model_choice']}, Uploaded Model: {obj.__class__.__name__}
            """)
    else:
        st.empty()


def main() -> None:
    """Convert uploaded machine learning models into various languages.
    """
    st.set_page_config(page_title="Machine Learning Model Converter", page_icon="🧊", layout="wide")
    st.title("MLMC: Machine Learning Model Converter")
    st.write("Translate your machine learning models into various programming languages.")

    left_col, right_col = st.columns(2, gap="large")

    with left_col:
        inputs = inputs_column()

    with right_col:
        outputs_column(inputs)


if __name__ == "__main__":
    main()
