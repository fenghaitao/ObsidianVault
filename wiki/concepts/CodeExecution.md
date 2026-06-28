---
title: "Code Execution"
type: concept
tags: [code, execution, analysis, data-processing, capability, feature]
sources: ["raw/01-articles/claude/2024-10-24 - Introducing the analysis tool in Claude.ai.md", "raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md"]
last_updated: 2026-06-28
---

# Code Execution

Code execution is a capability that allows Claude to write and run code (typically JavaScript) directly within the interface to process data, perform analysis, and produce precise computational results. This enables Claude to move beyond abstract reasoning to execute concrete operations with verifiable outputs.

## Overview

Rather than only generating code for users to run elsewhere, code execution allows Claude to:
- Write code to solve a problem
- Execute that code immediately
- Process results and iterate
- Provide mathematically precise and reproducible answers

## Capabilities

### Core Functionality
- **Language Support**: JavaScript (primary implementation in Claude.ai)
- **Code Sandbox**: Isolated execution environment for safe code running
- **Data Processing**: Clean, explore, and analyze data
- **Mathematical Operations**: Perform complex calculations
- **File Generation**: Create downloadable outputs (spreadsheets, CSVs, reports)
- **Visualizations**: Generate charts and visual representations
- **Multi-step Workflows**: Handle complex, sequential analysis tasks

### Output Types
- Direct analysis results
- Downloadable files and reports
- Charts and visualizations
- Real-time insights and metrics
- Processed and cleaned data

## Evolution & History

### Analysis Tool (October 2024)
The [[CodeExecution]] capability evolved from the "analysis tool" introduced in Claude.ai on October 24, 2024. The analysis tool was a built-in JavaScript code sandbox for data processing and analysis.

### Code Execution (November 2025+)
As of November 5, 2025, the analysis tool was deprecated in favor of expanded code execution capabilities with:
- Broader functionality (file generation, visualizations)
- More complex workflow support
- Enhanced developer experience

### File Creation via Private Computer Environment (September 2025+)
As of September 2025, [[Claude.ai]] and the desktop app gained a file creation and editing capability powered by a private computer environment. Claude can produce ready-to-use files (Excel spreadsheets, Word documents, PowerPoint presentations, PDFs) by writing and running code internally. The technical execution is invisible to the user; they simply describe what they need. Initially a preview for Max, Team, and Enterprise subscribers; GA for all paid plans on October 21, 2025. This feature includes internet access, so Anthropic recommends monitoring chats closely.

### Anthropic API Code Execution Tool (May 2025+)
As of May 2025, the [[Anthropic]] API offers the [[CodeExecutionTool|code execution tool]] (beta), enabling Python code execution in sandboxed containers:
- Language: Python (vs. JavaScript in Claude.ai)
- Sandboxed environment for secure execution
- Access to data science libraries
- Integration with [[FilesAPI]] for file access during execution
- Works with [[Claude4Opus]] and [[Claude4Sonnet]]
- Pricing: 50 free hours/day, then $0.05/hour per container

## Use Cases

### Data Analysis
- Process datasets
- Generate statistical insights
- Create analysis reports

### Data Transformation
- Clean and format data
- Convert between data formats
- Create structured exports

### Verification & Testing
- Verify calculations and results
- Test hypotheses computationally
- Validate data integrity

## Technical Context

Code execution relies on [[Claude]]'s coding capabilities, particularly those of models like [[Claude3.5Sonnet]], which have state-of-the-art code generation and understanding abilities.

## Related

- [[Claude.ai]] — product offering JavaScript code execution in web interface
- [[Claude3.5Sonnet]] — model powering code execution in Claude.ai with advanced coding abilities
- [[Claude4Opus]] — API model with Python code execution
- [[Claude4Sonnet]] — API model with Python code execution
- [[CodeExecutionTool]] — Anthropic API feature for Python code execution
- [[FilesAPI]] — integrates with API code execution for file access
- [[PromptCaching]] — works with code execution for long-running analysis
- [[Anthropic]] — provides API code execution tool
- [[ToolUse]] — related capability for Claude to interact with external systems
- [[summary-2024-10-24 - Introducing the analysis tool in Claude.ai]] — feature announcement and historical context
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement of API code execution tool
- [[summary-2025-09-09 - Claude can now create and edit files]] — file creation capability using private computer environment
