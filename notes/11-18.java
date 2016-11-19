class A {}

class T {
    public static void main (...) {
        A x = new A;
        assert x.getClass() == A.class

        Class c1 = x.getClass();
        Class c2 = A.class;
        assert c1 == c2;

        A y = (A) c1.newInstance();
        A z = (A) c2.newInstance();
        assert y != z

        Class c = Class.forName("A");
        A t = (A) c.newInstance();
