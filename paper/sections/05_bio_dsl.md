# 5. Bio-DSL: Language Design Rationale

## 5.1 Why a Domain-Specific Language?

Martin Fowler defines a domain-specific language (DSL) as "a computer language specialized to a particular application domain." DSLs trade generality for expressiveness within their domain.

### Benefits of DSLs

| Benefit | Explanation | Bio-DSL Application |
|---------|-------------|---------------------|
| **Expressiveness** | Say more with less | Describe complex assemblies concisely |
| **Readability** | Domain experts can understand | Biologists can read system descriptions |
| **Validation** | Domain-specific error checking | Catch interface mismatches at "compile time" |
| **Abstraction** | Hide implementation details | Focus on what, not how |

### Why Not Use Existing Languages?

General-purpose languages (Python, JavaScript) could describe biological systems, but:
- Too much flexibility allows invalid configurations
- No built-in understanding of biological constraints
- Error messages would be generic, not domain-specific

Existing biological languages (SBML, SBOL) operate at different abstraction levels:
- SBML: molecular reaction networks
- SBOL: genetic sequences
- Bio-DSL: organ/system-level composition

## 5.2 Design Goals

1. **Declarative**: Describe *what* the system is, not *how* to build it
2. **Readable**: A biologist should understand the intent without programming background
3. **Verifiable**: Static analysis can catch errors before physical assembly
4. **Executable**: Can generate runtime configurations and monitoring dashboards
5. **Composable**: Systems can be nested and reused

## 5.3 Language Constructs

### Component Declaration

```biodsl
// Import component from registry with version constraint
COMPONENT <alias> FROM "<source>@<version>" [AS <local_name>]

// Examples:
COMPONENT flexor FROM "muscle-actuator-human-skeletal@^2.3"
COMPONENT sensor FROM "piezo-force-sensor@~1.1" AS force_sensor
COMPONENT controller FROM "neural-organoid-spinal@>=0.8"
```

Version constraints follow npm conventions:
- `^2.3.0`: Compatible with 2.x.x (>=2.3.0 <3.0.0)
- `~1.1.0`: Approximately 1.1.x (>=1.1.0 <1.2.0)
- `>=0.8`: At least version 0.8

### Connection Declaration

```biodsl
// Basic connection
CONNECT <source>.<port> TO <target>.<port>

// Connection with adapter
CONNECT <source>.<port> TO <target>.<port> VIA <adapter>

// Connection with parameters
CONNECT <source>.<port> TO <target>.<port> WITH { <params> }

// Examples:
CONNECT sensor.output TO controller.input
CONNECT controller.output TO flexor.stimulation VIA signal_converter
CONNECT flexor.force_output TO sensor.input WITH { gain: 1.5, offset: 0 }
```

### Adapter Declaration

```biodsl
// Declare adapter for interface conversion
ADAPTER <alias> FROM "<source>@<version>" [WITH { <config> }]

// Examples:
ADAPTER signal_converter FROM "opto-electrical@2.0" WITH {
  input_type: "electrical",
  output_type: "optical",
  wavelength: 470 nm
}

ADAPTER perfusion_hub FROM "microfluidic-4ch@1.0" WITH {
  channels: 4,
  flow_rate: 0.5 mL/min
}
```

### Runtime Configuration

```biodsl
RUNTIME {
  // Perfusion settings
  perfusion: {
    medium: "DMEM + 10% FBS",
    temperature: 37 °C,
    pH: 7.4,
    flow_rate: 0.5 mL/min,
    oxygenation: true
  },
  
  // Control settings
  control: {
    mode: "closed_loop",
    algorithm: "PID",
    parameters: { Kp: 0.8, Ki: 0.2, Kd: 0.1 }
  },
  
  // Monitoring settings
  monitoring: {
    log_interval: 10 s,
    metrics: ["force", "viability", "temperature"],
    alerts: {
      "viability < 80%": "WARNING",
      "temperature > 39°C": "CRITICAL"
    }
  },
  
  // Safety settings
  safety: {
    emergency_stop: "viability < 50%",
    max_force: 100 mN
  }
}
```

### Behavioral Logic

```biodsl
// Event-triggered actions
ON <event> DO { <actions> }

// Condition-triggered actions
WHEN <condition> THEN { <actions> }

// Periodic actions
EVERY <interval> DO { <actions> }

// Examples:
ON STARTUP DO {
  SET perfusion.flow_rate = 0.5 mL/min
  WAIT 300 s  // Equilibration
  SET controller.mode = "active"
}

WHEN flexor.fatigue_index > 0.3 THEN {
  LOG "Fatigue detected"
  REDUCE flexor.stimulation_frequency BY 20%
}

EVERY 1 hour DO {
  RUN viability_check()
  IF any.viability < 85% THEN {
    INCREASE perfusion.flow_rate BY 10%
  }
}
```

### Test Declaration

```biodsl
TEST <name> {
  description: "<text>"
  
  GIVEN <preconditions>
  WHEN <actions>
  THEN <assertions>
}

// Example:
TEST contraction_response {
  description: "Verify muscle responds to stimulation"
  
  GIVEN flexor.state == "ready"
  WHEN STIMULATE flexor AT 10 Hz, 2 V FOR 1 s
  THEN EXPECT flexor.force IN [5, 15] mN WITHIN 200 ms
}

TEST closed_loop_tracking {
  description: "Verify feedback control accuracy"
  
  GIVEN system.mode == "closed_loop"
  WHEN SET target = sine_wave(0.5 Hz, 20 mN) FOR 60 s
  THEN EXPECT tracking_error < 3 mN RMS
}
```

## 5.4 Complete Example: Dual-Muscle Antagonist System

```biodsl
// ============================================
// Bio-Mechanical Arm Unit v0.1
// Dual-muscle antagonist with closed-loop control
// ============================================

// === Component Declarations ===
COMPONENT flexor FROM "muscle-actuator-human-skeletal@^2.3" {
  role: "agonist",
  force_range: [0, 50] mN
}

COMPONENT extensor FROM "muscle-actuator-human-skeletal@^2.3" {
  role: "antagonist", 
  force_range: [0, 50] mN
}

COMPONENT sensor FROM "piezo-force-sensor@~1.1" {
  range: [0, 100] mN,
  sampling_rate: 100 Hz
}

COMPONENT controller FROM "neural-organoid-spinal@>=0.8" {
  input_channels: 2,
  output_channels: 2
}

// === Adapter Declarations ===
ADAPTER perfusion FROM "microfluidic-4ch@1.0" {
  medium: "DMEM + 10% FBS",
  flow_rate: 0.5 mL/min PER channel
}

ADAPTER stim_converter FROM "opto-electrical@2.0" {
  wavelength: 470 nm
}

// === Connection Topology ===

// Controller to muscles (via optical stimulation)
CONNECT controller.output_1 TO flexor.stimulation 
  VIA stim_converter
  WITH { frequency: [1, 50] Hz, voltage: [0, 3] V }

CONNECT controller.output_2 TO extensor.stimulation
  VIA stim_converter
  WITH { frequency: [1, 50] Hz, voltage: [0, 3] V }

// Sensor feedback to controller
CONNECT sensor.output TO controller.feedback_input
  WITH { gain: 1.5 }

// Perfusion connections
CONNECT perfusion.ch1 TO flexor.perfusion_input
CONNECT perfusion.ch2 TO extensor.perfusion_input
CONNECT perfusion.ch3 TO controller.perfusion_input
CONNECT perfusion.ch4 TO sensor.perfusion_input

// === Runtime Configuration ===
RUNTIME {
  perfusion: {
    temperature: 37 °C,
    pH: 7.4,
    oxygenation: true,
    waste_removal: "continuous"
  },
  
  control: {
    mode: "closed_loop",
    target: "position",
    pid: { Kp: 0.8, Ki: 0.2, Kd: 0.1 }
  },
  
  monitoring: {
    interval: 10 s,
    metrics: [
      "flexor.force", "extensor.force",
      "sensor.reading", "controller.activity",
      "*.viability"
    ],
    alerts: {
      "viability < 80%": "WARNING",
      "force > 90 mN": "CRITICAL"
    }
  },
  
  safety: {
    max_force: 100 mN,
    emergency: {
      trigger: "viability < 50% OR force > 120 mN",
      action: "STOP_ALL; PERFUSION_ONLY"
    }
  }
}

// === Behavioral Logic ===
ON STARTUP DO {
  SET perfusion.flow_rate = 0.5 mL/min
  WAIT 300 s  // Equilibration period
  RUN calibration_sequence()
  SET controller.mode = "active"
  LOG "System initialized"
}

WHEN target_position CHANGES THEN {
  error = target_position - sensor.reading
  controller.compute(error)
}

WHEN flexor.fatigue_index > 0.3 THEN {
  LOG "Flexor fatigue detected"
  REDUCE flexor.stim_frequency BY 20%
  INCREASE extensor.stim_frequency BY 10%  // Compensate
}

EVERY 1 hour DO {
  RUN viability_check()
  RECORD performance_snapshot()
}

// === Test Suite ===
TEST unit_response {
  description: "Single muscle contraction test"
  GIVEN flexor.state == "ready"
  WHEN STIMULATE flexor AT 10 Hz, 2 V FOR 1 s
  THEN EXPECT flexor.force IN [5, 15] mN WITHIN 200 ms
}

TEST antagonist_balance {
  description: "Antagonist coordination test"
  GIVEN system.mode == "active"
  WHEN ACTIVATE flexor AND extensor SIMULTANEOUSLY
  THEN EXPECT |flexor.force - extensor.force| < 5 mN
}

TEST tracking_accuracy {
  description: "Closed-loop tracking test"
  GIVEN system.mode == "closed_loop"
  WHEN SET target = sine_wave(0.5 Hz, ±20 mN) FOR 60 s
  THEN EXPECT tracking_error < 3 mN RMS
}

// === Expected Performance ===
EXPECTED {
  position_accuracy: ±2 mN,
  bandwidth: [0, 2] Hz,
  lifetime: [7, 14] days,
  power_consumption: [50, 100] mW
}
```

## 5.5 Comparison with Related Languages

| Language | Abstraction Level | Purpose | Relationship to Bio-DSL |
|----------|------------------|---------|------------------------|
| **SBOL** | Genetic | DNA sequence description | Lower level; describes component internals |
| **SBML** | Molecular | Biochemical reaction networks | Lower level; models component dynamics |
| **CellML** | Cellular | Cell mathematical models | Lower level; component behavior models |
| **Bio-DSL** | Organ/System | Component composition | Higher level; system assembly |

Bio-DSL is designed to **complement** these languages:
- Use SBOL to describe genetic modifications within a component
- Use SBML to model the biochemical behavior of a component
- Use Bio-DSL to describe how components connect into systems

## 5.6 Tooling Vision

A complete Bio-DSL ecosystem would include:

1. **Parser/Validator**: Check syntax and semantic correctness
2. **Type Checker**: Verify interface compatibility
3. **Simulator**: Predict system behavior before physical assembly
4. **Code Generator**: Produce runtime configurations
5. **Visual Editor**: Drag-and-drop system design
6. **Package Manager**: Discover and install components
7. **Test Runner**: Execute test suites
8. **Documentation Generator**: Produce human-readable specs
