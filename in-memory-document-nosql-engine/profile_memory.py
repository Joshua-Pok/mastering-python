from src.engine.document import Document
import sys

from tests.test_memory import StandardDocument



def measure_bytes(doc_class):


    instances = [doc_class(str(i), {"active":True}) for i in range(1_000_000)]

    is_slotted = hasattr(doc_class, "__slots__")


    if is_slotted:
        total_bytes = sum(sys.getsizeof(obj) for obj in instances)
    else:
        total_bytes = sum(sys.getsizeof(obj) + sys.getsizeof(obj.__dict__) for obj in instances)


    print(total_bytes)
    return total_bytes



def run():
    print("Measuring usage over 1,000,000 instances")

    standard_mb = measure_bytes(StandardDocument)
    slotted_mb = measure_bytes(Document)


    saved_mb = standard_mb - slotted_mb
    saved_pct = (saved_mb / standard_mb) * 100
    print(f"{'Class':<25} {'Memory (MB)':>12}")
    print("-" * 38)
    print(f"{'StandardDocument':<25} {standard_mb:>11.2f} MB")
    print(f"{'Document (slotted)':<25} {slotted_mb:>11.2f} MB")
    print("-" * 38)
    print(f"{'Savings':<25} {saved_mb:>11.2f} MB  ({saved_pct:.1f}% reduction)")


if __name__ == "__main__":
    run()

