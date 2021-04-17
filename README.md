# MUSIQu
(Final project for PHYSICS 14N: Quantum Information: Visions and Emerging Technologies, Introductory Seminar 2018)

### What is MUSIQu?
- A qubit exists in a superposition of states
- Similarly, a musical chord is a superposition of different notes

MUSIQu aims to represent quantum computing in the *context of music*

**Purpose:** to present quantum computing in a unique, engaging, and potentially artistic way -- allows users to physically *hear* the effects of qubit operations

### How it Works: Musical Mappings
<img src=/Misc/musical_mappings.png alt="Musical Mappings" width="600"/>

**Consider the qubit:** q = 0.5 |000> + 0.5 |001> + 0.5 |010> + 0.5 |011>   

This maps to  C4, E4, G4, and B4 (Cmaj7 chord) - all played with equal volume

### Using the Program
First, run MUSIQu as a Python program. The following interface should pop up:
<img src=/Misc/interface_instructions.png alt="Interface Instructions" width="600"/>

Text File Input:
- Each line represents a single qubit -- supports any number of lines
- Format: three numbers (either 0 or 1) encoding the qubit, followed by a space, and then an optional number denoting the note duration (default value is 1.0, or quarter note). Ex: 001 0.5 ( |001>, eighth note)  
- For reference, example .txt files are provided

### A Few Quick Tips
- To play chords, qubits must exist in a superposition of states. This can be done through applying various Hadamard or quantum Fourier transforms
- Rhythms are for musical purposes only and do not correlate to the qubits
