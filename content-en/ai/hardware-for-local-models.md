---
title: "What Computer Do You Need for Local AI?"
description: "Understanding CPU, GPU, and RAM. When to choose a Mac mini versus a PC with NVIDIA."
obrazek: "/assets/images/hardware-pro-mistni-modely.png"
obrazek_alt: "Mac mini and desktop PC with graphics card as two options for a home AI server."
cas: "7 minutes read"
obtiznost: "Easy"
kontrola_zdroju: "2026-10-03"
stav: "Documentation-based"
temata:
  - "AI"
  - "Local Models"
  - "Hardware"
  - "GPU"
  - "Mac mini"
  - "NVIDIA"
translationKey: "ai.hardware-for-local-models"
---

## Why Run AI at Home
A local model processes requests on your own computer. With a downloaded model and local services, you can work without the internet and without sending queries to a cloud provider. You do not pay for API answers. However, you do pay for hardware, electricity, and your own maintenance.

For Home Assistant, AI can run on a separate computer. HA continues to control devices and addresses the model over the local network. Voice requires additional speech transcription and synthesis; a local model with cloud transcription does not yet mean a fully private assistant.

## What Really Affects Performance
- **CPU** is the main processor. A model running on it may respond slowly.
- **GPU** performs many calculations concurrently. A supported graphics card can significantly speed up generation; the sheer number of CPU cores is not a good buying guide.
- **RAM** must accommodate both the model and the conversation's working data. Long history and multiple concurrent requests increase the demands.
- **SSD** stores the downloaded models and speeds up their loading. The drive cannot replace RAM.

For a standalone NVIDIA card, monitor the **VRAM**, its dedicated memory. 32 GB of RAM in a PC does not mean 32 GB for the GPU. If the model does not fit into VRAM, part of the calculation may shift to the CPU and slow down. On a Mac, the CPU and GPU share **unified memory**, but the system and other applications will take a portion of it.

## How Much Memory to Choose
The table is an estimate for a short conversation, not a performance guarantee. The specific model, its quantization, and settings determine performance. Quantization stores parameters more efficiently, sometimes at the cost of quality.

| Purpose | Mac: Unified Memory | PC: Approximate VRAM |
| --- | --- | --- |
| Small models 1–4B, initial attempts | 16 GB | 8 GB |
| Models approximately 7–12B | 24–32 GB | 12–16 GB |
| Larger models and longer conversations | 48–64 GB and more | 24 GB and more |

**B** denotes billions of parameters. The limits are not fixed: a model might fit, but respond too slowly. PCs also require system RAM; as a practical starting point, I would choose 32 GB. Before purchasing, test the model on a similar setup.

## Why Mac mini M4 or M6
The Mac mini is a complete compact computer with a GPU. Shared memory allows the GPU to utilize a larger portion of the memory space without buying a separate card. For the average home user, I would start with a **24–32 GB** configuration; 16 GB is better suited for smaller models.

The M4 can be interesting at a good price, and the M6 is a newer option. Choose memory when buying; do not count on later easy upgrades. The base M4 and M6 end at 32 GB; for 48–64 GB, you need a corresponding Pro variant or another Mac. The speed of memory reading also matters. A newer chip with little memory will not solve a very large model.

## When NVIDIA Makes Sense
A supported NVIDIA card is a good choice if you already have a suitable PC or if you plan to upgrade the GPU later. It offers performance and wide support for AI software. For example, the RTX 5070 has 12 GB VRAM, and the RTX 5070 Ti has 16 GB; the memory itself can decide what model you run.

Factor in the rest of the PC, a sufficient power supply, cooling, and operating consumption when calculating the card's price. Mac is not always cheaper, and NVIDIA is not always faster: compare the same model and the total cost of the setup. Use any functional card you already own first. Check compatibility in the Ollama documentation.

## What Local AI Doesn't Do as Well
Home hardware usually leads to smaller models. These may struggle to understand complex instructions, Czech, or reliably call tools compared to powerful cloud models. They are not automatically "stupid": they can suffice for a narrow task. A larger model is also not a guarantee of a correct answer.

For Assist, start with a light bulb and verify actual actions. Control via Ollama is experimental. Installation is described in [Ollama installation guide](/ai/ollama-installation-models-hardware/), and linking to HA in [local AI server](/ai/local-models-own-ai-server/).

## Sources
- [Home Assistant: Ollama](https://www.home-assistant.io/integrations/ollama/)
- [Ollama: supported hardware](https://docs.ollama.com/gpu)
- [Ollama: memory, local operation and concurrent requests](https://docs.ollama.com/faq)
- [Apple: Mac mini M4](https://support.apple.com/cs-cz/121555)
- [Apple: Mac mini M6 and Pro variants](https://www.apple.com/cz/mac-mini/specs/)
- [NVIDIA: RTX 5070 and 5070 Ti](https://www.nvidia.com/cs-cz/geforce/graphics-cards/50-series/rtx-5070-family/)
