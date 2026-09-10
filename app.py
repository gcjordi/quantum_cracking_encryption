"""Optional Gradio UI for Quantum Cryptography Lab v2.0."""

from __future__ import annotations


def factor_for_ui(n: int, shots: int) -> str:
    from quantum_crypto_lab import factor_integer

    try:
        result = factor_integer(int(n), shots=int(shots))
    except Exception as exc:  # UI boundary
        return f"Error: {exc}"
    lines = [
        f"N: {result.n}",
        f"Backend: {result.backend_name}",
        f"Success: {result.success}",
        f"Factors: {result.factors}",
        "",
        "Attempts:",
    ]
    for attempt in result.attempts:
        lines.append(
            f"- a={attempt.base} route={attempt.route} order={attempt.order} "
            f"measurement={attempt.measurement} factors={attempt.factors} {attempt.note}"
        )
    return "\n".join(lines)


def main() -> None:
    try:
        import gradio as gr
    except ImportError as exc:
        raise SystemExit("Install the optional UI dependencies with: pip install -e '.[ui]'") from exc

    with gr.Blocks(title="Quantum Cryptography Lab v2.0") as demo:
        gr.Markdown(
            "# Quantum Cryptography Lab v2.0\n"
            "Provider-neutral educational Shor factorization. Use deliberately small composites."
        )
        n = gr.Number(value=15, precision=0, label="Composite N")
        shots = gr.Slider(256, 8192, value=4096, step=256, label="Measurement shots")
        run = gr.Button("Run Shor simulation")
        output = gr.Textbox(lines=12, label="Result")
        run.click(factor_for_ui, inputs=[n, shots], outputs=output)
    demo.launch()


if __name__ == "__main__":
    main()
