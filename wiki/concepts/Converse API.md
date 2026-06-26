---
title: "Converse API"
type: concept
tags: [aws, bedrock, api, multi-model]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md"]
last_updated: 2026-06-26
---
## Definition
The Converse API is a unified API in Amazon Bedrock that provides a standardized method for invoking different foundation models, handling model-specific translations of parameters, prompts, and output formats so developers can work across models with consistent code.

## Key Information
- Provides a single API call pattern regardless of which model is being used
- Standardized parameters (inference parameters are normalized across models)
- Handles system/user/assistant prompt translation for different model formats
- Produces consistent output formatting across models
- Has native function calling support — tools are passed as a list to the API call
- Developers simply specify the model ID to switch between models
- Code examples available in Python and other languages on community.aws
- Created to simplify multi-model development and evaluation

## Related
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source
- [[AmazonBedrock]]
- [[AWS]]
- [[Function Calling]]
- [[Model Evaluation]]
- [[Dennis Trope]] — author of code tutorials
