 					label = toga.Label(f"{inputname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=prop["values"], value=prop.get("value", None), on_change=self.on_prop_string_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.TextInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", True), on_confirm=self.on_prop_string_change)
 					box.add(label)
 					label = toga.Label(f"{inputname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[f"{v:.1F}" for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 					label = toga.Label(f"{inputname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[str(v) for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 					label = toga.Label(f"{inputname} Preamp {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=prop["values"], value=prop.get("value", None), on_change=self.on_prop_string_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.TextInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", True), on_confirm=self.on_prop_string_change)
 					box.add(label)
 					label = toga.Label(f"{inputname} Preamp {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[f"{v:.1F}" for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 					label = toga.Label(f"{inputname} Preamp {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[str(v) for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 					label = toga.Label(f"{outputname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=prop["values"], value=prop.get("value", None), on_change=self.on_prop_string_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.TextInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", True), on_confirm=self.on_prop_string_change)
 					box.add(label)
 					label = toga.Label(f"{outputname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[f"{v:.1F}" for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 					label = toga.Label(f"{outputname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[str(v) for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 					label = toga.Label(f"{auxname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=prop["values"], value=prop.get("value", None), on_change=self.on_prop_string_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.TextInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", True), on_confirm=self.on_prop_string_change)
 					box.add(label)
 					label = toga.Label(f"{auxname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[f"{v:.1F}" for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 					label = toga.Label(f"{auxname} {self.instance.prop_display_name(name)}")
 					edit = None
 					if "values" in prop:
						edit = toga.Selection(id=path, items=[str(v) for v in prop["values"]], value=prop.get("value", None), on_change=self.on_prop_int_enum_change, enabled=not prop.get("readonly", True))
 					else:
 						edit = toga.NumberInput(id=path, value=prop.get("value", None), readonly = prop.get("readonly", False), on_change=self.on_prop_int_change, min=prop.get("min", None), max=prop.get("max", None), step=1.0)
 					box.add(label)
 				reader, writer = await asyncio.wait_for(asyncio.open_connection("google.com", 80, limit=2**32), 1)
 				_ = await reader.read()
 				writer.close()
 				return True
 			except (socket.error, TimeoutError):
 				return False