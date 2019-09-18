# -*- coding: utf-8
import importlib
import logging

from django.db.utils import ProgrammingError

from pipeline.component_framework.library import ComponentLibrary
from pipeline.core.flow.activity import Service
from pipeline.component_framework.models import ComponentModel

logger = logging.getLogger(__name__)


class ComponentMeta(type):
    def __new__(cls, name, bases, attrs):
        super_new = super(ComponentMeta, cls).__new__

        # Also ensure initialization is only performed for subclasses of Model
        # (excluding Model class itself).
        parents = [b for b in bases if isinstance(b, ComponentMeta)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        # Create the class
        module_name = attrs.pop('__module__')
        new_class = super_new(cls, name, bases, {'__module__': module_name})
        module = importlib.import_module(new_class.__module__)

        # Add all attributes to the class
        attrs.setdefault('desc', '')
        for obj_name, obj in attrs.items():
            setattr(new_class, obj_name, obj)

        # check
        if not getattr(new_class, 'name', None):
            raise ValueError("component %s name can't be empty" %
                             new_class.__name__)

        if not getattr(new_class, 'code', None):
            raise ValueError("component %s code can't be empty" %
                             new_class.__name__)

        if not getattr(new_class, 'bound_service', None) or not issubclass(new_class.bound_service, Service):
            raise ValueError("component %s service can't be empty and must be subclass of Service" %
                             new_class.__name__)

        if not getattr(new_class, 'form', None):
            raise ValueError("component %s form can't be empty" % new_class.__name__)

        # category/group name
        group_name = getattr(
            module, "__group_name__",
            new_class.__module__.split(".")[-1].title()
        )
        setattr(new_class, 'group_name', group_name)
        new_name = u"%s-%s" % (group_name, new_class.name)

        # category/group name
        group_icon = getattr(
            module, "__group_icon__",
            ''
        )
        setattr(new_class, 'group_icon', group_icon)

        if not getattr(module, '__register_ignore__', False):
            ComponentLibrary.components[new_class.code] = new_class
            try:
                ComponentModel.objects.update_or_create(
                    code=new_class.code,
                    defaults={
                        'name': new_name,
                        'status': __debug__,
                    }
                )
            except Exception as e:
                if not isinstance(e, ProgrammingError):
                    logging.exception(e)

        return new_class
