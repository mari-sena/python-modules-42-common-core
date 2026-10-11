def validate_dark_ingredientes(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients

    allowed = dark_spell_allowed_ingredients()

    for ingredient in allowed:
        if ingredient in ingredients.lower():
            return f"{ingredients} VALID"

    return f"{ingredients} INVALID"
