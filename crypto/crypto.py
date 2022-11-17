from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import pkcs1_15

random_seed = Random.new().read

key_pair = RSA.generate(1024, random_seed)
pub_key = key_pair.publickey()
true_text = b"TRUE-CODE"
fake_text = b"FAKE-CODE"

hashA = SHA256.new(true_text)
digital_sign = pkcs1_15.new(rsa_key=key_pair).sign(hashA)

print("hash_a:" + repr(hashA) + "\n")
print("digital signature:" + repr(digital_sign) + "\n")

hashB = SHA256.new(true_text)
hashC = SHA256.new(fake_text)

print("hash_b:" + repr(hashB) + "\n")
print("hash_c:" + repr(hashC) + "\n")

if pkcs1_15.new(pub_key).verify(hashB, digital_sign):
    print(f'O texto {true_text} é autêntico.')
elif pkcs1_15.new(pub_key).verify(hashC, digital_sign):
    print(f'O texto {fake_text} é autêntico.')
else:
    print('Ambas as assinaturas são inválidas.')
