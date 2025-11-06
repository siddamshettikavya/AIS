"""
Task 6 – Environmental and Societal Impact of AI (Simplified)
Focus: Energy use, environmental impact, ethics, and balance.
"""

def calculate_energy(model, requests):
    if model == 'small': energy = 0.00001
    elif model == 'medium': energy = 0.00005
    else: energy = 0.0002
    co2 = energy * 0.5
    total_energy = energy * requests
    total_co2 = co2 * requests
    return total_energy, total_co2

# --- Examples ---
print("=== AI Energy & Environmental Impact ===")
models = ['small', 'medium', 'large']
requests = 10000

for m in models:
    e, c = calculate_energy(m, requests)
    print(f"\nModel: {m.capitalize()} ({requests} requests)")
    print(f"Energy Used: {e:.2f} kWh | CO₂: {c:.2f} kg")

# --- Discussion ---
print("\n=== Ethical Responsibility & Balance ===")
print("""
1. Every AI model consumes energy and emits CO₂.
2. Large models give higher accuracy but more environmental cost.
3. Developers must balance performance and sustainability.
4. Use smaller models when possible and optimize code.
5. Sustainable AI ensures fairness, cost reduction, and future safety.
""")
