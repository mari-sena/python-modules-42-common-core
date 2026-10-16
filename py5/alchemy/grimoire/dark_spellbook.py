from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ['bats', 'frogs', 'arsenic', 'eye-ball']


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = dark_validate_ingredients(ingredients)

    if "INVALID" in validation:
        return f"Spell rejected: {spell_name} ({validation})"

    return f"Spell recorded: {spell_name} ({validation})"
