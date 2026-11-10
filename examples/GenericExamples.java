import java.util.ArrayList;
import java.util.List;

/** Selected established Java generic rules, mapped to catalog IDs below. */
public class GenericExamples {
    static final class Box<T extends Number> {
        final T value;
        Box(T value) { this.value = value; }
        T get() { return value; }
    }

    // urn:csabs:law/JavaParameterizedType-member-argument-replacement:
    // the declared T member is observed as Integer for Box<Integer>.
    static Integer integerMember(Box<Integer> box) { return box.get(); }

    // urn:csabs:law/JavaWildcardCapture-super-capture-lower-bound:
    // Integer is an admissible write to List<? super Integer>; reading gives Object.
    static void appendInteger(List<? super Integer> values) { values.add(7); }
    static Number readNumber(List<? extends Number> values) { return values.get(0); }

    // urn:csabs:axiom/JavaWildcardCapture-fresh-nonrecursive:
    // capture one unknown element type as T, then read/write the same T.
    static void preserveFirst(List<?> values) { preserveCaptured(values); }
    private static <T> void preserveCaptured(List<T> values) {
        if (!values.isEmpty()) { values.set(0, values.get(0)); }
    }

    static <T extends Number> List<T> singleton(T value) { return List.of(value); }

    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<>(3);
        if (integerMember(integerBox) != 3) { throw new AssertionError("member substitution"); }

        List<Number> numbers = new ArrayList<>();
        appendInteger(numbers);
        preserveFirst(numbers);
        if (readNumber(numbers).intValue() != 7) { throw new AssertionError("wildcard capture"); }

        // urn:csabs:law/JavaTypeInference-target-narrows-solutions:
        // Number is fixed by List<Number> target; Integer input supplies a lower bound.
        List<Number> inferred = singleton(Integer.valueOf(11));
        if (inferred.get(0).intValue() != 11) { throw new AssertionError("target inference"); }

        // urn:csabs:law/JavaTypeErasure-same-head-erasure:
        // two source parameterizations share the runtime nominal class.
        Box<Double> doubleBox = new Box<>(2.5);
        if (integerBox.getClass() != doubleBox.getClass()) { throw new AssertionError("erasure"); }
        System.out.println("Java generic examples passed");
    }
}
