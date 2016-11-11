/*
In Java, what are the consequences of an abstract method?
    1. derived class must define or become abstract
    2. base class must be abstract
    3. definition in the base becomes prohibited
*/

class A {
    public void f (int) {}}

class B extends A {
    public void f (String) {}}

class T {
    public static void main (...) {
        B x = new B;
        x.f(2);}}                   // A.f

/*
Lookup differs between C++ and Java.
In C++ the name is being looked up. In Java the signature is being looked up.
The C++ way is better. It reduces the chance of a logic error.
*/

class A {
    public void f (long) {}}

class B extends A {
    public void f (int) {}}

class T {
    public static void main (...) {
        A x;
        if (...)
            x = new B();
        else
            x = new C();
        x.f(2);}}

/*
Dynamic binding is implemented via virtual function tables.
*/

class A {
    public final    void f (int) {}
    public          void g (int) {} // avoid
    public abstract void h (int);

/*
Changing f's signature either continues to work or causes a compilation error.
Changing g's signature can introduce a logic       error, because the derived classes are no longer overriding it.
Changing h's signature causes        a compilation error, because the derived classes are no longer overriding it.
*/
