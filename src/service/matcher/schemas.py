from dataclasses import dataclass

@dataclass
class MatchedCommand:
    command: str
    percent: int

@dataclass
class CommandTemplate:
    patterns: list[str]
    action_name: str
    desc: str | None = None