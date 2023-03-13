# NFA & DFA parser - Python

This Python script implements a way to create an DFA/NFA, distinguish between the two, and allows for words to be parsed by said automaton.
  
## I/O 

### Input

By passing the file name to the automata file as a string to the *readAutomat()* method, and by passing the file name of the word list to the *readCuvinte()* method. Do mind that a void line will be interpreted as the null word (λ).

Another feature of this script is the automatic evaluation and detection of undefined characters/states. If the state transitions have undefined characters/states, a ValueError will be raised.

### Output

By passing the file name to the output file as a string to the *checkWords()* method. If no string is passed, only console output will be given.

## Automata file structure

defined states

sigma (alphabet)

state1 symbol state2

list of initial states

list of final states

## Example of input files

***input automat.txt***

``` python
q0 q1 q2 q3
012
q0 1 q0
q0 0 q1
q1 1 q0
q1 0 q2
q2 2 q3
q0
q1 q3
```

***input cuvinte.txt***

``` python
110001010
110101002
10101010

```

## Example of output files

``` python
Automatul acesta NU este finit pentru cuvantul 110001010!
Automatul acesta este finit pentru cuvantul 110101002!
Drumurile cu care ajungem in stare finita sunt:
q0 q0 q0 q1 q0 q1 q0 q1 q2 q3 
Automatul acesta este finit pentru cuvantul 10101010!
Drumurile cu care ajungem in stare finita sunt:
q0 q0 q1 q0 q1 q0 q1 q0 q1 
Automatul acesta NU este finit pentru cuvantul λ!
```
