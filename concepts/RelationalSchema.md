# Named relational schema with attribute domains

A relation name, a finite set of attribute names, and a domain for each attribute determine its admissible named tuples.

**Notation:** Σ=(R,U,D); Tup(Σ)=∏_{a∈U}D(a)

**Stable ID:** `urn:csabs:concept/RelationalSchema`

**Categories:** Relational data modelling, Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Set](Set.md), [Total function](Function.md), [Cartesian product](CartesianProduct.md)

**Related concepts:** [Product Type](ProductType.md), [Map](Map.md)

## Backlinks

- [Finite database relation under bag semantics](BagRelation.md) — `requiresConcept`
- [Candidate key relative to functional dependencies](CandidateKey.md) — `relatedConcept`
- [Finite database relation under set semantics](DatabaseRelation.md) — `requiresConcept`
- [Finite typed entity-relationship instance](EntityRelationshipModel.md) — `requiresConcept`
- [Map](Map.md) — `relatedConcept`

## Mathematical formulation

A schema is (Attr,D) with finite attribute carrier Attr and domains D:Attr→Type. A tuple is a dependent function t:Π\_{a∈Attr}D(a); the empty schema is permitted.

**Lean formulation** (in its source module context):

```lean
structure RelationalSchema where
  Attribute : Type u
  finiteAttributes : Fintype Attribute
  Domain : Attribute → Type v
```

**Source:** [`Catalog.RelationalSchema`](../lean/Catalog/Database.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Finite named attribute type and dependent domain family; tuples assign every attribute.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: A schema determines total assignments with exactly its attributes. Named tuple equality is pointwise equality. A type-correct field update changes exactly its selected field.

**basisKind:** defined-structure

**basisScope:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.

**verificationObligation:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RelationalSchema-arity"></a>

### arity

`urn:csabs:operation/RelationalSchema-arity`

**signature:** arity : Schema→ℕ

**description:** Returns the number of attributes.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns the number of attributes.

<a id="node-urn-csabs-operation-RelationalSchema-admissible"></a>

### admissible

`urn:csabs:operation/RelationalSchema-admissible`

**signature:** admissible : Schema×NamedTuple→Prop

**description:** Tests exact field domain and domain membership; not a type-inference algorithm.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Tests exact field domain and domain membership; not a type-inference algorithm.

<a id="node-urn-csabs-operation-RelationalSchema-updateField"></a>

### updateField

`urn:csabs:operation/RelationalSchema-updateField`

**signature:** update_a : Tup(Σ)×D(a)→Tup(Σ)

**description:** Replaces the a field while preserving all other fields.

**precondition:** a∈U and the replacement belongs to D(a).

**postcondition:** Replaces the a field while preserving all other fields.

**totality:** total mathematical operation on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RelationalSchema-typing"></a>

### typing

`urn:csabs:axiom/RelationalSchema-typing`

**statement:** A schema determines total assignments with exactly its attributes.

**description:** A schema determines total assignments with exactly its attributes.

**formalStatement:** U finite; ∀a∈U:D(a)≠∅; t∈Tup(Σ) iff dom(t)=U ∧ ∀a∈U:t(a)∈D(a); arity(Σ)=|U|

**assumptions:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.1–3.2, pp. 30–32

**sourceNote:** Uses the named tuple-as-function perspective and the optional per-attribute domain mapping. The domain map is explicit in the schema record. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RelationalSchema-tuple-extensionality"></a>

### tuple-extensionality

`urn:csabs:axiom/RelationalSchema-tuple-extensionality`

**statement:** Named tuple equality is pointwise equality.

**description:** Named tuple equality is pointwise equality.

**formalStatement:** t=u iff ∀a∈U:t(a)=u(a), for t,u∈Tup(Σ)

**assumptions:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.1–3.2, pp. 30–32

**sourceNote:** Uses the named tuple-as-function perspective and the optional per-attribute domain mapping. The domain map is explicit in the schema record. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RelationalSchema-field-update"></a>

### field-update

`urn:csabs:axiom/RelationalSchema-field-update`

**statement:** A type-correct field update changes exactly its selected field.

**description:** A type-correct field update changes exactly its selected field.

**formalStatement:** update_a(t,v)(b)=if b=a then v else t(b), for b∈U; a∈U, v∈D(a)

**assumptions:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3.2, named tuples as total functions, p. 32; local functional-update interface

**sourceNote:** Specifies additional equations for the selected abstract interface; local conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RelationalSchema-update-readback"></a>

### update-readback

`urn:csabs:law/RelationalSchema-update-readback`

**statement:** Restoring the current field value leaves a tuple unchanged.

**description:** Restoring the current field value leaves a tuple unchanged.

**formalStatement:** update_a(t,t(a))=t

**assumptions:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.; a∈U.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.1–3.2, pp. 30–32

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** At a, the stored value is unchanged; at every other field the defining update rule preserves the value. Apply tuple extensionality.

**dependsOn:** [typing](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-typing); [tuple-extensionality](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-tuple-extensionality); [field-update](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-field-update)

<a id="node-urn-csabs-law-RelationalSchema-update-shadowing"></a>

### update-shadowing

`urn:csabs:law/RelationalSchema-update-shadowing`

**statement:** The last write to one field determines that field.

**description:** The last write to one field determines that field.

**formalStatement:** update_a(update_a(t,v),w)=update_a(t,w)

**assumptions:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.; a∈U; v,w∈D(a).

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.1–3.2, pp. 30–32

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Compare components: both sides have w at a and the original tuple value elsewhere.

**dependsOn:** [typing](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-typing); [tuple-extensionality](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-tuple-extensionality); [field-update](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-field-update)

<a id="node-urn-csabs-law-RelationalSchema-independent-update-commutation"></a>

### independent-update-commutation

`urn:csabs:law/RelationalSchema-independent-update-commutation`

**statement:** Updates at distinct fields commute.

**description:** Updates at distinct fields commute.

**formalStatement:** a≠b ⇒ update_a(update_b(t,w),v)=update_b(update_a(t,v),w)

**assumptions:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.; a,b∈U; v∈D(a); w∈D(b).

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.1–3.2, pp. 30–32

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Split an arbitrary field into a, b, or neither. Both sides have v, w, or the original value respectively; use extensionality.

**dependsOn:** [typing](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-typing); [tuple-extensionality](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-tuple-extensionality); [field-update](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-field-update)

## Theorems

<a id="node-urn-csabs-theorem-RelationalSchema-zero-arity"></a>

### zero-arity

`urn:csabs:theorem/RelationalSchema-zero-arity`

**statement:** There is exactly one tuple over an empty attribute set.

**description:** There is exactly one tuple over an empty attribute set.

**formalStatement:** U=∅ ⇒ Tup(Σ)={∅}

**assumptions:** U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.

**ruleRole:** derived-result

**proofSketch:** The unique function with empty domain is the empty function; extensionality identifies any two such tuples.

**dependsOn:** [typing](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-typing); [tuple-extensionality](RelationalSchema.md#node-urn-csabs-axiom-RelationalSchema-tuple-extensionality)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.1–3.2, pp. 30–32

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

## Concept provenance

- [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.1–3.2, pp. 30–32

**sourceNote:** Uses the named tuple-as-function perspective and the optional per-attribute domain mapping. The domain map is explicit in the schema record.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RelationalSchema",
    "type": "Concept",
    "shortForm": "RelationalSchema",
    "fullName": "Named relational schema with attribute domains",
    "category": [
      "urn:csabs:category/data-modelling",
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A relation name, a finite set of attribute names, and a domain for each attribute determine its admissible named tuples.",
    "notation": "Σ=(R,U,D); Tup(Σ)=∏_{a∈U}D(a)",
    "hasOperation": [
      "urn:csabs:operation/RelationalSchema-arity",
      "urn:csabs:operation/RelationalSchema-admissible",
      "urn:csabs:operation/RelationalSchema-updateField"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RelationalSchema-typing",
      "urn:csabs:axiom/RelationalSchema-tuple-extensionality",
      "urn:csabs:axiom/RelationalSchema-field-update"
    ],
    "hasLaw": [
      "urn:csabs:law/RelationalSchema-update-readback",
      "urn:csabs:law/RelationalSchema-update-shadowing",
      "urn:csabs:law/RelationalSchema-independent-update-commutation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RelationalSchema-zero-arity"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/Function",
      "urn:csabs:concept/CartesianProduct"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ProductType",
      "urn:csabs:concept/Map"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: A schema determines total assignments with exactly its attributes. Named tuple equality is pointwise equality. A type-correct field update changes exactly its selected field.",
    "basisKind": "defined-structure",
    "basisScope": "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.1–3.2, pp. 30–32",
    "sourceNote": "Uses the named tuple-as-function perspective and the optional per-attribute domain mapping. The domain map is explicit in the schema record.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise."
    ],
    "leanFormulation": "structure RelationalSchema where\n  Attribute : Type u\n  finiteAttributes : Fintype Attribute\n  Domain : Attribute → Type v",
    "formulationSource": "urn:csabs:source/local-lean-Database",
    "formulationLocator": "Catalog.RelationalSchema",
    "formulationScope": "model",
    "leanModelMapping": "Finite named attribute type and dependent domain family; tuples assign every attribute.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A schema is (Attr,D) with finite attribute carrier Attr and domains D:Attr→Type. A tuple is a dependent function t:Π_{a∈Attr}D(a); the empty schema is permitted."
  },
  {
    "id": "urn:csabs:operation/RelationalSchema-arity",
    "type": "Operation",
    "name": "arity",
    "signature": "arity : Schema→ℕ",
    "description": "Returns the number of attributes.",
    "concept": "urn:csabs:concept/RelationalSchema",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns the number of attributes."
  },
  {
    "id": "urn:csabs:operation/RelationalSchema-admissible",
    "type": "Operation",
    "name": "admissible",
    "signature": "admissible : Schema×NamedTuple→Prop",
    "description": "Tests exact field domain and domain membership; not a type-inference algorithm.",
    "concept": "urn:csabs:concept/RelationalSchema",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Tests exact field domain and domain membership; not a type-inference algorithm."
  },
  {
    "id": "urn:csabs:operation/RelationalSchema-updateField",
    "type": "Operation",
    "name": "updateField",
    "signature": "update_a : Tup(Σ)×D(a)→Tup(Σ)",
    "description": "Replaces the a field while preserving all other fields.",
    "concept": "urn:csabs:concept/RelationalSchema",
    "precondition": "a∈U and the replacement belongs to D(a).",
    "postcondition": "Replaces the a field while preserving all other fields.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/RelationalSchema-typing",
    "type": "Axiom",
    "name": "typing",
    "statement": "A schema determines total assignments with exactly its attributes.",
    "description": "A schema determines total assignments with exactly its attributes.",
    "formalStatement": "U finite; ∀a∈U:D(a)≠∅; t∈Tup(Σ) iff dom(t)=U ∧ ∀a∈U:t(a)∈D(a); arity(Σ)=|U|",
    "assumptions": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.1–3.2, pp. 30–32",
    "sourceNote": "Uses the named tuple-as-function perspective and the optional per-attribute domain mapping. The domain map is explicit in the schema record. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RelationalSchema-tuple-extensionality",
    "type": "Axiom",
    "name": "tuple-extensionality",
    "statement": "Named tuple equality is pointwise equality.",
    "description": "Named tuple equality is pointwise equality.",
    "formalStatement": "t=u iff ∀a∈U:t(a)=u(a), for t,u∈Tup(Σ)",
    "assumptions": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.1–3.2, pp. 30–32",
    "sourceNote": "Uses the named tuple-as-function perspective and the optional per-attribute domain mapping. The domain map is explicit in the schema record. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RelationalSchema-field-update",
    "type": "Axiom",
    "name": "field-update",
    "statement": "A type-correct field update changes exactly its selected field.",
    "description": "A type-correct field update changes exactly its selected field.",
    "formalStatement": "update_a(t,v)(b)=if b=a then v else t(b), for b∈U; a∈U, v∈D(a)",
    "assumptions": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§3.2, named tuples as total functions, p. 32; local functional-update interface",
    "sourceNote": "Specifies additional equations for the selected abstract interface; local conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RelationalSchema-update-readback",
    "type": "Law",
    "name": "update-readback",
    "statement": "Restoring the current field value leaves a tuple unchanged.",
    "description": "Restoring the current field value leaves a tuple unchanged.",
    "formalStatement": "update_a(t,t(a))=t",
    "assumptions": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.",
      "a∈U."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.1–3.2, pp. 30–32",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "At a, the stored value is unchanged; at every other field the defining update rule preserves the value. Apply tuple extensionality.",
    "dependsOn": [
      "urn:csabs:axiom/RelationalSchema-typing",
      "urn:csabs:axiom/RelationalSchema-tuple-extensionality",
      "urn:csabs:axiom/RelationalSchema-field-update"
    ]
  },
  {
    "id": "urn:csabs:law/RelationalSchema-update-shadowing",
    "type": "Law",
    "name": "update-shadowing",
    "statement": "The last write to one field determines that field.",
    "description": "The last write to one field determines that field.",
    "formalStatement": "update_a(update_a(t,v),w)=update_a(t,w)",
    "assumptions": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.",
      "a∈U; v,w∈D(a)."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.1–3.2, pp. 30–32",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Compare components: both sides have w at a and the original tuple value elsewhere.",
    "dependsOn": [
      "urn:csabs:axiom/RelationalSchema-typing",
      "urn:csabs:axiom/RelationalSchema-tuple-extensionality",
      "urn:csabs:axiom/RelationalSchema-field-update"
    ]
  },
  {
    "id": "urn:csabs:law/RelationalSchema-independent-update-commutation",
    "type": "Law",
    "name": "independent-update-commutation",
    "statement": "Updates at distinct fields commute.",
    "description": "Updates at distinct fields commute.",
    "formalStatement": "a≠b ⇒ update_a(update_b(t,w),v)=update_b(update_a(t,v),w)",
    "assumptions": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise.",
      "a,b∈U; v∈D(a); w∈D(b)."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.1–3.2, pp. 30–32",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Split an arbitrary field into a, b, or neither. Both sides have v, w, or the original value respectively; use extensionality.",
    "dependsOn": [
      "urn:csabs:axiom/RelationalSchema-typing",
      "urn:csabs:axiom/RelationalSchema-tuple-extensionality",
      "urn:csabs:axiom/RelationalSchema-field-update"
    ]
  },
  {
    "id": "urn:csabs:theorem/RelationalSchema-zero-arity",
    "type": "Theorem",
    "name": "zero-arity",
    "statement": "There is exactly one tuple over an empty attribute set.",
    "description": "There is exactly one tuple over an empty attribute set.",
    "formalStatement": "U=∅ ⇒ Tup(Σ)={∅}",
    "assumptions": [
      "U is finite, possibly empty; every D(a) is nonempty. Values use identity equality, with no NULL, missing field, or SQL type coercion. Tuple equality is componentwise."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "The unique function with empty domain is the empty function; extensionality identifies any two such tuples.",
    "dependsOn": [
      "urn:csabs:axiom/RelationalSchema-typing",
      "urn:csabs:axiom/RelationalSchema-tuple-extensionality"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.1–3.2, pp. 30–32",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
