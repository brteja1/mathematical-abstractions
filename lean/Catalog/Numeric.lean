module

public import Mathlib.Data.ZMod.Basic
public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.Order.Archimedean.Real.Basic
public import Lean.Elab.Tactic.Omega

@[expose] public section

namespace Catalog

abbrev NaturalNumber := Nat
abbrev Integer := Int
abbrev ArbitraryPrecisionInteger := Int
abbrev BitVector (width : Nat) := BitVec width
abbrev FixedWidthUnsignedInteger (width : Nat) (_ : 0 < width) := BitVec width
abbrev ModularInteger (modulus : Nat) (_ : 2 ≤ modulus) := ZMod modulus
abbrev CheckedInteger (lower upper : Int) (_ : lower ≤ upper) :=
  {z : Int // lower ≤ z ∧ z ≤ upper}
abbrev SaturatingInteger (lower upper : Int) (h : lower ≤ upper) :=
  CheckedInteger lower upper h

abbrev FixedWidthSignedInteger (width : Nat) (_ : 0 < width) :=
  {z : Int // -(2 ^ (width - 1) : Int) ≤ z ∧ z < (2 ^ (width - 1) : Int)}

def checkRange (lower upper : Int) (z : Int) :
    Option {z : Int // lower ≤ z ∧ z ≤ upper} :=
  if h : lower ≤ z ∧ z ≤ upper then some ⟨z, h⟩ else none

def checkedAdd {lower upper : Int} {h : lower ≤ upper}
    (x y : CheckedInteger lower upper h) := checkRange lower upper (x.val + y.val)

def saturate (lower upper : Int) (h : lower ≤ upper) (z : Int) :
    SaturatingInteger lower upper h :=
  ⟨min upper (max lower z), by constructor <;> omega⟩

def saturatingAdd {lower upper : Int} {h : lower ≤ upper}
    (x y : SaturatingInteger lower upper h) := saturate lower upper h (x.val + y.val)

def checkSigned (w : Nat) (h : 0 < w) (z : Int) : Option (FixedWidthSignedInteger w h) :=
  if hz : -(2 ^ (w - 1) : Int) ≤ z ∧ z < (2 ^ (w - 1) : Int) then some ⟨z, hz⟩ else none

def signedAdd {w : Nat} {h : 0 < w} (x y : FixedWidthSignedInteger w h) :=
  checkSigned w h (x.val + y.val)

/-- Division by zero and unrepresentable quotients have no defined result. -/
def signedDiv {w : Nat} {h : 0 < w} (x y : FixedWidthSignedInteger w h) :=
  if y.val = 0 then none else
    checkSigned w h (x.val.tdiv y.val)

inductive RoundingMode where
  | nearestEven | nearestAway | towardZero | towardPositive | towardNegative
  deriving DecidableEq

structure FloatFormat where
  width : Nat
  radix : Nat
  precision : Nat
  minExponent : Int
  maxExponent : Int
  subnormals : Bool
  radix_ge_two : 2 ≤ radix
  precision_positive : 0 < precision
  exponents_ordered : minExponent ≤ maxExponent

/-- The mathematical finite value set, including gradual underflow when enabled. -/
def floatRepresentable (f : FloatFormat) (x : ℝ) : Prop :=
  x = 0 ∨ ∃ (negative : Bool) (m : Nat) (e : Int),
    0 < m ∧ m < f.radix ^ f.precision ∧
    f.minExponent ≤ e ∧ e ≤ f.maxExponent ∧
    (f.radix ^ (f.precision - 1) ≤ m ∨ (f.subnormals = true ∧ e = f.minExponent)) ∧
    x = (if negative then -1 else 1) * (m : ℝ) *
      (f.radix : ℝ) ^ (e - (f.precision - 1 : Nat))

inductive FloatValue (f : FloatFormat) where
  | zero (negative : Bool)
  | finite (value : {x : ℝ // x ≠ 0 ∧ floatRepresentable f x})
  | infinity (negative : Bool)
  | nan (payload : Nat)

structure FloatFlags where
  invalid : Bool
  divideByZero : Bool
  overflow : Bool
  underflow : Bool
  inexact : Bool

inductive FloatOperation where
  | add | subtract | multiply | divide | squareRoot

/-- An execution interface, not a verified IEEE arithmetic implementation.
The run/round laws and NaN payload bounds still need a refinement before any
numeric law can be registered as a witness for this interface. -/
structure FloatingPointType (format : FloatFormat) where
  rounding : RoundingMode
  round : RoundingMode → ℝ → FloatValue format × FloatFlags
  run : RoundingMode → FloatOperation → List (FloatValue format) →
    FloatValue format × FloatFlags

def binary16Format : FloatFormat := ⟨16, 2, 11, -14, 15, true, by decide, by decide, by decide⟩
def binary32Format : FloatFormat := ⟨32, 2, 24, -126, 127, true, by decide, by decide, by decide⟩
def binary64Format : FloatFormat := ⟨64, 2, 53, -1022, 1023, true, by decide, by decide, by decide⟩
def binary128Format : FloatFormat := ⟨128, 2, 113, -16382, 16383, true, by decide, by decide, by decide⟩
abbrev Binary16 := FloatingPointType binary16Format
abbrev Binary32 := FloatingPointType binary32Format
abbrev Binary64 := FloatingPointType binary64Format
abbrev Binary128 := FloatingPointType binary128Format

end Catalog
