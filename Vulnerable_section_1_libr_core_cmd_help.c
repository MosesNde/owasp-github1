 		break;
 	case 'e': // echo
 		{
 		if (input[1] == 'n') { // mimic echo -n
 			const char *msg = r_str_chop_ro (input+2);
 			// TODO: replace all ${flagname} by its value in hexa