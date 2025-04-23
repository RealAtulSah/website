import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(32)
print("\nGenerated SESSION_SECRET:")
print(f"export SESSION_SECRET=\"{secret_key}\"\n")
print("Add this line to your .env file")
