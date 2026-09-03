"""
Package des benchmarks africains.
"""
from .senegal import get_senegal_benchmark, SENEGAL_BENCHMARK
from .nigeria import get_nigeria_benchmark, NIGERIA_BENCHMARK
from .kenya import get_kenya_benchmark, KENYA_BENCHMARK


ALL_BENCHMARKS = [
    SENEGAL_BENCHMARK,
    NIGERIA_BENCHMARK,
    KENYA_BENCHMARK,
]


def get_all_benchmarks():
    """Retourne tous les benchmarks disponibles."""
    return ALL_BENCHMARKS


def get_benchmark_by_country(country_code):
    """Retourne un benchmark par code pays."""
    for benchmark in ALL_BENCHMARKS:
        if benchmark['country_code'] == country_code.upper():
            return benchmark
    return None
