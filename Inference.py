import onnxruntime as ort
import numpy as np

session = ort.InferenceSession("models/titanic_model.onnx")

input_name = session.get_inputs()[0].name

output_name = session.get_outputs()[0].name

def predict(input_data):

    input_data = np.array(input_data, dtype=np.float32).reshape(1, -1)

    result = session.run([output_name], {input_name: input_data})

    probabilities = result[0][0]

    prediction = int(probabilities.item() > 0.5)

    return prediction


FEATURE_ORDER = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

def predict_from_dict(input_dict):
    input_list = [input_dict[feature] for feature in FEATURE_ORDER]
    return predict(input_list)

if __name__ == "__main__":
    example_input = {
        "Pclass": 1,
        "Sex": 0,
        "Age": 38,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 71.2833,
        "Embarked": 0
    }
    prediction = predict_from_dict(example_input)
    print(f"Predicted class: {prediction}")