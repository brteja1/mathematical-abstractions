#include <limits>
#include <tuple>
#include <type_traits>
#include <utility>

// Carriers: canonical C++ type identities, converted int constants and template
// declarations. Observations: is_same_v, integral constants, or compiler rejection.
// urn:csabs:law/TemplateMetafunction-equivalent-argument-observation:
// aliases and equal converted int arguments preserve the observed instantiation.
template<class T> struct atom_type { using type = T; };
template<class T> struct atom_type<T*> : atom_type<T> {};
template<class T, int N, template<class> class F> struct observed {
    using type = typename F<T>::type;
    static constexpr int value = N;
};
using Int = int;
static_assert(std::is_same_v<observed<Int*, 2 + 2, atom_type>,
                             observed<int*, 4, atom_type>>);
static_assert(std::is_same_v<typename atom_type<int**>::type, int>);

// urn:csabs:axiom/TemplateSpecialization-selection:
// no match -> primary; one match -> that partial; strict winner -> both-pointer.
template<class A, class B> struct choice { static constexpr int value = 0; };
template<class A, class B> struct choice<A*, B> { static constexpr int value = 1; };
template<class A, class B> struct choice<A, B*> { static constexpr int value = 2; };
template<class A, class B> struct choice<A*, B*> { static constexpr int value = 3; };
static_assert(choice<int, int>::value == 0);
static_assert(choice<int*, int>::value == 1);
static_assert(choice<int, int*>::value == 2);
static_assert(choice<int*, int*>::value == 3);

// urn:csabs:axiom/TemplateSubstitution-context-classification:
// a missing member in a function return-type immediate context rejects only
// that candidate. The fallback is separately supplied, not guaranteed by SFINAE.
template<class T> auto has_member(int) -> decltype(sizeof(typename T::member), std::true_type{});
template<class> auto has_member(...) -> std::false_type;
struct rich_object { using member = int; using extra = int; };
static_assert(!decltype(has_member<int>(0))::value);
static_assert(decltype(has_member<rich_object>(0))::value);

template<class T> struct required_helper { using member = typename T::member; };
template<class T> typename T::member lexical(typename required_helper<T>::member);
template<class> int lexical(...);
// urn:csabs:law/TemplateSubstitution-early-failure-stops:
// the invalid leading return type prevents reaching required_helper<int>.
static_assert(std::is_same_v<decltype(lexical<int>(0)), int>);

template<class T> concept HasMember = requires { typename T::member; };
template<class T> concept Rich = HasMember<T> && requires { typename T::extra; };
template<HasMember T> constexpr int constraint_rank(T) { return 1; }
template<Rich T> constexpr int constraint_rank(T) { return 2; }
// urn:csabs:law/TemplateConstraint-conjunction-subsumes-atom:
// Rich reuses the originating HasMember atom, selecting the stronger overload.
static_assert(constraint_rank(rich_object{}) == 2);

template<class T> constexpr bool unsafe_check() { return T::value; }
template<class T> concept Safe = HasMember<T> && unsafe_check<T>();
// urn:csabs:law/TemplateConstraint-false-left-skips-invalid-right:
// int fails HasMember before unsafe_check<int>'s invalid body is instantiated.
static_assert(!Safe<int>);

template<class... A> struct zip_types {
    template<class... B> using with = std::tuple<std::pair<A, B>...>;
};
// urn:csabs:law/TemplateParameterPack-zip-not-product:
// two pairs, corresponding order, duplicate arguments retained, and empty case.
static_assert(std::is_same_v<zip_types<int, int>::with<char, long>,
                             std::tuple<std::pair<int, char>, std::pair<int, long>>>);
static_assert(std::is_same_v<zip_types<>::with<>, std::tuple<>>);

template<int... N> constexpr int left_subtract = (10 - ... - N);
template<int... N> constexpr int right_subtract = (N - ... - 10);
template<bool... B> constexpr bool all = (B && ...);
// urn:csabs:axiom/TemplateParameterPack-fold-parentheses:
// nonassociative subtraction exposes grouping; empty binary folds keep init.
static_assert(left_subtract<1, 2> == 7);
static_assert(right_subtract<1, 2> == 9);
static_assert(left_subtract<> == 10 && right_subtract<> == 10);
static_assert(all<>);

constexpr int lookup_target(...) { return 0; }
template<class T> constexpr int staged_call(T value) { return lookup_target(value); }
constexpr int lookup_target(int) { return 1; }
namespace associated {
struct token {};
constexpr int lookup_target(token) { return 2; }
}
// urn:csabs:law/DependentNameLookup-later-ordinary-declaration-irrelevance:
// the later ordinary int overload is absent from definition-context candidates.
static_assert(staged_call(1) == 0);
// urn:csabs:axiom/DependentNameLookup-guarded-adl-union:
// an associated-namespace declaration is an admissible instantiation ADL candidate.
static_assert(staged_call(associated::token{}) == 2);

constexpr int guarded_increment(bool choose_safe, int x) { return choose_safe ? 1 : x + 1; }
// urn:csabs:law/CompileTimeEvaluation-unchosen-overflow-irrelevant:
// int width/range comes from this compiler; the overflowing branch is unchosen.
static_assert(guarded_increment(true, std::numeric_limits<int>::max()) == 1);
static_assert(guarded_increment(false, 4) == 5);

#if defined(TMP_FAIL_WRONG_KIND)
// urn:csabs:axiom/TemplateMetafunction-kind-and-domain: value is not a type.
using wrong_kind = observed<0, 4, atom_type>;
#endif

#if defined(TMP_FAIL_AMBIGUITY)
// urn:csabs:law/TemplateSpecialization-incomparable-ambiguity:
// both partials match and neither is more specialized than the other.
template<class A, class B> struct ambiguous_choice {};
template<class A, class B> struct ambiguous_choice<A*, B> { using type = int; };
template<class A, class B> struct ambiguous_choice<A, B*> { using type = int; };
using ambiguous_result = typename ambiguous_choice<int*, int*>::type;
#endif

#if defined(TMP_FAIL_HARD_ERROR)
// urn:csabs:law/TemplateSubstitution-hard-error-is-not-sfinae:
// helper instantiation is reached before the invalid trailing return type.
template<class T> auto hard(typename required_helper<T>::member) -> typename T::member;
template<class> int hard(...);
using hard_result = decltype(hard<int>(0));
#endif

#if defined(TMP_FAIL_CONSTRAINT_BODY)
// urn:csabs:axiom/TemplateConstraint-short-circuit:
// reversing the guard reaches a required error in unsafe_check<int>'s body.
template<class T> concept Unsafe = unsafe_check<T>() && HasMember<T>;
static_assert(!Unsafe<int>);
#endif

#if defined(TMP_FAIL_ATOMIC_IDENTITY)
// urn:csabs:axiom/TemplateConstraint-atom-identity:
// equivalent requires-expressions have distinct source origins; no subsumption.
template<class T> concept HasMemberAgain = requires { typename T::member; };
template<HasMember T> constexpr int atomic_rank(T) { return 1; }
template<class T> requires (HasMemberAgain<T> && true)
constexpr int atomic_rank(T) { return 2; }
constexpr int ambiguous_atomic_result = atomic_rank(rich_object{});
#endif

#if defined(TMP_FAIL_PACK_LENGTH)
// urn:csabs:axiom/TemplateParameterPack-simultaneous-expansion:
// unequal simultaneous packs are rejected, rather than truncated or multiplied.
using wrong_length = zip_types<int, long>::with<char>;
#endif

#if defined(TMP_FAIL_EMPTY_FOLD)
// urn:csabs:axiom/TemplateParameterPack-fold-parentheses:
// unary + has no empty-pack identity under this C++20 profile.
template<int... N> constexpr int unary_sum = (N + ...);
constexpr int invalid_empty_sum = unary_sum<>;
#endif

#if defined(TMP_FAIL_OVERFLOW)
// urn:csabs:law/CompileTimeEvaluation-overflow-is-not-wrapping:
// a required constant-expression evaluation reaches signed int overflow.
constexpr int invalid_overflow = guarded_increment(false, std::numeric_limits<int>::max());
#endif

int main() { return 0; }
