 	}
 
 	GenerateUuid(prefix) {
		return `${prefix}-${"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx".replace(/[x]/g, c=>(Math.random() * 16 | 0).toString(16))}`;
 	}
 
 	async InitializeComponents() {