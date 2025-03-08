# The Birthday Problem

The Birthday Problem is a classic probability puzzle that asks:  

**What is the probability that, in a group of $n$ people, at least two people share the same birthday?**

![Probability of Sahred Birthday](images/birthday-P(n).png)

Surprisingly, the probability is much higher than most people intuitively expect. Below, we’ll break down the problem and derive the solution step by step, explaining each equation in detail.

---

## Key Assumptions
1. There are 365 days in a year (ignoring leap years).
2. Birthdays are equally likely to occur on any day of the year.
3. The birthdays of individuals are independent of each other.

---
## Steps
### Step 1: Define the Problem
We want to calculate the probability $P(n)$ that at least two people in a group of $n$ share the same birthday. Instead of calculating this directly, it’s easier to calculate the complementary probability $P(\text{no shared birthdays})$ and then subtract it from 1.

Thus: 

$$
P(n) = 1 - P(\text{no shared birthdays}). 
$$


### Step 2: Calculate $P(\text{no shared birthdays})$
The probability that no two people share a birthday can be calculated as follows:  

1. The first person can have any birthday, so there are 365 possible choices out of 365:  

$$
\frac{365}{365} = 1. 
$$  


3. The second person must have a birthday different from the first person. There are 364 remaining choices:

$$ 
\frac{364}{365}.
$$ 

4. The third person must have a birthday different from the first two. There are 363 remaining choices:

$$ 
\frac{363}{365}.
$$ 

6. This pattern continues until the $n$-th person, who must have a birthday different from the first $n-1$ people. There are $365 - (n-1)$ remaining choices:

$$ 
\frac{365 - (n-1)}{365}.
$$ 

Since the birthdays are independent, we multiply these probabilities together to get the overall probability that no two people share a birthday:

$$ 
P(\text{no shared birthdays}) = \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365 - (n-1)}{365}.
$$ 

This can be written more compactly using factorial notation:

$$ 
P(\text{no shared birthdays}) = \frac{365!}{(365-n)! \cdot 365^n}.
$$ 


### Step 3: Calculate $P(n)$
Using the complementary probability, the probability that at least two people **share** a birthday is:

$$ 
P(n) = 1 - \frac{365!}{(365-n)! \cdot 365^n}.
$$ 


### Step 4: Simplify the Expression
For large $n$, calculating factorials directly can be computationally intensive. Instead, we can use an approximation. Recall that:

$$ 
\ln(P(\text{no shared birthdays})) = \ln\left(\frac{365!}{(365-n)! \cdot 365^n}\right).
$$ 

Using properties of logarithms and Stirling’s approximation, we can approximate the probability as:

$$ 
P(n) \approx 1 - e^{-\frac{n(n-1)}{2 \cdot 365}}.
$$ 

This approximation is particularly useful for large \( n \).


### Step 5: Solve for Specific Values of $n$
Let’s calculate $P(n)$ for some specific values of $n$:

1. For $n = 23$:

$$
P(23) = 1 - \frac{365!}{(365-23)! \cdot 365^{23}} \approx 0.507.
$$ 

This means there’s a 50.7% chance that at least two people in a group of 23 share a birthday.

2. For $n = 50$:

$$ 
P(50) \approx 0.970.
$$ 
   
The probability rises to 97% for a group of 50.

3. For $n = 70$:

$$ 
P(70) \approx 0.999.
$$ 

The probability is nearly 100% for a group of 70.

---

### Step 6: Generalization
The Birthday Problem can be generalized to other scenarios, such as:
- The probability of shared birthdays in a year with $D$ days (e.g., $D = 366$ for leap years).
- The probability of shared events in other contexts (e.g., shared hashes in cryptography).

The general formula becomes:

$$ 
P(n) = 1 - \frac{D!}{(D-n)! \cdot D^n}.
$$ 

---

## Summary
The Birthday Problem demonstrates how probabilities can defy intuition. Even though there are 365 days in a year, it only takes 23 people for the probability of a shared birthday to exceed 50%. This result has important implications in fields like cryptography, hashing algorithms, and risk analysis.

---
---

# Appendix: Stirling’s approximation

This will explain how we arrive at:

$$
P(n) \approx 1 - e^{-\frac{n(n-1)}{2 \cdot 365}}.
$$

---
## Steps 

### Step 1: Start with $P(\text{no shared birthdays})$
The probability that no two people share a birthday in a group of $n$ is:

$$
P(\text{no shared birthdays}) = \frac{365!}{(365-n)! \cdot 365^n}.
$$

Taking the natural logarithm of both sides:

$$
\ln(P(\text{no shared birthdays})) = \ln\left(\frac{365!}{(365-n)! \cdot 365^n}\right).
$$

 

### Step 2: Simplify Using Properties of Logarithms
Using the properties of logarithms, we can rewrite the right-hand side as:

$$
\ln\left(\frac{365!}{(365-n)! \cdot 365^n}\right) = \ln(365!) - \ln((365-n)!) - \ln(365^n).
$$

Simplify further:

$$
\ln(365!) - \ln((365-n)!) - n \ln(365).
$$

 

### Step 3: Apply Stirling’s Approximation
Stirling’s approximation states that for large $x$:

$$
\ln(x!) \approx x \ln(x) - x.
$$

Apply this to $\ln(365!)$ and $\ln((365-n)!)$:

1. For $\ln(365!)$:
   
$$
\ln(365!) \approx 365 \ln(365) - 365.
$$

3. For $\ln((365-n)!)$:

$$
\ln((365-n)!) \approx (365-n) \ln(365-n) - (365-n).
$$

Substitute these into the expression:

$$
\ln(P(\text{no shared birthdays})) \approx \left[365 \ln(365) - 365\right] - \left[(365-n) \ln(365-n) - (365-n)\right] - n \ln(365).
$$

 

### Step 4: Simplify the Expression
Expand and simplify the terms:

$$
\ln(P(\text{no shared birthdays})) \approx 365 \ln(365) - 365 - (365-n) \ln(365-n) + (365-n) - n \ln(365).
$$

Combine like terms:

$$
\ln(P(\text{no shared birthdays})) \approx 365 \ln(365) - n \ln(365) - (365-n) \ln(365-n) - n.
$$

Factor out $\ln(365)$ from the first two terms:

$$
\ln(P(\text{no shared birthdays})) \approx (365 - n) \ln(365) - (365-n) \ln(365-n) - n.
$$

 

### Step 5: Approximate $\ln(365-n)$

The Taylor series expansion of $\ln(1 - x)$ around $x = 0$ is:

$$
\ln(1 - x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \cdots
$$

For small $x$ (i.e., $|x| \ll 1$), the higher-order terms ($x^2, x^3, \dots$) become negligible, so we can approximate:

$$
\ln(1 - x) \approx -x
$$

For small $n$ relative to 365, we can use the approximation (Taylor Series Expansion):

Rewrite $365 - n$ as:

$$
365 - n = 365 \left(1 - \frac{n}{365}\right)
$$

Now, take the natural logarithm of both sides:

$$
\ln(365 - n) = \ln\left(365 \left(1 - \frac{n}{365}\right)\right)
$$

Using the property of logarithms, $\ln(ab) = \ln(a) + \ln(b)$ and using the Taylor series expansion $\ln(1 - x) \approx -x$, this becomes:

$$
\ln(365 - n) = \ln(365) + \ln\left(1 - \frac{n}{365}\right)
$$

$$
\ln(365-n) \approx \ln(365) - \frac{n}{365}.
$$

Substitute this into the expression:

$$
\ln(P(\text{no shared birthdays})) \approx (365-n) \ln(365) - (365-n) \left(\ln(365) - \frac{n}{365}\right) - n.
$$

Simplify:

$$
\ln(P(\text{no shared birthdays})) \approx (365-n) \ln(365) - (365-n) \ln(365) + \frac{(365-n)n}{365} - n.
$$

The $(365-n) \ln(365)$ terms cancel out:

$$
\ln(P(\text{no shared birthdays})) \approx \frac{(365-n)n}{365} - n.
$$

Factor out $n$:

$$
\ln(P(\text{no shared birthdays})) \approx n \left(\frac{365-n}{365} - 1\right).
$$

Simplify the term inside the parentheses:

$$
\frac{365-n}{365} - 1 = \frac{365-n - 365}{365} = \frac{-n}{365}.
$$

Thus:

$$
\ln(P(\text{no shared birthdays})) \approx n \left(-\frac{n}{365}\right) = -\frac{n^2}{365}.
$$

 

### Step 6: Exponentiate to Find $P(\text{no shared birthdays})$
Exponentiate both sides to solve for $P(\text{no shared birthdays})$:

$$
P(\text{no shared birthdays}) \approx e^{-\frac{n^2}{365}}.
$$

 

### Step 7: Refine the Approximation
A more accurate approximation accounts for the fact that the number of unique pairs of people in a group of $n$ is $\frac{n(n-1)}{2}$, not $n^2$. Thus, we refine the exponent:

$$
P(\text{no shared birthdays}) \approx e^{-\frac{n(n-1)}{2 \cdot 365}}.
$$


### Step 8: Compute $P(n)$
Finally, the probability that at least two people share a birthday is:

$$
P(n) = 1 - P(\text{no shared birthdays}).
$$

Substitute the approximation:

$$
P(n) \approx 1 - e^{-\frac{n(n-1)}{2 \cdot 365}}.
$$

---

## Summary
Using properties of logarithms and Stirling’s approximation, we derived the approximation:

$$ 
P(n) \approx 1 - e^{-\frac{n(n-1)}{2 \cdot 365}}.
$$ 

This formula is particularly useful for calculating the probability of shared birthdays without computing large factorials directly. For example, when $n = 23$:

$$
P(23) \approx 1 - e^{-\frac{23 \cdot 22}{2 \cdot 365}} \approx 1 - e^{-0.693} \approx 1 - 0.500 \approx 0.500.
$$

This matches the exact result of approximately **50.7%**.
