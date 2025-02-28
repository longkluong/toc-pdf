# %%
import os
import fitz


def create_toc(original_path, new_path, toc):
    doc = fitz.open(original_path)
    doc.set_toc(toc)
    doc.save(new_path)
    return


original_path = "/Users/longluong/Zotero/storage/BJUI3KDQ/Simon and Blume - 1994 - Mathematics for economists.pdf"
new_path = (
    "/Users/longluong/Downloads/Simon and Blume - 1994 - Mathematics for economists.pdf"
)
# Toc structure:
# List of a list of 3 elements:
# [lvl, title, page]
toc = [
    [1, " Contents", 28],
    [1, " Preface", 25],
    [1, " Part I - Introduction", 26],
    [1, "1 Introduction", 28],
    [2, "1.1 Mathematics in Economic Theory", 28],
    [2, "1.2 Models of Consumer Choice", 30],
    [1, "2 One-Variable Calculus: Foundations", 35],
    [2, "2.1 Functions on R1", 35],
    [2, "2.2 Linear Functions", 41],
    [2, "2.3 The Slope of Nonlinear Functions", 47],
    [2, "2.4 Compting Derivatives", 50],
    [2, "2.5 Differentiability and Continuity", 54],
    [2, "2.6 Higher-order Derivatives", 58],
    [2, "2.7 Approximation by Diferentials", 59],
    [1, "3 One-Variable Calculus: Applications", 64],
    [2, "3.1 Using the First Derivative for Graphing", 64],
    [2, "3.2 Second Derivatives and Convexity", 68],
    [2, "3.3 Graphing Rational Functions", 72],
    [2, "3.4 Tails and Horizontal Asymptotes", 73],
    [2, "3.5 Maxima and Minima", 76],
    [2, "3.6 Applications to Economics", 83],
    [1, "4 One-Variable Calculus: Chain Rule", 95],
    [2, "4.1 Composite Functions and the Chain Rule", 95],
    [2, "4.2 Inverse Functions and Their Derivatives", 100],
    [1, "5 Exponents and Logarithms", 107],
    [2, "5.1 Exponential Functions", 107],
    [2, "5.2 The Number e", 110],
    [2, "5.3 Logarithms", 113],
    [2, "5.4 Properties of Exp and Log", 116],
    [2, "5.5 Derivatives of Exp and Log", 118],
    [2, "5.6 Applications", 122],
    [1, " Part II - Linear Algebra", 130],
    [1, "6 Introduction to Linear Algebra", 132],
    [2, "6.1 Linear Systems", 132],
    [2, "6.2 Examples of Linear Models", 133],
    [1, "7 Systems of Linear Equations", 147],
    [2, "7.1 Gaussian and Gauss-Jordan Elimination", 147],
    [2, "7.2 Elementary Row Operations", 154],
    [2, "7.3 Systems with Many or No Solutions", 159],
    [2, "7.4 Rank -- The Fundamental Criterion", 167],
    [2, "7.5 The Linear Implicit Function Theorem", 175],
    [1, "8 Matrix Algebra", 178],
    [2, "8.1 Matrix Algebra", 178],
    [2, "8.2 Special Kinds of Matrices", 185],
    [2, "8.3 Elementary Matrices", 187],
    [2, "8.4 Algebra of Square Matrices", 190],
    [2, "8.5 Input-Output Matrices", 199],
    [2, "8.6 Partitioned Matrices (optional)", 205],
    [2, "8.7 Decomposing Matrices (optional)", 208],
    [1, "9 Determinants: An Overview", 213],
    [2, "9.1 The Determinant of a Matrix", 214],
    [2, "9.2 Uses of the Determinant", 219],
    [2, "9.3 IS-LM Analysis via Cramer's Rule", 222],
    [1, "10 Euclidean Spaces", 224],
    [2, "10.1 Points and Vectors in Euclidean Space", 224],
    [2, "10.2 Vectors", 227],
    [2, "10.3 The Algebra of Vectors", 230],
    [2, "10.4 Length and Inner Product in R^n", 234],
    [2, "10.5 Lines", 247],
    [2, "10.6 Planes", 251],
    [2, "10.7 Economic Applications", 257],
    [1, "11 Linear Independence", 262],
    [2, "11.1 Linear Independence", 262],
    [2, "11.2 Spanning Sets", 269],
    [2, "11.3 Basis and Dimension in Rn", 272],
    [2, "11.4 Epilogue", 274],
    [1, " Part III - Calculus of Several Variables", 276],
    [1, "12 Limits and Open Sets", 278],
    [2, "12.1 Sequences of Real Numbers", 278],
    [2, "12.2 Sequences in R^m", 285],
    [2, "12.3 Open Sets", 289],
    [2, "12.4 Closed Sets", 292],
    [2, "12.5 Compact Sets", 295],
    [2, "12.6 Epilogue", 297],
    [1, "13 Functions of Several Variables", 298],
    [2, "13.1 Functions Between Euclidean Spaces", 298],
    [2, "13.2 Geometric Representation of Functions", 302],
    [2, "13.3 Special Kinds of Functions", 312],
    [2, "13.4 Continuous Functions", 318],
    [2, "13.5 Vocabulary of Functions", 320],
    [1, "14 Calculus of Several Variables", 325],
    [2, "14.1 Definitions and Examples", 325],
    [2, "14.2 Economic Interpretation", 327],
    [2, "14.3 Geometric Intepretation", 330],
    [2, "14.4 The Total Derivative", 332],
    [2, "14.5 The Chain Rule", 338],
    [2, "14.6 Directional Derivatives and Gradients", 344],
    [2, "14.7 Explicit Functions from R^n to R^m", 348],
    [2, "14.8 Higher-order Derivatives", 353],
    [2, "14.9 Epilogue", 358],
    [1, "15 Implicit Functions and Their Derivatives", 359],
    [2, "15.1 Implicit Functions", 359],
    [2, "15.2 Level Curves and Their Tangents", 367],
    [2, "15.3 Systems of Implicit Functions", 375],
    [2, "15.4 Application: Comparative Statics", 385],
    [2, "15.5 The Inverse Function Theorem (optional)", 389],
    [2, "15.6 Application: Simpson's Paradox", 393],
    [1, " Part IV - Optimization", 398],
    [1, "16 Quadratic Forms and Definite Matrices", 400],
    [2, "16.1 Quadratic Forms ", 400],
    [2, "16.2 Definiteness of Quadratic Forms", 401],
    [2, "16.3 Linear Constraints and Bordered Matrices", 411],
    [2, "16.4 Appendix", 418],
    [1, "17 Unconstrained Optimization", 421],
    [2, "17.1 Definitions and Examples", 421],
    [2, "17.2 First Order Conditions", 422],
    [2, "17.3 Second Order Conditions", 423],
    [2, "17.4 Global Maxima and Minima", 427],
    [2, "17.5 Economic Applications", 429],
    [1, "18 Constrained Optimization I: First Order Conditions", 436],
    [2, "18.1 Examples", 437],
    [2, "18.2 Equality Constraints", 438],
    [2, "18.3 Inequality Constraints", 449],
    [2, "18.4 Mixed Constraints", 459],
    [2, "18.5 Constrained Minimization Problems", 461],
    [2, "18.6 Kuhn-Tucker Formulation", 464],
    [2, "18.7 Examples and Applications", 467],
    [1, "19 Constrained Optimization II", 473],
    [2, "19.1 The Meaning of The Multiplier", 473],
    [2, "19.2 Envelope Theorems", 478],
    [2, "19.3 Second Order Conditions", 482],
    [2, "19.4 Smooth Dependence on The Parameters", 494],
    [2, "19.5 Constraint Qualifications", 497],
    [2, "19.6 Proofs of First Order Conditions", 503],
    [1, "20 Homogeneous and Homothetic Functions", 508],
    [2, "20.1 Homogeneous Functions", 508],
    [2, "20.2 Homogenizing a Function", 518],
    [2, "20.3 Cardinal Versus Ordinal Utility", 521],
    [2, "20.4 Homothetic Functions", 525],
    [1, "21 Concave and Quasiconcave Functions", 530],
    [2, "21.1 Concave and Convex Functions", 530],
    [2, "21.2 Properties of Concave Functions", 542],
    [2, "21.3 Quasiconcave and Quasiconvex Functions", 547],
    [2, "21.4 Pseudoconcve Functions", 552],
    [2, "21.5 Concave Programming", 557],
    [2, "21.6 Appendix", 562],
    [1, "22 Economic Applications", 569],
    [2, "22.1 Utility and Demand", 569],
    [2, "22.2 Economic Application: Profit and Cost", 582],
    [2, "22.3 Pareto Optima", 590],
    [2, "22.4 The Fundamental Welfare Theorems", 594],
    [1, " Part V - Eigenvalues and Dynamics", 602],
    [1, "23 Eigenvalues and Eigenvectors", 604],
    [2, "23.1 Definitions and Examples", 604],
    [2, "23.2 Solving Linear Difference Equations", 610],
    [2, "23.3 Properties of Eigenvalues", 622],
    [2, "23.4 Repeated Eigenvalues", 626],
    [2, "23.5 Complex Eigenvalues and Eigenvectors", 634],
    [2, "23.6 Markov Processes", 640],
    [2, "23.7 Symmetric Matrices", 645],
    [2, "23.8 Definiteness of Quadratic Forms", 651],
    [2, "23.9 Appendix", 654],
    [1, "24 Ordinary Differential Equations: Scalar Equations", 658],
    [2, "24.1 Definitions and Examples", 658],
    [2, "24.2 Explicit Solutions", 664],
    [2, "24.3 Linear Second Order Equations", 672],
    [2, "24.4 Existence of Solutions", 682],
    [2, "24.5 Phase Portraits and Equilibria on R1", 691],
    [2, "24.6 Appendix: Applications", 695],
    [1, "25 Ordinary Differential Equations: Systems of Equations", 699],
    [2, "25.1 Planar Systems: An Introduction", 699],
    [2, "25.2 Linear Systems via Eigenvalues", 703],
    [2, "25.3 Solving Linear Systems by Substitution", 707],
    [2, "25.4 Steady States and Their Stability", 709],
    [2, "25.5 Phase Portraits of Planar Systems", 714],
    [2, "25.6 First Integrals", 728],
    [2, "25.7 Liapunov Functions", 736],
    [2, "25.8 Appendix: Linearization", 740],
    [1, " Part VI - Advance Linear Algebra", 742],
    [1, "26 Determinants: The Details", 744],
    [2, "26.1 Definitions of the Determinant", 744],
    [2, "26.2 Properties of the Determinant", 751],
    [2, "26.3 Using Determinants", 760],
    [2, "26.4 Economic Applications", 764],
    [2, "26.5 Appendix", 768],
    [1, "27 Subspaces Attached to a Matrix", 775],
    [2, "27.1 Vector Spaces and Subspaces", 775],
    [2, "27.2 Basis and Dimension of a Proper Subspace", 780],
    [2, "27.3 Row Space", 782],
    [2, "27.4 Column Space", 785],
    [2, "27.5 Nullspace", 790],
    [2, "27.6 Abstract Vector Spaces", 796],
    [2, "27.7 Appendix", 799],
    [1, "28 Applications of Linear Independence", 804],
    [2, "28.1 Geometry of Systems of Equations", 804],
    [2, "28.2 Portfolio Analysis", 808],
    [2, "28.3 Voting Paradoxes", 809],
    [2, "28.4 Activity Analysis: Feasibility", 816],
    [2, "28.5 Activity Analysis: Efficiency", 818],
    [1, " Part VII - Advanced Analysis", 826],
    [1, "29 Limits and Compact Sets", 828],
    [2, "29.1 Cauchy Sequences", 828],
    [2, "29.2 Compact Sets", 832],
    [2, "29.3 Connected Sets", 834],
    [2, "29.4 Alternative Norms", 836],
    [2, "29.5 Appendix", 841],
    [1, "30 Calculus of Several Variables II", 847],
    [2, "30.1 Weierstrass's and Mean Value Theorems", 847],
    [2, "30.2 Taylor Polynomials on R1", 852],
    [2, "30.3 Taylor Polynomials in Rn", 857],
    [2, "30.4 Second Order Optimization Conditions", 861],
    [2, "30.5 Constrained Optimization", 866],
    [1, " Part VIII - Appendices", 870],
    [1, "A1 Sets, Numbers, and Proofs", 872],
    [2, "A1.1 Sets, Numbers, and Proofs", 872],
    [2, "A1.2 Numbers", 873],
    [2, "A1.3 Proofs", 876],
    [1, "A2 Trigonometric Functions", 884],
    [2, "A2.1 Definitions", 884],
    [2, "A2.2 Graphing", 888],
    [2, "A2.3 The Pythagorean Theorem", 890],
    [2, "A2.4 Evaluating Trigonometric Functions", 891],
    [2, "A2.5 Multiangle Formulas", 893],
    [2, "A2.6 Functions of Real Numbers", 893],
    [2, "A2.7 Calculus with Trig Functions", 895],
    [2, "A2.8 Taylor Series", 897],
    [2, "A2.9 Proof of Theorem A2.3", 898],
    [1, "A3 Complex Numbers", 901],
    [2, "A3.1 Background", 901],
    [2, "A3.2 Solutions of Polynomial Equations", 903],
    [2, "A3.3 Geometric Representation", 904],
    [2, "A3.4 Complex Numbers as Exponents", 907],
    [2, "A3.5 Difference Equations", 909],
    [1, "A4 Integral Calculus", 912],
    [2, "A4.1 Antiderivatives", 912],
    [2, "A4.2 The Fundamental Theorem of Calculus", 914],
    [2, "A4.3 Applications", 915],
    [1, "A5 Introduction to Probability", 919],
    [2, "A5.1 Probability of an Event", 919],
    [2, "A5.2 Expectation and Variance", 920],
    [2, "A5.3 Continuous Random Variables", 921],
    [1, "A6 Selected Answers", 924],
    [1, " Index", 946],
]

if __name__ == "__main__":
    create_toc(original_path, new_path, toc)
