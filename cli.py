import argparse
import openfhe
import numpy as np
import pandas as pd
import joblib
from fhe_inference import perform_fhe_inference

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="FHE-based house price prediction CLI")
    parser.add_argument("--sample", type=str, required=True, help="Path to the input ciphertext file")
    parser.add_argument("--output", type=str, required=True, help="Path to the output ciphertext file")
    parser.add_argument("--cc", type=str, required=True, help="Path to the serialized crypto context file")
    parser.add_argument("--key_pub", type=str, required=True, help="Path to the public key file")
    parser.add_argument("--key_mult", type=str, required=True, help="Path to the evaluation (multiplication) key file")
    parser.add_argument("--key_rot", type=str, required=True, help="Path to the rotation key file")
    args = parser.parse_args()

    # Load the cryptocontext, public key, multiplication key, and rotation keys
    cc = openfhe.deserialize_crypto_context_binary(args.cc)
    public_key = openfhe.deserialize_public_key_binary(args.key_pub, cc)
    mult_key = openfhe.deserialize_eval_mult_key_binary(args.key_mult, cc)
    rot_keys = openfhe.deserialize_rotation_keys_binary(args.key_rot, cc)

    # Load the encrypted input
    encrypted_input = openfhe.deserialize_ciphertext_binary(args.sample, cc)

    # Perform FHE inference
    encrypted_prediction = perform_fhe_inference(encrypted_input, cc, public_key, mult_key, rot_keys)

    # Serialize the encrypted prediction to a file
    openfhe.serialize_ciphertext_binary(args.output, encrypted_prediction)

    print("FHE inference completed. The encrypted prediction is saved in", args.output)

if __name__ == "__main__":
    main()