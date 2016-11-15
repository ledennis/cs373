abstract class A {
    public final    void f (int) {} // child can not override
    public          void g (int) {} // child can     override
    public abstract void h (int);   // child must    override

A x;
if (...)
    x = new B;
else
    x = new C;
x.f(2);

/*
Java does not exhibit dynamic binding in the following:
    final   method
    private method
    static  method
    final   class
*/

class Lazy {
    static Lazy l;

    private Lazy () {}

    public static Lazy only () {
        if (l == null)
            l = new Lazy();
        return l;}}

class Eager {
    static Eager e = new Eager;

    private Eager () {}

    public static eager only () {
        return e;}}
