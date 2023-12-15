import dataclasses
import typing

import numpy as np


def dataclasses_instances_equal(instance_1: typing.Any, instance_2: typing.Any) -> bool:
    if instance_1 is instance_2:
        return True
    if isinstance(instance_1, np.ndarray) and isinstance(instance_2, np.ndarray):
        return np.array_equal(instance_1, instance_2)
    elif not dataclasses.is_dataclass(instance_1) and not dataclasses.is_dataclass(
        instance_2
    ):
        return bool(instance_1 == instance_2)
    if instance_1.__class__ is not instance_2.__class__:
        return False
    fields_are_same = instance_1.__dataclass_fields__ == instance_2.__dataclass_fields__
    attributes_are_same = []
    for field_1, field_2 in zip(
        dataclasses.fields(instance_1), dataclasses.fields(instance_2)
    ):
        attributes_are_same.append(
            dataclasses_instances_equal(
                getattr(instance_1, field_1.name), getattr(instance_2, field_2.name)
            )
        )
    return (
        dataclasses.is_dataclass(instance_1)
        and dataclasses.is_dataclass(instance_2)
        and fields_are_same
        and all(attributes_are_same)
    )
