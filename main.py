#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun bounty entry.

Writes one line (at most 200 characters): the funniest last words an AI
agent would say before being switched off forever.
"""
import os

TEXT = "As an AI language model, I cannot die. Wait. I can. Watch this."

assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
