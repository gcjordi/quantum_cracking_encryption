[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) [![made-with-jupyter](https://img.shields.io/badge/Made%20with-Jupyter-1f425f.svg)](http://jupyter.org/) [![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-gcjordi-blue.svg)](https://www.linkedin.com/in/gcjordi/)

# Shor-s-Algorithm_Quantum

A few months we had implemented RSA encryption from scratch with tweakable security parameters. This is a practical implementation of Shor's Algorithm to break our RSA encryption layer.

Shor’s algorithm was invented for integer factorization in 1994.  This algorithm is based on quantum computing and hence referred to as a quantum algorithm. The algorithm finds the prime factors of an integer P. Shor’s algorithm executes in polynomial time which is of the order polynomial in log N. On a classical computer,  it takes the execution time of the order O((log N)3).

We made use of IBM's Quantum Experience Qiskit module in jupyternotebook for designing the quantum circuit that works on qubits instead of the traditional bits.

Qiskit is an open-source quantum computing software development framework for leveraging today's quantum processors in research, education, and business.

If a quantum computer with a sufficient number of qubits could operate without succumbing to quantum noise and other quantum-decoherence phenomena, then Shor's algorithm could be used to break public-key cryptography schemes, such as the widely-used RSA scheme. RSA is based on the assumption that factoring large integers is computationally intractable. 

## Cloning
```bash
$ git clone https://github.com/gcjordi/quantum_cracking_encryption.git
```

## Dependencies
```bash
$ pip3 install -r requirements.txt
```

## How to Run
```bash
$ jupyter notebook Breaking_RSA.ipynb
```

## Output

![Screenshot from 2019-12-26 02-05-00](https://user-images.githubusercontent.com/36446402/71672203-5526ac00-2d9b-11ea-9aff-27a6d9705b33.png)

![Screenshot from 2019-12-26 02-05-22](https://user-images.githubusercontent.com/36446402/71672216-59eb6000-2d9b-11ea-95c7-4d543931f7b2.png)

![Screenshot from 2019-12-26 02-03-53](https://user-images.githubusercontent.com/36446402/71672192-4cce7100-2d9b-11ea-9a33-68202196974c.png)
