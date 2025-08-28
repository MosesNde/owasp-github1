 	_text.resize(10);
 }
 
 void Console::printTosText(int tosIndex) {
 	const Common::String &text = _tosText->getText(tosIndex);
 	// debugN("tos %d: ", tosIndex);