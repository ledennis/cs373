// ---------------------
// SingletonPattern.java
// ---------------------

// https://en.wikipedia.org/wiki/Singleton_pattern

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

class Eager {
    private static final Eager _only = new Eager();

    private Eager ()
        {}

    public static Eager only () {
        return _only;}

    public String f () {
        return "Eager.f()";}}

class Lazy {
    private static Lazy _only;

    private Lazy ()
        {}

    public static Lazy only () {
        if (Lazy._only == null)
            Lazy._only = new Lazy();
        return Lazy._only;}

    public String f () {
        return "Lazy.f()";}}

public final class SingletonPattern extends TestCase {
    public void test_1 () {
    	assertEquals(Eager.only(), Eager.only());}

    public void test_2 () {
    	assertEquals("Eager.f()", Eager.only().f());}

    public void test_3 () {
    	assertEquals(Lazy.only(), Lazy.only());}

    public void test_4 () {
    	assertEquals("Lazy.f()", Lazy.only().f());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(SingletonPatternT.class));}}

/*
% javac -Xlint SingletonPattern.java

% java -ea SingletonPattern
....
Time: 0.001

OK (4 tests)

*/
