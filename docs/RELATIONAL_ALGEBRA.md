# Codd relational algebra and SQL

The existing [DatabaseRelation](../concepts/DatabaseRelation.md) models finite sets of named tuples. Its interface includes selection, projection, union, natural join, intersection, difference, expanded Cartesian product, theta join and division. [RelationalSchema](../concepts/RelationalSchema.md) supplies typed attributes; [BagRelation](../concepts/BagRelation.md) represents duplicate occurrences separately.

The additions follow E. F. Codd’s [Relational Completeness of Data Base Sublanguages](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf), §§2.3.1–2.3.5, printed pp.7–13 (consulted 2026-11-27). Products concatenate disjoint attribute blocks, theta joins filter products, and division checks every divisor tuple for each observed candidate. Compatible named schemas replace Codd’s positional coordinates. Codd’s empty positional projection list means identity; the catalog retains its existing projection onto no attributes, which produces the singleton empty tuple from a nonempty relation. This adaptation is explicit in the concept record.

| Catalog operation | SQL correspondence under set semantics |
|---|---|
| Selection | `WHERE` with total predicates on non-NULL values |
| Projection | `SELECT DISTINCT` of the selected columns |
| Union / intersection / difference | `UNION` / `INTERSECT` / `EXCEPT`, with aligned compatible columns |
| Expanded product | `CROSS JOIN`, with distinct output attribute names |
| Theta join | `JOIN ... ON`, retaining both input blocks |
| Natural join | Match every common attribute and retain one copy |
| Division | Observed candidates for which no required divisor tuple is missing; expressible with nested `NOT EXISTS` |

For disjoint blocks X,Y, division is

```text
R ÷ S = {x ∈ πX(R) : ∀y ∈ S, x⊕y ∈ R}
      = πX(R) − πX((πX(R) × S) − R).
```

Thus `R ÷ ∅ = πX(R)` and `∅ ÷ S = ∅`, including when both are empty. An SQL translation must start from observed candidates to preserve this behavior.

SQL requires its own semantic mapping: PostgreSQL documents that [`SELECT ALL` retains duplicates while `DISTINCT` removes them](https://www.postgresql.org/docs/current/queries-select-lists.html#QUERIES-DISTINCT), and that [ordinary comparisons involving NULL can yield unknown](https://www.postgresql.org/docs/current/functions-comparison.html). Identity equality here excludes SQL collation/coercion differences. Bags, NULL, ordering, aggregation and outer joins are outside this set profile.

[Lean model and witnesses](../lean/Catalog/RelationalAlgebra.lean) check the added operation equations and division laws using Mathlib finite sets. They do not establish correctness of a SQL implementation. Witness status requires fresh compiler and axiom-audit evidence, separately from catalog/RDF validation.
