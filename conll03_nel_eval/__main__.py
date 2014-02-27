#!/usr/bin/env python
import argparse
import sys
from filter import Filter
from evaluate import Evaluate
from analyze import Analyze
from significance import Significance
from release import Release
from merge import Merge
from knit import Tagme
from fetch_map import Fetch
from grep import Grep

APPS = [
    Evaluate,
    Analyze,
    Significance,
    Filter,
    Grep,
    Release,
    Merge,
    Tagme,
    Fetch,
]


def main(args=sys.argv[1:]):
    p = argparse.ArgumentParser(description='Evaluation tools for Named Entity Linking output.')
    sp = p.add_subparsers()
    for a in APPS:
        a.add_arguments(sp)

    namespace = vars(p.parse_args(args))
    cls = namespace.pop('cls')
    try:
        obj = cls(**namespace)
    except ValueError as e:
        p.error(e.message)
    print obj()

if __name__ == '__main__':
    main()
