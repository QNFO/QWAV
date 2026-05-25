---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: Everything Is Divisible
aliases:
  - Everything Is Divisible
modified: 2026-05-05T11:28:29Z
---

# Everything Is Divisible

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.20037645](http://doi.org/10.5281/zenodo.20037645)
**Date:** 2026-05-05
**Version:** 0.7

## Prologue: A Stone That Cannot Be Cut

Pick up a stone. Any stone will do—a piece of granite from a riverbed, a shard of flint from a chalk cliff, a fragment of basalt from a volcanic slope. Hold it in your palm. It feels solid. It feels whole. It feels, in a word that will occupy us for the remainder of this inquiry, *indivisible*.

Now ask a simple question: what is this stone made of?

You might begin by striking it with a hammer. The stone shatters. It is not one thing after all; it is many smaller stones. Each fragment can itself be struck and broken. If you continue, you will eventually reach grains—tiny crystals visible under a magnifying glass. Each crystal grain is a regular arrangement of atoms, just as a brick wall is a regular arrangement of bricks. The stone, it turns out, is not a single, seamless object. It is a mosaic.

Zoom in further. What is a crystal grain made of? It is made of molecules—clusters of atoms bound together by electrical forces. A grain of quartz, for example, consists of silicon dioxide molecules: one silicon atom bonded to two oxygen atoms, repeated in a three-dimensional lattice billions of times over. The “indivisible” grain turns out to be divisible into molecules.

What is a molecule made of? Atoms. The silicon dioxide molecule can be separated—with sufficient energy—into a silicon atom and two oxygen atoms. The “indivisible” molecule is divisible into atoms.

What is an atom made of? A nucleus surrounded by electrons. The nucleus contains protons and neutrons. A silicon atom, specifically, has 14 protons, 14 neutrons (in its most common form), and 14 electrons. The “indivisible” atom—the word “atom” itself comes from a root meaning “uncuttable”—is divisible into subatomic particles.

What is a proton made of? Quarks. Three quarks—two “up” quarks and one “down” quark—bound together by the strong nuclear force. The “indivisible” proton is divisible into quarks.

And what are quarks made of? Here the chain of questioning reaches a curious terminus. According to our best current understanding, quarks are elementary: they have no known substructure. But the word “elementary” carries within it a long and humbling history. Atoms were once elementary. Then protons and neutrons were elementary. Then quarks. At each stage, the supposedly fundamental, supposedly indivisible building block of matter was revealed—upon closer inspection, with more powerful instruments, under a finer conceptual resolution—to be composite. Divisible after all.

The pattern is unmistakable. Every time we have declared an entity to be indivisible, we have later discovered that it is not. The declaration “this is indivisible” has, throughout the history of inquiry, turned out to be a statement about the limits of our instruments, our concepts, or our imagination—not about the entity itself. It is a statement about us, not about the stone.

Now pivot from stones to numbers. Take the number 7. Is 7 divisible? If you try to divide 7 by 2, you get 3 with a remainder of 1. If you try to divide 7 by 3, you get 2 with a remainder of 1. If you try 7 divided by 4, 5, or 6, you always get a remainder. The only numbers that divide 7 without remainder are 1 and 7 itself. In the language we will develop shortly, 7 is *prime*. It appears to be a numerical atom—an indivisible building block of the counting numbers.

But is it really? The stone taught us a lesson: what appears indivisible at one level of analysis may be perfectly divisible at another. The question is not whether 7 is divisible or not. The question is: *in what sense, under what measuring scheme, from what perspective* are we asking?

This treatise pursues a single, unifying idea. The idea is that divisibility—and its apparent opposite, indivisibility—are not properties that objects possess in themselves. They are properties that emerge from a choice of how to look. Change the way you measure, and you change what counts as a building block. Change the building blocks, and you change what counts as prime. There is no fact of the matter about what something is “really” made of, independent of the ruler you hold against it.

What follows is a careful, step-by-step construction of this idea. We begin with the most basic concepts—counting, adding, multiplying, dividing—and we build, layer by layer, until we reach a vantage point from which the entire landscape of numbers reveals itself as a single, unified structure in which every measurement scheme has equal standing, and no entity is intrinsically indivisible.

---

# Part I: The Core Thesis

---

## 1.1 What “Divisible” Means

Before we can ask whether anything is truly indivisible, we must say precisely what we mean by “divisible.” The concept is grounded in the simplest of all mathematical activities: counting.

### The Natural Numbers

Imagine you are tallying objects—sheep in a field, coins in a purse, days until the harvest. You point to the first object and say “one.” You point to the second and say “two.” You point to the third and say “three.” And so on. The numbers that arise from this process—one, two, three, four, five, and their endless successors—are called the **natural numbers**. We denote the entire collection by the symbol **N**:

$$
\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \ldots\}
$$

(Some mathematicians include zero among the natural numbers. For our purposes, we begin at 1. The choice does not affect any of the reasoning that follows.)

### Addition and Multiplication

From counting we can build two fundamental operations.

**Addition** is the operation of combining counts. If you have a pile of 3 apples and a pile of 4 apples, and you push them together, you have a pile of 7 apples. We write:

$$
3 + 4 = 7
$$

More generally, addition tells us how many objects we have when we combine two collections. You can think of addition as counting forward on the number line: starting at 3, take 4 steps to the right, and you land on 7.

**Multiplication** is repeated addition. If you have 4 bags, and each bag contains 3 apples, then the total number of apples is 3 added to itself 4 times:

$$
3 + 3 + 3 + 3 = 12
$$

We write this more compactly as:

$$
4 \times 3 = 12
$$

We call 4 and 3 the **factors** of this multiplication, and 12 the **product**. You can also think of multiplication as arranging objects in a rectangular grid: 4 rows of 3 apples each gives a rectangle with 12 apples in total.

Multiplication is commutative: the order of the factors does not matter. Four rows of three is the same total as three rows of four:

$$
4 \times 3 = 3 \times 4 = 12
$$

### The Definition of Division

We are now ready to define division precisely.

**Definition.** Let $a$ and $b$ be natural numbers. We say that **$a$ divides $b$**, and write

$$
a \mid b,
$$

if there exists a natural number $k$ such that

$$
b = a \times k.
$$

In other words, $a$ divides $b$ exactly when $b$ can be expressed as $a$ multiplied by some whole number, with no remainder.

If $a$ divides $b$, we call $a$ a **divisor** (or **factor**) of $b$, and we call $b$ a **multiple** of $a$.

**Examples.**

- Does 3 divide 12? Yes, because $12 = 3 \times 4$. We write $3 \mid 12$.
- Does 5 divide 12? No. There is no natural number $k$ such that $5 \times k = 12$. (The closest we can get is $5 \times 2 = 10$ and $5 \times 3 = 15$.)
- Does 1 divide every natural number? Yes. For any natural number $n$, we have $n = 1 \times n$. So $1 \mid n$ always.
- Does every natural number divide itself? Yes. For any $n$, we have $n = n \times 1$. So $n \mid n$ always.

### Primes and Composites

Now we can classify natural numbers according to how many divisors they have.

**Definition.** A natural number greater than 1 is called **prime** if its only divisors are 1 and itself. In other words, a prime number cannot be written as a product of two smaller natural numbers.

**Definition.** A natural number greater than 1 that is not prime is called **composite**. A composite number can be written as a product of two smaller natural numbers.

**Definition.** The number 1 is neither prime nor composite. It stands alone as the multiplicative identity—the number that, when multiplied by any other number, leaves that number unchanged.

**Examples of primes:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...

- 2 is prime because its only divisors are 1 and 2. (There is no natural number $k$ with $1 < k < 2$.)
- 3 is prime because the only candidates for a nontrivial factor between 1 and 3 is 2, and $3 \neq 2 \times k$ for any natural $k$.
- 5 is prime: 2, 3, and 4 all fail to divide 5 evenly.
- 7 is prime: 2, 3, 4, 5, and 6 all fail to divide 7 evenly.

**Examples of composites:** 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, ...

- 4 is composite because $4 = 2 \times 2$.
- 6 is composite because $6 = 2 \times 3$.
- 12 is composite because $12 = 2 \times 6 = 3 \times 4 = 2 \times 2 \times 3$.

### The Fundamental Insight

The definition of “prime” depends entirely on the definition of “division,” which depends entirely on the operation of multiplication, which is built from addition, which is built from counting. The entire edifice rests on the most basic act of tallying.

But notice something subtle. When we ask “does 3 divide 12?” we are asking a question within a specific context: the context of the natural numbers and ordinary multiplication. What if we change the context? What if we measure division differently? Could a number that is prime in one context become composite in another?

This is the question that will animate everything that follows.

---

## 1.2 Two Ways of Measuring a Number

Consider the number 12. There are (at least) two fundamentally different questions you can ask about 12. The first is: *how big is it?* The second is: *what is it made of?*

### 1.2.1 Measuring by Size: The Absolute Value

The most familiar way to measure a number is to ask how far it is from zero. This distance is called the **absolute value**.

**Definition.** For any number $n$, the absolute value of $n$, written $\lvert n \rvert$, is defined as follows:

- If $n \geq 0$, then $\lvert n \rvert = n$.
- If $n < 0$, then $\lvert n \rvert = -n$ (which turns a negative number into the corresponding positive number).

In plain language: the absolute value strips away the sign and tells you the magnitude. Whether you owe 5 dollars or have 5 dollars, the number 5 has absolute value 5.

**Examples.**

$$
\lvert 12 \rvert = 12, \quad \lvert -12 \rvert = 12, \quad \lvert 7 \rvert = 7, \quad \lvert 0 \rvert = 0, \quad \lvert -100 \rvert = 100
$$

The absolute value satisfies a property called the **triangle inequality**.

**Triangle Inequality.** For any two numbers $a$ and $b$,

$$
\lvert a + b \rvert \leq \lvert a \rvert + \lvert b \rvert.
$$

In plain language: the distance of the sum from zero is never greater than the sum of the individual distances. If you walk 3 meters east and then 4 meters north, you end up 5 meters from your starting point. The direct distance (5) is less than the total distance walked (3 + 4 = 7). This is the geometric content of the triangle inequality: the straight path between two points is never longer than a path that goes through a third point.

The triangle inequality captures something essential about how we measure size: sizes add up. If you have two quantities, each of some size, combining them generally gives something whose size is at most the sum of the individual sizes, and often close to that sum.

### 1.2.2 Measuring by Divisibility: The p-Adic Valuation

Now consider a completely different way of measuring a number. Instead of asking “how big is it?” ask “what is it made of?” More precisely: for a chosen prime number $p$, ask “how many times does $p$ divide this number?”

Every natural number greater than 1 can be broken down into a product of primes. For example:

$$
12 = 2 \times 2 \times 3 = 2^2 \times 3^1
$$

$$
60 = 2 \times 2 \times 3 \times 5 = 2^2 \times 3^1 \times 5^1
$$

$$
1000 = 2 \times 2 \times 2 \times 5 \times 5 \times 5 = 2^3 \times 5^3
$$

This decomposition—called the **prime factorization**—is unique: every natural number can be expressed as a product of primes in exactly one way (up to the order of the factors). The number 1, by convention, has an empty prime factorization.

For a fixed prime $p$, we can ask: what is the exponent of $p$ in the prime factorization of a given number $n$? This exponent is called the **$p$-adic valuation** of $n$, written $v_p(n)$.

**Definition.** Let $p$ be a prime number, and let $n$ be a nonzero integer. The **$p$-adic valuation** of $n$, written $v_p(n)$, is the exponent of $p$ in the prime factorization of $n$. That is:

$$
v_p(n) = \text{the largest integer } e \geq 0 \text{ such that } p^e \text{ divides } n.
$$

If $p$ does not divide $n$ at all, then $v_p(n) = 0$.

**Examples for $n = 12$:**

- The prime factorization of 12 is $2^2 \times 3^1$. No other primes appear.
- $v_2(12) = 2$, because $2^2 = 4$ divides 12, but $2^3 = 8$ does not divide 12 evenly (12 ÷ 8 = 1.5, not a whole number).
- $v_3(12) = 1$, because 3 divides 12 once ($12 = 3 \times 4$), but 9 does not divide 12.
- $v_5(12) = 0$, because 5 does not divide 12 at all.
- $v_7(12) = 0$, because 7 does not divide 12 at all.

**More examples:**

- For $n = 60 = 2^2 \times 3 \times 5$:
  - $v_2(60) = 2$
  - $v_3(60) = 1$
  - $v_5(60) = 1$
  - $v_7(60) = 0$

- For $n = 7$ (a prime itself):
  - $v_2(7) = 0$
  - $v_3(7) = 0$
  - $v_5(7) = 0$
  - $v_7(7) = 1$

- For $n = 1$: every $v_p(1) = 0$ for all primes $p$, because 1 has no prime factors.

### 1.2.3 From Valuation to Size: The p-Adic Absolute Value

The valuation $v_p(n)$ tells us how divisible $n$ is by $p$. But we might want a measurement that behaves more like the ordinary absolute value—a measurement of “size,” but where being highly divisible by $p$ corresponds to being *small*. This is the **$p$-adic absolute value**.

**Definition.** Let $p$ be a prime number. For any nonzero number $n$, define the **$p$-adic absolute value** of $n$, written $\lvert n \rvert_p$, as:

$$
\lvert n \rvert_p = p^{-v_p(n)}
$$

For $n = 0$, we define $\lvert 0 \rvert_p = 0$.

In words: take the prime $p$, raise it to the power of *minus* the valuation, and that number is the $p$-adic size. The more times $p$ divides $n$, the larger $v_p(n)$ becomes, and the smaller $p^{-v_p(n)}$ becomes. A number that is highly divisible by $p$ is—in the $p$-adic sense—very small.

**Examples.**

For $n = 12$:

- $\lvert 12 \rvert_2 = 2^{-2} = \frac{1}{4} = 0.25$
- $\lvert 12 \rvert_3 = 3^{-1} = \frac{1}{3} \approx 0.333\ldots$
- $\lvert 12 \rvert_5 = 5^{-0} = 1$
- $\lvert 12 \rvert_7 = 7^{-0} = 1$
- $\lvert 12 \rvert_{11} = 11^{-0} = 1$

For $n = 60$:

- $\lvert 60 \rvert_2 = 2^{-2} = \frac{1}{4}$
- $\lvert 60 \rvert_3 = 3^{-1} = \frac{1}{3}$
- $\lvert 60 \rvert_5 = 5^{-1} = \frac{1}{5}$
- $\lvert 60 \rvert_7 = 7^{-0} = 1$

For $n = 7$:

- $\lvert 7 \rvert_2 = 2^{-0} = 1$
- $\lvert 7 \rvert_7 = 7^{-1} = \frac{1}{7}$

For $n = 1$: $\lvert 1 \rvert_p = p^{-0} = 1$ for every prime $p$.

**Interpreting the p-adic size.** In ordinary terms, 12 is “bigger” than 7 (since $\lvert 12 \rvert = 12 > 7 = \lvert 7 \rvert$). But in the 2-adic sense, 12 is “smaller” than 7, because $\lvert 12 \rvert_2 = \frac{1}{4} < 1 = \lvert 7 \rvert_2$. The number 12 is highly divisible by 2; the number 7 is not divisible by 2 at all. The p-adic metric reverses our intuition: divisibility *shrinks* a number.

### 1.2.4 The Ultrametric Inequality

The p-adic absolute value satisfies a remarkable property that is stronger than the ordinary triangle inequality.

**Ultrametric (Strong Triangle) Inequality.** For any numbers $a$ and $b$,

$$
\lvert a + b \rvert_p \leq \max(\lvert a \rvert_p, \; \lvert b \rvert_p).
$$

In plain language: the p-adic size of a sum is never larger than the *larger* of the individual p-adic sizes. Unlike ordinary sizes, which can add up to produce something bigger than either term, p-adic sizes do not accumulate.

**Example.** Consider $a = 4$ and $b = 12$.

- $\lvert 4 \rvert_2 = 2^{-2} = \frac{1}{4}$ (because $4 = 2^2$)
- $\lvert 12 \rvert_2 = 2^{-2} = \frac{1}{4}$ (because $12 = 2^2 \times 3$)
- $\lvert 4 + 12 \rvert_2 = \lvert 16 \rvert_2 = 2^{-4} = \frac{1}{16}$ (because $16 = 2^4$)

Now check the ordinary triangle inequality:
$$
\lvert 4 + 12 \rvert = \lvert 16 \rvert = 16 \leq \lvert 4 \rvert + \lvert 12 \rvert = 4 + 12 = 16 \quad \checkmark
$$

And check the ultrametric inequality:
$$
\lvert 4 + 12 \rvert_2 = \frac{1}{16} \leq \max\left(\frac{1}{4}, \frac{1}{4}\right) = \frac{1}{4} \quad \checkmark
$$

Indeed, $\frac{1}{16}$ is much smaller than $\frac{1}{4}$. The sum is *smaller* than either term—a situation that never occurs with ordinary absolute values (except when terms cancel, which is a different phenomenon). In the p-adic world, two numbers that are both divisible by $p$ can combine to produce a number that is *even more* divisible by $p$. The divisibility deepens.

**Contrast with ordinary addition.** If you add two ordinary numbers, each of size about 100, you get a number of size about 200. The sizes approximately add. But if you add two numbers that are both highly divisible by 2 (say, each divisible by $2^2 = 4$), their sum is divisible by at least $2^2$ as well, and possibly by a higher power of 2. The “2-divisibility” of the sum is at least the minimum of the “2-divisibilities” of the terms, not their sum.

In plain language: in the ordinary world, two raindrops combine to make a bigger puddle. In the p-adic world, two numbers that are “small” (highly divisible by $p$) combine to make something that is also “small”—it never becomes “large.” This is a profoundly different geometry.

### 1.2.5 Two Worlds, One Number

We now have two distinct measurement schemes for a single number:

| Measurement Scheme | What It Measures | Example: $\lvert 12 \rvert$ |
|---|---|---|
| Ordinary absolute value $\lvert \cdot \rvert$ | Distance from zero | $\lvert 12 \rvert = 12$ |
| 2-adic absolute value $\lvert \cdot \rvert_2$ | Divisibility by 2 | $\lvert 12 \rvert_2 = \frac{1}{4}$ |
| 3-adic absolute value $\lvert \cdot \rvert_3$ | Divisibility by 3 | $\lvert 12 \rvert_3 = \frac{1}{3}$ |
| 5-adic absolute value $\lvert \cdot \rvert_5$ | Divisibility by 5 | $\lvert 12 \rvert_5 = 1$ |

The same number, 12, has four different “sizes,” depending on which ruler we use. None of these sizes is more “real” than the others. They are answers to different questions. The ordinary size answers “how many?” The 2-adic size answers “how even?” The 3-adic size answers “how divisible by three?” Each measurement reveals a different aspect of the number, and no single measurement captures the whole.

---

## 1.3 The Thesis Stated

We have now developed enough machinery to state the central claim of this treatise clearly.

**Thesis.** No entity—no number, no object, no building block of any kind—is intrinsically indivisible. What we call “indivisible” is always and only *indivisible relative to a chosen measurement context.* Change the context, and the indivisible becomes divisible. The distinction between what a thing is (its being, its ontic character) and how we measure it (our knowledge of it, our epistemic access) collapses. There is no fact of the matter about what something is “really” made of, independent of the ruler you choose to hold against it.

Let us unpack this thesis in three layers.

**First layer: the empirical argument from the Prologue.** The history of physics is a history of discovering that what was previously thought indivisible is in fact divisible. The solid stone divides into grains, the grains into molecules, the molecules into atoms, the atoms into protons and electrons, the protons into quarks. At no point in this chain do we find a bottom—a truly fundamental, truly indivisible entity. We find only successive layers, each of which serves as a provisional “bottom” until we develop finer instruments. The pattern suggests, though it does not prove, that the notion of an intrinsic, context-independent indivisible entity is incoherent.

**Second layer: the mathematical argument from measurement schemes.** The number 7 is prime—indivisible—in the ordinary arithmetic of the natural numbers with ordinary multiplication. But as we have just seen in Section 1.2, “prime” is a notion defined entirely in terms of the division relation, and the division relation is defined in terms of ordinary multiplication. If we change the way we measure—if we adopt, say, the 7-adic metric—then the number 7 acquires the size $\frac{1}{7}$, making it “small” and deeply divisible by 7 in that measurement context. The same number appears prime under one ruler and highly divisible under another. “Prime” is not a property of 7; it is a property of how 7 behaves relative to ordinary multiplication. Change the notion of multiplication—change the metric—and primality evaporates.

**Third layer: the collapse of ontic/epistemic.** We are accustomed to thinking that objects have properties independently of our observations. A stone has a certain mass whether we measure it or not. But the lesson of the p-adic metrics is more radical. There is no “true” size of the number 12. There is an ordinary size (12), a 2-adic size ($\frac{1}{4}$), a 3-adic size ($\frac{1}{3}$), and infinitely many others. Which one is “real”? They all are, and none is privileged. The number does not *have* a size; it *is given* a size by a choice of measurement. The measurement does not reveal a pre-existing property; it constitutes the property within a framework of inquiry.

This collapse of the distinction between what something is and how we measure it is the deepest implication of the thesis. It is not that we are ignorant of the true size and must approximate it with various metrics. It is that “size” has no meaning apart from a metric, and there are many equally valid metrics. The entity itself is not “really” one thing or another; it participates in all measurement contexts simultaneously, revealing different aspects depending on which question we ask.

---

# Part II: Number-Theoretic Foundations

---

## 2.1 Primality Depends on the Metric

In Section 1.1, we defined a prime number as a natural number greater than 1 whose only divisors are 1 and itself. This definition appears absolute. It seems to pick out a fixed set of numbers—{2, 3, 5, 7, 11, 13, ...}—that are prime regardless of perspective. But the definition depends on a hidden assumption: that “division” means ordinary division in the natural numbers, which is equivalent to asking whether a number can be expressed as a product of *smaller natural numbers* under ordinary multiplication.

When we change the measurement context—when we shift from the ordinary absolute value to a p-adic absolute value—the whole notion of “divisor” and “prime” transforms. Let us see how.

### 2.1.1 The Ordinary Perspective

Under the ordinary absolute value metric, the number 3 is prime. Its only positive divisors are 1 and 3. There is no natural number $k$, with $1 < k < 3$, such that $3 = k \times m$ for some natural $m$. The number 3 is a numerical atom—an indivisible building block from which, together with other primes, all natural numbers can be constructed.

The number 12, by contrast, is composite: $12 = 2 \times 6 = 3 \times 4 = 2^2 \times 3$. Its ordinary size is $\lvert 12 \rvert = 12$.

### 2.1.2 The 3-Adic Perspective

Now adopt the 3-adic metric. Measure everything by how divisible it is by 3.

Under this metric:

- $\lvert 3 \rvert_3 = 3^{-1} = \frac{1}{3}$
- $\lvert 12 \rvert_3 = 3^{-1} = \frac{1}{3}$ (because $12 = 2^2 \times 3$, and $v_3(12) = 1$)

Remarkably, 3 and 12 have the *same* 3-adic size. In this measurement context, 3 is not a mysterious indivisible atom; it is just a number that is divisible by 3 exactly once—exactly like 12, 6, 15, 21, and infinitely many others. The special status of 3 as “prime” evaporates. What matters in the 3-adic world is not whether a number can be factored into smaller natural numbers, but *how many factors of 3 it contains.*

We can push this further. Consider the number 9:

- $\lvert 9 \rvert_3 = 3^{-2} = \frac{1}{9}$

The number 9 is “smaller” in the 3-adic sense than either 3 or 12. It is *more* divisible by 3. In the 3-adic world, 9 is a kind of “subatomic” version of 3—a number that embodies the essence of “three-ness” even more intensely than 3 itself. The number 27 ($\lvert 27 \rvert_3 = \frac{1}{27}$) is even smaller. The number 81 ($\frac{1}{81}$) is smaller still. There is no lower bound: by taking higher and higher powers of 3, we can produce numbers that are arbitrarily small in the 3-adic sense. The “indivisible” atom has become infinitely divisible—it contains within itself an endless hierarchy of ever-smaller entities, each a purer distillation of divisibility-by-3.

### 2.1.3 The 2-Adic Perspective on 3

Now shift to the 2-adic metric. What happens to 3?

- $\lvert 3 \rvert_2 = 2^{-0} = 1$

Because 3 contains no factor of 2, its 2-adic size is exactly 1. In the 2-adic world, 3 is not small; it is not large; it is of unit size—it is what we call a **$p$-adic unit**. A number with $\lvert n \rvert_p = 1$ is, from the perspective of the p-adic metric, invisible in its divisibility structure. It neither shrinks nor grows; it passes through the 2-adic lens unchanged. In this sense, 3 is to the 2-adic metric what the number 1 is to the ordinary metric: a neutral, structureless entity that contributes nothing to the measurement.

### 2.1.4 A Table of Perspectives

To make the relativity of primality vivid, consider the number 12 as seen through several different metrics:

| Metric | Value for 12 | Interpretation |
|---|---|---|
| Ordinary $\lvert \cdot \rvert_\infty$ | 12 | 12 is large; it is 12 units from zero. |
| 2-adic $\lvert \cdot \rvert_2$ | $\frac{1}{4}$ | 12 is small; it is highly divisible by 2. |
| 3-adic $\lvert \cdot \rvert_3$ | $\frac{1}{3}$ | 12 is moderately small; it is divisible by 3 once. |
| 5-adic $\lvert \cdot \rvert_5$ | 1 | 12 is neutral; 5 does not divide 12, so the 5-adic metric sees nothing special. |
| 7-adic $\lvert \cdot \rvert_7$ | 1 | Likewise neutral. |
| 11-adic $\lvert \cdot \rvert_{11}$ | 1 | Neutral. |

And the same for the prime number 7:

| Metric | Value for 7 | Interpretation |
|---|---|---|
| Ordinary $\lvert \cdot \rvert_\infty$ | 7 | 7 is prime and of moderate size. |
| 2-adic $\lvert \cdot \rvert_2$ | 1 | Neutral—7 is a unit, invisible to the 2-adic metric. |
| 3-adic $\lvert \cdot \rvert_3$ | 1 | Neutral. |
| 5-adic $\lvert \cdot \rvert_5$ | 1 | Neutral. |
| 7-adic $\lvert \cdot \rvert_7$ | $\frac{1}{7}$ | Ah! Now 7 is small. In the 7-adic metric, 7 is highly divisible by 7—indeed, it is the *first* number in an infinite descending chain of ever-smaller powers: 7, 49, 343, ... |

The lesson is inescapable. Every number is prime from some perspectives and composite (or at least “divisible”) from others. Even the most paradigmatic prime—say, 2—is not prime in any absolute sense. In the ordinary metric, 2 is prime. In the 2-adic metric, 2 has size $\frac{1}{2}$; it is the gateway to an infinite hierarchy of divisibility. In the 3-adic metric, 2 has size 1; it is invisible. Primality is not a property of a number. It is a property of a number *as seen through a particular metric.*

---

## 2.2 Rational Numbers and Negative Exponents

So far, we have considered only the natural numbers and, in discussing absolute value, the integers (which include negative numbers). But the world of numbers is larger. We now extend our analysis to **rational numbers**.

### 2.2.1 What Is a Rational Number?

A **rational number** is any number that can be expressed as a fraction:

$$
\frac{a}{b}
$$

where $a$ and $b$ are integers and $b \neq 0$. The number $a$ is called the **numerator**; the number $b$ is called the **denominator**.

Every integer is a rational number (just set $b = 1$). For example, $5 = \frac{5}{1}$. Every natural number is an integer, so every natural number is also a rational number. The rational numbers extend the integers by including all possible ratios of integers.

We denote the set of all rational numbers by $\mathbb{Q}$.

**Examples of rational numbers:** $\frac{1}{2}$, $\frac{3}{4}$, $-\frac{7}{3}$, $\frac{22}{7}$, $0 = \frac{0}{1}$, $100 = \frac{100}{1}$.

### 2.2.2 Extending the p-Adic Valuation

How should we measure the divisibility-by-$p$ of a rational number like $\frac{1}{2}$? The idea is natural: the $p$-adic valuation of a fraction should be the valuation of the numerator minus the valuation of the denominator.

**Definition.** Let $x = \frac{a}{b}$ be a rational number, with $a, b$ integers and $b \neq 0$. The **$p$-adic valuation** of $x$ is:

$$
v_p(x) = v_p(a) - v_p(b)
$$

where the valuations on the right-hand side are the ordinary valuations for integers defined in Section 1.2.2.

This definition is well-posed: it does not depend on the particular representation of $x$ as a fraction. If $\frac{a}{b} = \frac{c}{d}$ (that is, if the two fractions represent the same rational number), then $v_p(a) - v_p(b) = v_p(c) - v_p(d)$. The valuation genuinely measures a property of the rational number itself, not of the particular way we choose to write it.

The **$p$-adic absolute value** extends in the same way:

$$
\lvert x \rvert_p = p^{-v_p(x)} \quad \text{for } x \neq 0, \qquad \lvert 0 \rvert_p = 0.
$$

### 2.2.3 Examples

**Example 1: $\frac{1}{2}$.**

- The numerator is 1, which has $v_2(1) = 0$.
- The denominator is 2, which has $v_2(2) = 1$.
- Therefore, $v_2\left(\frac{1}{2}\right) = 0 - 1 = -1$.
- And $\lvert \frac{1}{2} \rvert_2 = 2^{-(-1)} = 2^1 = 2$.

In the 2-adic metric, $\frac{1}{2}$ has size 2. It is “large” because its denominator contains a factor of 2 that the numerator cannot cancel. A negative valuation means the number is “blown up” by the p-adic metric—the more factors of $p$ in the denominator, the larger the p-adic size.

Contrast this with the ordinary absolute value: $\lvert \frac{1}{2} \rvert = \frac{1}{2}$. In the ordinary world, $\frac{1}{2}$ is small (less than 1). In the 2-adic world, it is large (greater than 1). The same number, two radically different sizes.

**Example 2: $\frac{12}{5}$.**

- $12 = 2^2 \times 3$. So $v_2(12) = 2$, $v_3(12) = 1$, and $v_5(12) = 0$.
- $5 = 5^1$. So $v_2(5) = 0$, $v_3(5) = 0$, $v_5(5) = 1$.
- Therefore:
  - $v_2\left(\frac{12}{5}\right) = 2 - 0 = 2$, so $\lvert \frac{12}{5} \rvert_2 = 2^{-2} = \frac{1}{4}$.
  - $v_3\left(\frac{12}{5}\right) = 1 - 0 = 1$, so $\lvert \frac{12}{5} \rvert_3 = 3^{-1} = \frac{1}{3}$.
  - $v_5\left(\frac{12}{5}\right) = 0 - 1 = -1$, so $\lvert \frac{12}{5} \rvert_5 = 5^{-(-1)} = 5$.

The number $\frac{12}{5}$ is simultaneously small in the 2-adic sense ($\frac{1}{4}$), small in the 3-adic sense ($\frac{1}{3}$), and large in the 5-adic sense (5). In the ordinary sense, it is $\lvert \frac{12}{5} \rvert = \frac{12}{5} = 2.4$.

**Example 3: $\frac{2}{3}$.**

- $v_2(2) = 1$, $v_2(3) = 0$ → $v_2\left(\frac{2}{3}\right) = 1$, so $\lvert \frac{2}{3} \rvert_2 = \frac{1}{2}$.
- $v_3(2) = 0$, $v_3(3) = 1$ → $v_3\left(\frac{2}{3}\right) = -1$, so $\lvert \frac{2}{3} \rvert_3 = 3$.
- For all other primes $p$, $v_p(\frac{2}{3}) = 0$, so $\lvert \frac{2}{3} \rvert_p = 1$.

### 2.2.4 The Simultaneous Multiplicity of Sizes

The examples above illustrate a fundamental fact: a rational number can be simultaneously large in one metric and small in another. There is no contradiction because the metrics measure different things. The 2-adic metric measures divisibility by 2; the 3-adic metric measures divisibility by 3. A number can be highly divisible by 2 and not at all by 3, producing a small 2-adic size and a large 3-adic size simultaneously.

This is not a curiosity. It is the key to understanding the deep structure of numbers. A number does not have *a* size. It has a *profile* of sizes—one for each prime, plus the ordinary size at infinity. The complete description of a number is not a single magnitude but a collection of magnitudes, one for each possible question you can ask about it.

---

## 2.3 The Product Formula: All Metrics Together

If a number has many sizes—one ordinary size and one for each prime—how do these sizes relate to one another? Do they vary independently, or is there a constraint that ties them all together?

The answer is one of the most beautiful identities in all of mathematics. It is called the **adelic product formula**, and it states that the sizes of a rational number, across all possible metrics, multiply together to exactly 1.

### 2.3.1 Statement of the Product Formula

**Product Formula.** Let $x$ be any nonzero rational number. Let $\lvert x \rvert_\infty$ denote the ordinary absolute value (the “size at infinity”). For each prime $p$, let $\lvert x \rvert_p$ denote the $p$-adic absolute value. Then:

$$
\lvert x \rvert_\infty \times \lvert x \rvert_2 \times \lvert x \rvert_3 \times \lvert x \rvert_5 \times \lvert x \rvert_7 \times \lvert x \rvert_{11} \times \cdots = 1
$$

where the product runs over all primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on, without end.

This is an infinite product. For all but finitely many primes $p$, $\lvert x \rvert_p = 1$ (because only finitely many primes can appear in the numerator or denominator of a given rational number). So the infinite product is effectively a finite product—all but finitely many factors are 1, and multiplying by 1 does nothing.

### 2.3.2 Verification for $x = 12$

Let us verify the formula for $x = 12$.

- **Ordinary size:** $\lvert 12 \rvert_\infty = 12$.

- **Prime-by-prime:**
  - $12 = 2^2 \times 3$. The primes 2 and 3 appear; all others do not.
  - $\lvert 12 \rvert_2 = 2^{-2} = \frac{1}{4}$
  - $\lvert 12 \rvert_3 = 3^{-1} = \frac{1}{3}$
  - $\lvert 12 \rvert_5 = 5^{-0} = 1$
  - $\lvert 12 \rvert_7 = 1$
  - $\lvert 12 \rvert_{11} = 1$
  - ... and so on for all other primes: all 1.

- **Product:**
  $$
  12 \times \frac{1}{4} \times \frac{1}{3} \times 1 \times 1 \times 1 \times \cdots = 12 \times \frac{1}{12} = 1
  $$

  The product is exactly 1. ✓

### 2.3.3 Verification for $x = \frac{1}{2}$

- **Ordinary size:** $\lvert \frac{1}{2} \rvert_\infty = \frac{1}{2}$.

- **Prime-by-prime:**
  - $\frac{1}{2}$ has a factor of 2 in the denominator.
  - $\lvert \frac{1}{2} \rvert_2 = 2$
  - For all other primes $p$, $\lvert \frac{1}{2} \rvert_p = 1$.

- **Product:**
  $$
  \frac{1}{2} \times 2 \times 1 \times 1 \times \cdots = 1
  $$

  ✓

### 2.3.4 Verification for $x = \frac{12}{5}$

- **Ordinary size:** $\lvert \frac{12}{5} \rvert_\infty = \frac{12}{5}$.

- **Prime-by-prime (as computed in Section 2.2.3):**
  - $\lvert \frac{12}{5} \rvert_2 = \frac{1}{4}$
  - $\lvert \frac{12}{5} \rvert_3 = \frac{1}{3}$
  - $\lvert \frac{12}{5} \rvert_5 = 5$
  - All other primes: 1.

- **Product:**
  $$
  \frac{12}{5} \times \frac{1}{4} \times \frac{1}{3} \times 5 = \frac{12 \times 5}{5 \times 4 \times 3} = \frac{60}{60} = 1
  $$

  ✓

### 2.3.5 Why the Formula Works

The product formula is not magic. It follows directly from the unique prime factorization of integers. Let us sketch the reasoning for a general rational number $x = \frac{a}{b}$ (with $a, b$ positive for simplicity; negative numbers work similarly because absolute values ignore signs).

Write the prime factorization of $a$ and $b$:

$$
a = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}, \qquad b = q_1^{f_1} q_2^{f_2} \cdots q_m^{f_m}
$$

where the $p_i$ and $q_j$ are primes, and the $e_i, f_j$ are positive integers. Some primes may appear in both $a$ and $b$; we can combine them. Ultimately, every rational number can be written uniquely (up to sign) as:

$$
x = \prod_{p \text{ prime}} p^{\,n_p}
$$

where $n_p$ is an integer (positive, negative, or zero) called the **exponent** of $p$ in $x$. Only finitely many $n_p$ are nonzero.

Then:

- The ordinary size is $\lvert x \rvert_\infty = \prod_{p} p^{\,n_p}$ (with the understanding that a negative exponent $n_p$ moves that prime factor to the denominator).
- The $p$-adic size is $\lvert x \rvert_p = p^{-n_p}$.

Therefore, the product over all metrics is:

$$
\lvert x \rvert_\infty \times \prod_{p} \lvert x \rvert_p = \left(\prod_{p} p^{\,n_p}\right) \times \left(\prod_{p} p^{-n_p}\right) = \prod_{p} p^{\,n_p - n_p} = \prod_{p} p^0 = 1
$$

Each prime’s contribution to the ordinary size is exactly cancelled by its contribution to the corresponding p-adic size. The product formula is an identity—a tautology, in the best sense: it reveals that the various sizes of a number are not independent; they are locked together in a perfect, universal balance.

### 2.3.6 The Deep Implication: No Metric Is Privileged

The product formula teaches us a profound lesson. A number can be large in some metrics, but only if it is correspondingly small in others, so that the total product is exactly 1. If a number is huge in the ordinary sense—say, $1,000,000$—then it must have substantial prime factors. Those prime factors reduce its size in the corresponding p-adic metrics, keeping the overall balance.

**Example.** $x = 1,000,000 = 10^6 = 2^6 \times 5^6$.

- $\lvert x \rvert_\infty = 1,000,000$—enormous.
- $\lvert x \rvert_2 = 2^{-6} = \frac{1}{64}$—tiny.
- $\lvert x \rvert_5 = 5^{-6} = \frac{1}{15,625}$—extremely tiny.
- All other $\lvert x \rvert_p = 1$.
- Product: $1,000,000 \times \frac{1}{64} \times \frac{1}{15,625} = \frac{1,000,000}{1,000,000} = 1$. ✓

The ordinary enormity of one million is exactly compensated by its extreme 2-adic and 5-adic smallness. No single metric tells the whole story. If you only look at the ordinary size, you see a giant. If you only look at the 5-adic size, you see an infinitesimal speck. Neither perspective is more correct. They are complementary, and together they form a complete, balanced description.

This is the mathematical counterpart of the central thesis. Just as no physical scale of analysis (grains, molecules, atoms, quarks) is privileged—each reveals a different level of structure—no numerical metric is privileged. The object itself does not have “a” size. It has a family of sizes, constrained by a global identity. What the object “is” depends on which member of the family you choose to look at.

---

## 2.4 There Is No Bottom: Rational Numbers Have No Building Blocks

We have seen that primality—the apparent atomicity of certain numbers—dissolves when we change the metric. But perhaps there is a deeper sense in which numbers have building blocks. Even if 3 is not intrinsically prime, perhaps the rational numbers as a whole can be built up from some set of fundamental, indivisible elements—“rational atoms”—just as molecules are built from atoms (or so we thought before we discovered subatomic particles).

This section shows that no such atoms exist for the rational numbers. The rational numbers are fundamentally *bottomless*: you can always divide further, decompose further, find structure within structure. There is no level at which you hit an indivisible foundation.

### 2.4.1 What Would Count as a “Basis”?

To ask whether the rational numbers have building blocks, we first need to say precisely what we mean by “building blocks.” We need a definition of a **basis**.

**Definition.** Let $S$ be a collection of mathematical objects. Let $B$ be a subset of $S$. We say that $B$ is a **basis** for $S$ (over the integers) if every element of $S$ can be expressed *uniquely* as a finite combination of elements of $B$, where the coefficients in the combination are integers.

The word “uniquely” is crucial. If a basis exists, then every element of $S$ has exactly one representation in terms of the basis elements, just as every molecule has a unique chemical formula in terms of atoms. The basis elements are the “atoms”—the primitive, indivisible constituents from which everything else is built.

**Example: The integers have a basis.** The set $B = \{1\}$ is a basis for the integers $\mathbb{Z}$ over $\mathbb{Z}$. Every integer $n$ can be written uniquely as $n = n \times 1$, with coefficient $n$ (an integer). There is exactly one basis element, and it generates everything. The integer 1 is the “atom” of the integers.

**Another example: Pairs of integers.** The set $B = \{(1,0), (0,1)\}$ is a basis for the collection of all pairs of integers ($\mathbb{Z} \times \mathbb{Z}$). Any pair $(a, b)$ can be written uniquely as $a \times (1,0) + b \times (0,1)$. No other representation exists.

### 2.4.2 The Rational Numbers Have No Basis

**Claim.** The rational numbers $\mathbb{Q}$ have no basis over the integers $\mathbb{Z}$.

**Reasoning.** Suppose, for the sake of argument, that a basis $B$ exists. Let $b$ be any element of this basis. Since $b$ is a rational number, we can write $b = \frac{p}{q}$ for some integers $p, q$ with $q \neq 0$.

Now consider the rational number $\frac{b}{2}$. This is also a rational number. By the definition of a basis, $\frac{b}{2}$ must be expressible as a unique integer combination of basis elements:

$$
\frac{b}{2} = c_1 b_1 + c_2 b_2 + \cdots + c_k b_k
$$

for some basis elements $b_1, \ldots, b_k \in B$ and integers $c_1, \ldots, c_k$.

But also, we can multiply both sides of this equation by 2:

$$
b = 2c_1 b_1 + 2c_2 b_2 + \cdots + 2c_k b_k
$$

This expresses the basis element $b$ as an integer combination of other basis elements. But we also have the trivial representation $b = 1 \times b$. So $b$ now has *two different* representations as an integer combination of basis elements: one using the coefficient 1 on $b$ itself, and one using coefficients $2c_i$ on other basis elements. This violates uniqueness.

The only way to avoid this contradiction would be if $b$ could not be divided by 2—that is, if $\frac{b}{2}$ were not a rational number, or if $b$ were somehow indivisible by 2. But every rational number can be divided by 2 to produce another rational number. This is a fundamental property of $\mathbb{Q}$.

### 2.4.3 Divisibility: The Property That Destroys Atoms

The property that prevents the rational numbers from having a basis is called **divisibility**.

**Definition.** A collection of mathematical objects $M$ (with an operation of multiplication by integers) is called **divisible** if, for every element $m \in M$ and every nonzero integer $n$, there exists an element $x \in M$ such that $n \times x = m$.

In plain language: you can always “divide” any element by any nonzero integer and stay within the collection. The element $x = \frac{m}{n}$ is the result of this division.

The rational numbers $\mathbb{Q}$ are divisible: for any rational $q$ and any nonzero integer $n$, the number $\frac{q}{n}$ is also rational. The integers $\mathbb{Z}$ are *not* divisible: you cannot divide 3 by 2 and get an integer. Divisibility is precisely what distinguishes $\mathbb{Q}$ from $\mathbb{Z}$.

And divisibility is precisely what makes a basis impossible. If a collection is divisible, you can always “split” any candidate basis element further, producing ambiguity in representation. There are no atoms in a divisible structure—no elements that cannot be further decomposed.

### 2.4.4 Concrete Illustration: Trying to Build from “Atoms”

Let us try, concretely, to construct a basis for the rational numbers, to see why the attempt fails.

We need a set $B$ of rational numbers such that every rational number can be written uniquely as an integer combination of elements of $B$.

**Attempt 1.** Let $B = \{1\}$. Can every rational number be written as $n \times 1$ for some integer $n$? No. The number $\frac{1}{2}$ cannot be so expressed. $B$ fails to generate everything.

**Attempt 2.** Add $\frac{1}{2}$ to the basis: $B = \{1, \frac{1}{2}\}$. Now we can express $\frac{1}{2} = 1 \times \frac{1}{2}$. But can we express $\frac{1}{3}$? No. We need to add $\frac{1}{3}$. And $\frac{1}{4}$? We could write $\frac{1}{4} = \frac{1}{2} \times \frac{1}{2}$, but that is multiplication, not integer combination. Integer combinations only allow adding and subtracting, not multiplying basis elements together. So we need $\frac{1}{4}$ as a separate basis element. But then $\frac{1}{4} = 2 \times \frac{1}{8}$, so we need $\frac{1}{8}$. And then $\frac{1}{16}$, and so on.

**Attempt 3.** Perhaps we can take all fractions of the form $\frac{1}{p^k}$ for all primes $p$ and all positive integers $k$. Then $B = \{\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \ldots, \frac{1}{3}, \frac{1}{9}, \frac{1}{27}, \ldots, \frac{1}{5}, \frac{1}{25}, \ldots\}$. This is an infinite set. Can every rational number be expressed as an integer combination of these? Consider $\frac{1}{6}$. Is $\frac{1}{6}$ an integer combination of $\frac{1}{2}$ and $\frac{1}{3}$? We need integers $a, b$ such that $\frac{1}{6} = a \times \frac{1}{2} + b \times \frac{1}{3}$. This gives $\frac{1}{6} = \frac{3a + 2b}{6}$, so $3a + 2b = 1$. One solution is $a = 1, b = -1$: indeed, $\frac{1}{2} - \frac{1}{3} = \frac{3 - 2}{6} = \frac{1}{6}$. But is this representation unique? Consider also $\frac{1}{6} = -\frac{1}{2} \times \frac{1}{2} + \frac{1}{2} \times \frac{1}{3} + \cdots$—there are many possible combinations because we can add and subtract multiples that cancel out. Uniqueness fails.

In fact, no finite or even infinite set can serve as a basis. The rational numbers are *infinitely divisible*: for any rational $q$ and any integer $n$, there is a rational $r$ with $n \times r = q$. This infinite divisibility makes unique decomposition impossible. There is always a finer grain, a smaller piece, a deeper level of division.

### 2.4.5 The Bottomless Nature of Rationality

The rational numbers thus embody, in pure form, the thesis of this treatise. Not only are individual numbers not intrinsically indivisible, but the entire system of rational numbers has *no* indivisible building blocks. There is no bottom. There is no set of “rational atoms” from which everything else is uniquely constructed. Any candidate building block can be divided further, and any representation in terms of a proposed basis can be altered by splitting the basis elements more finely.

This is not a defect of the rational numbers. It is their essential nature. They are a *field*—a number system in which you can add, subtract, multiply, and divide (by anything except zero). Fields are the natural habitat of division. And in a field, the very idea of an indivisible atom is foreign. Everything flows; everything divides.

---

## 2.5 Beyond Primes: Transcendental Decompositions

We have seen that the notion of what a number is “made of” depends on the metric. The ordinary metric decomposes numbers into prime factors; the p-adic metrics decompose numbers by their divisibility by a single prime. But the relativity of decomposition goes deeper still. We can change not just the metric but the entire *representational base*—the set of building blocks we use to express numbers. When we do so, even the most familiar numbers can acquire surprising decompositions.

### 2.5.1 Representing Numbers in a Base

Most of us are accustomed to writing numbers in **base 10** (decimal). In base 10, the number $3742$ is shorthand for:

$$
3742 = 3 \times 10^3 + 7 \times 10^2 + 4 \times 10^1 + 2 \times 10^0
$$

The “building blocks” of this representation are the powers of 10: $10^0 = 1, 10^1 = 10, 10^2 = 100, 10^3 = 1000$, and so on. Any whole number can be expressed as a sum of these building blocks, with coefficients taken from the set $\{0, 1, 2, \ldots, 9\}$.

But we can equally well use **base 2** (binary). In base 2, the number $12$ is:

$$
12 = 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 0 \times 2^0
$$

written as $1100$ in binary notation. The building blocks are powers of 2: $1, 2, 4, 8, 16, \ldots$, and the coefficients are only 0 or 1.

Or **base 3**: $12 = 1 \times 3^2 + 1 \times 3^1 + 0 \times 3^0 = 110_3$.

Or any base $b$ (with $b \geq 2$): every natural number can be expressed uniquely as a sum of powers of $b$ with coefficients in $\{0, 1, \ldots, b-1\}$. The choice of base is a choice of building blocks. And the same number looks different—has a different “anatomy”—depending on which base you choose.

### 2.5.2 What If the Base Is Not an Integer?

The bases we have considered so far—2, 3, 10—are all integers greater than 1. What happens if we choose a base that is not an integer? What if we try to write numbers using powers of $\pi$ (approximately 3.14159...)?

The number $\pi$ is special. It is **transcendental**, which means it is not the root of any polynomial equation with integer coefficients. (By contrast, $\sqrt{2}$ is *not* transcendental, because it satisfies the equation $x^2 - 2 = 0$, whose coefficients 1, 0, and -2 are integers. The number $\sqrt{2}$ is called **algebraic**.)

Because $\pi$ is transcendental, the powers of $\pi$—that is, $\pi^0 = 1, \pi^1 = \pi, \pi^2, \pi^3, \ldots$—satisfy no linear relation with integer coefficients. In more technical language, the set $\{1, \pi, \pi^2, \pi^3, \ldots\}$ is linearly independent over the rational numbers. This means that no nontrivial finite sum of the form

$$
c_0 + c_1 \pi + c_2 \pi^2 + \cdots + c_k \pi^k
$$

with integer coefficients $c_i$ can equal zero unless all $c_i$ are zero.

### 2.5.3 Decomposing an Integer in Base $\pi$

Now consider the number 12. Can we write 12 as a finite sum of powers of $\pi$ with integer coefficients? That is, can we find integers $a_0, a_1, a_2, \ldots, a_k$ such that:

$$
12 = a_0 + a_1 \pi + a_2 \pi^2 + \cdots + a_k \pi^k
$$

Because $\pi$ is transcendental, the only way a polynomial in $\pi$ with integer coefficients can equal the integer 12 is if the constant term is 12 and all other coefficients are zero—giving the trivial representation $12 = 12 \times 1$. So a *finite* exact representation using integer coefficients is only possible in the trivial way.

**However**, if we allow *infinite* series—representations that go on forever—the situation changes dramatically. Every real number has a representation as an infinite series of powers of $\pi$ with integer coefficients (this is a consequence of $\pi$ being greater than 1 and transcendental). The number 12 can be written as an infinite sum involving powers of $\pi$. This is directly analogous to how every real number has a decimal expansion in base 10—but with $\pi$ as the base instead of 10.

### 2.5.4 The Philosophical Point

The lesson of base-$\pi$ expansions is not that they are practical (they are not) or that they form a metric (they do not, in the sense of satisfying the axioms of an absolute value that would extend the product formula). The lesson is conceptual.

When we say that 12 is “made of” the primes 2 and 3 (as $12 = 2^2 \times 3$), we are making a statement *within a particular representational system*—the system of prime factorization under ordinary multiplication. When we say that 12 is “made of” the powers of 10 (as $12 = 1 \times 10^1 + 2 \times 10^0$), we are making a statement within a different system—the decimal positional notation. When we say that 12 can be expressed in terms of $\pi$, we are using yet another system.

None of these systems is “the true” decomposition. Each reveals a different aspect of 12. The prime factorization reveals its multiplicative structure. The decimal expansion reveals its size relative to powers of 10. The base-$\pi$ expansion reveals that 12 can be related to the transcendental number $\pi$ through an infinite series, a fact that is invisible to both the prime factorization and the decimal expansion.

The notion of what a number “is made of” depends entirely on the representational system you choose. Change the system, and you change the anatomy of the number. There is no “true” anatomy independent of a choice of representation.

---

## 2.6 Primitive Elements Are Relative

We close Part II with one more illustration of the thesis: the relativity of what it means to be “primitive”—to be a generator, a source, an origin. In the mathematical theory of number fields, a **primitive element** is an element that, when combined with the rational numbers using addition, subtraction, multiplication, and division, generates everything else in the field. But “primitive” is never absolute; it is always relative to a starting point.

### 2.6.1 What Is a Number Field?

A **number field** is a collection of numbers that is closed under addition, subtraction, multiplication, and division (by nonzero elements), and that contains the rational numbers $\mathbb{Q}$. In less formal terms: a number field is a number system that extends the rational numbers by including some new numbers, and that allows you to perform all four arithmetic operations without leaving the system.

**Example.** Consider the set of all numbers of the form $a + b\sqrt{2}$, where $a$ and $b$ are rational numbers. This is a number field. Let us verify:

- **Addition:** $(a + b\sqrt{2}) + (c + d\sqrt{2}) = (a + c) + (b + d)\sqrt{2}$. The result is of the same form.
- **Subtraction:** $(a + b\sqrt{2}) - (c + d\sqrt{2}) = (a - c) + (b - d)\sqrt{2}$. Same form.
- **Multiplication:** $(a + b\sqrt{2})(c + d\sqrt{2}) = ac + ad\sqrt{2} + bc\sqrt{2} + 2bd = (ac + 2bd) + (ad + bc)\sqrt{2}$. Same form.
- **Division:** $\frac{1}{a + b\sqrt{2}} = \frac{a - b\sqrt{2}}{a^2 - 2b^2} = \frac{a}{a^2 - 2b^2} - \frac{b}{a^2 - 2b^2}\sqrt{2}$. Since $a, b$ are rational, the result is again of the form (rational) + (rational)$\sqrt{2}$, provided the denominator $a^2 - 2b^2$ is not zero.

This field is called $\mathbb{Q}(\sqrt{2})$—“the rational numbers with $\sqrt{2}$ adjoined.”

### 2.6.2 What Is a Primitive Element?

Within a number field $K$, a **primitive element** is a single element $\alpha$ such that every element of $K$ can be expressed in terms of $\alpha$ and the rational numbers, using only addition, subtraction, multiplication, and division.

In the example $\mathbb{Q}(\sqrt{2})$, the element $\sqrt{2}$ itself is primitive: every element $a + b\sqrt{2}$ is built from $\sqrt{2}$ and rational numbers. But $\sqrt{2}$ is not the only primitive element. The number $1 + \sqrt{2}$ is also primitive. So is $3\sqrt{2} + 1$. So is $\frac{\sqrt{2}}{2}$. All of these can generate the entire field.

### 2.6.3 Primitive Relative to What?

Here is the crucial point. The definition of “primitive” depends on the **base field**—the starting point from which generation occurs.

In the example above, we said $\sqrt{2}$ is primitive for $\mathbb{Q}(\sqrt{2})$ *over $\mathbb{Q}$*—meaning that starting from the rational numbers and adjoining $\sqrt{2}$, we can generate everything in $\mathbb{Q}(\sqrt{2})$.

But now consider a larger field—say, $\mathbb{Q}(\sqrt{2}, \sqrt{3})$, which contains all numbers of the form $a + b\sqrt{2} + c\sqrt{3} + d\sqrt{6}$ with rational coefficients $a, b, c, d$. Over $\mathbb{Q}$, a primitive element for this field might be $\sqrt{2} + \sqrt{3}$ (it turns out this single element generates the whole field). But $\sqrt{2}$ alone is *not* primitive for $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ over $\mathbb{Q}$—you cannot generate $\sqrt{3}$ from $\sqrt{2}$ using only rational operations.

However, $\sqrt{2}$ *is* primitive for $\mathbb{Q}(\sqrt{2})$ over $\mathbb{Q}$. And $\sqrt{3}$ is primitive for $\mathbb{Q}(\sqrt{3})$ over $\mathbb{Q}$. And $\sqrt{2}$ is also primitive for $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ over $\mathbb{Q}(\sqrt{3})$—if you are allowed to start from a broader base that already includes $\sqrt{3}$, then adjoining $\sqrt{2}$ gives you everything.

The status of being “primitive” shifts as the base field shifts. The same element—$\sqrt{2}$—is:

- Primitive for $\mathbb{Q}(\sqrt{2})$ over $\mathbb{Q}$.
- NOT primitive for $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ over $\mathbb{Q}$.
- Primitive for $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ over $\mathbb{Q}(\sqrt{3})$.

### 2.6.4 “Primitive” Is a Relation, Not a Property

This pattern is exactly analogous to what we observed about primality in Section 2.1. Just as “prime” is not a property of a number but a property of a number *relative to a metric*, so “primitive” is not a property of an element but a property of an element *relative to a base field and a target field.*

The grammar of the word itself gives us a clue. We do not say (or should not say) “$\sqrt{2}$ is primitive.” We say “$\sqrt{2}$ is primitive *for K over F*.” The phrase “for ... over ...” encodes the relational structure. Stripped of that structure, the word “primitive” has no fixed meaning.

This is a linguistic symptom of a deeper conceptual truth. The concepts of “primitive,” “fundamental,” “basic,” “elementary”—all the words we use to designate the ultimate constituents of things—are inherently relational. They make sense only within a framework that specifies: *generated from what?* and *generating what?* Without such a framework, the question “what is this made of?” has no determinate answer.

### 2.6.5 The General Principle

We can now state the general principle that unifies Sections 2.1 through 2.6:

**The Relativity Principle.** The status of a mathematical object as “indivisible,” “prime,” “basic,” “primitive,” or “elementary” is never an intrinsic property of the object itself. It is always a relational property, defined relative to:

1. **A notion of measurement or size** (as in the contrast between ordinary and p-adic metrics).
2. **A notion of decomposition or representation** (as in the contrast between prime factorization, base-b expansion, and base-$\pi$ expansion).
3. **A base system from which generation begins** (as in the contrast between different base fields for a primitive element).

Change any of these contextual parameters, and what was indivisible becomes divisible. What was prime becomes composite. What was primitive becomes derivative. What was fundamental becomes constructed.

There is no Archimedean point—no fixed, context-independent vantage from which the “true” building blocks of mathematics can be discerned. The building blocks shift with the framework. And the frameworks are many, equally valid, and incommensurable—though, as the product formula showed us, not unrelated. They form a balanced, interconnected family, each constraining the others, none dominating the others.

---

# Part III: Physical Analogy and Consilience

---

## 3.1 The Hierarchy of “Made Of”

Take a stone in your hand. You can feel its weight, its texture, its solidity. It seems to be one thing—a single, unified object. But you can break it. Strike it with a hammer, and it splits into smaller stones. Grind those smaller stones, and you get a powder of tiny grains. Look at those grains under a microscope, and you see they are made of crystals—regular arrangements of shapes that repeat in all directions.

At each step, what you thought was a “whole” turns out to be a collection of smaller parts. The stone was made of crystals. The crystals are made of smaller units that repeat. Those units, it turns out, are made of molecules—clusters of atoms bound together.

A molecule is not just a miniature lump of the same stuff. A water molecule is not a tiny drop of water; it is two atoms of hydrogen and one atom of oxygen linked in a specific geometry. If you split the molecule, you no longer have water at all—you have hydrogen gas and oxygen gas. The thing we call “water” exists only because of a particular arrangement of parts. Change the arrangement, and the thing vanishes, replaced by something else entirely.

Go deeper. Atoms themselves have internal structure. An atom consists of a dense central nucleus surrounded by a cloud of electrons. The nucleus contains almost all the mass, yet it occupies a volume a trillion times smaller than the atom as a whole. If an atom were the size of a sports stadium, its nucleus would be a grain of sand on the center spot. Between nucleus and electrons lies mostly empty space. The solidity of the stone—the reason your hand cannot pass through it—is not due to hard little balls filling the space. It is due to the electromagnetic forces that resist when electron clouds from your hand approach electron clouds from the stone. Solidity is a relationship, not a substance.

The nucleus itself is composite. It is made of protons and neutrons, collectively called nucleons. A proton carries a positive electric charge; a neutron carries none. They are bound together by a new force—the strong nuclear force—which is far more powerful than the electromagnetic force at short distances, but rapidly diminishes beyond the nucleus’s tiny radius.

And protons and neutrons? They too have parts. Each proton and each neutron is made of three quarks, bound together by particles called gluons—the carriers of the strong force. Quarks come in different types, named “up” and “down” for the ones that make up ordinary matter. A proton is two up quarks and one down quark. A neutron is one up and two down.

What are quarks made of? Here the chain of “made of” hits a barrier—not a philosophical one, but a physical one. Quarks cannot be isolated. If you try to pull two quarks apart, the force between them does not weaken with distance, as gravity and electromagnetism do. Instead, the force remains constant, like a stretched rubber band. The energy you invest in pulling them apart grows until there is enough energy to create a new quark–antiquark pair out of the vacuum. The new quarks immediately bind with the ones you were trying to separate, and you end up not with a free quark, but with new composite particles. This phenomenon is called **confinement**.

The word “confinement” means exactly what it sounds like: quarks are confined inside larger particles and cannot be extracted. This is not a technological limitation—a matter of building a better hammer. It is a consequence of the way the strong force behaves. The question “what is a quark made of?” becomes experimentally meaningless, because there is no procedure—even in principle—by which you could take a quark apart and examine its insides.

But this does not mean we stop asking questions. We can ask a different kind of question: not “what is a quark made of?” but “what description underlies the description of quarks?” The answer points to **quantum fields**. A quantum field is the fundamental way modern physics describes reality: the universe is not a collection of particles moving through space, but a collection of fields that pervade all of space. What we call a “particle” is a localized excitation of a field—a ripple, a quantized vibration. An electron is a ripple in the electron field. A quark is a ripple in the quark field. A gluon is a ripple in the gluon field.

The field description shifts the question again. Instead of asking “what is a particle made of?” we ask “what are the patterns that emerge from interacting fields?” And here a remarkable discovery appears: in many physical systems, particularly in condensed matter—the study of solids and liquids—we find entities that behave exactly like particles, but which are unquestionably not fundamental. They are patterns of collective motion. They are **quasiparticles**.

---

## 3.2 Quasiparticles: The Decisive Example

A **quasiparticle** is a collective excitation—a coordinated motion of many elementary constituents—that behaves, for all practical purposes, as if it were a single particle. It has a well-defined momentum, a well-defined energy, and often a well-defined mass. It can scatter off other particles. It can carry heat. It can be created and destroyed. In every operational sense—in every way you could design an experiment to detect it—it is a particle.

Yet it is “made of” nothing. Or rather, it is “made of” the correlated motion of the underlying material. Remove that material, and the quasiparticle ceases to exist. There is no “quasiparticle-stuff.”

Consider the clearest example: a **phonon**. The word “phonon” comes from the Greek root for sound, and that is exactly what it is—a quantum of sound vibration.

Imagine a crystal: a regular, repeating lattice of atoms, like oranges stacked in a crate. The atoms are not frozen in place; they oscillate around their equilibrium positions. Because they are connected by bonds, the motion of one atom influences its neighbors. If you displace one atom, the disturbance propagates through the lattice like a wave traveling across a field of wheat. This wave carries energy and momentum.

In classical physics, you describe this as a sound wave. In quantum physics, you discover that the energy of the wave is not continuous. It comes in discrete packets—quanta. Each quantum of vibrational energy is a phonon. A phonon is to a sound wave what a photon is to a light wave.

A phonon has all the properties you expect from a particle. It carries momentum $p$. It carries energy $E$, proportional to its frequency. It can collide with other phonons. It can scatter off impurities in the crystal. When you heat the crystal, you create more phonons. When the crystal cools, phonons are absorbed. The thermal conductivity of a material—how well it conducts heat—depends largely on how phonons move through it.

Now ask the question: what is a phonon made of?

You cannot answer “atoms,” because a phonon is not an atom. It is not localized on any particular atom. It is a coordinated pattern of displacement across vast numbers of atoms. You cannot point to a location and say “here is the phonon,” any more than you can point to a single molecule in an ocean wave and say “here is the wave.” The wave is the pattern, not the water.

You could answer: a phonon is “made of” nothing but the correlated motion of atoms in a lattice. But that answer only makes sense if you have already chosen the lattice description as your frame of reference. If you switch to a description in terms of phonons themselves, then the lattice is a background, and phonons are the fundamental entities of that description. Neither description is more correct. They are different choices about how to organize the same physical reality.

A more exotic example is the **anyon**. An anyon is a quasiparticle that can exist only in systems confined to two spatial dimensions—for instance, electrons trapped at the interface between two semiconductors. In our three-dimensional world, all particles fall into two categories: bosons and fermions. This classification determines how identical particles behave when you exchange their positions. For bosons, the mathematical description (the wavefunction) remains unchanged when two identical particles are swapped. For fermions, it flips sign—multiplies by $-1$.

Anyons are different. When you swap two anyons, the wavefunction picks up a phase factor—a rotation in the mathematical description—that can be any angle, not just 0° (boson) or 180° (fermion). Hence the name “any-on”: particles that can have *any* statistical phase. This fractional behavior is only possible because two-dimensional space has a different topology from three-dimensional space: the path one particle takes around another cannot be continuously shrunk to a point without crossing the other particle. The mathematics of exchange is richer in two dimensions.

An anyon is a collective excitation of the two-dimensional electron system. It is “made of” electrons. But it has properties—fractional statistics—that no individual electron possesses. Once again, the whole has properties that the parts do not, and the parts themselves can be described as excitations of something else.

These examples demonstrate a profound point. The question “what is something made of?” does not have a single, context-independent answer. The answer depends on which description you choose to work in. A phonon is a fundamental entity in the phonon description. It is a derived, collective phenomenon in the atomic-lattice description. Both descriptions are valid; they are simply different maps of the same territory, with different scales and different features highlighted.

The phonon is real. It scatters, carries heat, and leaves measurable traces in experiments. But it is not “made of” any substance more fundamental than the pattern of relationships that constitutes it. This brings us to a larger principle: what counts as “fundamental” depends on the scale at which you look.

---

## 3.3 Scale-Dependent Reality: The Renormalization Group

When you change the magnification on a microscope, the world you see changes. At one magnification, you see the intricate veins of a leaf. Turn the knob, and you see individual cells with their walls and nuclei. Turn it further, and you see the organelles within each cell. Turn it further still, and you see the protein complexes embedded in membranes. At each level, the relevant entities—the “degrees of freedom” you use to describe what you see—are different. There is no single “right” magnification.

Physics makes this intuition rigorous. A physical system can be probed at different energy scales. Energy and distance are inversely related in quantum physics: higher energy means you can resolve shorter distances. Just as a microscope with a shorter wavelength of light can see finer details, a higher-energy probe can “see” smaller structures.

At low energies—corresponding to large distances and everyday temperatures—you see molecules and their collective behaviors. Water, at room temperature, is a liquid: molecules sliding past each other, forming and breaking hydrogen bonds, exhibiting viscosity and surface tension. These are collective properties. No single water molecule has viscosity. Viscosity is a property of the ensemble, describable at the molecular scale but not reducible to any one molecule.

Raise the energy. At higher temperatures or with more energetic probes, the molecules break apart into atoms. Now you are in the regime of atomic physics. The degrees of freedom are individual atoms, their electrons, their energy levels. You no longer talk about water; you talk about hydrogen and oxygen.

Raise the energy further. The atoms ionize—electrons are stripped off—and you have a plasma: a soup of bare nuclei and free electrons. Now the degrees of freedom are charged particles interacting through electromagnetic forces.

Raise the energy still further. The nuclei themselves become accessible. You see protons and neutrons, and the strong force that binds them. The relevant description is nuclear physics.

Higher still. The protons and neutrons reveal their internal structure: quarks and gluons. At these energies, the strong force becomes weak—a phenomenon called asymptotic freedom—and quarks behave almost as if they were free particles. The description is now quantum chromodynamics, the theory of quarks and gluons.

What is remarkable is that at each scale, the description is self-contained. You do not need to know about quarks to describe water flowing through a pipe. The equations that govern fluid flow are true and complete at their own scale. You cannot predict the viscosity of water by solving quark equations—or rather, you could in principle, but the computational task is impossible and, more importantly, unnecessary. The viscosity emerges at the molecular scale; it is a property of the collective, not of the micro-constituents.

This layered autonomy of scales is formalized by the **renormalization group**.

The name is unfortunate—it sounds like a bureaucratic committee for rescaling something. But the idea is straightforward. Imagine you have a physical system described at a certain level of detail—say, a crystal lattice with individual atoms, their masses, and the spring-like forces between them. You can ask: if I look at this system from a greater distance, so that I cannot see individual atoms, what effective description emerges? You “zoom out” by averaging over blocks of atoms, systematically eliminating the fine-grained details and deriving new equations for the coarse-grained variables.

This process—averaging over short-distance degrees of freedom and deriving effective long-distance equations—is the core of the renormalization group. As you zoom out, some details become irrelevant: they wash out and do not affect the large-scale behavior. Other details are relevant: they grow in importance and determine the macroscopic properties. Still others are marginal: they neither grow nor shrink, and they require more careful treatment.

The crucial insight is that the degrees of freedom themselves change as you change scale. What looks like a set of interacting atoms at one scale looks like a smooth elastic medium at a larger scale. What looks like a turbulent fluid at one scale looks like a set of effective “eddy” quasiparticles at another. There is no privileged scale. No level of description is more fundamental than any other, except relative to a particular question you are asking.

If you want to know why copper conducts electricity, the electron description is appropriate. If you want to know why a copper wire bends rather than shatters, the crystal-grain description is appropriate. If you want to know why copper is reddish-orange, you need the atomic description—specifically, the energy levels of copper atoms. None of these descriptions is the “true” one. Each answers a different question, and each is valid within its domain.

The renormalization group reveals that the boundary between “fundamental” and “emergent” is itself scale-dependent. The electron, which we treat as fundamental in atomic physics, may itself be an emergent quasiparticle in some deeper description—a collective excitation of more basic fields. But at the scales we can currently probe, it is elementary. The word “elementary” does not mean “intrinsically indivisible.” It means “indivisible at the energies we can access.” It is a statement about our measurement context, not about ultimate reality.

---

## 3.4 Consilience: The Same Pattern in Numbers and Matter

We have now traveled through two vast landscapes: the landscape of numbers, explored in Parts I and II of this treatise, and the landscape of matter, explored here. At first glance, they could not be more different. Numbers are abstract; matter is concrete. Numbers are timeless; matter unfolds in time. Numbers obey logical deduction; matter obeys physical law.

Yet at a structural level, they reveal exactly the same pattern.

Recall the central discovery from our study of numbers. A rational number—a simple fraction like 3/4 or 22/7—does not have a single, objective “size.” Its size depends on which metric you choose to measure it with.

The ordinary, everyday metric—the one we learn in school—tells us that 3/4 has size 0.75. This is the absolute value, denoted $\lvert 3/4 \rvert_\infty$. It measures how far a number is from zero on the familiar number line. It is the metric that answers the question: “How much of something do I have?”

But there are other metrics, the p-adic metrics, one for each prime number $p$. The 2-adic metric, for example, measures a number not by its distance from zero, but by how many times it can be divided by 2. A number that can be divided by 2 many times is “small” in the 2-adic sense, regardless of how large it is in the ordinary sense. The number 1024 (which is $2^{10}$) is huge in ordinary terms but tiny in the 2-adic metric because it is deeply divisible by 2. Conversely, the number 3 has ordinary size 3, but it is “large” in the 2-adic metric because it is not divisible by 2 at all.

Each metric provides a complete, logically consistent way of measuring size. No metric is truer than any other. They are simply different measurement contexts, each answering a different question. The 2-adic metric answers: “How does this number relate to the prime 2?” The 3-adic metric answers: “How does it relate to the prime 3?” The ordinary metric answers: “How far is it from zero on the real line?”

And yet these metrics are not independent. They are bound together by a profound relationship: the **adelic product formula**. For any rational number, if you multiply its size in the ordinary metric by its size in every p-adic metric (for every prime $p$), the product is always exactly 1. Always. No exceptions.

Let us see it with a concrete example. Take the number 12. Its ordinary size is $\lvert 12 \rvert_\infty = 12$. Its 2-adic size: $12 = 2^2 \times 3$, so it can be divided by 2 twice. In the 2-adic metric, this means $\lvert 12 \rvert_2 = 1/4$. Its 3-adic size: $12 = 2^2 \times 3$, divisibility by 3 once gives $\lvert 12 \rvert_3 = 1/3$. For all other primes $p$ (5, 7, 11, ...), 12 is not divisible, so $\lvert 12 \rvert_p = 1$. Now multiply all of them together:

$$
\lvert 12 \rvert_\infty \times \lvert 12 \rvert_2 \times \lvert 12 \rvert_3 \times \lvert 12 \rvert_5 \times \lvert 12 \rvert_7 \times \cdots = 12 \times (1/4) \times (1/3) \times 1 \times 1 \times \cdots = 12 / 12 = 1.
$$

The product formula is a global constraint. It says: the number, regarded across all possible measurement contexts, has an invariant total “size” of 1. The different metrics distribute this unity among themselves—one metric gives a large number, another gives a compensating small number. None gives the “true” size; together they give the complete picture.

Now consider what we have found in physics.

A physical system—say, a piece of copper—does not have a single, objective set of “parts.” Its parts depend on the energy scale at which you probe it. At one scale, the parts are crystal grains. At another, they are atoms. At another, they are electrons and nuclei. At another, they are quarks and gluons. At another, they are phonons and other collective excitations.

No scale is privileged. The quarks are not “more real” than the phonons. The atoms are not “more fundamental” than the crystal grains. Each description is a valid measurement context, and each answers a different question. The question “What is copper made of?” has no single answer. It has only the answers that arise from specific choices of scale and specific types of experimental probe.

And yet the descriptions are not independent. They are linked by the renormalization group. The equations that govern quarks and gluons at high energies flow, under the renormalization group transformation, into the equations that govern protons and neutrons at lower energies. Those, in turn, flow into the equations that govern nuclei. Those flow into the equations that govern atoms. Those flow into the equations that govern molecules and crystals.

The renormalization group provides the global constraint: the physics must be consistent across scales. You cannot arbitrarily change the quark-level description without affecting the atomic-level description. They are bound together, just as the p-adic sizes of a rational number are bound together by the product formula.

Here is the structural parallel, laid out side by side:

| In Number Theory | In Physics |
|---|---|
| A rational number | A physical system |
| A p-adic metric (one per prime) | An energy scale (one per range of phenomena) |
| The ordinary metric (absolute value) | The macroscopic, everyday scale |
| Size in a given metric | Degrees of freedom at a given scale |
| No metric is privileged | No energy scale is privileged |
| The product formula binds all sizes | The renormalization group binds all scales |

The pattern is identical. In both domains, the naive expectation is that things have a single, intrinsic decomposition into atomic parts—that a number is built from prime factors in a unique way, that matter is built from elementary particles in a unique way. In both domains, this naive expectation breaks down under careful examination.

A rational number does have a unique prime factorization—that is true. But the *metric properties* of that number—the question “how big is it?”—depend on which p-adic metric you use. The prime factors are not building blocks that determine the number’s behavior in all contexts. They are features that become relevant only when you choose a particular measurement context.

Similarly, matter does have constituents—quarks, electrons, and so on—at a particular scale. But what counts as a constituent, and what counts as a collective property, depends on the energy scale. The fact that a proton is “made of” quarks does not make the quark description more fundamental than the proton description. It makes it relevant at higher energies. At lower energies, the proton is the natural, irreducible unit.

The radical conclusion is this: the distinction between what a thing IS and how we MEASURE it collapses.

There is no measurement-independent fact of the matter about what is “fundamental.” A phonon is fundamental in the context of lattice vibrations. An electron is fundamental in the context of atomic physics. A quark is fundamental in the context of high-energy collisions. Each is a legitimate, self-contained description. Each predicts observables—things you can measure—that are true in its domain.

This is not relativism. It is not the claim that “anything goes” or that all descriptions are equally valid for all purposes. The claim is that validity is always relative to a measurement context. A description that is complete and predictive at one scale is not “wrong” just because a more fine-grained description exists at another scale. The fluid description of water is not wrong because water is made of molecules. It is the correct description for questions about fluid flow, and it would be a mistake—practically and conceptually—to insist that you must talk about molecules when you are trying to design a plumbing system.

And crucially, the different contexts are not isolated worlds. They are connected by precise mathematical relationships. In number theory, the product formula. In physics, the renormalization group flow equations. These connecting principles ensure that the whole—the number, the physical system—is coherent across all contexts. The whole is not a sum of atomic parts, assembled by a cosmic inventory. The whole is a pattern of relationships across all possible measurement contexts, governed by global constraints that guarantee consistency.

The adelic product formula and the renormalization group are, at this level of abstraction, the same idea. They both express the principle of **contextual invariance**: the entity in question has no privileged decomposition, but it has a complete description that encompasses all decompositions, and that description obeys a global conservation law. For numbers, the conservation law is that the product of all metric sizes equals one. For physical systems, the conservation law is that the physics flows consistently from one scale to the next under coarse-graining.

---

This consilience—this convergence of independent lines of reasoning on the same structural truth—is not a coincidence. It arises because both number theory and physics are, at root, attempts to answer the same kind of question: “What is this thing, truly?” And in both domains, a patient, rigorous investigation leads to the same answer: “The question is ill-posed unless you specify a measurement context. Give me a context, and I will give you a description. Change the context, and the description changes—but the underlying invariance remains.”

Everything is divisible. But divisibility is not a property of the thing itself. It is a property of the relationship between the thing and the frame you use to look at it. The stone is not composed of atoms in some absolute sense; it is composed of atoms when you probe it at atomic energy scales. The stone is composed of crystals when you probe it at optical scales. The stone is a solid object when you hold it in your hand. All these descriptions are true. None is the ultimate truth.

The pursuit of “what things are really made of” does not end at a final, indivisible layer. It ends at the recognition that the question itself assumes a fixed measurement frame, and that no such frame is uniquely sanctioned by nature. The deepest thing we can say about a number, or a stone, is not what it is made of, but how it responds across all the different ways we can interrogate it—and how those responses, diverse as they are, fit together into a coherent whole.

---

# Part IV: Category-Theoretic and Logical Deepening

In the preceding parts, we traced a single pattern through numbers and physical matter: the property of being “indivisible” is never absolute. It always depends on the measurement context. A number is prime in the ordinary integers, but not in the Gaussian integers. A particle is elementary in one effective theory, but composite in a deeper theory. The “what” of indivisibility shifts with the “how” of measurement. The adelic product formula and the renormalization group each showed, in their own domains, that no single metric or scale tells the whole story.

In this part, we ask a deeper question: is this pattern itself a mere curiosity, or is it forced by the very structure of systematic thought? We will see that the relativity of indivisibility is not just a recurring empirical observation. It is baked into the logical and structural foundations of all formal reasoning. The tools we use—symmetry groups, coordinate systems, categories, types, formal systems—each introduce their own choices, and with them, their own boundaries between the divisible and the indivisible.

We proceed in six sections. First, we examine the most fundamental symmetries in algebra and find that they too depend on a prior choice. Second, we look at the framework that unified our view of numbers—the adeles—and discover that it is itself built on arbitrary coordinates. Third, we climb the ladder of abstraction through categories and find that “indivisible” means something different at every level. Fourth, we compare different mathematical worlds and see that the predicate “is prime” does not transfer between them. Fifth, we confront the boundary of formal systems: there are truths that cannot be proved, and the boundary shifts with the system. Finally, we see that even within a fixed system, some questions about indivisibility have no algorithmic answer.

---

## 4.1 Symmetries Are Not Absolute

A **symmetry** is a transformation that leaves something unchanged. Imagine a square drawn on a piece of paper. If you rotate the square by one quarter of a full turn around its centre, it looks exactly the same—each corner moves to the position of another corner, and the shape as a whole is indistinguishable from its starting configuration. If you reflect the square across a line through its centre, it again looks exactly the same. The set of all such transformations—rotations, reflections, and every combination you can make by performing one after another—forms what mathematicians call a **group**.

A group is a collection of transformations together with a rule for combining them: do first one, then the other. This rule must satisfy three natural conditions. (1) There is a “do nothing” transformation, called the **identity**, which leaves everything as it was. (2) Every transformation can be undone: for each element, there is an **inverse** transformation that returns the object to its original state. (3) The order of grouping does not matter: if you have three transformations A, B, C, then doing (A then B) then C produces the same final result as doing A then (B then C). This is called **associativity**. These three conditions capture the essence of what it means to be a collection of symmetries.

Groups appear throughout mathematics and physics. They describe the symmetries of geometric shapes, the patterns in crystals, the conservation laws of physics (every conservation law corresponds to a symmetry, as we glimpsed in Part III), and—most relevant for our present purpose—the structure of solutions to polynomial equations.

Consider equations like

$$
x^2 - 2 = 0, \qquad x^3 + x + 1 = 0, \qquad x^5 - 4x + 2 = 0.
$$

The numbers that satisfy such equations, when the coefficients are ordinary integers, are called **algebraic numbers**. The simplest algebraic numbers are the ones we learn in school: $\sqrt{2}$ satisfies the first equation; the golden ratio satisfies $x^2 - x - 1 = 0$. But algebraic numbers also include vastly more complicated numbers—numbers that cannot be expressed by any finite combination of roots, additions, multiplications, and divisions. Nevertheless, they all arise as solutions to some polynomial equation with integer coefficients.

The algebraic numbers form a remarkable structure: you can add them, subtract them, multiply them, and divide them (except by zero), and the result is always another algebraic number. A set equipped with these four operations, satisfying the familiar rules of arithmetic, is called a **field**. The algebraic numbers are a field—in fact, they are the smallest field that contains all the rational numbers and a solution to every possible polynomial equation with rational coefficients.

Now, some algebraic numbers stand in a symmetric relation to one another. Take the equation $x^2 - 2 = 0$. It has two solutions: $\sqrt{2}$ and $-\sqrt{2}$. If you take any true statement about arithmetic that involves only integers and these two numbers—say, $( \sqrt{2} )^2 - 2 = 0$—and you swap $\sqrt{2}$ with $-\sqrt{2}$, the statement remains true: $( -\sqrt{2} )^2 - 2 = 0$. No equation with integer coefficients can distinguish between them. The swap is a symmetry of the field of algebraic numbers.

More dramatically, consider the equation $x^3 - 2 = 0$. It has three solutions in the algebraic numbers: the real cube root $\sqrt[3]{2}$, and two complex numbers obtained by multiplying the real root by complex cube roots of unity. Any equation with integer coefficients that holds for one of these three solutions holds for all three in exactly the same pattern. The six possible rearrangements of these three roots form a group—the same group as the symmetries of an equilateral triangle.

The collection of *all* symmetries of the entire field of algebraic numbers that leave the rational numbers untouched is a group of staggering size and complexity. It is called the **absolute Galois group** of the rational numbers. This group encodes, in a single algebraic structure, the solvability of all polynomial equations, the distribution of prime numbers in arithmetic progressions, the structure of modular forms, and deep connections to modern physics.

But here is the crucial point—the one that matters for our thesis. To define this group, you must first choose something called an **algebraic closure**.

An algebraic closure is a maximal field of algebraic numbers. It is a field that contains a root of every polynomial equation with coefficients in that field, and it cannot be enlarged without losing the property of being a field. In other words, it is a complete universe of algebraic numbers—a realm in which every polynomial equation has as many solutions as its degree suggests.

The problem is that there is no single, canonical algebraic closure. You can construct many different ones. They are all **isomorphic**—a word we must now define.

Two mathematical structures are isomorphic if there is a one-to-one correspondence between their elements that perfectly preserves all the operations and relations of the structure. If you have two groups, and there is a mapping between them that sends the identity to the identity, products to products, and inverses to inverses, in a way that is bijective (every element in the first corresponds to exactly one in the second, and vice versa), then the groups are isomorphic. For all structural purposes, they are identical—you cannot tell them apart by their internal patterns. But they may be different as sets: the elements may have different names, different constructions, different “substance.”

Different choices of algebraic closure yield isomorphic fields. But they are not identical. One algebraic closure might be constructed using complex numbers as a starting point; another might be built purely algebraically without any reference to geometry. They contain different objects. Yet each is a fully satisfactory universe of algebraic numbers.

Because the symmetry group is defined as the group of transformations of a *particular* algebraic closure, different choices of closure yield different symmetry groups. These groups are isomorphic—they have exactly the same abstract structure—but they are different sets of transformations, acting on different sets of objects. You cannot point to a unique, absolute, symmetry group of the algebraic numbers. You must first pick a coordinate system—an algebraic closure—and only then can you speak of the symmetries.

This is a profound fact. The absolute Galois group is often described as the ultimate symmetry group of arithmetic, the fundamental object that governs the hidden harmonies of numbers. Yet even this “absolute” depends on a choice. The symmetry is relative to the universe of objects you decide to work in.

Notice the pattern we first saw in Part I and Part III. A number is prime only relative to a metric. A particle is elementary only relative to an energy scale. And now, the symmetries of numbers themselves are defined only relative to a choice of algebraic closure. The relativity has moved from the objects we study to the very symmetries that are supposed to structure them.

---

## 4.2 The Coordinate System Is a Choice

In Part II, we encountered the adeles. They are a single mathematical ring that simultaneously encodes the p-adic metric for every prime $p$, together with the ordinary real metric, all unified under the product formula. The adeles were our key example of a framework that reveals the relativity of measurement: what looks prime in the 2-adic metric may look composite in the 3-adic metric, and the adeles hold all metrics at once, showing that no single metric is privileged.

But the adeles themselves are built using a choice. To construct the adele ring, you must choose, for each prime number $p$, a **uniformizer**. Let us understand what this means.

Consider the p-adic integers, which we denote $\mathbb{Z}_p$. These are the completion of the ordinary integers with respect to the p-adic metric—roughly, a number is “p-adically small” if it is divisible by a high power of $p$. Within $\mathbb{Z}_p$, the element $p$ generates a special set: the **maximal ideal**, which consists of all p-adic integers that are divisible by $p$ (i.e., those that are not invertible in $\mathbb{Z}_p$). The element $p$ is a uniformizer—it is a single element that generates this ideal.

But $p$ is not the only uniformizer. Any element of the form $p \cdot u$, where $u$ is a **unit** (an element that has a multiplicative inverse in $\mathbb{Z}_p$), also generates the same maximal ideal. For example, in the 2-adic integers, both 2 and $-2$ and $6 = 2 \cdot 3$ (since 3 is a unit in $\mathbb{Z}_2$) are uniformizers. They all produce the same ideal, the same topology, and the same valuation—the same way of measuring size.

Choosing a uniformizer is like choosing which direction is “up” on a map. Different choices give different coordinate labels, but the underlying geography—the pattern of distances, the topology, the ring structure—is unchanged. The adele ring built with one set of uniformizers is isomorphic to the adele ring built with another set. But they are not the same ring. They are different sets with different elements, even though the pattern of relationships among those elements is identical.

This is not a defect peculiar to the adeles. It is a general phenomenon in mathematics. Whenever we build an object intended to serve as a universal framework—a single structure that captures all perspectives—the construction itself requires arbitrary choices. The framework is not uniquely determined. There is no escape from choice. The act of construction always leaves a residue of arbitrariness.

A vivid illustration comes from **Arakelov geometry**. This is a way of doing geometry over the integers rather than over the real numbers or the complex numbers. In ordinary algebraic geometry, you study shapes defined by polynomial equations, and you can treat all points of the shape on an equal footing. But when you work over the integers, there is a fundamental asymmetry: the “point at infinity”—the place that corresponds to the ordinary real metric—behaves differently from the points corresponding to the finite primes.

In Arakelov geometry, you must decide how to treat the point at infinity. You can compactify the geometric object by adding a “fiber at infinity,” but there are many inequivalent ways to do so. You can assign different metrics—different ways of measuring size—to this fiber. The choice affects the formulas for intersection numbers, volumes, and heights—the geometric invariants that the theory computes. There is no single, canonical way to complete the picture. Different choices lead to equivalent theories. But they are not identical theories. They involve different intermediate constructions and different numerical values for the same geometric quantity, even though they ultimately agree on the deep structural facts.

The lesson is striking. The adeles—the very framework that reveals the relativity of measurement—are themselves relative to a choice. The ladder of relativity has no bottom rung. The adeles taught us that “prime” is relative to a metric. But “adele” is relative to a choice of uniformizer. And the geometric framework that unifies the finite and infinite places is relative to a choice of compactification.

This is not a cause for despair. It is a structural fact about systematic thought: every universal perspective is achieved from a particular standpoint. The view from everywhere is always constructed from a view from somewhere.

---

## 4.3 Levels of Description

We have been moving upward through levels of abstraction. We started with numbers. Then we considered metrics—ways of measuring numbers. Then we considered the adeles—a framework that contains all metrics. Then we considered the symmetries of the algebraic numbers and the coordinate choices that go into the adele construction. At each step, we have asked what “indivisible” means, and at each step, we have found that the answer depends on a prior choice.

Now we must ask: is there a systematic way to talk about these levels themselves? Is there a language that can describe objects, transformations, transformations-between-transformations, and so on, in a unified way?

The language for this is **category theory**. We will build the concept step by step.

A **category** consists of two ingredients: **objects** and **morphisms** (also called transformations or arrows). The objects can be anything. The morphisms are ways of moving from one object to another.

Formally, a category has:

- A collection of objects. These could be sets, groups, topological spaces, vector spaces, numbers—anything.
- For any two objects $A$ and $B$, a collection of morphisms from $A$ to $B$. We write $f: A \to B$ to mean “$f$ is a morphism from $A$ to $B$.”
- A rule for **composing** morphisms. If $f: A \to B$ and $g: B \to C$, then there is a morphism $g \circ f: A \to C$ (read “$g$ after $f$”).
- Composition must be associative: $(h \circ g) \circ f = h \circ (g \circ f)$.
- Every object $A$ must have an **identity morphism** $\operatorname{id}_A: A \to A$, which does nothing when composed with other morphisms: $\operatorname{id}_B \circ f = f$ and $g \circ \operatorname{id}_B = g$.

Examples make this vivid:

- **The category of sets:** Objects are sets. Morphisms are ordinary functions between sets. Composition is function composition. The identity morphism is the function that sends each element to itself.
- **The category of groups:** Objects are groups. Morphisms are group homomorphisms—functions that respect the group operation (if $f(xy) = f(x)f(y)$). Composition and identities work similarly.
- **The category of topological spaces:** Objects are topological spaces (sets equipped with a notion of “closeness” or “neighbourhood”). Morphisms are continuous functions. Composition is again function composition.

In each case, the objects are the “things” of a certain kind, and the morphisms are the “structure-preserving maps” between those things. The choice of what counts as a morphism is part of the definition of the category. You could take the same objects (say, groups) but allow only a restricted class of morphisms (say, only isomorphisms, the bijective homomorphisms) and you would get a different category.

Now comes the crucial move. Category theory can talk about itself. Just as we formed the category of sets, we can form the category of categories. Here the objects are categories, and the morphisms are **functors**. A functor $F: \mathcal{C} \to \mathcal{D}$ is a mapping that sends:

- each object of $\mathcal{C}$ to an object of $\mathcal{D}$,
- each morphism of $\mathcal{C}$ to a morphism of $\mathcal{D}$,

in a way that preserves the categorical structure: $F(\operatorname{id}_A) = \operatorname{id}_{F(A)}$ and $F(g \circ f) = F(g) \circ F(f)$. A functor is a transformation of one whole category into another.

But we are not done. We can consider transformations *between functors*. Suppose $F$ and $G$ are two functors from category $\mathcal{C}$ to category $\mathcal{D}$. A **natural transformation** $\alpha: F \Rightarrow G$ is a way of systematically relating the images of $F$ and $G$. For each object $X$ in $\mathcal{C}$, it provides a morphism $\alpha_X: F(X) \to G(X)$ in $\mathcal{D}$. These morphisms must fit together coherently: for any morphism $f: X \to Y$ in $\mathcal{C}$, the diagram

$$
\begin{matrix}
F(X) & \xrightarrow{\alpha_X} & G(X) \\
\Big\downarrow {F(f)} & & \Big\downarrow {G(f)} \\
F(Y) & \xrightarrow{\alpha_Y} & G(Y)
\end{matrix}
$$

must commute—meaning going right then down gives the same result as going down then right.

This gives us three distinct levels:

- **Level 0:** Objects (numbers, spaces, groups).
- **Level 1:** Morphisms between objects.
- **Level 2:** Natural transformations between morphisms-between-objects.

And it does not stop there. There are transformations between natural transformations, called **modifications**. There are transformations between modifications, and so on. In general, there is an infinite hierarchy of **n-categories**, where you have objects, 1-morphisms, 2-morphisms, 3-morphisms, and so on. Each level has its own kind of entity, and its own rules for composition.

What does this have to do with indivisibility?

At each level, the question “what is indivisible?” means something fundamentally different, because the entities at each level are different kinds of things.

- **At Level 0**, an indivisible object is one that cannot be decomposed into a combination of simpler objects within the given category. In the category of sets, an indivisible object might be a singleton set: it cannot be written as a disjoint union of non-empty sets. In the category of groups, a **simple group** is one that has no normal subgroups other than the trivial group and itself—it cannot be broken apart by group-theoretic operations. In the category of representations, an **irreducible representation** is one that has no proper subrepresentations.

- **At Level 1**, an indivisible morphism is one that cannot be factored as a composition of two non-trivial morphisms (neither of which is an isomorphism). In the category of sets, a function between finite sets is indivisible if it cannot be written as a composition of two functions that are not bijections. In the category of topological spaces, an **irreducible continuous map** is one that cannot be factored through a non-trivial space. In the category of modules, an **indecomposable map** is one that cannot be split.

- **At Level 2**, an indivisible natural transformation is one that cannot be expressed as a vertical or horizontal composition of simpler natural transformations.

The definitions change at each level because the nature of the entities changes. There is no single notion of “indivisible” that applies uniformly across all levels. You must choose a level—you must decide what kind of entity you are treating as the basic unit—before the question even makes sense.

Moreover, the levels interact in ways that undermine any hope of a global definition. An object that is indivisible at Level 0 may, when viewed from Level 1, appear as the identity morphism on that object. But every identity morphism can be factored trivially (e.g., as the composition of two isomorphisms). What is atomic at one level is composite at the next.

This is a structural reflection of the pattern we have traced throughout. Just as “prime” depends on metric, and “elementary” depends on energy scale, and “symmetry” depends on algebraic closure, “indivisible” depends on the categorical level you choose to inhabit. The hierarchy of categories is a hierarchy of perspectives, and each perspective brings its own atoms.

---

## 4.4 Different Worlds, Different Primes

We return to the concrete question that began our investigation: what does it mean to be prime? In the ordinary integers $\mathbb{Z}$, a prime is a number greater than 1 whose only positive divisors are 1 and itself. The number 5 is prime; the number 6 is not, because 6 = 2 × 3. This definition seems so natural that one might think it is universal.

But we have already seen that it is not. In the Gaussian integers (numbers of the form $a + bi$ where $a, b$ are ordinary integers and $i^2 = -1$), the number 5 is not prime, because $5 = (2 + i)(2 - i)$. And in the 2-adic integers $\mathbb{Z}_2$, the situation is even more radical.

The **2-adic integers** are a number system built from the 2-adic metric. In this system, a number is “small” if it is divisible by a high power of 2. The 2-adic integers are the completion of the ordinary integers with respect to this metric—all sequences that are “Cauchy” (the terms get arbitrarily close to each other) in the 2-adic sense have limits in $\mathbb{Z}_2$. This is analogous to how the real numbers complete the rationals with respect to the ordinary absolute value, but the resulting number system is very different.

In $\mathbb{Z}_2$, the element 2 plays a unique role. It generates the maximal ideal: every element of $\mathbb{Z}_2$ that does not have a multiplicative inverse (i.e., every non-unit) is divisible by 2. The element 2 is the *uniformizer*. But what about 3? In the ordinary integers, 3 is prime. In $\mathbb{Z}_2$, however, 3 is a *unit*: it has a multiplicative inverse. Indeed, 3 × 11 = 33 ≡ 1 (mod 16), and more elaborate constructions show that 3 has an inverse in the full 2-adic integers. Any odd integer is a unit in $\mathbb{Z}_2$. The number 5 is also a unit. So is 7, 11, and every odd prime.

The notion of “prime” has been turned inside out. In $\mathbb{Z}_2$, there is only one prime in the sense of a generator of the maximal ideal: the element 2 (up to multiplication by a unit). All the ordinary odd primes cease to be prime—they become units, analogous to 1 and −1 in the ordinary integers.

This is not a perversity of the 2-adic numbers. It is the general situation in any p-adic integer ring $\mathbb{Z}_p$. The element $p$ is the unique prime (uniformizer); all other ordinary primes, being coprime to $p$, are units in $\mathbb{Z}_p$. In each p-adic world, there is only one special element that plays the role of building block. Which element that is depends on which $p$ you chose.

What we are witnessing here is a deep principle of **type theory**. Type theory is a foundational language for mathematics, alternative to set theory, in which every mathematical object belongs to exactly one **type**. The type of an object determines what operations can be performed on it and what properties can be meaningfully ascribed to it.

In type theory, the natural numbers $\mathbb{N}$ form a type. The integers $\mathbb{Z}$ form a different type (though related by an embedding). The 2-adic integers $\mathbb{Z}_2$ form yet another type. There is also a type for the 3-adic integers, the real numbers, the complex numbers, and so on. Each type has its own internal structure, its own operations, and its own predicates.

A **predicate** is a statement that can be true or false depending on which element of a type it is applied to. “Is prime” is a predicate. But “is prime” is not a single predicate that floats above all types. It is defined *internally to each type* by type-specific rules. The predicate $P_{\mathbb{N}}(n)$ for “$n$ is prime in $\mathbb{N}$” is defined by divisibility within $\mathbb{N}$. The predicate $P_{\mathbb{Z}_2}(x)$ for “$x$ is a uniformizer in $\mathbb{Z}_2$”—if one even chooses to call it “is prime”—is defined by the p-adic valuation. These are two different predicates. They happen to share a name in informal language, but they are distinct mathematical entities. There is no overarching “is prime” that subsumes both.

You cannot take the predicate $P_{\mathbb{N}}$ and apply it to an element of $\mathbb{Z}_2$. The type system forbids it. An element of $\mathbb{Z}_2$ is not an element of $\mathbb{N}$ (even though there is a canonical embedding of $\mathbb{N}$ into $\mathbb{Z}_2$, the embedded natural numbers are not identical to the originals—they are images under a mapping). The question “is 3 prime?” is not well-posed until you specify the type. In $\mathbb{N}$, yes. In $\mathbb{Z}_2$, the question is ill-typed; but if you embed 3 into $\mathbb{Z}_2$ and ask “is this a uniformizer?”, the answer is no.

This is not a defect of the number systems. It is a reflection of the fact that mathematical structures are autonomous worlds, each with its own internal logic. When we move from one world to another, we must redefine our terms. What counts as a building block in one world may be a composite or a unit in another.

The lesson for our central thesis is unambiguous. There is no universal notion of “prime” that makes sense across all mathematical contexts. The question “is this prime?” is always accompanied by an implicit “in which world?” And the worlds are genuinely different—not just different perspectives on the same underlying reality, but different realities with their own constitutive rules, their own identity criteria, and their own notions of atomicity.

---

## 4.5 The Limits of Formal Systems

We have been charting the layers of context on which the concept of indivisibility depends. At each step, we have found that the question “what is indivisible?” requires a prior choice: of metric, of energy scale, of algebraic closure, of coordinate system, of categorical level, of type. One might hope that, at least, we could formalize our reasoning within a single system and say with certainty: “In *this* formal system, *these* are the atoms, and *this* is the criterion for indivisibility.”

But even this hope—the hope of a fixed, self-contained framework—runs into a wall. The boundary between the provable and the unprovable within a formal system is itself relative. There is no formal system in which every truth is provable, and no notion of provability that is absolute.

Let us define our terms carefully.

A **formal system** is a set of rules for manipulating symbols. It consists of four components:

- An **alphabet**: a finite or countable set of symbols.
- A **grammar**: a set of rules specifying which finite strings of symbols count as well-formed formulas.
- A set of **axioms**: a distinguished set of well-formed formulas that are taken as given, as starting points for reasoning.
- A set of **inference rules**: mechanical rules that allow you to derive new well-formed formulas from ones you already have. Each inference rule has a finite number of premises and one conclusion, and the rule can be checked by a purely mechanical procedure.

A familiar example is **Peano arithmetic**, which formalizes the ordinary arithmetic of the natural numbers. Its alphabet includes symbols for 0, the successor function (representing “the next number”), addition, multiplication, equality, parentheses, and the logical connectives (“and”, “or”, “not”, “if...then”, “for all”). Its axioms include statements such as:

- 0 is not the successor of any number.
- If the successor of x equals the successor of y, then x equals y.
- x + 0 = x, and x + successor(y) = successor(x + y).
- x × 0 = 0, and x × successor(y) = (x × y) + x.
- The principle of mathematical induction: if a property holds for 0, and if whenever it holds for n it also holds for the successor of n, then it holds for all natural numbers.

From these axioms, using the inference rules (which allow substitution of equals for equals, the detachment rule known as *modus ponens*, and the introduction and elimination of quantifiers), you can prove a vast range of theorems about natural numbers.

A **proof** in a formal system is a finite sequence of formulas, each of which is either an axiom or follows from earlier formulas by one of the inference rules. A formula is **provable** if there exists a proof whose last line is that formula.

Now, two remarkable facts emerge about any formal system that is powerful enough to describe ordinary arithmetic and whose axioms are **recursively enumerable** (there is a mechanical procedure that will eventually list all the axioms, though the list may be infinite). These facts are not accidents of a particular construction. They are structural properties of formal reasoning itself.

**First fact: Incompleteness.** There are statements in the language of the formal system that are true—when interpreted as statements about the natural numbers, which the system is intended to describe—but cannot be proved within the system. The system does not capture all truths of arithmetic.

The argument for this is not a trick; it is a deep diagonalization. Within a formal system that can encode arithmetic, you can encode statements *about the system itself*. You can assign a unique numerical code (a “serial number”) to every formula and every proof. Then you can construct a formula that asserts, in effect, “There is no proof in this system of the formula with serial number $n$,” where $n$ is the serial number of that very formula. In other words, you can construct a formula that says “I am not provable in this system.”

If this formula were provable, then the system would have proved a statement that asserts its own unprovability. Since the system is assumed to be sound (it only proves truths), the formula would be both provable and true—but its truth would consist precisely in its being unprovable. This is a contradiction. Therefore the formula is not provable—which is exactly what the formula asserts. So the formula is true, but unprovable.

This is not a paradoxical self-reference like “this statement is false.” It is a constructive self-reference like “this statement is unprovable,” and the outcome is not a contradiction but a demonstration of a truth beyond the system’s reach.

**Second fact: No system can prove its own consistency.** A formal system is **consistent** if it does not prove a contradiction—that is, it never proves both a formula and its negation. The second remarkable fact is that if a formal system (of the kind described above) can prove its own consistency, then it is actually inconsistent. In a consistent system, the statement “the system is consistent” is itself one of the unprovable truths.

The consequence is that we can never use a formal system to certify its own reliability. To prove that Peano arithmetic is consistent, we must move to a stronger system—for instance, set theory. But set theory cannot prove its own consistency either. To prove set theory’s consistency, we must move to an even stronger system. And so on. There is no ultimate system that stands above the hierarchy and validates all the rest.

What does this mean for our thesis?

The boundary between “provable” and “unprovable” is relative to the formal system you are working in. There is no absolute notion of provability. A statement that is unprovable in one system may become provable in a stronger system. But the stronger system will have its own unprovable truths. The line between “we can prove this” and “we cannot prove this” shifts as we change our foundational commitments.

This is exactly the pattern we have seen in every domain. In number theory, what is prime depends on metric. In physics, what is elementary depends on energy scale. In algebra, what is symmetric depends on choice of closure. In geometry, what is a uniformizer depends on choice of coordinate. In category theory, what is indivisible depends on level. And now, in logic, what is provable depends on the formal system. The relativity of “indivisible” is, at bottom, a relativity of all judgement—a reflection of the fact that every determination of truth requires a framework, and every framework has its own blind spots.

---

## 4.6 Undecidability in Practice

The incompleteness described in the previous section concerns the limits of what can be *proved* from axioms. But even if a statement is provable or refutable in principle, there may be no mechanical procedure—no algorithm, no computer program—that can determine, for every possible input within a given class, whether the statement holds. This is the phenomenon of **undecidability**.

A **decision problem** is a question that can be asked about a whole family of inputs, each of which should receive a yes-or-no answer. The problem is **decidable** if there exists an algorithm that, given any input from the family, terminates after a finite number of steps and outputs the correct answer. The problem is **undecidable** if no such algorithm exists.

The classic undecidable problem is the **halting problem**. Consider a computer program written in some fixed programming language. The program takes an input string. The question: will this program eventually stop running on this input, or will it run forever?

One might hope to write a master analysis program—a “halt-checker”—that reads the code of any program P and any input I, and correctly answers whether P halts on I. But no such halt-checker can exist.

The argument is a beautiful diagonal construction. Suppose, for the sake of contradiction, that a halt-checker H exists. H takes two inputs: the source code of a program P, and an input string I. H(P, I) outputs “yes” if P halts on I, and “no” otherwise. Now construct a new program D that does the following: it reads a single input string X. Then it calls H(X, X)—asking the halt-checker whether the program whose code is X halts when given its own code as input. If H says “yes,” then D enters an infinite loop (so D does *not* halt). If H says “no,” then D immediately halts.

Now what happens when D is given its own source code as input? That is, we run D(D). If D halts on input D, then by construction H(D, D) must have said “no”—meaning H predicted that D would not halt on D. But D did halt. Contradiction. If D does not halt on input D, then H(D, D) must have said “yes”—meaning H predicted that D would halt on D. But D did not halt. Contradiction.

Therefore H cannot exist. The halting problem is undecidable. There is no algorithm that can analyse every program and every input and reliably predict whether the program will stop.

Now, the halting problem is not an isolated curiosity. It can be *embedded* into many natural mathematical questions. That is, the undecidability of the halting problem can be used to show that other problems are also undecidable: if you could solve the other problem algorithmically, you could solve the halting problem, which is impossible.

Here are several important examples:

- **The word problem for groups.** A group can be presented by specifying a set of generators and a set of relations—equations that the generators satisfy. A “word” is a finite product of generators and their inverses. The question: given two words, do they represent the same element of the group? For certain specific finitely presented groups, this problem is undecidable. There is no algorithm that can take any two words and determine whether they are equal in the group.

- **Tiling problems.** Given a finite set of polygonal tiles (say, squares with notched edges, like jigsaw puzzle pieces), can they tile the infinite plane without overlaps or gaps? For some sets of tiles, the answer is yes; for others, no. But there is no general algorithm that can decide, for any given set of tiles, whether it tiles the plane. The problem is undecidable.

- **The irreducibility of polynomials.** A polynomial with integer coefficients is **irreducible** if it cannot be factored into two non-constant polynomials with integer coefficients. For univariate polynomials (polynomials in one variable), there are algorithms that determine irreducibility—the problem is decidable. But for multivariate polynomials (polynomials in several variables) of sufficiently high degree, the problem is undecidable. There is no algorithm that can examine an arbitrary multivariate polynomial and reliably determine whether it is irreducible.

- **The membership problem for certain subrings.** Consider a ring—a set where you can add, subtract, and multiply. The question: given an element, is it a member of a specified subring? In certain rings, this problem is undecidable.

The last two examples are directly relevant to our central question. There are mathematical structures—rings of polynomials, for instance—where the question “is this element indivisible?” (i.e., irreducible) is algorithmically undecidable. There is no procedure that can examine an arbitrary element and reliably determine whether it can be factored further.

This means that the relativity of indivisibility has a final, practical dimension. Even if you fix a measurement context—choose a specific ring, a specific type, a specific formal system—the property of being indivisible may not be *effectively determinable* within that context. The limits of algorithmic reasoning impose a barrier on our ability to identify the “atoms” of a given world. Not only do we have to choose a context before asking the question; sometimes, even after all choices are made, there is no systematic way to obtain the answer.

---

## Coda: The Pattern Completed

We set out to examine a simple thesis: no entity is intrinsically indivisible. “Indivisible” always means “indivisible relative to a chosen measurement context.”

We began in the concrete world of numbers. Primes turned out to depend on the metric. The same number—2, 3, 5—appears as a prime in one p-adic world and as a unit in another. The adelic product formula showed that all metrics must be considered together, and that no single metric captures the whole truth. Rational numbers, we saw, have no privileged decomposition; they are not built from a fixed set of atoms.

We then looked at the physical world. Quasiparticles—phonons, anyons, magnons—taught us that “what something is made of” depends on the scale at which we probe it. The renormalization group showed that the laws of physics change with energy scale, and that the particles we call elementary are artifacts of the effective theory we happen to be using.

Now we have ascended to the level of logic and structure. We have found that the relativity of indivisibility is not a contingent feature of numbers or matter. It is woven into the fabric of systematic thought itself. The symmetries of the algebraic numbers require a choice of algebraic closure before they can even be defined. The adelic framework that unifies all metrics is itself built on arbitrary coordinate choices. The ladder of categories shows that “indivisible” means something different at every level. Different mathematical types, like the ordinary integers and the p-adic integers, have their own internal notions of primality that do not transfer between types. Formal systems, even the best we can construct, have blind spots: truths they cannot prove, and boundaries of provability that shift when we strengthen the system. And even within a fixed formal system, the question “is this indivisible?” may be algorithmically undecidable.

The thread that runs through all these observations is the same: **every judgement of atomicity requires a framework, and every framework is a choice.** There is no view from nowhere. There is no absolute prime, no absolute elementary particle, no absolute symmetry, no absolute categorical atom, no absolute proof. The line between the indivisible and the divisible is not a line drawn in nature. It is a line that we draw, with a specific tool, for a specific purpose, in a specific context—and sometimes, even with the best tools, the line cannot be drawn at all.

This is not a counsel of despair. It is an invitation to precision. When we say something is indivisible, we should always ask: *in what sense, under what operations, relative to what framework?* The question is the answer. Everything is divisible—if you choose the right lens. And the choice of lens is always ours.

---

# Part V: The Loop Closes—Self-Reference

## 5.1 The Argument Applied to Itself

We have arrived at a turning point. The thesis of this document is:

> No entity is intrinsically indivisible. “Indivisible” always means “indivisible relative to a chosen measurement context.”

This thesis has been illustrated in numbers, in matter, and in logical structure. But the thesis is itself an entity—a claim, a string of words, a piece of reasoning. If the thesis is true, it must apply to itself. So we must ask: is the claim “everything is divisible” itself divisible?

To answer, we must first recall what “divisible” means in the context of an argument. In Part I, we defined divisibility for numbers: a number $a$ divides a number $b$ if there exists a whole number $k$ such that $b = a \times k$. That definition was precise because numbers have a multiplication operation. An argument does not have multiplication. But it does have a structure: it can be broken into parts. So we extend the idea: an argument is *divisible* if it can be decomposed into distinct sub-arguments, each of which contributes to the whole, and none of which is identical to the whole.

Apply this to our thesis. The claim “everything is divisible” is not an atomic, indivisible assertion. It is a summary at the end of a chain of reasoning. We can decompose it into sub-claims:

- **Sub-claim about numbers** (Part II): Primality is metric-dependent. A number that is prime in ordinary arithmetic may be composite in another metric, and vice versa. The p-adic metrics reveal that “size” and “divisibility” are two different ways of measuring, and neither is privileged. The adelic product formula constrains them all.

- **Sub-claim about matter** (Part III): Elementary particles are scale-dependent. What counts as a fundamental constituent at one energy scale becomes a composite at another. Quasiparticles—patterns of collective motion—behave exactly like particles but are “made of” nothing but relationships. The renormalization group enforces consistency across scales.

- **Sub-claim about logic and structure** (Part IV): Even the most abstract frameworks require choices. Symmetries depend on a choice of algebraic closure. The notion of “prime” does not transfer between different mathematical types. Formal systems have intrinsic limits—there are truths they cannot prove, questions they cannot decide.

Each of these sub-claims can be further decomposed. The sub-claim about numbers breaks into claims about p-adic valuation, the product formula, and the basis problem. The claim about valuation breaks into definitions of absolute value, triangle inequality, and ultrametric inequality. The ultrametric inequality breaks into a statement about the relationship between addition and the p-adic size—a statement that can itself be proved by examining the prime factorization of sums.

And each of those pieces can be decomposed further. A definition is made of words. Each word has a meaning, which can be unpacked into a longer explanation. Each explanation uses more words, which themselves require definition. There is no atomic argument—no smallest unit of meaning that cannot be further analyzed.

This might seem like a weakness. If every claim depends on further claims, and those on further claims, does anything ever get established? The concern is ancient: if every statement requires justification, and justification requires further statements, then no statement can ever be finally justified. The chain of reasons would recede infinitely, and knowledge would be impossible.

But this concern assumes that justification must terminate—that there must be a bedrock of self-evident truths from which all else derives. Our thesis denies that such a bedrock exists. Not just for numbers or particles, but for arguments themselves. The argument is not weakened by its infinite decomposability. It is *characterized* by it. The document you are reading is, by its own thesis, an entity that has no final atomic parts.

---

## 5.2 The Infinite Regress

If we keep asking “and what is THAT made of?”—not about stones or quarks, but about the arguments we have built—where does it lead? Let us trace the regress in each of our three domains.

**In numbers.** We began with prime numbers—the building blocks of ordinary arithmetic. We asked: are primes truly indivisible? We found that primality depends on metric. But then we could ask: what is a metric made of? A metric is a function assigning a size to each number, satisfying certain axioms (positivity, multiplicativity, the triangle inequality). But what are functions? They are sets of ordered pairs. What are sets? They are the basic objects of a foundational theory. And what are the basic objects of THAT theory made of? The chain continues: p-adic metrics led us to p-adic numbers, to adeles, to the product formula. But the adeles are a particular construction within a larger subject called algebraic number theory. Algebraic number theory studies fields—sets closed under arithmetic—and their extensions. The symmetries of fields are groups. The representations of those groups are studied in a program that connects number theory to geometry. This program treats representations on an equal footing, without privileging any one. And the search for deeper unity leads to objects called motives—hypothetical building blocks for a conjectural “universal cohomology theory”—and beyond motives, to higher categories. At each stage, what looked fundamental turns out to be a shadow of a deeper structure. There is no indication that the ladder stops.

**In matter.** We began with stones and worked downward: crystals, molecules, atoms, nuclei, protons, quarks. At the quark level, we encountered confinement—the impossibility of isolating a quark. But we could still ask: what is a quark, as a theoretical entity? It is an excitation of a quantum field. What is a quantum field? A mathematical object assigning an operator to every point in spacetime. What is spacetime? In our best current theories, it is a smooth four-dimensional continuum. But at extremely small distances—the Planck length, roughly $10^{-35}$ meters—the smoothness of spacetime is expected to break down. The search for a theory of quantum gravity aims to describe what spacetime itself is “made of.” Candidates include strings, loops, causal sets, or non-commutative algebras. Each candidate pushes the question back: what is a string made of? What is a causal set made of? The regress continues.

**In logic.** We saw that any formal system powerful enough to describe ordinary arithmetic has limits: statements it cannot prove, its own consistency it cannot establish. But we can step outside any given system and examine it from a stronger system. That stronger system is itself a formal system. It too has limits. It cannot prove its own consistency. So we can step outside IT, to a meta-meta-system. The hierarchy of formal systems—each able to prove the consistency of the one below it, but not its own—appears unbounded. There is no “maximally powerful” formal system that contains all others and can prove everything true about arithmetic.

In all three domains, the regress is genuinely infinite. It is not a temporary limitation of our current knowledge. It is structural. The question “and what is THAT made of?” always has a coherent answer—but that answer invites the same question again. There is no final answer that silences the question.

Is this a vicious regress or a virtuous one?

A *vicious regress* is one that undermines the claim that set it in motion. If I claim “every statement must be justified by a more basic statement,” and that claim leads to an infinite chain of justifications, then my claim about justification can never be satisfied—and the claim refutes itself. A *virtuous regress* is one that reveals the structure of the subject matter without destroying it. If I claim “every physical object is composed of smaller parts,” and this leads to an infinite descent, the claim is not refuted; it is confirmed at every step. The infinite descent is the truth of the matter.

Our thesis is of the second kind. It does not say “there is a final atomic layer.” It says the opposite: there is no final atomic layer, and the attempt to find one always generates a new context. The infinite regress is not a bug; it is the feature. The argument demonstrates its own conclusion by exhibiting the very divisibility it asserts.

---

## 5.3 The Fixed Point

If the regress never hits bottom, is there anything that stays the same? Is there an invariant—something that does not change as we ask the question across different contexts?

The process itself is the invariant. The act of asking “what is it made of?”—of decomposing an entity into constituents relative to a chosen measurement—is the one thing that recurs at every level. The answer changes. The method of decomposition changes. But the *form of the question* remains.

This is a pattern we have seen repeatedly, in different guises. Each of our earlier domains contained a “loop”—a structure that returns to itself after ranging over all contexts. And each loop had a *coherence condition*: a global constraint that all the local contexts must satisfy together.

**The product formula** (Part II). For any rational number $x$, the ordinary size $\lvert x \rvert_\infty$ multiplied by the p-adic size $\lvert x \rvert_p$ for every prime $p$ gives exactly 1. This formula loops over all primes—over all possible p-adic measurement contexts—and returns a fixed value. The loop has no beginning and no privileged point: you can start at any prime, go through all of them, and end with the ordinary absolute value. The order does not matter. The constraint is global: the different local sizes are not independent; they must multiply to 1. This is a coherence condition on measurements.

**The renormalization group** (Part III). A physical system can be described at many energy scales. The renormalization group provides equations—the renormalization group flow—that connect the description at one scale to the description at another. If you start at a very high energy scale, with a particular set of effective degrees of freedom and interaction strengths, and you “flow down” by averaging out short-distance details, you eventually reach the low-energy effective description. The flow has fixed points—special descriptions that remain unchanged under rescaling. These fixed points describe systems with scale invariance: they look the same at all scales. But even away from fixed points, the flow is subject to a global constraint: the descriptions at different scales must be mutually consistent. You cannot change the high-energy theory without changing the low-energy predictions, and vice versa. The loop over energy scales has a coherence condition.

**Logical consistency** (Part IV). A formal system is a set of rules for deriving statements. The rules must not produce a contradiction—a statement and its negation both provable. This is the consistency condition. It is a global constraint on all possible derivations within the system. No individual derivation can be checked against it in isolation; it refers to the totality of what the system can prove. Moreover, a sufficiently strong system cannot prove its own consistency from within. The consistency condition can only be seen from outside—by moving to a stronger system. The loop of formal systems (each proving the consistency of the one below) has a coherence condition at each level, but the condition itself is relative to the next level.

Each of these is an instance of the same abstract pattern:

> A collection of local contexts, no one of which is privileged. A relation that connects them pairwise (change of metric, change of scale, change of formal system). A global constraint that all local contexts, taken together, must satisfy.

The pattern is a loop. It has no beginning and no end. You can enter at any point—any prime, any energy scale, any formal system—and traverse the entire circle. The coherence condition is what makes the loop a loop and not a disconnected collection of isolated perspectives. Without the product formula, the p-adic metrics would be separate worlds with no relation to ordinary size. Without the renormalization group, physics at different scales would be independent—and inconsistent. Without consistency conditions, a formal system would be useless—anything could be proved.

The invariant across all contexts is not a *thing*. It is the pattern of how different measurement contexts constrain one another. This is the fixed point: not a final substance, but a structure of relationships that recurs whenever we ask the question “what is it made of?” seriously and completely.

---

## 5.4 The Collapse

We can now state the deepest consequence of our thesis.

If every entity is divisible relative to some measurement context, and every measurement context is itself constructed (it can be further decomposed relative to another context), then there is no context that is not itself subject to the same question. There is no privileged “bottom” layer of reality—no layer of things whose nature is independent of all measurement.

This collapses a distinction that has structured much of human thought: the distinction between what a thing *is* (its intrinsic nature, its ontology) and how we *measure* or *know* it (our perspective, our epistemology). The distinction is often illustrated by the metaphor of a map and a territory. The map is our representation, our measurement. The territory is the thing itself, which exists independently and has its own definite properties. A good map corresponds to the territory; a bad map does not. The territory is the ultimate arbiter.

Our thesis implies that this metaphor is misleading. There is no territory independent of all maps. Every attempt to specify the territory uses a map—a particular measurement context, a particular set of concepts and distinctions. And that map can itself be mapped by another map. There is no map that is not also a territory relative to some more fine-grained description. And there is no territory that cannot be mapped—cannot be treated as a representation from some higher perspective.

This is not a claim that reality is a fiction or that “anything goes.” The global constraints we have identified—the product formula, the renormalization group, logical consistency—are real and binding. They are not optional. A description that violates them is false. But the constraints are constraints *on measurements*, not on a measurement-independent reality. They say: if you choose this metric, and this one, and this one, their values must multiply to 1. They do not say: the number 12 has an intrinsic size, and the metrics approximate it. The number 12 has no intrinsic size. Its size is always size-in-a-metric. The product formula relates sizes-in-different-metrics. It never mentions a metric-free size.

Similarly, the renormalization group does not say: there is a true, scale-independent description of the physical system, and the effective descriptions at various scales approximate it. It says: the descriptions at different scales constrain each other. The quark-level description and the atomic-level description are two different valid descriptions. Neither is the “true” one. They are different answers to different questions, and the renormalization group tells you how to translate between them.

In logic, consistency is a condition on a formal system. It says: this system must not prove a contradiction. It does not say: there is an absolute notion of truth, and the system approximates it. Different formal systems have different sets of provable statements. None is the “true” set. Each is a different measurement context for truth.

The ontic/epistemic distinction collapses into a single structure: a web of measurement contexts, each internally coherent, each related to others by translation rules, and all subject to global coherence conditions. What a thing “is” is nothing other than the totality of its behaviors across all possible measurement contexts, constrained by the requirement that those behaviors fit together. There is no fact of the matter apart from a chosen measurement. The measurement *is* the fact.

We can put it sharply: to ask what something “really” is, independent of all measurement, is to ask a question that has no meaning. It is like asking for the product of all sizes without specifying which metric—the question presupposes a context-free perspective that does not exist. The only meaningful questions are: “What is its size in this metric?” “What are its degrees of freedom at this scale?” “What is provable about it in this formal system?” And then: “How do the answers in different contexts relate to each other?”

---

# Part VI: Synthesis and Consequences

## 6.1 Mathematics and Physics Converge

The previous parts of this document have traced a single pattern through three domains that are normally kept separate: the theory of numbers, the study of matter, and the analysis of logical structure. Each domain was explored independently, using its own methods and its own characteristic questions. Yet at a structural level, they arrived at the same place.

In numbers: the property of being “indivisible” (prime) depends on which metric you choose. There is no metric-independent notion of primality. The p-adic metrics and the ordinary metric together form a balanced whole, governed by the product formula.

In matter: the property of being “elementary” (fundamental, not made of anything else) depends on the energy scale at which you probe. There is no scale-independent notion of elementarity. The effective descriptions at different scales together form a balanced whole, governed by the renormalization group.

This convergence is not an analogy. It is not a suggestive metaphor. It is a precise structural identity. Both domains exhibit:

- A **collection of local contexts** (metrics, scales), each of which provides a complete and internally consistent description.
- **No privileged context**: no metric is truer than any other; no scale is more fundamental than any other.
- **Translation rules** that connect descriptions in different contexts (change of metric, renormalization group flow).
- A **global coherence condition** that all local descriptions must jointly satisfy (the product formula, the mutual consistency of the renormalization group).

The language differs. In number theory, we speak of absolute values, valuations, completions, adeles. In physics, we speak of effective field theories, running couplings, relevant and irrelevant operators. But the underlying mathematical structure—a collection of local objects glued together by a global condition—is the same.

Why should this be? Why should the abstract study of whole numbers and the empirical study of matter converge on the same structural insight?

The answer, we suggest, is that both are studies of *measurement*. Number theory studies the measurement of divisibility and size. Physics studies the measurement of energy, momentum, and forces. Measurement always involves a choice: a choice of what to compare, a choice of what to treat as the standard. That choice creates a context. And wherever there are multiple contexts, the question of how they relate arises. The pattern we have identified—local contexts, no privilege, translation rules, global constraint—is the pattern of any coherent system of multiple measurements. It is the structure of measurement itself.

---

## 6.2 No Final Theory of Atoms

The history of both mathematics and physics is, in large part, a history of searching for atoms—for indivisible building blocks from which everything else derives. In mathematics: the prime numbers, the axioms of geometry, the foundations of set theory. In physics: the chemical elements, then the atoms, then the elementary particles, then the quantum fields. At each stage, the discovery that the supposed atoms were divisible was treated as progress—a step closer to the true bottom. The hope was that eventually we would reach a layer that could not be further divided, a set of ultimate constituents and ultimate laws from which all else follows.

This hope is still alive in contemporary research. The search for a “theory of everything” in physics aims to find the fundamental degrees of freedom and the fundamental equations that describe them, from which the entire universe—galaxies, stars, life, consciousness—would in principle be derivable. In mathematics, the search for “the field with one element” aims to find a hypothetical object that would stand to the integers as the integers stand to polynomial rings—an ultimate foundation for arithmetic.

But the pattern we have traced suggests that this hope is misplaced—not because the search is too difficult, but because it is misdirected. The striking fact about every successful “deepening” in the history of these subjects is that it did not find a bottom. It found a new way of relating existing contexts.

- The discovery of p-adic numbers did not reduce ordinary arithmetic to something simpler. It revealed that ordinary arithmetic is one among many equally valid metrics. The advance was not downward to a foundation; it was sideways, to a larger family of contexts and the relations among them.

- The discovery of quarks did not end the search for constituents. It revealed that protons and neutrons have internal structure, but it also introduced confinement—the impossibility of isolating those constituents. The advance was not to a final building block; it was to a new description that is valid at higher energies, and to the renormalization group that connects it to the lower-energy description.

- The discovery of undecidability did not find a perfect logical system. It showed that every sufficiently strong system has limits, and that the limit shifts when you move to a stronger system. The advance was not to a system without limits; it was to a precise understanding of the hierarchy of systems and the trade-offs involved in choosing one.

The search for a final theory of atoms consistently succeeds not by reaching an absolute bottom, but by formalizing the *relativity of context*. The “field with one element” does not exist as a literal field; it is a guiding idea that organizes a web of analogies between different number systems. The Langlands program—the vast effort to connect number theory and geometry—does not reduce one to the other. It establishes correspondences: ways of translating statements between the two domains, without claiming that either is more fundamental.

Non-commutative geometry provides a particularly clear example. In ordinary geometry, a space is a set of points. The points are the indivisible atoms of the space. But at very small distances—near the Planck scale—the notion of a point breaks down. Non-commutative geometry replaces the algebra of functions on a space (which encodes the space’s structure) with a non-commutative algebra—an algebra where the order of multiplication matters. In this framework, there are no points. Instead, there are “states”—assignments of values to observables. A state is not a location; it is a particular pattern of measurement outcomes. The geometry is not built from indivisible points; it is built from relationships among possible measurements.

All these developments share a common feature: they abandon the search for absolute atoms and instead formalize the relationships between different contexts. They succeed not by answering the question “what is it made of?” once and for all, but by showing that the question itself is context-dependent and that the interesting structure lies in how the answers in different contexts constrain each other.

---

## 6.3 The Only Absolute Is Relativity Itself

If there is no privileged measurement context, no bottom layer, no ultimate atoms, then what—if anything—is absolute?

The history of thought often moves by identifying a new relativity and then discovering a new absolute behind it. The discovery that motion is relative (there is no absolute rest) led to the absolute speed of light. The discovery that simultaneity is relative led to the absolute structure of spacetime. In each case, what was lost as an absolute property of objects was recovered as an absolute structure of relationships.

Our thesis suggests a similar move, but with a crucial difference. The absolute we have found is not a *thing*—not a substance, not a field, not a law of nature, not a set of axioms. It is a *pattern*: the pattern of how different measurement contexts constrain one another. This pattern appears, as we have seen, as the product formula in number theory, as the renormalization group in physics, as the consistency conditions and the hierarchy of formal systems in logic. In the abstract language of category theory, it appears as *universal properties*—specifications of an object not by what it is made of, but by how it relates to all other objects of a certain kind.

The pattern can be described abstractly:

1. There is a family of local contexts (metrics, scales, systems).
2. No context is privileged.
3. There are rules for translating between contexts.
4. There is a global consistency condition that all contexts, taken together, must satisfy.

This pattern is relational through and through. It makes no reference to anything outside the family of contexts. The contexts are defined by their internal structure and by their relationships to other contexts. The global condition is a condition on those relationships. There is no “outside”—no vantage point from which the whole pattern can be seen as an object, independent of any particular context.

In this sense, the absolute is not a foundation. It is a *coherence requirement*. It does not ground the structure from below; it binds the structure from within. It says: if you adopt these local perspectives, they must fit together in this way. But it does not compel you to adopt any particular set of perspectives, and it does not exist independently of the perspectives it binds.

This is a subtle idea. Let us approach it by analogy. Consider a language. A language has words, grammar rules, and conventions of use. There is no “absolute” English—no Platonic form of the language that exists independently of all speakers. Yet English is not arbitrary. There are rules that speakers follow, and those rules can be studied and described. The rules are not imposed from outside; they emerge from the practice of speaking and writing. They are real constraints, but they are constraints *of* the practice, not constraints *on* the practice from some external authority.

Our pattern—local contexts with a global coherence condition—is like the grammar of measurement. It is not imposed by a measurement-independent reality. It is the structural requirement that any family of measurements must satisfy to be mutually interpretable. The requirement is real and binding. A family of metrics that violated the product formula would not correspond to any coherent notion of number. A family of effective theories that violated the renormalization group would not describe a consistent physical world. But the requirement does not refer to anything outside the family. It is the condition for the family to hang together as a family.

Thus the only absolute is relativity itself—not relativity as a doctrine that “everything is relative,” but relativity as a *structure*: the structure of how contexts relate, how perspectives translate, how measurements constrain one another. This structure is not a thing among things. It is the form of coherence itself.

---

## 6.4 The Performative Close

A document that makes a claim should be examined to see whether it exemplifies its own claim. If this document asserts that every entity is divisible, that no argument has an atomic core, that the process of decomposition has no end—then the document itself should exhibit these properties. Otherwise it would be a counterexample to itself.

And so it does. This document is not a linear chain of reasoning that starts from self-evident premises and proceeds step by step to an inescapable conclusion. It is a web. Each section refers to others. The Prologue gestures forward to the Product Formula; Part V loops back to Part I; Part VII opens questions that re-examine the Prologue. You can read the document in any order. You can start with the physical analogy and then ask what it has to do with numbers. You can start with the undecidability results and then wonder how they connect to quasiparticles. The connections are there, but they are not linear. They form a network.

Each section is divisible into subsections. Each section has a title and a sequence of paragraphs. The titles could be different; the paragraphs could be reordered; the examples could be replaced. The argument has no unique decomposition. There is no single, canonical way to break it into parts.

Each definition uses words that themselves require definition. Consider the first sentence of Part I: “Before we can ask whether anything is truly indivisible, we must say precisely what we mean by ‘divisible.’” To define “divisible,” we used words like “number,” “integer,” “factor.” Each of those words can be defined—and was defined, in context. But those definitions use still more words. If you insisted on defining every word before using it, you would never finish the first paragraph. The document does not attempt to build from an absolutely primitive vocabulary. It starts in the middle, with words the reader is assumed to understand, and it refines their meanings as it goes. This is not a flaw. It is the only way language works. There are no absolutely primitive words.

Even the central thesis—“everything is divisible”—is itself a string of words. The word “everything” is a quantifier; its meaning depends on the domain of discourse. The word “divisible” we have struggled to define across contexts. The word “is” is the copula, whose logic has been debated for millennia. The thesis does not stand outside the web of language. It is a node in the web.

The act of reading this document is the act of traversing a loop. You can stop at any point. When you finish Part VII, you can close the book and consider the matter concluded. But the loop continues whether you follow it or not. The questions at the end are genuine. The regress does not halt because you stop reading. The document is, by its own nature, unfinished—because any claim in it can be further analyzed, any definition further unpacked, any connection further explored.

This is not a failure of the argument. It is the argument’s enactment. The document does not merely state that everything is divisible; it *performs* divisibility. It is itself an instance of the pattern it describes. And in this, it is no different from any other text, or any other object of thought. Every text is divisible into paragraphs, sentences, words, letters, ink, paper, molecules, atoms. Every idea is divisible into sub-ideas, assumptions, implications, examples. The document is not special. It is just unusually explicit about its own structure.

The question “is the argument finished?” has no answer, because the argument’s nature is to be unfinished—to always admit further decomposition. Every ending is a choice of where to stop. This ending is a choice. The next part, by convention the last, is not a conclusion. It is an opening.

---

# Part VII: Open Questions

A document that claims nothing is final should not end with finality. It should end with questions—genuine questions, whose answers are not known and whose pursuit continues the trajectory of the work. Here are five such questions.

---

## 7.1 Can the Product Formula Be Generalized?

The adelic product formula states that for any rational number, the product of its size in all completions equals 1. This formula unifies the ordinary metric and all p-adic metrics. But as we noted in Part V, the adeles are themselves a construction that rests on deeper structures—motives, higher categories, and conjectural objects that aim to capture the “essence” of algebraic varieties.

A natural question is: does the product formula generalize to these deeper levels? Is there a “motivic product formula”—a global constraint relating the local factors of a motive at all places, including the archimedean place and all finite primes? If so, what would such a formula mean? Would it involve new kinds of “places” beyond the usual primes—perhaps places associated with higher-dimensional representations?

More generally: the product formula is an instance of a local-to-global principle. In many areas of mathematics, a property holds globally if and only if it holds locally at every place. But the local-to-global principle does not always hold—it fails for certain cubic curves, for example. Understanding when it holds and when it fails is a central theme of modern number theory. Is the product formula itself a special case of a deeper local-to-global principle, one that applies to structures we have not yet fully formalized?

---

## 7.2 Does the Basis Problem Have a Physical Analog?

In Part II, we proved that the rational numbers have no basis over the integers. There is no finite set of rational numbers from which all others can be built by integer combinations. The rationals are “infinitely divisible” over the integers: any rational can be divided by any non-zero integer, yielding another rational. This structural fact—the absence of atomic building blocks—is a precise mathematical expression of the idea that “there is no bottom.”

Does this have a physical analog? The question of whether spacetime is fundamentally discrete or continuous is one of the oldest in physics. If spacetime is discrete, there would be a smallest possible length—an indivisible atom of space. If it is continuous, arbitrarily small distances are possible.

But perhaps the situation is more subtle. The rational numbers are neither a discrete set of isolated points (like the integers) nor a continuum (like the real numbers). They are dense—between any two rationals there is another rational—yet they have no basis. Could physical spacetime be analogous? Could it be “divisible” in the sense that there is no smallest length, yet not a smooth continuum in the usual sense? The mathematical structure of the rationals as a divisible module might provide a model for a kind of spacetime that is not atomic but also not continuous—a space where you can always zoom in further, but where the zooming never reveals a final indivisible unit.

---

## 7.3 Univalence and Undecidability: A Hidden Connection?

In Part IV, we discussed the principle of univalence: equivalent structures should be treated as identical. In the language of type theory, this means that if two objects are isomorphic, there is a path (an equivalence) between them, and this path allows us to transport properties and constructions from one to the other. Univalence encodes the idea that *representation should not matter*—only structure matters.

But we also saw that formal systems have intrinsic limits: undecidable questions, unprovable truths. These limits arise from the capacity of a system to encode statements that refer to themselves—to represent their own syntax internally.

Is there a connection? Both univalence and undecidability involve the relationship between a thing and its representation. Univalence says that different representations of the same structure are interchangeable. Undecidability says that some questions about a representation cannot be answered from within the system that uses that representation.

Could it be that univalence, pushed to its extreme, encounters a limit analogous to undecidability? If we treat all equivalent structures as identical, we collapse the distinction between an object and its representation. But some representations—those that involve self-reference—may resist this collapse. A formal system that can represent itself cannot fully “univalentize” that representation without paradox. Exploring this tension might shed light on both univalence and the limits of formal systems.

---

## 7.4 Is There a Maximally Powerful Formal System?

We have seen that any sufficiently strong formal system cannot prove its own consistency. A stronger system can prove the consistency of a weaker one. This suggests a hierarchy: system S₀, system S₁ that proves Con(S₀), system S₂ that proves Con(S₁), and so on. This hierarchy can be extended into the transfinite—the theory of ordinal numbers provides ways to iterate consistency assertions far beyond the finite.

But does the hierarchy have a summit? Is there a formal system that is “maximally powerful”—a system that can prove every true statement about the natural numbers? The incompleteness phenomena suggest that the answer is no: for any system, there is a stronger one. The hierarchy is unbounded.

Yet this answer raises further questions. If the hierarchy is unbounded, does it have a well-defined “limit”—a single structure that somehow encompasses all systems? This is related to the question of whether there is an “absolute” notion of provability that transcends any particular formal system. Some logicians have explored notions of “provability in all reasonable systems” or “truth in the intended model of arithmetic.” But these notions are themselves subject to the same kind of relativity: they can only be defined from a particular meta-theoretic standpoint.

The geometry of the space of all formal systems—how they relate, which ones extend which, where consistency strength increases—is an active area of research. It is not known whether the hierarchy of consistency strengths is well-ordered (whether there are no infinite descending chains of stronger and stronger systems), and what the “global structure” of this hierarchy looks like.

---

## 7.5 What Is the Status of the Claim “Everything Is Divisible”?

This is the most reflexive of our questions. We have spent many pages arguing that no entity is intrinsically indivisible, that divisibility is always relative to a measurement context, that the ontic/epistemic distinction collapses. But what kind of claim is this?

Is it a **theorem**? If so, in what formal system is it proved? It cannot be a theorem of ordinary arithmetic, because its subject matter includes the interpretation of formal systems themselves—it is a meta-mathematical claim. It might be formalizable in a sufficiently strong system of type theory or category theory. But then that system would itself have limits, and the claim would be relative to the system.

Is it a **philosophical principle**? If so, on what grounds should it be accepted? It cannot be accepted on the grounds that it is self-evident, because it denies the existence of self-evident foundations. It cannot be accepted as the conclusion of a decisive argument, because it asserts that no argument has a decisive, atomic core. It seems to undermine the very notion of a philosophical principle that commands assent by its own intrinsic clarity.

Is it a **performative act**? The document enacts its thesis: it is infinitely divisible, it has no atomic core, it loops back on itself. Perhaps the claim is not a proposition to be evaluated as true or false, but a practice to be engaged in—a way of reading, a way of questioning, a way of refusing to accept that any stopping point is final.

And crucially: does the claim apply to itself? If “everything is divisible” is true, then the claim itself is divisible—it can be decomposed, analyzed, broken into sub-claims, none of which is atomic. But if the claim is divisible, what is it divisible *into*? The sub-claims we enumerated at the start of Part V. And those sub-claims are themselves divisible. And so on. The claim does not ground itself; it dissolves itself.

If the claim does NOT apply to itself—if it claims a special status, an indivisible truth—then it contradicts its own content. It would be an exception to the rule it states, and the rule would be false (or at least, not universally true). So the claim must apply to itself. But self-application leads to the regress we have traced. The claim forces an infinite process of decomposition.

This is not a refutation. It is a confirmation. The claim “everything is divisible” is true precisely because it cannot be stated as a final, atomic truth. Its truth consists in the fact that it opens a process that has no end. To assert it is to begin questioning. To accept it is to accept that the questioning will never stop.

The document you hold is not a container of finished truths. It is an instrument for a particular kind of thinking—a thinking that refuses the comfort of final foundations and learns to navigate the web of contexts, guided by the coherence conditions that bind them. The last word is not an answer. It is an invitation.

---

*End of Parts I through VII.*