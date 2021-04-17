# ==============================================================================
#
# MUSIQu.py
# Author: Kangrui Xue
# WARNING: code is outdated (from Freshman year) -- needs refactoring
#
# ==============================================================================

from Tkinter import *
from tkFileDialog import askopenfilename
import copy

def hadamard(q):
    for i in range(0, len(states)):
        states[i] = states[i] + H(q)
def pauliX(q):
    for i in range(0, len(states)):
        states[i] = states[i] + X(q)
def pauliY(q):
    for i in range(0, len(states)):
        states[i] = states[i] + Y(q)
def pauliZ(q):
    for i in range(0, len(states)):
        states[i] = states[i] + Z(q)

# ==============================================================================
from math import pi
# quantum fourier transform implementation
def QFT(q0, q1, q2):
    for i in range(0, len(states)):
        states[i] = states[i] + Program().inst(H(q2), CPHASE(pi/2.0, q1, q2), H(q1),
            CPHASE(pi/4.0, q0, q2), CPHASE(pi/2.0, q0, q1), H(q0), SWAP(q0, q2) )
def reset():
    for i in range(0, len(states)):
        states[i] = backup[i]

# ==============================================================================
# read initial qubit states from text file
def getFile(f):
    del states[:]
    del rhythm[:]
    file = open(askopenfilename(), "r")
    for line in file:
        p = Program()
        p.inst(I(0)) if line[2] == "0" else p.inst(X(0))
        p.inst(I(1)) if line[1] == "0" else p.inst(X(1))
        p.inst(I(2)) if line[0] == "0" else p.inst(X(2))
        rhythm.append(float(line[4:])) if len(line) >= 5 else rhythm.append(1)
        states.append(p)
    for i in range(0, len(states)):
        backup.append(copy.deepcopy(states[i]))

# ==============================================================================
def run():
    # calculates probabilities after qubit operations
    coefs = []
    for i in range(0, len(states)):
        coefs.append(qvm.wavefunction( states[i] ).amplitudes)
    probs = np.square(np.abs(coefs))
    print(probs)
    playAudio(probs)

# ==============================================================================
def playAudio(volume):
    import pyaudio
    audio = pyaudio.PyAudio()
    fs = 44100    # sampling rate, Hz, must be integer
    tempo = 2.0   # quarter note length, float
    stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    notes = []
    for i in range (0, len(states)):
        n = []   # superposition of musical notes to represent qubit states
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*261.63/fs)).astype(np.float32))
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*329.63/fs)).astype(np.float32))
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*392.00/fs)).astype(np.float32))
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*493.88/fs)).astype(np.float32))
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*293.66/fs)).astype(np.float32))
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*349.23/fs)).astype(np.float32))
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*440.00/fs)).astype(np.float32))
        n.append((np.sin(2*np.pi*np.arange(fs*tempo*rhythm[i])*523.25/fs)).astype(np.float32))
        notes.append(n)

    for i in range(0, len(states)): # loops through all qubits
        stream.write(volume[i][0]*notes[i][0] + volume[i][1]*notes[i][1] + volume[i][2]*notes[i][2] + volume[i][3]*notes[i][3]
                     + volume[i][4]*notes[i][4] + volume[i][5]*notes[i][5] + volume[i][6]*notes[i][6] + volume[i][7]*notes[i][7])
        # adds brief pause between notes for improved clarity
        stream.write(0*(np.sin(2*np.pi*np.arange(fs*tempo*0.1)/fs)).astype(np.float32))

    stream.stop_stream()
    stream.close()
    audio.terminate()

# ==============================================================================
from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import I, X, Y, Z, H, CPHASE, CNOT, SWAP, MEASURE
import numpy as np

qvm = QVMConnection()
states = []
rhythm = []
backup = []

window = Tk()
window.title("MUSIQu")
window.configure(background="white")

Button(window, text="Select File", width=10, command=lambda:getFile("")).grid(row=0, columnspan=5)

Label (window, text="q[0]:", fg="black", font="none 12 bold").grid(row=1, column=0)
Button(window, text="X", width=3, command=lambda:pauliX(0)).grid(row=1, column=1)
Button(window, text="Y", width=3, command=lambda:pauliY(0)).grid(row=1, column=2)
Button(window, text="Z", width=3, command=lambda:pauliZ(0)).grid(row=1, column=3)
Button(window, text="H", width=3, command=lambda:hadamard(0)).grid(row=1, column=4)

Label (window, text="q[1]:", fg="black", font="none 12 bold").grid(row=2, column=0)
Button(window, text="X", width=3, command=lambda:pauliX(1)).grid(row=2, column=1)
Button(window, text="Y", width=3, command=lambda:pauliY(1)).grid(row=2, column=2)
Button(window, text="Z", width=3, command=lambda:pauliZ(1)).grid(row=2, column=3)
Button(window, text="H", width=3, command=lambda:hadamard(1)).grid(row=2, column=4)

Label (window, text="q[2]:", fg="black", font="none 12 bold").grid(row=3, column=0)
Button(window, text="X", width=3, command=lambda:pauliX(2)).grid(row=3, column=1)
Button(window, text="Y", width=3, command=lambda:pauliY(2)).grid(row=3, column=2)
Button(window, text="Z", width=3, command=lambda:pauliZ(2)).grid(row=3, column=3)
Button(window, text="H", width=3, command=lambda:hadamard(2)).grid(row=3, column=4)

Button(window, text="QFT", width=5, command=lambda:QFT(0,1,2)).grid(row=4, column=0, columnspan=2)
Button(window, text="Reset", width=10, command=reset).grid(row=4, column=2, columnspan=3)

Button(window, text="Run", width=10, command=run).grid(row=5, columnspan=5)

window.mainloop()
