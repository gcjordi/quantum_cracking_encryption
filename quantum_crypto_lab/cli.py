from __future__ import annotations

import argparse

from .shor import factor_integer


def main() -> None:
    parser = argparse.ArgumentParser(description="Educational Shor factorization simulator")
    parser.add_argument("n", type=int, help="small composite integer, e.g. 15, 21 or 35")
    parser.add_argument("--shots", type=int, default=4096)
    args = parser.parse_args()
    result = factor_integer(args.n, shots=args.shots)
    print(result)


if __name__ == "__main__":
    main()
