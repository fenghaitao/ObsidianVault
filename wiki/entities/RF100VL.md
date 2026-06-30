---
title: "RF100VL"
type: entity
tags: [dataset, computer-vision, object-detection, transfer-learning, benchmark]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
RF100VL is a dataset introduced by Roboflow that measures how well vision foundation models transfer to diverse downstream object detection tasks, enabling systematic evaluation of foundation model deployment strategies.

## Key Information
- Published by Roboflow
- Measures foundation model transfer performance on object detection, a canonical vision-centric task
- Used to benchmark RFDetR against fine-tuning SAM 3
- Shows RFDetR achieves ~40x speedup at same accuracy versus SAM 3 fine-tuning, and ~15x speedup with meaningful accuracy improvement
- Enables systematic comparison of deployment strategies for vision foundation models

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[Roboflow]] — publisher
- [[RFDetR]] — model evaluated using this dataset
- [[SAM (Segment Anything Model)]] — baseline compared against
- [[Foundation Models]] — models being evaluated for transfer
