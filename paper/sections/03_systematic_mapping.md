# 3. Systematic Mapping: Software Engineering → Biological Engineering

## 3.1 Mapping Framework

Not all software engineering concepts transfer equally to biology. We propose a three-category framework for analyzing mappings:

| Mapping Type | Definition | Transfer Difficulty |
|--------------|------------|---------------------|
| **Direct** | Concept transfers with minimal adaptation | Low |
| **Analogous** | Core idea transfers but requires domain-specific adaptation | Medium |
| **Novel** | No software equivalent; requires new solutions | High |

This categorization helps practitioners understand which software practices can be immediately adopted, which require careful adaptation, and which represent open research challenges.

## 3.2 Direct Mappings

These concepts can be transferred almost verbatim from software engineering:

### Semantic Versioning

Software's Semantic Versioning (SemVer) specification defines version numbers as MAJOR.MINOR.PATCH:
- MAJOR: incompatible API changes
- MINOR: backward-compatible functionality additions
- PATCH: backward-compatible bug fixes

This transfers directly to Bio-Components:
- **MAJOR**: Interface-incompatible changes (e.g., different input signal type)
- **MINOR**: Backward-compatible enhancements (e.g., improved force output)
- **PATCH**: Optimizations without interface changes (e.g., faster response time)

Example: `muscle-actuator-human-skeletal@2.3.1`
- Version 2: Second-generation interface (incompatible with v1)
- .3: Third feature addition since v2.0
- .1: First optimization patch

### Dependency Declaration

Software package manifests (package.json, requirements.txt) declare dependencies with version constraints:
```json
{
  "dependencies": {
    "tensorflow": "^2.0.0",
    "numpy": ">=1.19,<2.0"
  }
}
```

Bio-Component manifests can use identical syntax:
```yaml
dependencies:
  perfusion-medium: "DMEM@^1.0"
  oxygen-supply: ">=15%"
  temperature-control: "37±2°C"
  co-culture:
    - "endothelial-cells@^1.2"  # for vascularization
```

### Documentation Standards

README files, API documentation, and usage examples transfer directly. A Bio-Component should include:
- **Description**: What the component does
- **Requirements**: Environmental conditions needed
- **Interface Specification**: Inputs, outputs, parameters
- **Usage Examples**: How to integrate with other components
- **Known Limitations**: Failure modes, incompatibilities
- **Changelog**: Version history

### Licensing

Software licenses (MIT, Apache, GPL) define usage rights. Biological components need similar frameworks:
- **Usage Rights**: Who can use the component
- **Modification Rights**: Can the component be genetically modified?
- **Sharing Requirements**: Must derivatives be shared?
- **Attribution**: How to credit original developers
- **Commercial Use**: Restrictions on commercial applications

## 3.3 Analogous Mappings

These concepts require adaptation but preserve core principles:

### Testing → Validation

| Software Testing | Biological Validation | Adaptation Notes |
|-----------------|----------------------|------------------|
| Unit Test | Viability Test | Test single component function |
| Integration Test | Compatibility Test | Test component interactions |
| Stress Test | Endurance Test | Long-term, extreme conditions |
| Regression Test | Batch Consistency Test | New batches match previous |
| Performance Test | Efficiency Test | Output per resource consumed |

Key differences:
- Software tests are deterministic; biological tests are statistical
- Software tests run in milliseconds; biological tests take days/weeks
- Software tests are automated; biological tests require manual intervention

Adaptation: Define **acceptance criteria** as statistical thresholds rather than exact values:
```yaml
tests:
  viability:
    metric: "cell_survival_rate"
    threshold: ">= 90%"
    confidence: "95%"
    sample_size: 10
```

### API Contract → Interface Protocol

Software APIs define:
- Input types and validation rules
- Output types and guarantees
- Error conditions and handling

Bio-Interfaces define:
- Input signal types and acceptable ranges
- Output characteristics and tolerances
- Failure modes and detection methods

Example software API:
```typescript
function processSignal(input: number): number {
  // Precondition: 0 <= input <= 100
  // Postcondition: returns processed value in [0, 1]
  // Throws: InvalidInputError if precondition violated
}
```

Equivalent Bio-Interface:
```yaml
interface:
  input:
    type: "electrical"
    voltage: { min: 0, max: 5, unit: "V" }
    frequency: { min: 1, max: 100, unit: "Hz" }
  output:
    type: "mechanical"
    force: { min: 0, max: 50, unit: "mN" }
    response_time: { typical: 150, max: 300, unit: "ms" }
  failure_modes:
    - condition: "voltage > 5V"
      result: "cell_damage"
      detection: "impedance_spike"
```

### Error Handling → Failure Mode Management

Software distinguishes:
- **Exceptions**: Unexpected conditions that can be caught and handled
- **Errors**: Serious problems that may require termination
- **Warnings**: Non-critical issues that should be logged

Biological systems have analogous categories:
- **Recoverable Degradation**: Temporary performance drop (fatigue)
- **Irreversible Damage**: Permanent function loss (necrosis)
- **Systemic Risk**: Threats to other components (inflammation, infection)

```yaml
failure_handling:
  fatigue:
    type: "recoverable"
    detection: "force_output < 80% baseline"
    response: "reduce_stimulation_frequency"
    recovery_time: "2-4 hours"
  
  necrosis:
    type: "irreversible"
    detection: "viability < 50%"
    response: "isolate_and_replace"
    propagation_risk: "medium"
```

### Logging → Biomarker Recording

Software logging captures:
- Timestamps
- Event types (INFO, WARN, ERROR)
- Contextual data
- Stack traces for debugging

Biological logging captures:
- Timestamps
- Physiological measurements
- Environmental conditions
- Anomaly indicators

```yaml
logging:
  continuous:
    - metric: "force_output"
      frequency: "100 Hz"
    - metric: "temperature"
      frequency: "1 Hz"
  
  event_triggered:
    - event: "stimulation"
      capture: ["voltage", "frequency", "duration"]
    - event: "anomaly"
      capture: ["all_metrics", "image_snapshot"]
```

## 3.4 Novel Challenges Requiring New Solutions

These challenges have no direct software equivalent and require innovative approaches:

### Immune Compatibility

Software components do not "reject" each other. Biological components from different sources may trigger immune responses.

**Required Innovation**: Immune Compatibility Protocol
```yaml
immune_profile:
  mhc_class_i: ["HLA-A*02:01", "HLA-B*07:02"]
  mhc_class_ii: ["HLA-DR*04:01"]
  known_antigens: ["collagen_type_i"]
  
compatibility_requirements:
  autologous: "preferred"
  allogeneic: "requires_matching"
  xenogeneic: "requires_isolation_barrier"
```

### Signal Crosstalk

Software processes are isolated by operating system memory protection. Biological components share chemical environments where signals can interfere.

**Required Innovation**: Biological Noise Isolation Specification
```yaml
signal_isolation:
  electrical:
    shielding: "required"
    max_crosstalk: "-40 dB"
  
  chemical:
    diffusion_barrier: "hydrogel_encapsulation"
    half_life_requirement: "< 10 seconds"
```

### Metabolic Coupling

Software components consume CPU and memory independently. Biological components share metabolic resources and produce waste that affects neighbors.

**Required Innovation**: Metabolic Dependency Graph
```yaml
metabolism:
  consumes:
    - glucose: "2.5 µmol/hour"
    - oxygen: "5.0 µmol/hour"
  
  produces:
    - lactate: "4.0 µmol/hour"
    - co2: "4.5 µmol/hour"
  
  toxic_threshold:
    lactate: "< 20 mM in shared medium"
```

### Living Degradation

Software does not age (though it can become obsolete). Biological components inherently degrade over time.

**Required Innovation**: Degradation Prediction Model
```yaml
degradation:
  expected_lifetime:
    mean: 14
    std: 3
    unit: "days"
  
  degradation_markers:
    - marker: "force_decline"
      threshold: "20% from baseline"
      interpretation: "approaching_end_of_life"
  
  replacement_protocol:
    trigger: "viability < 70%"
    procedure: "hot_swap_with_backup"
```

### Ethical Constraints

Software has no inherent ethical status. Biological components, especially those derived from humans or involving neural tissue, raise ethical considerations with no software parallel.

**Required Innovation**: Ethical Constraint Language
```yaml
ethics:
  source:
    consent: "informed_consent_documented"
    donor_type: "adult_volunteer"
  
  constraints:
    - "no_consciousness_capable_assemblies"
    - "no_reproductive_applications"
    - "destruction_protocol_required"
  
  oversight:
    irb_approval: "required"
    review_frequency: "annual"
```
