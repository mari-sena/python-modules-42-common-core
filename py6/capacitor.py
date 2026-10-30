
from ex3 import TransformCreatureFactory
from ex3.capability import TransformCapability
from ex3.creature import Creature


def test_transformation(creature: Creature) -> None:
    if not isinstance(creature, TransformCapability):
        raise TypeError("This creature cannot transform")

    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print("  base:")
    test_transformation(factory.create_base())

    print("  evolved:")
    test_transformation(factory.create_evolved())


if __name__ == "__main__":
    main()
