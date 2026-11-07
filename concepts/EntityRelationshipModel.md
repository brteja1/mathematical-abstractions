# Finite typed entity-relationship instance

Finite typed entity sets and positive-arity relationship sets with named roles and typed total entity/relationship attributes.

**Notation:** E_k⊆fin ID; R_r⊆fin Πi:Fin(arity(r)). E_role(r,i)

**Stable ID:** `urn:csabs:concept/EntityRelationshipModel`

**Categories:** Relational data modelling

**Kind:** semantic-model

**Prerequisites:** [Finite set collection](FiniteSet.md), [Dependent function (Pi type)](DependentFunction.md), [Named relational schema with attribute domains](RelationalSchema.md)

## Interface and scope

**axiomBasis:** Kinds, attribute-name families, entity sets and relationship sets are finite; arity(r)>0; row∈R_r ⇒ ∀i:Fin(arity(r)), row(i)∈E_role(r,i); For each existing entity or relationship and declared attribute, exactly one value in its declared domain is assigned

**basisKind:** extensional-structural-definition

**basisScope:** Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-EntityRelationshipModel-entities"></a>

### entities

`urn:csabs:operation/EntityRelationshipModel-entities`

**signature:** entities : Kind_E→FinSet(ID)

**description:** Returns E_k.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns E_k.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-EntityRelationshipModel-relationships"></a>

### relationships

`urn:csabs:operation/EntityRelationshipModel-relationships`

**signature:** relationships : (r:Kind_R)→FinSet(Πi:Fin(arity(r)).ID)

**description:** Returns existing typed role tuples.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns existing typed role tuples.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-EntityRelationshipModel-entity-attribute"></a>

### entity-attribute

`urn:csabs:operation/EntityRelationshipModel-entity-attribute`

**signature:** attribute : (k:Kind_E)→E_k→(a:Attr(k))→Domain(k,a)

**description:** Reads a typed scalar or explicitly product-valued entity attribute.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Reads a typed scalar or explicitly product-valued entity attribute.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-EntityRelationshipModel-relationship-attribute"></a>

### relationship-attribute

`urn:csabs:operation/EntityRelationshipModel-relationship-attribute`

**signature:** relationshipAttribute : (r:Kind_R)→R_r→(a:RAttr(r))→RDomain(r,a)

**description:** Reads a relationship-specific typed attribute.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Reads a relationship-specific typed attribute.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-EntityRelationshipModel-finite-schema"></a>

### finite-schema

`urn:csabs:axiom/EntityRelationshipModel-finite-schema`

**statement:** Defining requirement: Kinds, attribute-name families, entity sets and relationship sets are finite; arity(r)>0

**formalStatement:** Kinds, attribute-name families, entity sets and relationship sets are finite; arity(r)>0

**assumptions:** Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-EntityRelationshipModel-role-integrity"></a>

### role-integrity

`urn:csabs:axiom/EntityRelationshipModel-role-integrity`

**statement:** Defining requirement: row∈R_r ⇒ ∀i:Fin(arity(r)), row(i)∈E_role(r,i)

**formalStatement:** row∈R_r ⇒ ∀i:Fin(arity(r)), row(i)∈E_role(r,i)

**assumptions:** Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-EntityRelationshipModel-attribute-totality"></a>

### attribute-totality

`urn:csabs:axiom/EntityRelationshipModel-attribute-totality`

**statement:** Defining requirement: For each existing entity or relationship and declared attribute, exactly one value in its declared domain is assigned

**formalStatement:** For each existing entity or relationship and declared attribute, exactly one value in its declared domain is assigned

**assumptions:** Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-EntityRelationshipModel-no-dangling-role"></a>

### no-dangling-role

`urn:csabs:law/EntityRelationshipModel-no-dangling-role`

**statement:** row∈R_r ⇒ row(i)∈E_role(r,i)

**formalStatement:** row∈R_r ⇒ row(i)∈E_role(r,i)

**assumptions:** Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [role-integrity](EntityRelationshipModel.md#node-urn-csabs-axiom-EntityRelationshipModel-role-integrity)

**proofSketch:** Instantiate role-integrity at i.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-EntityRelationshipModel-empty-entity-role"></a>

### empty-entity-role

`urn:csabs:theorem/EntityRelationshipModel-empty-entity-role`

**statement:** E_role(r,i)=∅ ⇒ R_r=∅

**formalStatement:** E_role(r,i)=∅ ⇒ R_r=∅

**assumptions:** Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [role-integrity](EntityRelationshipModel.md#node-urn-csabs-axiom-EntityRelationshipModel-role-integrity)

**proofSketch:** A relationship tuple would supply an entity in that empty set by role integrity; hence no tuple can exist.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Peter Pin-Shan Chen: The Entity-Relationship Model—Toward a Unified View of Data](https://weichselbraun.net/dbs/pdf/literature/chen.pdf); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/EntityRelationshipModel",
    "type": "Concept",
    "shortForm": "EntityRelationshipModel",
    "fullName": "Finite typed entity-relationship instance",
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Finite typed entity sets and positive-arity relationship sets with named roles and typed total entity/relationship attributes.",
    "notation": "E_k⊆fin ID; R_r⊆fin Πi:Fin(arity(r)). E_role(r,i)",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/DependentFunction",
      "urn:csabs:concept/RelationalSchema"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/EntityRelationshipModel-entities",
      "urn:csabs:operation/EntityRelationshipModel-relationships",
      "urn:csabs:operation/EntityRelationshipModel-entity-attribute",
      "urn:csabs:operation/EntityRelationshipModel-relationship-attribute"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/EntityRelationshipModel-finite-schema",
      "urn:csabs:axiom/EntityRelationshipModel-role-integrity",
      "urn:csabs:axiom/EntityRelationshipModel-attribute-totality"
    ],
    "hasLaw": [
      "urn:csabs:law/EntityRelationshipModel-no-dangling-role"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/EntityRelationshipModel-empty-entity-role"
    ],
    "axiomBasis": "Kinds, attribute-name families, entity sets and relationship sets are finite; arity(r)>0; row∈R_r ⇒ ∀i:Fin(arity(r)), row(i)∈E_role(r,i); For each existing entity or relationship and declared attribute, exactly one value in its declared domain is assigned",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EntityRelationshipModel-entities",
    "type": "Operation",
    "name": "entities",
    "signature": "entities : Kind_E→FinSet(ID)",
    "description": "Returns E_k.",
    "concept": "urn:csabs:concept/EntityRelationshipModel",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns E_k.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EntityRelationshipModel-relationships",
    "type": "Operation",
    "name": "relationships",
    "signature": "relationships : (r:Kind_R)→FinSet(Πi:Fin(arity(r)).ID)",
    "description": "Returns existing typed role tuples.",
    "concept": "urn:csabs:concept/EntityRelationshipModel",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns existing typed role tuples.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EntityRelationshipModel-entity-attribute",
    "type": "Operation",
    "name": "entity-attribute",
    "signature": "attribute : (k:Kind_E)→E_k→(a:Attr(k))→Domain(k,a)",
    "description": "Reads a typed scalar or explicitly product-valued entity attribute.",
    "concept": "urn:csabs:concept/EntityRelationshipModel",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Reads a typed scalar or explicitly product-valued entity attribute.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EntityRelationshipModel-relationship-attribute",
    "type": "Operation",
    "name": "relationship-attribute",
    "signature": "relationshipAttribute : (r:Kind_R)→R_r→(a:RAttr(r))→RDomain(r,a)",
    "description": "Reads a relationship-specific typed attribute.",
    "concept": "urn:csabs:concept/EntityRelationshipModel",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Reads a relationship-specific typed attribute.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EntityRelationshipModel-finite-schema",
    "type": "Axiom",
    "name": "finite-schema",
    "statement": "Defining requirement: Kinds, attribute-name families, entity sets and relationship sets are finite; arity(r)>0",
    "formalStatement": "Kinds, attribute-name families, entity sets and relationship sets are finite; arity(r)>0",
    "assumptions": [
      "Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/EntityRelationshipModel"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EntityRelationshipModel-role-integrity",
    "type": "Axiom",
    "name": "role-integrity",
    "statement": "Defining requirement: row∈R_r ⇒ ∀i:Fin(arity(r)), row(i)∈E_role(r,i)",
    "formalStatement": "row∈R_r ⇒ ∀i:Fin(arity(r)), row(i)∈E_role(r,i)",
    "assumptions": [
      "Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/EntityRelationshipModel"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EntityRelationshipModel-attribute-totality",
    "type": "Axiom",
    "name": "attribute-totality",
    "statement": "Defining requirement: For each existing entity or relationship and declared attribute, exactly one value in its declared domain is assigned",
    "formalStatement": "For each existing entity or relationship and declared attribute, exactly one value in its declared domain is assigned",
    "assumptions": [
      "Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/EntityRelationshipModel"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/EntityRelationshipModel-no-dangling-role",
    "type": "Law",
    "name": "no-dangling-role",
    "statement": "row∈R_r ⇒ row(i)∈E_role(r,i)",
    "formalStatement": "row∈R_r ⇒ row(i)∈E_role(r,i)",
    "assumptions": [
      "Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/EntityRelationshipModel"
    ],
    "dependsOn": [
      "urn:csabs:axiom/EntityRelationshipModel-role-integrity"
    ],
    "proofSketch": "Instantiate role-integrity at i.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/EntityRelationshipModel-empty-entity-role",
    "type": "Theorem",
    "name": "empty-entity-role",
    "statement": "E_role(r,i)=∅ ⇒ R_r=∅",
    "formalStatement": "E_role(r,i)=∅ ⇒ R_r=∅",
    "assumptions": [
      "Fixed finite schema of entity/relationship kinds and attribute names. Entity sets may overlap in global ID. Relations are sets of role tuples, so no duplicate relationship occurrence identity. Attributes total with declared domains; optionality must use an Option domain. No weak entities, inheritance or extra participation/cardinality constraints assumed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/EntityRelationshipModel"
    ],
    "dependsOn": [
      "urn:csabs:axiom/EntityRelationshipModel-role-integrity"
    ],
    "proofSketch": "A relationship tuple would supply an entity in that empty set by role integrity; hence no tuple can exist.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/chen-er-core"
    ],
    "sourceLocator": "ACM TODS 1(1), 1976, pp. 9–36; §§2.2.1–2.2.4: entity sets, typed roles, relations and attributes",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
