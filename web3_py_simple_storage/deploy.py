from solcx import compile_standard, install_solc
import json

with open("SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

print("Installing...")
install_solc("0.6.0")
# compile our solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)
# print(compiled_sol)

# with open("compiled_code.json", "w") as file:
# json.dump(compiled_sol, file)
