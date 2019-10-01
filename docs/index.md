JSGraphics
==========

The JSGraphics library can be used to easily manipulate an HTML5 Canvas, and 
is used by Stanford's <a href="https://cs106aj.stanford.edu" target="_blank">CS106AJ</a> 
and <a href="https://cs106ax.stanford.edu" target="_blank">CS106AX</a> curricula.

For students: How to read this documentation
---------------------------------------------
This document is intended to read like documentation you might find for any library online.
It's a good thing to be able to read it, and see what such documentation might look like.
If you're ever working on larger projects, you're very likely to be reading documentation
just like this!

Because this is likely the first time you're looking at documentation like this, you'll
see some notation and vocabulary you haven't seen before. I'll briefly go over this
so you this documentation will be useful to you!

### Vocabulary
Some of these definitions may seem scary at first. Don't worry, I'll give an example below.

Word  | Definition
------|-----------
Class | A blueprint for an object. A class says what an object will contain, and also defines all of its functionality. If an object matches a class, we say that object is an *instance* of that class.
Extends | We say that one class *extends* another if the second class has all the same things as the first class, plus extras or changes (but not deletions). If class B extends class A, we say that B is a *subclass* of A, and that A is the *superclass* of B.
Abstract Class | A class with missing parts. An abstract class says what a *subclass* will contain, but it doesn't define all of its functionality. You can't really use abstract classes on their own --- you have to use one of their *subclasses*.
Factory Function | A function that creates an instance of a class.
Method | A function that's a part of a class's functionality. You can only call normal methods on *instances* of a class.
Abstract Method | A method inside an abstract class that's not defined (i.e. that one of the subclasses must define).
Static Method | A method that's part of a *class*, not its instances. You can only call static methods on the class itself.
Field (a.k.a. Instance Variable) | A variable that's part of a class's instances. Each instance of a class will have its own values for each field, and instances don't share fields. It follows, then that you can only access fields from an instance of a class.
Static Field | A variable that's part of a *class*, not its instances. You can only access a static field on the class itself.
Const | Short for *constant*. It means the value shouldn't ever be modified.

#### Vocabulary Example:

```javascript
/**
 * Classes aren't actually a construct inside Javascript. Rather,
 * they're just the idea of what an instance contains. In this case,
 * ClassA has three things: x, y, and a function called addTogether that
 * adds x and y together.
 */
function ClassA(x, y) {  // Our factory function for ClassA.
    let instance = {  // We create our instance here.
        x: x,  // A field (instance variable)
        y: y,  // Another field.
        addTogether: function() { // A method.
          return x + y;
        }
    };
    return instance;
}

//  This is a static method!
ClassA.fromString = function(str) {  // Makes a ClassA from a string like "1, 2"
    let split = str.split(",");
    if(split.length !== 2) return null;
    let parsedX = parseInt(split[0].trim());
    let parsedY = parseInt(split[1].trim());
    return ClassA(parsedX, parsedY);
};

let a1 = ClassA(1, 2);
let a2 = ClassA(3, 4);

console.log(a1.x);  // Prints 1
console.log(a1.addTogether());  // Prints 3
console.log(a2.x);  // Prints 3
console.log(a2.addTogether());  // Prints 7
//  Notice how, even though they're both ClassA's, they have different values?
//  That's the power of instances!


let a3 = ClassA.fromString("5, 6"); 
// See how we said ClassA.fromString? That's how you use static methods.
console.log(a3.addTogether());  // Prints 11

// Now, you can't call static methods from instances! This will crash!
#a1.fromString("7, 8");

function ClassB(x, y, z) {  // Factory function for ClassB
    let aInstance = ClassA(x, y);  // We're extending ClassA here!
    aInstance.z = z;  // See how we're starting with ClassA, then adding a z value...
    aInstance.addTogether = function() {  // ...then changing what addTogether does!
        return aInstance.x + aInstance.y + aInstance.z;
    };
    
    return aInstance;
}

b1 = ClassB(1, 2, 3);
console.log(b1.addTogether());  // Prints 6
```

### Notation

When looking through this documentation, you'll see method definitions that look like this:

*function* ClassName::@d.methodName(parameter1, parameter2[, optionalParameter="default value"])
:   This is a description of what this function does. We have two required parameters, and
    one optional parameter. @p.optionalParemeter has a default value of `"default value"`
    if you omit it.

or this:

@static *function* ClassName.@d.staticMethod([param1="", param2=""[, param3=""]])
:   We have zero required parameters here! You'll notice that we have brackets in brackets.
    That just means that if we want to give @p.param3, we have to also give @p.param1 and @p.param2.
    It also means that @p.param1 and @p.param2 have to be together (if you include one, you have
    to include both. Here's an example:
    
```javascript
ClassName.staticMethod()        // OK! All parameters are optional.
ClassName.staticMethod(1)       // Won't work! Either both or neither of param1 or param2 need to be specified.
ClassName.staticMethod(1, 2)    // OK! param3 is optional, even when param1 and param2 are specified.
ClassName.staticMethod(1, 2, 3) // OK! We've now given all optional parameters.
```

Something you might notice that you haven't seen before is the `::` in `ClassName::methodName`.
This just means that `methodName` is a *method* of `ClassName`, and you can't actually call it directly. Example:
```javascript
// Fails -- methodName is a method, so you can't call it directly from the class.
#ClassName.methodName(1, 2, "hi");

let anInstance = ClassName();
anInstance.methodName(1, 2, "hi");  // This works!
```

You might notice that `staticMethod` has a `.` instead of `::`. This is the reverse of what we just saw:
```javascript
// This works! staticMethod is static, so we call it directly on the class.
ClassName.staticMethod(1, 2, "hi");

let anInstance = ClassName();
// This fails! Static methods need to be called on the class.
#anInstance.staticMethod(1, 2, "hi");
```
