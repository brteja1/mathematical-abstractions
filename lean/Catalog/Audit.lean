module

public import Lean

@[expose] public section

open Lean Elab Command

/-- Accept only actual theorem declarations. A constant postulated by `axiom`
has a different ConstantInfo constructor and is rejected even if its type fits. -/
elab "#catalog_witness " decl:ident : command => do
  let name ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo decl
  match (← getEnv).find? name with
  | some (.thmInfo _) => pure ()
  | _ => throwError "Catalog witnesses must be theorem declarations: {name}"
  let axioms ← collectAxioms name
  for a in axioms do
    unless a == ``propext || a == ``Quot.sound || a == ``Classical.choice do
      throwError "Unapproved axiom in witness {name}: {a}"
  logInfo m!"CATALOG_WITNESS {name} | {String.intercalate "," (axioms.toList.map toString)}"

elab "#catalog_model " decl:ident : command => do
  let name ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo decl
  match (← getEnv).find? name with
  | some (.axiomInfo _) => throwError "Model is an opaque axiom: {name}"
  | none => throwError "Missing model: {name}"
  | _ => pure ()
  let axioms ← collectAxioms name
  for a in axioms do
    unless a == ``propext || a == ``Quot.sound || a == ``Classical.choice do
      throwError "Unapproved axiom in model {name}: {a}"
  logInfo m!"CATALOG_MODEL {name}"
