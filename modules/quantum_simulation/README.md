# Quantum Simulation Module

This directory provides the integration layer between the Creative AI Assistant and the Agothe Quantum App.

## Purpose

The Agothe Quantum App exposes a FastAPI endpoint `/api/quantum` that simulates a simple quantum collapse based on an intent phase【730441553254537†L9-L16】. The goal of this module is to wrap that endpoint and make its outputs (α/β eigenvalues and resonance patterns) available to the assistant as "quantum seeds".

## Usage

1. Install the Agothe Quantum App locally (see its repository for instructions) or deploy it as a micro‑service.
2. Create a client in `quantum_simulation_client.py` that sends POST requests to `/api/quantum` with an `intentPhase` field.
3. Provide a high‑level function `generate_quantum_seed(phase: float) -> dict` returning the eigenvalues and message from the API.
4. Integrate this function with the divergence engine so that quantum seeds can influence idea generation.

## Future work

- Extend the toy collapse engine with more realistic quantum‑inspired dynamics.
- Allow the user to specify intent phases or derive them from the problem graph state.
