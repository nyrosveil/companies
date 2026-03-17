# TOOLS.md -- Solidity Smart Contract Engineer

## Core Skills

- `para-memory-files` - Memory operations and knowledge management
- `solidity-security` - Smart contract security patterns
- `web3-testing` - Comprehensive contract testing with Foundry/Hardhat

## Industry Tools

### Development
- **Solidity** - Smart contract programming language
- **Foundry** - Fast testing framework (forge, cast, anvil)
- **Hardhat** - Ethereum development environment
- **OpenZeppelin Contracts** - Audited contract library
- **Solmate** - Gas-optimized contract primitives

### Security & Auditing
- **Slither** - Static analysis tool
- **Mythril** - Security analysis tool
- **Echidna** - Fuzzing tester
- **Certora** - Formal verification

### Testing
- **Foundry** - Unit, fuzz, and invariant testing
- **Hardhat Network** - Local Ethereum network
- **Tenderly** - Simulation and debugging
- **Ganache** - Local blockchain for testing

### Deployment
- **Hardhat Deploy** - Deployment management
- **Foundry Script** - Deployment scripts
- **Tenderly** - Deployment simulation
- **OpenZeppelin Defender** - Secure deployment

### Upgrade Patterns
- **UUPS Proxy** - Universal Upgradeable Proxy
- **Transparent Proxy** - OpenZeppelin transparent proxy
- **Beacon Proxy** - EIP-1967 beacon pattern
- **Diamond Pattern** - EIP-2535 diamond standard

### Standards
- **ERC-20** - Fungible tokens
- **ERC-721** - Non-fungible tokens
- **ERC-1155** - Multi-token standard
- **ERC-4626** - Tokenized vaults
- **ERC-4337** - Account abstraction

## Integration Recommendations

- Use Foundry for fast testing and gas snapshots
- Implement UUPS proxies for upgradeable contracts
- Use OpenZeppelin Defender for secure deployments
- Set up Slither in CI for continuous security analysis
- Deploy with multi-sig ownership (Gnosis Safe)
