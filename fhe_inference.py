import openfhe
import numpy as np
import pandas as pd
import joblib
import json

# Function to perform FHE inference
def perform_fhe_inference(encrypted_input, cc, public_key, mult_key, rot_keys):
    """
    Performs FHE inference on the encrypted input.

    Args:
        encrypted_input: The encrypted input ciphertext.
        cc: The cryptocontext.
        public_key: The public key.
        mult_key: The multiplication key.
        rot_keys: The rotation keys.

    Returns:
        The encrypted prediction.
    """

    # Load the model and scaler
    model = joblib.load("model.joblib")
    scaler = joblib.load("scaler.joblib")

    # Extract the coefficients and intercept from the model
    coefficients = model.coef_
    intercept = model.intercept_

    # Perform the FHE computation
    encrypted_prediction = cc.EvalMult(encrypted_input, coefficients[0])
    for i in range(1, len(coefficients)):
        encrypted_prediction = cc.EvalAdd(encrypted_prediction, cc.EvalMult(encrypted_input, coefficients[i]))
    encrypted_prediction = cc.EvalAdd(encrypted_prediction, intercept)

    return encrypted_prediction


if __name__ == "__main__":
    # Load the test case
    with open("test_case.json", "r") as f:
        test_case = json.load(f)[0]

    # Load the cryptocontext, public key, multiplication key, and rotation keys
    cc = openfhe.deserialize_crypto_context_binary("cc.bin")
    public_key = openfhe.deserialize_public_key_binary("pub.bin", cc)
    mult_key = openfhe.deserialize_eval_mult_key_binary("mult.bin", cc)
    rot_keys = openfhe.deserialize_rotation_keys_binary("rot.bin", cc)
    secret_key = openfhe.deserialize_secret_key_binary("secret_key", cc)

    # Get the input vector from the test case
    input_vector = np.array(test_case["runs"][0]["input"][0]["value"])

    # Encrypt the input vector
    plaintext = openfhe.Plaintext(input_vector)
    encrypted_input = cc.Encrypt(public_key, plaintext)

    # Perform FHE inference
    encrypted_prediction = perform_fhe_inference(encrypted_input, cc, public_key, mult_key, rot_keys)

    # Decrypt the prediction
    decrypted_prediction = cc.Decrypt(secret_key, encrypted_prediction)

    # Get the expected output from the test case
    expected_output = test_case["runs"][0]["output"][0]

    # Print the difference between the predicted and expected values
    print("Predicted value:", decrypted_prediction)
    print("Expected value:", expected_output)
    print("Difference:", decrypted_prediction - expected_output)