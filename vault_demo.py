import os, hvac

client = hvac.Client(url=os.getenv("VAULT_ADDR", "http://127.0.0.1:8200"),
                     token=os.getenv("VAULT_TOKEN"))
assert client.is_authenticated(), "Vault auth failed"

resp = client.secrets.kv.v2.read_secret_version(path="pygoat",
                                                raise_on_deleted_version=True)
data = resp["data"]["data"]

def masked(v):
    return (v[:3] + "***") if v else "<MISSING>"

print("Secrets retrieved from central Vault server:")
for k, v in data.items():
    print(f"  {k}: {masked(v)}")
print("Source: HashiCorp Vault (centralized secret manager)")
