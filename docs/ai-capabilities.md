---
id: ai-capabilities
title: AI Capabilities
sidebar_position: 5
---

# AI Capabilities

What TchueKAM's agent can do, and how.

## Reasoning
TchueKAM uses state-of-the-art language understanding to:
- Break down complex questions into steps
- Plan multi-step tasks before acting
- Explain its reasoning when asked
- Recognize when it needs more information

## Tool use
The agent doesn't just talk — it acts. Built-in tools include:

- **File operations** — read, write, edit, search across your workspace
- **Shell execution** — run commands with your approval
- **Web search and fetch** — bring in fresh information
- **Image analysis** — understand screenshots and diagrams
- **Code execution** — run Python, JavaScript, and shell scripts in a sandbox

TchueKAM picks the right tool for each task automatically.

## Memory
- **Short-term memory** — tracks the current conversation thread
- **Long-term memory** — remembers important facts about you and your projects across sessions
- **Workspace memory** — separate context per folder

You can review, edit, and delete memories at any time from Settings → Memory.

## Code understanding
- Reads and reasons about codebases in any major language
- Detects bugs, security issues, and code smells
- Suggests refactors with rationale
- Generates tests that actually run

## Multi-step workflows
Ask TchueKAM to do something complex like _"set up a new React project with TypeScript, Tailwind, and a basic auth flow"_ — it'll plan, execute step-by-step, and check in with you when decisions need your input.

## Privacy boundaries
- The agent **never** sends data outside your machine without an explicit user action
- File reads, shell commands, and network requests are all logged
- You can audit every action TchueKAM took from Settings → Activity Log

## Limits
TchueKAM is powerful but not omniscient. It can:
- Make mistakes — always verify generated code before running in production
- Be slow on very large files or codebases — break tasks into smaller chunks
- Miss recent information — use web search for anything time-sensitive
