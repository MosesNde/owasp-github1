     @NotNull
     private String fullName;
 
    @Pattern(regexp = "[_\\-\\.0-9a-z]{1,127}", message = "Password must contain only underscores, hyphens, dots, digits, and lowercase letters, and be between 1 and 127 characters long.")
     @NotNull
     private String password;
 