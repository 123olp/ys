# 4. Bio-Component Specification: Design Rationale

## 4.1 Design Principles from Software Engineering

The Bio-Component Specification draws from established software engineering principles:

### SOLID Principles Applied

| Principle | Software Definition | Bio-Component Application |
|-----------|--------------------|-----------------------------|
| **Single Responsibility** | A class should have one reason to change | A component should perform one biological function |
| **Open/Closed** | Open for extension, closed for modification | Components can be enhanced without changing interfaces |
| **Liskov Substitution** | Subtypes must be substitutable for base types | Compatible components must be interchangeable |
| **Interface Segregation** | Many specific interfaces over one general | Fine-grained interface definitions |
| **Dependency Inversion** | Depend on abstractions, not concretions | Depend on interface specs, not specific implementations |

### Convention over Configuration

Borrowed from Ruby on Rails: provide sensible defaults to minimize required configuration.

```yaml
# Minimal specification (defaults applied)
component:
  id: "muscle-actuator-v1"
  type: "actuator"
  source: "human-skeletal"

# System applies defaults:
# - temperature: 37°C
# - pH: 7.4
# - oxygen: 20%
# - standard mammalian culture medium
```

### Schema-First Design

Like OpenAPI/Swagger for REST APIs, we define the schema before implementations:

```yaml
# Bio-Component Spec Schema (JSON Schema format)
$schema: "https://wetware-engineering.org/schema/bio-component/1.0"
type: object
required: [id, name, version, type, interface]
properties:
  id:
    type: string
    pattern: "^[a-z0-9-]+$"
  version:
    type: string
    pattern: "^\\d+\\.\\d+\\.\\d+$"
```

## 4.2 Specification Structure

### Complete Schema Overview

```yaml
bio-component: "1.0"  # Spec version

# === IDENTIFICATION ===
info:
  id: string                    # Unique identifier
  name: string                  # Human-readable name
  version: string               # Semantic version
  description: string           # Brief description
  license: string               # Usage license
  authors: [string]             # Contributors
  repository: url               # Source repository

# === CLASSIFICATION ===
classification:
  type: enum [actuator, sensor, processor, metabolic, structural, connector]
  domain: string                # e.g., "musculoskeletal", "neural"
  tags: [string]                # Searchable tags

# === BIOLOGICAL SOURCE ===
source:
  organism: string              # e.g., "Homo sapiens"
  tissue_type: string           # e.g., "skeletal muscle"
  cell_types: [string]          # e.g., ["myocyte", "fibroblast"]
  cell_line: string             # If immortalized
  genetic_modifications: [string]
  culture_protocol: url         # Reference to protocol
  biosafety_level: enum [BSL-1, BSL-2, BSL-3]

# === INTERFACE DEFINITION ===
interface:
  inputs: [InputPort]
  outputs: [OutputPort]
  
# === ENVIRONMENTAL REQUIREMENTS ===
requirements:
  physical: PhysicalRequirements
  chemical: ChemicalRequirements
  biological: BiologicalRequirements

# === PERFORMANCE CHARACTERISTICS ===
performance:
  functional: FunctionalMetrics
  reliability: ReliabilityMetrics
  resources: ResourceConsumption

# === FAILURE MODES ===
failure_modes: [FailureMode]

# === TESTING ===
testing:
  unit_tests: [TestCase]
  integration_tests: [IntegrationTest]
  certification: CertificationStatus

# === DEPENDENCIES ===
dependencies:
  components: [ComponentDependency]
  adapters: [AdapterDependency]
  protocols: [ProtocolDependency]
```

### Input/Output Port Definition

```yaml
InputPort:
  id: string                    # Port identifier
  type: enum [electrical, chemical, mechanical, optical, thermal, perfusion]
  required: boolean             # Is this input mandatory?
  
  parameters:
    range: [min, max]           # Acceptable input range
    unit: string                # Physical unit
    resolution: number          # Minimum detectable change
    response_time: number       # Time to respond (ms)
  
  defaults:
    value: any                  # Default if not connected
  
  validation:
    constraints: [string]       # e.g., "frequency < 100 Hz"

OutputPort:
  id: string
  type: enum [electrical, chemical, mechanical, optical, thermal, secretion]
  
  parameters:
    range: [min, max]
    unit: string
    precision: number           # Output precision
    latency: number             # Output delay (ms)
  
  monitoring:
    metrics: [string]           # Observable metrics
    sampling_rate: number       # Hz
```

### Environmental Requirements

```yaml
PhysicalRequirements:
  temperature:
    optimal: number
    range: [min, max]
    unit: "°C"
    tolerance: number           # Acceptable deviation
  
  pressure:
    range: [min, max]
    unit: "mmHg"
  
  humidity:
    range: [min, max]
    unit: "%"

ChemicalRequirements:
  pH:
    optimal: number
    range: [min, max]
  
  osmolarity:
    range: [min, max]
    unit: "mOsm/L"
  
  oxygen:
    range: [min, max]
    unit: "%"
  
  glucose:
    range: [min, max]
    unit: "mM"
  
  custom_factors:
    - name: string
      concentration: number
      unit: string

BiologicalRequirements:
  immune_isolation: boolean
  sterility: enum [sterile, clean, standard]
  co_culture_requirements: [string]
```

## 4.3 Versioning Strategy

### Semantic Versioning for Biology

We adopt SemVer with biological interpretations:

**MAJOR version** (X.0.0): Interface-breaking changes
- Input/output port type changes
- Required parameter additions
- Environmental requirement changes that affect compatibility

**MINOR version** (0.X.0): Backward-compatible additions
- New optional output ports
- Performance improvements
- Additional monitoring capabilities

**PATCH version** (0.0.X): Backward-compatible fixes
- Protocol optimizations
- Documentation updates
- Minor performance tuning

### Build Metadata

Extended version format for biological specificity:
```
{version}+{batch}.{donor}.{modification}

Examples:
2.3.1+batch20251228.donor42.wildtype
2.3.1+batch20251228.donor42.gfp-tagged
```

### Compatibility Declarations

```yaml
compatibility:
  backward_compatible_with: ["2.2.x", "2.1.x"]
  known_incompatible: ["1.x.x"]
  
  interface_changes:
    - version: "2.0.0"
      change: "electrical input voltage range expanded"
      migration: "no action required for existing users"
```

## 4.4 Example: Complete Muscle Actuator Specification

```yaml
bio-component: "1.0"

info:
  id: "muscle-actuator-human-skeletal"
  name: "Human Skeletal Muscle Actuator"
  version: "2.3.1"
  description: "Contractile muscle tissue for force generation"
  license: "CC-BY-SA-4.0"
  authors: ["Wetware Engineering Project"]
  repository: "https://github.com/wetware/muscle-actuator"

classification:
  type: "actuator"
  domain: "musculoskeletal"
  tags: ["muscle", "contractile", "force-generation", "human"]

source:
  organism: "Homo sapiens"
  tissue_type: "skeletal muscle"
  cell_types: ["myocyte", "satellite cell"]
  culture_protocol: "https://protocols.io/wetware/muscle-culture-v2"
  biosafety_level: "BSL-1"

interface:
  inputs:
    - id: "electrical_stimulation"
      type: "electrical"
      required: true
      parameters:
        voltage: { range: [0, 5], unit: "V" }
        frequency: { range: [1, 100], unit: "Hz" }
        pulse_width: { range: [0.1, 10], unit: "ms" }
      response_time: 50  # ms
    
    - id: "perfusion_input"
      type: "perfusion"
      required: true
      parameters:
        flow_rate: { range: [0.1, 2.0], unit: "mL/min" }
        
  outputs:
    - id: "force_output"
      type: "mechanical"
      parameters:
        force: { range: [0, 50], unit: "mN" }
        displacement: { range: [0, 5], unit: "mm" }
      latency: 150  # ms
      monitoring:
        metrics: ["force", "displacement", "velocity"]
        sampling_rate: 100  # Hz

requirements:
  physical:
    temperature: { optimal: 37, range: [35, 39], unit: "°C" }
  chemical:
    pH: { optimal: 7.4, range: [7.2, 7.6] }
    oxygen: { range: [15, 25], unit: "%" }
    glucose: { range: [5, 25], unit: "mM" }

performance:
  functional:
    max_force: { value: 50, unit: "mN" }
    response_time: { typical: 150, max: 300, unit: "ms" }
    contraction_velocity: { max: 10, unit: "mm/s" }
  reliability:
    lifetime: { mean: 14, std: 3, unit: "days" }
    failure_rate: { value: 0.01, unit: "per_hour" }
  resources:
    oxygen_consumption: { value: 5, unit: "µmol/hour" }
    glucose_consumption: { value: 2.5, unit: "µmol/hour" }

failure_modes:
  - id: "fatigue"
    type: "recoverable"
    probability: 0.3
    detection: "force_output < 80% baseline"
    impact: "reduced_performance"
    mitigation: "reduce stimulation, allow recovery"
  
  - id: "necrosis"
    type: "irreversible"
    probability: 0.05
    detection: "viability < 50%"
    impact: "component_loss"
    mitigation: "replace component"

testing:
  unit_tests:
    - id: "contraction_response"
      description: "Verify force output on stimulation"
      protocol: "stimulate 10Hz 2V for 1s, measure force"
      acceptance: "force in [5, 15] mN within 200ms"
    
    - id: "viability_check"
      description: "Verify cell survival"
      protocol: "live/dead staining"
      acceptance: "viability > 90%"

dependencies:
  adapters:
    - id: "perfusion-adapter"
      version: "^1.0.0"
  protocols:
    - name: "standard-mammalian-culture"
      version: "2.1"
```
