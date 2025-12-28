# 7. Related Work and Positioning

## 7.1 Synthetic Biology and Standardization

### BioBricks and iGEM

The BioBricks Foundation and iGEM (International Genetically Engineered Machine) competition pioneered biological standardization at the genetic level. BioBricks defined standard assembly methods for DNA parts, enabling students worldwide to combine genetic components.

**Relationship to Wetware Engineering**:
- BioBricks operates at the **genetic level** (DNA sequences)
- Wetware Engineering operates at the **organ/system level** (tissues, organoids)
- They are **complementary**: BioBricks could define the genetic content *within* a Bio-Component

### SBOL (Synthetic Biology Open Language)

SBOL provides a standardized data format for describing genetic designs, enabling exchange between software tools and laboratories.

**Relationship to Wetware Engineering**:
- SBOL describes **what genes are in a component**
- Bio-Component Spec describes **what the component does as a functional unit**
- SBOL could be embedded within Bio-Component Spec for genetic traceability

```yaml
# Bio-Component with embedded SBOL reference
source:
  genetic_design:
    sbol_uri: "https://synbiohub.org/design/muscle-v2"
    modifications: ["GFP reporter", "tetracycline-inducible"]
```

### Comparison Table

| Aspect | BioBricks/SBOL | Wetware Engineering |
|--------|---------------|---------------------|
| Abstraction level | Genetic (DNA) | Organ/System (tissue) |
| Unit of composition | DNA part | Functional module |
| Assembly method | Restriction enzymes, Gibson | Physical/fluidic connection |
| Standardization focus | Sequence format | Interface protocol |
| Primary users | Molecular biologists | Tissue engineers, roboticists |

## 7.2 Organ-on-Chip and Organoids

### Organ-on-Chip Technology

Organ-on-chip devices culture human cells in microfluidic environments that mimic organ physiology. Companies like Emulate and TissUse have commercialized multi-organ systems.

**Relationship to Wetware Engineering**:
- Organ-on-chip provides **physical implementations** of Bio-Components
- Current systems lack **standardized interfaces** between chips
- Wetware Engineering provides the **abstraction framework** they need

### Organoid Research

Organoids are self-organizing 3D tissue cultures that recapitulate organ structure and function. Brain organoids, gut organoids, and kidney organoids have advanced rapidly.

**Relationship to Wetware Engineering**:
- Organoids are excellent **candidate Bio-Components**
- Current organoid research focuses on **individual organs**, not composition
- Wetware Engineering provides **composition methodology**

### What's Missing

| Current State | Wetware Engineering Adds |
|--------------|-------------------------|
| Each lab develops proprietary protocols | Standardized specifications |
| No interface standards between organs | Bio-Interface Protocol |
| Results described in papers | Machine-readable descriptions |
| Composition is ad-hoc | Declarative composition language |
| No version control | Semantic versioning |

## 7.3 Systems Biology Modeling

### SBML (Systems Biology Markup Language)

SBML is a standard format for representing computational models of biological processes, particularly biochemical reaction networks.

### CellML

CellML describes mathematical models of cellular function, enabling model sharing and reuse.

**Relationship to Wetware Engineering**:
- SBML/CellML describe **how components behave internally** (simulation)
- Bio-DSL describes **how components connect externally** (composition)
- They serve different purposes and can be used together

```yaml
# Bio-Component with SBML behavior model
behavior:
  model_type: "SBML"
  model_uri: "https://biomodels.org/MODEL123"
  parameters:
    - name: "contraction_rate"
      value: 0.5
      unit: "1/s"
```

### Comparison

| Aspect | SBML/CellML | Bio-DSL |
|--------|------------|---------|
| Purpose | Simulate behavior | Describe composition |
| Focus | Internal dynamics | External connections |
| Output | Simulation results | Runtime configuration |
| Users | Computational biologists | System builders |

## 7.4 Biohybrid Robotics

### Living Machines

Research groups have created robots powered by biological actuators: muscle-powered swimmers, insect-machine hybrids, and biohybrid grippers.

**Relationship to Wetware Engineering**:
- Biohybrid robotics demonstrates **feasibility** of biological components
- Current work is **bespoke**—each system designed from scratch
- Wetware Engineering provides **reusable framework**

### Key Publications

- Raman & Bashir (2017): Biohybrid actuators review
- Ricotti et al. (2017): Biohybrid systems for robotics
- Park et al. (2016): Muscle-powered swimming robot

These works prove biological components can be engineered. Wetware Engineering asks: how do we make this **systematic and reproducible**?

## 7.5 Software Engineering for Biology

### Laboratory Automation

Tools like Autoprotocol and Antha provide programming languages for laboratory procedures, enabling reproducible experiments.

**Relationship to Wetware Engineering**:
- Lab automation describes **how to make components**
- Wetware Engineering describes **how to compose components**
- They address different phases of the development lifecycle

### Workflow Systems

Galaxy, Nextflow, and Snakemake manage computational biology workflows.

**Relationship to Wetware Engineering**:
- Workflow systems manage **data analysis pipelines**
- Bio-DSL manages **physical system composition**
- Different domains, similar abstraction principles

## 7.6 Positioning Summary

```
                    Abstraction Level
                    
    High    ┌─────────────────────────────────┐
            │     Wetware Engineering          │
            │     (System Composition)         │
            └─────────────────────────────────┘
                           ↑
                    Uses components from
                           ↑
    Medium  ┌─────────────────────────────────┐
            │   Organ-on-Chip / Organoids      │
            │   (Physical Implementation)      │
            └─────────────────────────────────┘
                           ↑
                    Built using
                           ↑
    Low     ┌─────────────────────────────────┐
            │   BioBricks / SBOL / SBML        │
            │   (Genetic / Molecular)          │
            └─────────────────────────────────┘
```

**Wetware Engineering's unique contribution**: Providing the **system-level abstraction layer** that connects molecular/genetic engineering to functional biological systems, using software engineering principles.

## 7.7 What We Are NOT Claiming

To be clear about scope:

1. **We are not claiming to have built working systems**. This paper proposes a framework; implementation is future work.

2. **We are not claiming biology is "just like" software**. Section 6 details fundamental differences requiring novel solutions.

3. **We are not claiming to replace existing approaches**. We complement synthetic biology, organoid research, and systems biology.

4. **We are not claiming immediate practical application**. The roadmap spans decades.

What we ARE claiming: **The conceptual framework of software engineering—modularity, interfaces, composition, versioning—provides valuable abstractions for biological system construction, and articulating this framework is a necessary first step.**
