\# Part 4 — LangGraph Support Agent



\## Overview



Part 4 converts the Part 3 Support Agent into a graph-based workflow using LangGraph.



The agent maintains a shared state and executes multiple processing nodes in sequence:



1\. Look up order information

2\. Predict return risk

3\. Predict product category

4\. Generate a human-readable support response



This demonstrates how multiple existing AI/ML tools can be orchestrated using LangGraph.



\---



\## Architecture



```text

&#x20;               ┌──────────────┐

&#x20;               │    START     │

&#x20;               └──────┬───────┘

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │  lookup\_order    │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │   return\_risk   │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │ product\_category│

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │    response     │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;               ┌──────────────┐

&#x20;               │     END      │

&#x20;               └──────────────┘

