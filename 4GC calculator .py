# GC content calculator with loop and validation

valid_bases = {"A", "T", "G", "C"}

while True:
    dna_sequence = input("\nEnter your DNA sequence (or type 'exit' to quit): ").upper()

    if dna_sequence == "EXIT":
        print("👋 Exiting GC calculator. Goodbye!")
        break

    if not set(dna_sequence).issubset(valid_bases):
        print("❌ Invalid DNA sequence! Use only A, T, G, and C.")
        continue

    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")

    gc_content = ((g_count + c_count) / len(dna_sequence)) * 100

    print(f"✅ Valid DNA. GC Content: {gc_content:.4f}%")
