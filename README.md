# CS-3250 Notes

### 5/29/19 first thoughts on classes

Classes:


```
Player class
    name
    currrent position as instance of Place
    health/damage
    inventory
        equipped?
    abilities/traits/perks (?)

Place class
    name
    description
    triggers - a method that modifies description field (adds clues as they are discovered)
    items/objects/clues
    enemies/NPCs as instances of Player
    loot (separate from items/objects?)
    adjacency list (N, S, E, W, NE, NW, SE, SW, up, down) as a dict, maybe?
    transitions allowed (are some directions blocked by clues yet to be discovered? Locked doors?)
```


> Perhaps the adjacency list can be a dict with direction names as keys, and tuples consisting of `(Place, bool)` for an instance of place (or `null`), and a `boolean` to tell us if we can enter. Something like:
>
>
> `{"N", (placeToNorth, true), "S", (placeToSouth, false), "E", (null, false), ...}`


Gameplay loop:


> methods for actions like movement, equipping, inspecting, using... etc.


**Movement:**
* `get` movement command (e.g.: "N" entered into CLI)
* `get` player's current position
* `get` current position's adjacency list
* `set` player's current position to `currentPlace.adj("N")` (or whatever) if able, error if not

**Equipping:**
* `get` equip command (e.g.: "equip knife" entered into CLI)
* `get` player's inventory
* `get` player's equipped (equip multiple? Lantern + knife? Do we need to break Item classes into utilities and weapons)
* `set` player's equipped to `inventory.Items("knife")` if applicable

### 6/3/19 class notes

**TODO:**
* read scrum guide
* ~~get books~~
* VENV
* ***5 dysfunctions, design patterns (FOR FIRST TEST)***

### Zork notes

Bit of a learning curve. Not sure if there's a `help` function of any sort, but that sort of added to the appeal for me personally.


**Things I like:**
* The simplicity—seriously, this game is charming as heck
* The writing is short and sweet—some of the descriptions are a little bland, but in general I've really enjoyed it
* There's a definite rush of excitement when you uncover a clue

**Things I don't like:**
* Some commands don't seem to have enough aliases
* Sometimes movement seems unable to be reversed (i.e., go east, then go west, sometimes you end up somewhere other than where you previously were)

### 6/6/19 class notes

**TODO:**
* ~~VENV, unit tests~~
* read *The Cathedral and the Bazaar*

### Graph theory research notes

Mostly review for me, although the video I watched contained some interesting worked examples:

* The lecturer introduces the results of two studies considering the relati ve promiscuity between men and women with opposite gender partners. Both results are mathematically proven erroneous using only basic graph theory properties.
* The Graph Coloring Problem is discussed in the context of final exam scheduling for classes with overlapping enrollment.

Sources: [Lec 6 | MIT 6.042J Mathematics for Computer Science, Fall 2010](https://youtu.be/h9wxtqoa1jY)

### 6/6/19 class notes

* Program requirements
    * statements that define and quantify what the program needs to do
    * the work requirements aren't used in the same way as elsewhere
    * software requirements tend to be negotiable

* Functional requirements
    * what a program *needs* to do
    * binary; yes or no

* Non-functional requirements
    * the manner in which the functional requirements need to be achieved
    * performance, usability, maintainability
    * tend to be on scale

* Design constraints
    * statements that constrain the ways in which the software can be designed and implemented
    * platform, language, database, webapp, GUI, etc.

### 6/10/19 class notes

* Graphs
    * connected: can we reach every vertex
    * fully connected: can we reach every vertex via only one edge traversal
    * Dijkstra: if a path exists, there exists a shortest path between two verticies
    * [NetworkX](https://networkx.github.io)
        * graphs, digraphs, multigraphs

### 6/12/19 class notes

* Non-functional examples
    * performance
    * real-time performance
    * maintainability
        * readability
        * modularity
        * debugability
        * traceability
    * modifiabiity
* Analysis
    * static — analyzing the non-running code
        * linters, cyclomatic complexity, method length
        * style guide
    * dynamic — analyzing a running program
        * code smells, bugs, security vulnerabilities
* Testing
    * Acceptance
    * Unit: method-level testing
    * Integration: class-level testing
    * System (does the program work?!)
    * Mutation testing (making small random changes and watching test coverage)

### 6/19/19 class notes

* **Design patterns**
    * Formalized best practices applicable to common application problems
    * OO design patterns generally show relationships and interactions between classes and patterns
    * Creates a shared vocabulary
        * Developers can interact in more concise ways
    * Keeps thinking/designing at the abstract (pattern) level
    * Originated as an architectural concept by Christopher Alexander (1977/79)
        * In 1987, Kent Back and Ward Cunningham began experimenting with the idea of applying patterns to programming—specifically pattern languages—and presented their results at the OOPSLA conference that yeah
        * In software, Alexander is regarded as the father of the pattern language movement
        * Wiki came from Alexander's philosophy
        * A Pattern Language: *Towns, Buildings, Construction* (1977)
        * *The Timeless Way of Building* (1979)
        * ~98% of the US population lives within six turns of a major highway (US roads form a fractal grid)
        * *Notes on the Synthesis of Form*
    * Groups and Concepts
        * Design patterns were originally grouped into categories:
            * Creational
            * Structural
            * Behavioral
        * Described using the concepts:
            * Delegation
            * Aggregation
            * Consultation
    * First Design Principle
        * Identify and separate dynamic and static elements
        * Alter or extend without affecting other parts
        * Basis of almost every design pattern
        * Conducive to more easily reusable objects
        * Objects delegate behavior to other objects
    * Second Design Principle
        * Program to an interface, not an implementation
            * Not necessarily a Java interface
            * Program to a supertype
                * `private Map<String, Boolean> urls = new ConcurrentHashMap<String, Boolean>();`
            * Can then better use polymorphism
            * Can more easily change implementation
    * Third Design Principle
        * Favor composition over inheritance
        * Favor *has-a* relationships over *is-a* relationships (cat *is a* mammal *is an* animal; platypus inherits from other "classes")
        * Inheritance limits resusability
* **Strategy Pattern**
    * Defines a family of algorithms, encapsulates each one, and makes them interchangeable (sorting algorithms for different situations)
    * Strategy lets the algorithm vary independently from the clients that use it
    * `Context` *decides* which algorithm is required → `Strategy` *returns* the algorithm chosen by `Context`
* **Observer Pattern**
    * Defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and update automatically
    * An object, called the `Subject` maintains a list of its dependents, called `Observers`, and notifies them automatically of any state changes
    * Mainly used to implement distributed event handling systems in "event-driven" software
    * Key part in the familiar model-view-controller (MVC) architecture
    * Design principle
        * Strive for loosley-coupled designs between objects that interact
            * Highly cohesive objects/methods (highly specialized, do only one thing)
        * Objects have very little information about each other
        * No shared state
    * Helps decouple objects
    * Subject knows only that the observer implements the `Observer` interface
    * New observers can be added at any time
    * New types of observers can be added
    * Can reuse subjects and observers independently
    * Changes have no affect on each other
    * **WARNINGS**
        * Doesn't depend on order of evaluation of notifications
        * Java `Observable` is a class
            * Not an interface
            * Must inherit
            * `setChanged()` is protected

### Mocking

* **Input Output Unit Testing**
    * Want to add `conftest`
    * Mocking used for any application using *any* input (network cards, typed user input, mouse movement)
    * Go to `requirements-dev.txt`, add `pytest-mock`
    * `fixture` an argument passed into a test

```python
@pytest.fixture
def run(capsys, mocker):
    def _do_run(method, *args, **kwargs):
        mocked_input = mocker.patch('builtins.input')
        if 'input_values' in kwargs:
            mocked_input.side_effect = kwargs['input_values']
            del kwargs['input_values']
        else:
            mocked_input.side_effect = ['whatever']
        method(*args, **kwargs)
        captured = capsys.readouterr()
        return captured.out, captured.err

    return _do_run
```

### 6/20/19

* Add `Player.previous_room()`
* Add `Player.adjacent()`
* Store room data as tuple:
    * `(Player.adjacent(direction_request), Boolean)`
* Write actual navigation method to:
    1. set `Player.previous_room()` to `Player.current_room()`
    2. check `Player.adjacent(direction_request)[1]` is True, else we can't move 
    3. if `2. == True` set `Player.current_room()` to `Player.adjacent(direction_request)`

**Example map data:**

```yaml
Boss:
    adjacent:
        north: ["Gold", True]
        south: ["Entrance", False]
        east: ["Cave", False]
        west: ["Armory", False]
    description:
    items:
    clues:
Entrance:
    adjacent:
        north: ["Boss", True]
        south: [null, False]
        east: ["Cave", True]
        west: ["Armory", True]
    description:
    items:
    clues:
Armory:
    adjacent:
        north: ["Boss", True]
        south: [null, False]
        east: ["Entrance", True]
        west: [null, False]
    description:
    items:
    clues:
Cave:
    adjacent:
        north: ["Boss", True]
        south: [null, False]
        east: [null, False]
        west: ["Entrance", True]
    description:
    items:
    clues:
Gold:
    adjacent:
        north: [null, False]
        south: ["Boss", True]
        east: [null, False]
        west: [null, False]
    description:
    items:
    clues:
```


### 6/24/19 class notes

* Open/Close principle
* Decorators
    * Have the same super type of the objects they decorate
    * Can have one or more decorators
    * Can pass wrapped object anywhere original could be passed
    * Adds behavior before and/or after delegating object
    * Objects can be decorated at runtime
**Decorator Pattern**
* Attaches additional responsibilities to an object dynamically
* Provide a flexible alternative to sub-classing for extending functionality
* Inheritance
    * Using inheritance to get type matching but not behavior
        * Java requires this, other languages don't
**Factory pattern**
* Handles the details of object creation
    * Encapsulates the creation in a subclass
    * Decouples interface from creation
* Can return a variety of types
* Client doesn't care which types
* Can add additional types easily
* If static, can't subtype to extend
* Helps create objects without having to specify the exact class of the object that will be created
* Don't have to be abstract
    * Can have default and that can call down if necessary
* **Dependency Inversion Principle**
    * Depend upon abstractions
    * Do not depend upon concrete classes
    * High-level modules should not depend on low-level modules
        * Both should depend on abstractions
    * Abstractions should not depend on details
    * No variable should hold a reference to a concrete class
    * No class should derive from a concrete class
    * No method should override an implemented method of any of its base classes
* **Dependency Injection**
    * One object supplies the dependencies of another object
    * Passing of a dependency to a dependent object
    * Values produces within the class from new or static methods is prohibited
    * Should accept values passed in from outside
    * Allows the client to make acquiring dependencies someone else's problem
    * Intended to decouple objects to the extent that no client code has to be changed simply because an object it depends on needs to be changed to a different one
* **Inversion of Control**
    * A design principle in which custom-written portions of a computer program receive the flow of control from a generic framework
    * A software architecture with this design inverts control as compared to traditional procedural programming
        * In traditional programming, the custom code that expresses the purpose of the program calls into reusable libraries to take care of generic tasks
        * With inversion of control, it is the framework that calls into the custom, or task-specific, code
* **Abstract Factory Pattern**
    * Provides an interface for creating families of related or dependent objects
**Abstract vs non-**
* Factory
    * Creation through an interface
    * Creates objects of a single type
* Abstract Factory
    * Creation through composition
    * Instantiated via new and passed
    * Creates families of related objects via factories
**The Singleton**
* Need only one of
    * Thread pools, caches, dialog boxes, prefernces, logging, device drivers, I/O
    * But: might not need each time, so lazy initialization

```Java
// NOTE: This is not thread safe!
public class Singleton {
    private static Singleton uniqueInstance;
    
    private Singleton() {}

    // public static synchronized fixes race condition here
    public static Singleton getInstance() {
        if (uniqueInstace == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }

    public String getDescription() {
        return "I'm a classic Singleton!";
    }
}
```

* Threading
    * Synchronize `getInstance`
    * Eagerly create
* Visibility and Synchronization
    * Visibility assures that all threads read the same value of a variable
    * Synchronization makes sure that only one thread can write to a variable
    * These are two different things!
* Volatile
    * Reads and writes happen to main memory
        * Not from individual CPU caches
    * Writes to a volatile also write all the thread-visible variables to main memory
    * Reads from a volatile re-read all thread-visible ...
* Atomic
    * Reads and writes are atomic for reference variables and for most primitive variables (except long and double)
    * Reads and writes are atomic for all variables declared volatile (including long and double)
    * And there are `AtomicInt`, `AtomicLong`, ...
* Volatile is not always enough
    * If there is a read/modify/write such as variable++
    * Must use synchronized keyword is to remove ...

### 6/26/19 class notes

**Command Pattern**

* Behavioral design pattern in which an object is used to encapsulated all the information needed to perform an action or trigger an event at a later time
* Client is responsible for creating a concrete command and setting its receiver
* Invoker holds a command object and at some point calls its `execute()` method
* Command declares an interface that has at least an `execute()`

**Adapter and Facade**

* Adapter converts the interface of a class into another interface the clients expect
    * Lets classes work together that couldn't otherwise because of incompatible interfaces
    * Two types
        * Object adapters use composition
        * Class adapters use inheritance
* Facade provides a unified interface to a set of interfaces in a subsystem
    * Defines a higher-level interface that makes the subsystem easier to use
* Adapter alters an interface to make it usable
* Facade makes a complicated interface easier to use

**Principle of Least Knowledge**

* Talk to only immediate friends
* Decouples
* Law of Demeter
* Methods may talk to
    * Their own object
    * Objects passed as parameters
    * Objects they instantiate
    * Instance variables

**Template method**

* Behavioral design pattern that defines the program skeleton of an algorithm in an operation, deferring some steps to subclasses
* Lets one redefine certain steps of an algorithm without changing the algorithm's structure

**Hot beverage**

* For both coffee and tea
    * boil water (same, in base class)
    * use hot water to extract (different abstract in base class)
    * pour into cup (same)
    * add condiments (different)
* prepareRecipe is template method
    * all steps present
    * some are handled by base class
    * some by subclass
* Hooks
    * Can define concrete methods that do nothing unless subclass overrides them
    * Use abstract when subclass must implement, hooks when optional
* Hollywood principle
    * Don't call us, we'll call you
    * Low-level hooks into system, high-level calls at the appropriate time
    * Java `Arrays.sort` calls `compareTo()`

**Summary**

* To prevent subclasses from changing the algorithm, make the template method final
* Both the strategy and template patterns encapsulate algorithms
    * Strategy via composition
    * Template via inheritance
* Factory is a very specialized template
    * Returns result from subclass

### 7/10/19 class notes

**Static Factory Methods over Constructors**

* One advantage, they have names
* A class can have only one constructor with a given name
* Static factory methods don't have to create a new object
* Constructors always do
* Helps with immutable classes and pre-constructed instances
* Singletons, flyweights, non-instantiable
* Can return a subtype
* Polymorphic
* Returned class doesn't need to exist at the time the class is written
* Disadvantages
    * Classes without public or protected constructors cannot be sub-classed

**Consider a Builder when faced with many constructor parameters**

* Create empty instance and have many sets
    * Problem: instance in inconsistent state
* Builder pattern
* `build()` is a parameter-less static method
* Required parameters passed into constructor
    * Optionals `set()`
    * Other languages have optional parameters instead

### 7/15/19 class notes

**Consistency**

* Do not write an equals method that depends on reliable resources

**equals recipe**

* Check for `object == this`
* Use `instanceof` to check for type
* Cast argument to correct type
* Check `Test ==` for all significant fields
    * Except for `Float.compare`, `Double.compare`, and `Arrays.equal`
* Also override `hashCode`
* use `@Override`

**Creating a hashCode**

* Set `result = 17`
* For all the fields
    * bool → `c = f ? 1 : 0`
    * byte, char, short, int → `c = (int) f`
    * beaty went too fast
    .
    .
    .
* Update result = `31 * result + c`
* Exclude any redundant fields
    * You shouldn't have any anyway
* Ignore any fields ignored by `equals`


**Classes and Interfaces**

* Minimize the accessibility of classes and members
* Hide as much as possible
* Encapsulation
* Conducive to decoupling
* If a class is used nowhere else, nest it within its user
* Try to avoid `protected` as well
* If a method overrides a superclass method, it must have the same access level
    * Liskov inversion principle

### 7/18/19 class notes

**Prefer class hierarchies to tagged classes**

* Verbose, error-prone, and inefficient
* imitation of a real class hierarchy

**Favor static member classes over non-static**

* A nested class is defined within another class
* Only serves the enclosing class
* Four kinds
    * static
    * non-static
    * anonymous
    * local
* Last three are called inner classes
* Anonymous classes
    * have no names
    * not a member of enclosing class
    * declared and instantiated at the same 
    
**Generics**

* Typing
    * Java's type system is very complex
    * it adds various mechanism to add "generics"
    * other languages simply have references to objects and duck typing
* gereic classes and interfaces are known as generic types
* generic types define sets of parameterized types

### Item generation ideas

**item generation:**
1. size
2. base_name(size)
3. rarity(type)
4. material(rarity, size)
5. condition(rarity, material) → name
6. stats(rarity, material)

**dungeon filler generation:**
1. size + hardness
2. base_name(size)
3. material(type)
4. condition(material) → name

**dungeon flavor text generation:**
1. size
2. base_name(size)
3. material(size)
4. condition(material)
5. flavor(material, condition)

### 7/22/19 class notes

* Arrays are covariant
    * if sub is a subtype of super, sub[] is a subtype of super[]
* Generics are invariant

**Arrays vs generics**

* Arrays are reified
    * element types are enforced at *runtime*
* Generics are implemented by type erasure
    * types enforced at compile time and erase type at runtime
* Cannot create arrays of generic types, parameterized types, or type parameters
* `List<String>` is not a subtype of `List<Object>`

    ```Java
    public void pushAll(Iterable<? extends E> src) {
        for (E e : src)
            push(e);
    }
    ```

* PECs: producer/extends, consumer/super
* do not use wildcard return types
    * client of class shouldn't have to know about wildcards

**Enumerations and annotations**

* Use enumerations instead of integer constants
    * Java's enumerations are more powerful than other languages'
    * They're almost classes
        * can't extend but can implement an interface
    * Export one instance of each enumeration via a public static final field
    * provide compile-time type safety
    * can't pass or assign incorrectly
    * don't count on ordinal values
    * use constructor instead
    * use `EnumSets` instead of bit fields

* prefer annotations to naming patterns
    * JUnit a major example
    * consistently use `@override`
        * makes sure you are actually overriding
    * ammarker interface is one with no methods
        * serializable is an example
        * indicates object can be written via `ObjectOutputStream`

**Reflection**

* examine, introspect, and modify its own structure and behavior at runtime
    * early programs were self-modifying in order to loop
* reflection allows inspection of classes, interfacesm fields, and methods at runtime
* it also allows instantiation of new objects and invocation of methods
* reflection is often used as part of software testing, such as for the runtime creation/instantiation of mock objects

### 7/24/19 class notes

**most parameters have restrictions on their validity**

* AKA preconditions
* program defensively
* catch problems as soon as possible
* fail fast
* method may die
    * or worse, work but in an unexpected way
* throw an exception
    * an `IllegalArgumentException`

### 7/25/19 class notes

**Lambdas and streams**

* prefer lambdas to anonymous classes
* e.g., strategy patterns
* functional interfaces
    * lambda expresions
    * method references

### 7/29/19 class notes

**Exceptions**

* use only for *exceptional* conditions
* a well-designed API must not force its clients to use exceptions for ordinary control flow
* three types
    * checked exceptions (can't ignore)
        * use for recoverable conditions
        * avoid unnecessary use
    * runtime exceptions
        * can possibly recover from
        * used for precondition violations and programming errors (array index out of bounds)
    * errors
        * resource deficiencies
        * don't subclass `Error`
        * don't throw any `AssertionError`
* Create state-testing methods
* Favor standard exceptions (avoid creating your own)
* Match exceptions to the level of abstraction where the error occured
* Declare all checked exceptions individually
* document precisely the conditions one is thrown
* use `@throws` for checked but not for unchecked
* in exception messages include any values, parameters, and fields that contributed to the error
* failed method should leave the object in the state it was prior to the invocation
* check *before* using parameters
* don't ignore exceptions (no empty catch blocks, you dunce!)

**reg-ex**

```python
>>> import re
>>> re.search('a', 'a')
<re.Match object; span=(0, 1), match='a'>
>>> re.search('a', 'b')
>>> re.search('.', 'b')
<re.Match object; span=(0, 1), match='b'>
>>> re.search('..', 'b')
>>> re.search('..', 'ab')
<re.Match object; span=(0, 2), match='ab'>
>>> re.search('..', 'abc')
<re.Match object; span=(0, 2), match='ab'>
>>> re.search('^.*$', 'abc')
<re.Match object; span=(0, 3), match='abc'>
>>> re.search('^.*$', '')
<re.Match object; span=(0, 0), match=''>
>>> re.search('^..*$', 'abc')
<re.Match object; span=(0, 3), match='abc'>
>>> re.search('^..+$', 'abc')
<re.Match object; span=(0, 3), match='abc'>
>>> re.search('^a.+$', 'abc')
<re.Match object; span=(0, 3), match='abc'>
>>> re.search('^a+b?$', 'aaaaaaaaaab')
<re.Match object; span=(0, 11), match='aaaaaaaaaab'>
>>> re.search('^a+?$', 'aaaaaaaaaa')
<re.Match object; span=(0, 10), match='aaaaaaaaaa'>
>>> re.search('a+?', 'aaaaaaaaaa')
<re.Match object; span=(0, 1), match='a'>
>>> re.search('a+?b', 'abcaaaa')
<re.Match object; span=(0, 2), match='ab'>
>>> re.search('a+?b?c', 'abcaaaa')
<re.Match object; span=(0, 3), match='abc'>
>>> re.search('a+?b?c', 'cccabcaabbbaa')
<re.Match object; span=(3, 6), match='abc'>
>>> re.search('a+b+c', 'cccabcaabbbaa')
<re.Match object; span=(3, 6), match='abc'>
>>> re.search('a+|b+|c', 'cccabcaabbbaa')
<re.Match object; span=(0, 1), match='c'>
>>> re.search('a+|b+|c?', 'cccabcaabbbaa')
<re.Match object; span=(0, 1), match='c'>
>>> re.search('a+?|b+?|c?', 'cccabcaabbbaa')
<re.Match object; span=(0, 1), match='c'>
>>> re.search('a+?|b+?|c+', 'cccabcaabbbaa')
<re.Match object; span=(0, 3), match='ccc'>
>>> re.search('[0-9]+', '981365awfwwa')
<re.Match object; span=(0, 6), match='981365'>
>>> re.search('[^0-9]+', '981365awfwwa')
<re.Match object; span=(6, 12), match='awfwwa'>
>>> re.search(r'(.)(.).\2\1', 'radar')
<re.Match object; span=(0, 5), match='radar'>
>>>
```
