import re
from rapidfuzz import process, fuzz
from .templates import templates, exceptions
from .schemas import CommandTemplate, MatchedCommand

class Matcher:
    _templates: list[CommandTemplate]
    
    def __init__(self):
        self._templates = templates
        
    def match(self, user_input: str):
        best_score = 0
        best_action = ""
        
        user_input = self._normalize_input(user_input)
        
        for template in self._templates:
            best_match = process.extractOne(
                user_input,
                template.patterns,
                scorer=fuzz.WRatio
            )
            if best_match and best_match[1] > best_score:
                best_score = best_match[1]
                best_action = template.action_name

        if best_score > 70:
            return MatchedCommand(best_action, best_score)
        return MatchedCommand("", best_score)

    def _normalize_input(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)  # убираем знаки препинания
        words = text.split()
        filtered = [w for w in words if w not in exceptions]
        return " ".join(filtered)