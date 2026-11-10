-- Illustrative VHDL-2008-compatible subset of the IEEE 1076-2019 profiles.
-- No GHDL compiler evidence is claimed until the documented commands are run.
package vector_family is
  generic (type element_type; width : positive := 4);
  type vector is array (0 to width - 1) of element_type;
end package;

-- urn:csabs:law/VHDLGenericInterface-named-permutation:
-- named matching is independent of list order; elaboration uses formal order.
package bit_vectors is new work.vector_family
  generic map (width => 8, element_type => bit);

-- urn:csabs:axiom/VHDLGenericInterface-kind-specific-defaults:
-- width may use its constant default; mandatory element_type is supplied.
package default_vectors is new work.vector_family
  generic map (element_type => bit);

entity generic_interfaces_tb is
end entity;

architecture checks of generic_interfaces_tb is
  constant bits8 : work.bit_vectors.vector := (others => '0');
  constant bits4 : work.default_vectors.vector := (others => '0');
begin
  -- urn:csabs:axiom/VHDLGenericElaboration-kind-specific-elaboration:
  -- actual bit type and width/default determine the instantiated array subtype.
  assert bits8'length = 8 severity failure;
  assert bits4'length = 4 severity failure;

  -- urn:csabs:law/VHDLGenericElaboration-null-generate-empty:
  -- positive-direction range 1 to 0 is null, so this failure is not instantiated.
  absent : for i in 1 to 0 generate
    assert false report "null range instantiated a block" severity failure;
  end generate;
end architecture;
