#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "openfhe.h"

using namespace lbcrypto;

int main() {
    // Load the test case
    std::ifstream test_case_file("test_case.json");
    std::string test_case_json((std::istreambuf_iterator<char>(test_case_file)),
                     std::istreambuf_iterator<char>());

    // Parse the test case JSON (replace with a proper JSON parsing library)
    // For simplicity, I'm assuming the test case JSON is a simple array of numbers
    std::vector<double> input_vector;
    // TODO: Implement JSON parsing

    // Load the crypto context, public key, secret key, mult key, and rot keys
    CryptoContext<DCRTPoly> cc = CryptoContextFactory<DCRTPoly>::DeserializeFromFile("cc.bin");
    PublicKey<DCRTPoly> public_key;
    {
        std::ifstream ifs("pub.bin", std::ios::binary);
        if (!ifs.is_open()) {
            std::cerr << "Cannot open serialization file." << std::endl;
            return 1;
        }
        public_key = PublicKey<DCRTPoly>(cc);
        public_key->Load(cc, ifs);
    }
    PrivateKey<DCRTPoly> secret_key;
    {
        std::ifstream ifs("secret_key", std::ios::binary);
        if (!ifs.is_open()) {
            std::cerr << "Cannot open serialization file." << std::endl;
            return 1;
        }
        secret_key = PrivateKey<DCRTPoly>(cc);
        secret_key->Load(cc, ifs);
    }
    EvalMultKey<DCRTPoly> mult_key;
        {
        std::ifstream ifs("mult.bin", std::ios::binary);
        if (!ifs.is_open()) {
            std::cerr << "Cannot open serialization file." << std::endl;
            return 1;
        }
        mult_key = EvalMultKey<DCRTPoly>(cc);
        mult_key->Load(cc, ifs);
    }
    EvalAutomorphismKey<DCRTPoly> rot_keys;
        {
        std::ifstream ifs("rot.bin", std::ios::binary);
        if (!ifs.is_open()) {
            std::cerr << "Cannot open serialization file." << std::endl;
            return 1;
        }
        rot_keys = EvalAutomorphismKey<DCRTPoly>(cc);
        rot_keys->Load(cc, ifs);
    }

    // Encrypt the input vector
    Plaintext plaintext = cc->MakeCKKSPackedPlaintext(input_vector);
    auto ciphertext = cc->Encrypt(public_key, plaintext);

    // Perform FHE inference (replace with the actual inference logic)
    auto encrypted_result = ciphertext; // Placeholder

    // Decrypt the result
    Plaintext decrypted_result;
    cc->Decrypt(secret_key, encrypted_result, &decrypted_result);

    // Print the result
    std::cout << "Result: " << decrypted_result << std::endl;

    return 0;
}