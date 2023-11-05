from textwrap import dedent

CONTRACTS = (
    dedent("""\
        contract {contract_name} {{
            uint {var1_name};
            function {func_name}(uint {arg1_name}) public {{ {var1_name} = {arg1_name}; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            uint public {var1_name} = 0;
            function {func_name}() public {{ {var1_name}++; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            bool public {var1_name} = false;
            function {func_name}() public {{ {var1_name} = !{var1_name}; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}() external payable {{}}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            string public {var1_name};
            function {func_name}(string calldata {arg1_name}) public {{ {var1_name} = {arg1_name}; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}() public {{ selfdestruct(payable(msg.sender)); }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            event {event_name}(uint indexed value);
            function {func_name}(uint {arg1_name}) public {{ emit {event_name}({arg1_name}); }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}() public view returns (uint) {{ return block.timestamp; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}() public view returns (address) {{ return msg.sender; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            bytes32 public {var1_name};
            function {func_name}(bytes32 {arg1_name}) public {{ {var1_name} = {arg1_name}; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}(address {arg1_name}) public {{ {arg1_name}.delegatecall(abi.encodeWithSignature("{func_call1}()")); }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}(uint {arg1_name}, uint b) public pure returns (uint) {{ return {arg1_name} * b; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}(uint {arg1_name}) public pure returns (bool) {{ return {arg1_name} % 2 == 0; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}(address {arg1_name}, address {arg2_name}, uint256 {arg3_name}) public {{ {arg1_name}.call(abi.encodeWithSignature("{func_call1}(address,uint256)", {arg2_name}, {arg3_name})); }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}() public view returns (uint) {{ return address(this).balance; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            bytes1 public {var1_name};
            function {func_name}(bytes1 {arg1_name}) public {{ {var1_name} = {arg1_name}; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            function {func_name}() public view returns (uint) {{ return block.difficulty; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            bool public {var1_name};
            function {func_name}(bool {arg1_name}) public {{ {var1_name} = {arg1_name}; }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            uint[] public {var1_name};
            function {func_name}(uint {arg1_name}) public {{ {var1_name}.push({arg1_name}); }}
        }}"""
    ),
    dedent("""\
        contract {contract_name} {{
            address {var1_name} = msg.sender;
            modifier {modifier_name}() {{ require(msg.sender == {var1_name}); _; }}
            function {func_name}() public {modifier_name} {{  }}
        }}"""
    )
)
