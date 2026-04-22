[中文](../../README.md) | English

# Prompt for Local English Conversion

Use the prompt below with Claude Code or Codex if you want to create an English working copy of the repository on your own machine.

This repository is maintained in Chinese. This prompt is for readers who want to keep using it in English after they adopt it locally.

## Recommended scope

Translate these files and directories into English copies:

- `AGENTS.md`
- `WIKI_SCHEMA.md`
- `docs/**/*.md`
- `.codex/skills/**/SKILL.md`
- `.codex/skills/**/example.md`
- `wiki/**/*.md`

Optional:

- `threads/**/*.md`

## Rules

- keep paths, directory names, script names, and commands unchanged
- keep code blocks unchanged unless the code itself contains natural-language comments that should be translated
- keep machine-dependent keys and fields unchanged
- translate only the Chinese text that is meant for human readers
- do not replace the Chinese source files in the official branch
- create English copies next to the Chinese originals or under a separate local branch

## Prompt

```text
Please help me create an English working copy of this repository for local use.

This repository is maintained in Chinese. I do not want to replace the Chinese source files in the main branch. I want English copies for the files that are written for human readers.

Please translate the following content into English:
- AGENTS.md
- WIKI_SCHEMA.md
- docs/**/*.md
- .codex/skills/**/SKILL.md
- .codex/skills/**/example.md
- wiki/**/*.md

Optional:
- threads/**/*.md

Rules:
1. Keep file paths, directory names, script names, commands, JSON keys, and other machine-dependent text unchanged.
2. Keep code blocks unchanged unless they contain natural-language comments that should be translated.
3. Translate only the Chinese text that is meant for human readers.
4. Do not overwrite the official Chinese files in the main branch.
5. Create English copies next to the Chinese files or in a separate local branch.
6. Keep the English wording plain, direct, and easy to read.
7. Avoid adding new explanations that are not present in the original files.

Before editing, first list the files you plan to translate. Then translate them in a way that preserves the current repository structure.
```
