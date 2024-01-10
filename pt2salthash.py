import hashlib
from passlib.hash import lmhash
with open("1000-most-common-passwords.txt","r") as f1:
    with open("NTLM-SALTED-1000-most-common-passwords.txt", "w") as f2:
        for ind, line in enumerate(f1.readlines()):
            nl = line.strip()+str(ind)
            lm = lmhash.hash(nl.strip())
            nt = hashlib.new("md4",nl.strip().encode("utf-16le")).hexdigest()
            f2.write(f"user{ind}::{lm}:{nt}:::\n")