from typing import List, Dict


def guidance() -> Dict[str, List[str]]:
    """
    Concise guidance for "Human Oversight in Healthcare" (AI ECG anomaly detection).
    Returns three short lists answering the required questions.
    """
    return {
        "Should doctors rely fully on AI outputs?": [
            "No — AI should assist, not replace clinical judgment.",
            "Treat AI as one input alongside history, exam, and other tests.",
            "Confirm unexpected/high-risk findings with clinician review or independent testing."
        ],
        "Mandatory oversight before deployment:": [
            "Clinical validation (prospective/local studies) demonstrating safety and effectiveness.",
            "Regulatory approval or clearance per local rules (e.g., FDA/CE where applicable).",
            "Technical validation: metrics, calibration, known failure modes, and reproducibility.",
            "Data governance: provenance, representativeness, privacy, and monitoring for drift.",
            "Operational controls: human-in-the-loop workflows, clear UI for uncertainty, and fail-safes."
        ],
        "How responsibility should be shared:": [
            "Developers: build, test, document limitations, and provide monitoring tools.",
            "Healthcare organizations: validate locally, train staff, set usage policies, and monitor outcomes.",
            "Clinicians: interpret AI output, make final decisions, and document overrides/adverse events.",
            "Regulators/ethics boards: set standards, audit compliance, and require harm reporting.",
            "Shared: clear contracts, incident-response plans, and continuous improvement."
        ]
    }


def print_guidance(g: Dict[str, List[str]]) -> None:
    for title, items in g.items():
        print(title)
        for i, item in enumerate(items, 1):
            print(f" {i}. {item}")
        print()


if __name__ == "__main__":
    print("Task 4 — Human Oversight in Healthcare (ECG AI)\n")
    print_guidance(guidance())
