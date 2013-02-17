####################################################################################################################
# Python classes for performing certain calculations at module system build time.
####################################################################################################################

class LazyIdEvaluation:
  """Base class for identifier calculations delayed to module system build time."""

  def recurse(self, processor, i):
    if isinstance(i, LazyIdEvaluation):
      i = i.process(processor)
    return processor.process_id(i)

class add(LazyIdEvaluation):
  """Adds multiple identifiers."""

  def __init__(self, *args):
    self.ids = args

  def process(self, processor):
    return sum(self.recurse(processor, i) for i in self.ids)

class sub(LazyIdEvaluation):
  """Subtracts one identifier from another."""

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def process(self, processor):
    return self.recurse(processor, self.a) - self.recurse(processor, self.b)

class price(LazyIdEvaluation):
  """Gets the price of an item id."""

  def __init__(self, item_id):
    self.item_id = item_id

  def process(self, processor):
    import module_items
    return module_items.items[processor.process_id(self.item_id, "itm")][5]

class block:
  """Inserts a list of operations inside an exisiting block."""

  def __init__(self, block):
    self.block = block
