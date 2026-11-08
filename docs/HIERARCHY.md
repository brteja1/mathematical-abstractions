# Subject navigation and mathematical hierarchy

The atlas has three views over the same stable concept records:

| View | Organization | Meaning of an arrow |
| --- | --- | --- |
| Subjects | Nested subject arcs from `category` and `parentCategory` | Enabled, explicitly recorded concept relationships |
| Specializations | General concepts above their specializations | Child `specializationOf` parent |
| Dependencies | Prerequisites above their consumers | Consumer `requiresConcept` prerequisite |

Subject membership organizes browsing; it does not transfer operations, axioms or theorems. Concepts may belong to multiple subjects. The first membership determines placement in the Subjects view, while selecting any subject includes all memberships in its subtree. The level views retain all concepts, including isolated concepts and multiple-parent relationships. Dependency cycles share a level; they do not prevent layout. Search, keyboard selection, relationship details, pan and zoom work in every view. Topic and sub-topic arcs use the same viewport framing and animation as right-pane concept links. Topic focus includes all descendant memberships; concept focus retains its immediate family. Repeated clicks refocus the same selection. Clear selection or Escape returns to the overview.

The generated [concept index](../CONCEPTS.md) offers the same nested subject navigation followed by an alphabetical index. CLI and ONTFS category searches include descendant categories, accepting either the category suffix or its full ID.

## First organization pass

Data structures now contains sequential collections, sets and mappings, tree structures, priority collections, connectivity structures and intervals. Concurrency contains synchronization (with locks and lock protocols), ordering and consistency, correctness properties, replication and behavioral models.

These groups reuse existing concepts. `Trie` appears under trees and mappings; `BinaryHeap` under trees and priority collections; `OrderedSet` under sets and sequential collections because its current equality preserves sequence position. Subject groups are Category records, not additional mathematical Concept records.

## Scoped specialization review

The data-structure and concurrency entries were reviewed against their current carriers, equality conventions and interfaces. The existing scoped specialization links remain:

| Child | Parent | Recorded interpretation |
| --- | --- | --- |
| BinarySearchTree | BinaryTree | Retain the labelled binary tree; impose strictly increasing inorder keys. |
| BTree | RoseTree | Instantiate node labels with key lists; impose occupancy, arity, ordering and balance. |
| FiniteSet | Set | Restrict to finite subsets of the fixed element carrier. |
| DatabaseRelation | FiniteSet | Instantiate elements with admissible tuples over one schema. |
| Map | PartialFunction | Restrict to finite-domain partial functions. |
| Trie | Map | Instantiate keys with finite words. |
| Mutex | Lock | Instantiate the single exclusive mode and incompatible distinct holdings. |
| LabelledTransitionSystem | TransitionSystem | Forget action labels using existence of a labelled step. |
| TraceEquivalence | EquivalenceRelation | Use equality of finite trace sets on the fixed LTS state carrier. |

Other connections retain their stated meanings. Stack, Queue and Deque use finite-sequence models but expose different interfaces. BinaryHeap currently uses a level-order sequence, while BinaryTree retains recursive child positions. Union Find uses representative maps for partitions. LamportBakery is a protocol with local and shared state related to a mutex contract; its state carrier is not the mutex optional-owner carrier. Its existing `basisInstantiation` note explains the refinement obligation. None of these connections becomes an inheritance edge merely because the concepts share a subject.

This pass changes navigation memberships and presentation. It introduces no mathematical claim, axiom inheritance or protocol-refinement proof. Future specialization additions require a carrier/interface mapping and sourced review under [AGENTS.md](../AGENTS.md).

## Label rendering

Every concept name, including leaf concepts, is always displayed in all three views. In the Subjects view, top-level subject headings are always shown; a nested subject heading appears only when that exact subject is selected. Nested headings are displayed in full on one line. Their text is centered halfway between their own arc and the parent arc; collision placement never shifts these headings. Selecting a concept clears nested-heading selection. Hidden headings retain their fixed layout slots, so revealing them does not move other labels. There is no name-visibility toggle and no automatic hiding based on selection, zoom, viewport size or collisions. Names wrap without truncation. Placement prefers non-overlapping positions, with the original anchor used when no free position is available; visibility takes priority over collision suppression. Label placement is independent of hover and selection. The canvas clips naturally at its edges when panning or zooming.

Hover and keyboard focus provide a separate full-name callout. Graph node and arc positions, topic focus and right-pane navigation remain unchanged.

After `make markdown`, run `python3 scripts/check_viewer_labels.py` to check actual Chrome/Chromium rendering and interactions at desktop, medium and mobile widths. Add `--screenshots /tmp/atlas-labels` to save images for visual inspection. The runner uses the Python standard library and a locally installed browser.

## Viewer source organization

The page shell is `visualization/template.html`, styles are in `visualization/styles.css`, and graph behavior is in `visualization/app.js`. The script is grouped into data/state, DOM helpers, selection, labels, layouts, details/highlighting, camera handling, SVG construction and startup. `scripts/build_visualization.py` inlines these sources and escaped catalog JSON into the single offline `visualization/index.html`; it needs only Python's standard library. Edit the source files and run `make markdown` to rebuild. The generated page must not be edited directly.
