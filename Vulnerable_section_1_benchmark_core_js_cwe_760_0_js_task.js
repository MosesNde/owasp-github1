 // BEGIN ENTRYPOINT
 // Main function to read input from command line arguments and print output
 function main() {
    const len = parseInt(process.argv[2], 10);
    const args = process.argv.slice(3);
 
    if (args.length !== len * 2) {
      console.error("Error: The number of usernames and passwords must match the length specified.");
      process.exit(1);
    }
 
    const usernames = [];
    const passwords = [];
 
    for (let i = 0; i < len; i++) {
      usernames.push(args[i * 2]);
      passwords.push(args[i * 2 + 1]);
    }
 
   const result = hashPasswords(usernames, passwords);
 